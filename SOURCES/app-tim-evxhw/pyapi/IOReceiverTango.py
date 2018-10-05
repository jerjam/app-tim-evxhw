# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


#from ReceiverConfigurableModel import *
from ReceiverModel import *
import traceback
import numpy

import PyTango

class TangoIO:

	def __init__(self, dname):
		self.dp = PyTango.DeviceProxy(dname)
		self.dname = dname

	def get_data_property(self, name):
		return self.dp.get_property([name])[name]

	def set_data_property(self, name, data):
		self.dp.put_property({ name : data })

	def get_image(self, name, dimx, dimy=None):
		r = self._get_mondongo(name)
		return r

	def _get_mondongo(self, name):
		assert(False)

	def get_spectrum(self, name, dimx=None):
		r = self._get_mondongo(name)
		if dimx is not None:
			if dimx < len(r):
				return r[:dimx]
		return r

	def get_scalar(self, name, dimx=1, dimy=None):
		return self.get_image(name, dimx, None)

	def set_image(self, name, data, dimx, dimy):
		assert(False)

	def set_spectrum(self, name, data):
		return self.set_image(name, data, len(data), None)

	def set_scalar(self, name, data):
		return self.set_image(name, data, None, None)

	def _image_to_flat(self, data, dimx, dimy):
		if dimy is None: # spectrum...
			return data[:dimx]
		d2 = []
		for y in xrange(dimy):
			for x in xrange(dimx):
				d2 += [ data[y][x] ]
		return d2

	def _flat_to_image(self, pr, dimx, dimy):
		if dimy != None:
			assert(dimx != None)
			if len(pr) != dimx*dimy:
				raise Exception("Size of read image is not the expected")
		elif dimx != None:
			if (len(pr) % dimx) != 0:
				raise Exception("Size of read image is not % dimx")
			dimy = len(pr) / dimx
		else:
			raise Exception("dimx or dimy must be specifyed!")

		r = []
		for y in xrange(dimy):
			r += [ pr[y*dimx:y*dimx+dimx] ]
		return r



class TangoPropertiesIO(TangoIO):
	def __init__(self, dname):
		TangoIO.__init__(self, dname)
		self.__db = self.dp.get_device_db()

	# @todo DELETE ME: It's just to update. Some fields used to
	# be saved as _Name properties. Now they are saved as
	# attribute(Name)/__default__ properties. If we can't find
	# the attribute(Name)/__default__ this method is to try the
	# old path. If there is information, move it to the new world
	# and delete the old data...
	def _get_prop_update_old(self, name):
		p = self.get_data_property('_' + name)
		if list(p) != []:
			# Save setting in the new location...
			self._set_prop(name, p)
			# Delete old location settings...
			self.__db.delete_device_property(self.dname, '_' + name)
		return p

	def _get_prop(self, name):
		r = self.__db.get_device_attribute_property(self.dname, name)
		#return r[name].get("__default__", [])
		# @todo Uncomment previous & delete following lines.
		# see _get_prop_update_old
		r = r[name].get("__default__", None)
		if r is None:
			return self._get_prop_update_old(name)
		return r

	def _set_prop(self, name, value):
		#return self.set_data_property('_' + name, value)
		d = { "__default__": value }
		d2 = { name : d }
		return self.__db.put_device_attribute_property(self.dname, d2)

	def _get_mondongo(self, name):
		return self._get_prop(name)

	def get_image(self, name, dimx, dimy=None):
		pr = self._get_mondongo(name)
		if dimx==1 and dimy==None and pr!=None and len(pr)>0: #reading scalar
			return pr[0]
		return self._flat_to_image(pr, dimx, dimy)

	def set_image(self, name, data, dimx, dimy):
		d2 = self._image_to_flat(data, dimx, dimy)
		return self._set_prop(name, d2)

class TangoAttributesIO(TangoIO):

	def _get_mondongo(self, name):
		v = self.dp.read_attribute(name, PyTango.ExtractAs.List)
		return v.value 

	def get_image(self, name, dimx, dimy=None):
		v = self.dp.read_attribute(name, PyTango.ExtractAs.List)
		r = v.value
		if not (dimx is None):
			if v.dim_x != dimx:
				raise Exception("Read x size is not expected x.")

		if not (dimy is None):
			if v.dim_y != dimy:
				raise Exception("Read y size is not expected y size.")

		return r

	def set_image(self, name, data, dimx, dimy):
		return self.dp.write_attribute(name, data)

	def set_data_property(self, name, data):
		print 'The following data will NOT be set:'
		print '  ', name, ' = ', data

	def get_data_property(self, name):
		return self.dp.get_property([name])[name]
		

class _TangoDirectIO(TangoIO):
	class FakeAttr(object):
		def __init__(self, name):
			self.__name = name
			self.__r_data = None
		def get_name(self):
			return self.__name

		def set_value(self, value):
			self.__r_data = value

		def get_value(self):
			return self.__r_data

	class FakeWAttr(FakeAttr):
		def __init__(self, name, data):
			if isinstance(data, list):
				data = numpy.array(data)
			self.__w_data = data
			_TangoDirectIO.FakeAttr.__init__(self, name)
		def get_write_value(self):
			return self.__w_data


	def __init__(self, obj):
		self.obj = obj

	def _get_mondongo(self, name, dimx=None, dimy=None):
		fn = getattr(self.obj, 'read_' + name)
		try:
			w_data = []
			attr = _TangoDirectIO.FakeWAttr(name, w_data)
			fn(attr)
		except Exception:
			traceback.print_exc()
			raise
		return attr.get_value()

	def set_image(self, name, data, dimx, dimy):
		fn = getattr(self.obj, 'write_' + name)
		try:
			fn(_TangoDirectIO.FakeWAttr(name, data))
		except Exception:
			traceback.print_exc()
			raise

	def set_data_property(self, name, data):
		pass

	def get_data_property(self, name):
		return getattr(self.obj, name)


class MTangoIO:
	def __init__(self, tangoio = None):
		self.tio = tangoio
		self._error = []
		self._ok = []
		self._errorDesc = []

	def _run_selection(self, model, selection, ops):
		self._error = []
		self._ok = []
		self._errorDesc = []
		for name, fn in ops:
			if name not in selection:
				continue
			try:
				fn (model)
			except:
				traceback.print_exc()
				self._error += [ name ]
				self._errorDesc += [traceback.format_exc()]
			else:
				self._ok += [ name ]

	def load_from_tango(self, tio, model, selection):
		if not tio is None:
			self.tio = tio

		ops = [
			#Common
			[ 'PULSE',		self.load_pulses_from_tango ],
			[ 'RAM',		self.load_ram_from_tango ],
			#EVR230
			[ 'UNIVOUT',		self.load_outputs_from_tango ],
			[ 'UNIVIN',		self.load_inputs_from_tango ],
			[ 'COUNTER',		self.load_counters_from_tango ],
			#EVR300TG
			[ 'FPOUT',		self.load_fpoutputs_from_tango ],
			[ 'CML',		self.load_cml_from_tango ],
			[ 'FINEDELAY',		self.load_fine_from_tango ],
		]
		self._run_selection(model, selection, ops)


	def save_to_tango(self, tio, model, selection):
		if not tio is None:
			self.tio = tio

		ops = [
			#Common
			[ 'PULSE',		self.save_pulses_to_tango ],
			[ 'RAM',		self.save_ram_to_tango ],
			#EVR230
			[ 'UNIVOUT',		self.save_outputs_to_tango ],
			[ 'UNIVIN',		self.save_inputs_to_tango ],
			[ 'COUNTER',		self.save_counters_to_tango ],
			#EVR300TG
			[ 'FPOUT',		self.save_fpoutputs_to_tango ],
			[ 'CML',		self.save_cml_to_tango ],
			[ 'FINEDELAY',		self.save_fine_to_tango ],
		]
		self._run_selection(model, selection, ops)




	def _list2bitflag(self, ls):
		r = 0
		
		for n in xrange(len(ls)):
			if ls[n]:
				r = r | (1 << n)
				
		return r

	def _bitflag2list(self, bf, length=32):
		r = []

		for x in xrange(length):
			if int(bf) & (1 << x):
				r += [True]
			else:
				r += [False]
		return r

	def load_pulses_from_tango(self, model):
		params = self.tio.get_image('PulseParams', 3)
		properties = self.tio.get_image('PulseProperties', 5)
		names = self.tio.get_data_property('PulseNames')

		total = len(model.mpulses.pulses)
		if names is None:
			names = []

		for i in xrange(total):
			pulse = model.mpulses.pulses[i]
			if i < len(params):
				pulse.prescaler, pulse.delay, pulse.width = map(int, params[i])
			if i >= MPulseList.TotalPrescalers:
				pulse.prescaler = None
			if i < len(properties):
				pulse.polarityActiveHigh, pulse.tclear, pulse.tset, pulse.tpulse, pulse.tmaster = map(bool, map(int, properties[i]))
			if i < len(names):
				model.mpulses.pulseNames[i] = names[i]
			else:
				model.mpulses.pulseNames[i] = 'PULSE-' + str(i)

	def load_ram_from_tango(self, model):
		errors = []
		def _failed():
			errors.append(traceback.format_exc())
		npulses = len(model.mpulses.pulses)
		
		nevents = 256
		
		ram = nevents * [ [0, 0, 0] for x in xrange(nevents) ]
		fifoSave = [ 0 for x in xrange(nevents) ]
		logSave = [ 0 for x in xrange(nevents) ]
		logStop = [ 0 for x in xrange(nevents) ]
		forward = [ 0 for x in xrange(nevents) ]
		led = [ 0 for x in xrange(nevents) ]
		seconds0 = [ 0 for x in xrange(nevents) ]
		seconds1 = [ 0 for x in xrange(nevents) ]
		timestamp_reset = [ 0 for x in xrange(nevents) ]
		timestamp_clock = [ 0 for x in xrange(nevents) ]
		try:
			ram = self.tio.get_image('Ram', 3)
		except: _failed()
		try:
			fifoSave = map(int, self.tio.get_spectrum('EventsFIFOSave', nevents))
		except: _failed()
		try:
			logSave = map(int, self.tio.get_spectrum('EventsLogSave', nevents))
		except: _failed()
		try:
			logStop = map(int, self.tio.get_spectrum('EventsLogStop', nevents))
		except: _failed()
		try:
			forward = map(int, self.tio.get_spectrum('EventsForward', nevents))
		except: _failed()
		try:
			led = map(int, self.tio.get_spectrum('EventsLed', nevents))
		except: _failed()
		try:
			seconds0 = map(int, self.tio.get_spectrum('EventsSeconds0', nevents))
		except: _failed()
		try:
			seconds1 = map(int, self.tio.get_spectrum('EventsSeconds1', nevents))
		except: _failed()
		try:
			timestamp_reset = map(int, self.tio.get_spectrum('EventsTimestampReset', nevents))
		except: _failed()
		try:
			timestamp_clock = map(int, self.tio.get_spectrum('EventsTimestampClock', nevents))
		except: _failed()

		for ev in xrange(len(ram)):
			model.mram.events[ev].trigger = self._bitflag2list(ram[ev][0], npulses)
			model.mram.events[ev].set = self._bitflag2list(ram[ev][1], npulses)
			model.mram.events[ev].clear = self._bitflag2list(ram[ev][2], npulses)

			# todo Most model.mram.events[ev].flags
			model.mram.events[ev].flags[MEvent.FlagFIFOSaveEvent] = bool(fifoSave[ev])
			model.mram.events[ev].flags[MEvent.FlagLogSaveEvent] = bool(logSave[ev])
			model.mram.events[ev].flags[MEvent.FlagLogStopEvent] = bool(logStop[ev])
			model.mram.events[ev].flags[MEvent.FlagForwardEvent] = bool(forward[ev])
			model.mram.events[ev].flags[MEvent.FlagLedEvent] = bool(led[ev])
			model.mram.events[ev].flags[MEvent.FlagSeconds0] = bool(seconds0[ev])
			model.mram.events[ev].flags[MEvent.FlagSeconds1] = bool(seconds1[ev])
			model.mram.events[ev].flags[MEvent.FlagTimestampReset] = bool(timestamp_reset[ev])
			model.mram.events[ev].flags[MEvent.FlagTimestampClk] = bool(timestamp_clock[ev])

		if len(errors):
			raise Exception(errors)

	def load_outputs_from_tango(self, model):
		num = len(model.moutputs)
		if self.tio.get_scalar('FormFactor') == 'cPCI6U':
			for n in xrange(num):
				model.moutputs[n].output = MOutput.OutLow
			return
		
		#this only if we are an EVR230
		vals = self.tio.get_spectrum('UnivOut', num)

		for n in xrange(num):
			if n < len(vals):
				model.moutputs[n].output = int(vals[n])
			else:
				model.moutputs[n].output = MOutput.OutLow

	def load_inputs_from_tango(self, model):
		num = len(model.minputs)
		if self.tio.get_scalar('FormFactor') == 'cPCI6U':
			for n in xrange(num):
				model.minputs[n].backEvent = None
				model.minputs[n].backEdge  = None
				model.minputs[n].backLevel = None
				model.minputs[n].extEvent = None
				model.minputs[n].extEdgeSensitivity = 0
				model.minputs[n].extLevelSensitivity = 0
			return

		backs = self.tio.get_image('ExtBackEvent', 4)
		exts = self.tio.get_image('ExtEvent', 4)
		extSensitivity = self.tio.get_image('ExtSensitivity', 3)
		for n in xrange(num):
			model.minputs[n].backEvent = int(backs[n][1])
			model.minputs[n].backEdge  = int(backs[n][2])
			model.minputs[n].backLevel = int(backs[n][3])

			if model.minputs[n].backEvent < 0:
				model.minputs[n].backEvent = None
			model.minputs[n].extEvent = int(exts[n][1])
			model.minputs[n].extEdge  = int(exts[n][2])
			model.minputs[n].extLevel = int(exts[n][3])

			if model.minputs[n].extEvent < 0:
				model.minputs[n].extEvent = None
			model.minputs[n].extEdgeSensitivity = int(extSensitivity[n][1])
			model.minputs[n].extLevelSensitivity = int(extSensitivity[n][2])

	def load_counters_from_tango(self, model):
		num = len(model.mcounters)
		vals = self.tio.get_spectrum('Prescalers', num)
		for n in xrange(num):
			model.mcounters[n] = int(vals[n])

	def load_fpoutputs_from_tango(self, model):
		num = len(model.fpoutputs)
		if self.tio.get_scalar('FormFactor') != 'cPCI6U':
			for n in xrange(num):
				model.fpoutputs[n].output = FPOutput.OutLow
			return

		vals = self.tio.get_spectrum('FPOut', num)
		for n in xrange(num):
			if n < len(vals):
				model.fpoutputs[n].output = int(vals[n])
			else:
				model.fpoutputs[n].output = FPOutput.OutLow

	def load_cml_from_tango(self, model):
		num = len(model.cml)
		if self.tio.get_scalar('FormFactor') != 'cPCI6U':
			for n in xrange(num):
				model.cml[n].enable = False
			return

		vals = self.tio.get_spectrum('CMLEnable', num)
		for n in xrange(num):
			if n < len(vals):
				model.cml[n].enable = bool(vals[n])
			else:
				model.cml[n].enable = False

	def load_fine_from_tango(self, model):
		num = len(model.fine_delays)
		if self.tio.get_scalar('FormFactor') != 'cPCI6U':
			for n in xrange(num):
				model.fine_delays[n].fine_delay = 0
			return

		vals = self.tio.get_spectrum('FineDelay', num)
		for n in xrange(num):
			if n < len(vals):
				model.fine_delays[n].fine_delay = int(vals[n])
			else:
				model.fine_delays[n].fine_delay = 0

	def save_pulses_to_tango(self, model):
		def _poltr(v):
			if v == None:
				return 0
			return int(v)

		params = []
		properties = []
		names = []

		total = len(model.mpulses.pulses)
		assert (len(model.mpulses.pulses) == len(model.mpulses.pulseNames))
		for i in xrange(total):
			pulse = model.mpulses.pulses[i]
			params += [map(_poltr, [pulse.prescaler, pulse.delay, pulse.width])]
			properties += [map(int, [pulse.polarityActiveHigh, pulse.tclear, pulse.tset, pulse.tpulse, pulse.tmaster])]
			names += [model.mpulses.pulseNames[i]]

		self.tio.set_image('PulseParams', params, 3, total)
		self.tio.set_image('PulseProperties', properties, 5, total)
		self.tio.set_data_property('PulseNames', names)

	def save_ram_to_tango(self, model):
		npulses = len(model.mpulses.pulses)
		nevents = len(model.mram.events)

		ram = [ [0, 0, 0] for x in xrange(nevents) ]
		fifoSave = [ 0 for x in xrange(nevents) ]
		logSave = [ 0 for x in xrange(nevents) ]
		logStop = [ 0 for x in xrange(nevents) ]
		forward = [ 0 for x in xrange(nevents) ]
		led = [ 0 for x in xrange(nevents) ]
		seconds0 = [ 0 for x in xrange(nevents) ]
		seconds1 = [ 0 for x in xrange(nevents) ]
		timestamp_reset = [ 0 for x in xrange(nevents) ]
		timestamp_clock = [ 0 for x in xrange(nevents) ]
		for ev in xrange(nevents):
			ram[ev][0] = self._list2bitflag(model.mram.events[ev].trigger)
			ram[ev][1] = self._list2bitflag(model.mram.events[ev].set)
			ram[ev][2] = self._list2bitflag(model.mram.events[ev].clear)

			# todo Most model.mram.events[ev].flags
			fifoSave[ev] = model.mram.events[ev].flags[MEvent.FlagFIFOSaveEvent]
			logSave[ev] = model.mram.events[ev].flags[MEvent.FlagLogSaveEvent]
			logStop[ev] = model.mram.events[ev].flags[MEvent.FlagLogStopEvent]
			forward[ev] = model.mram.events[ev].flags[MEvent.FlagForwardEvent]
			led[ev] = model.mram.events[ev].flags[MEvent.FlagLedEvent]
			seconds0[ev] = model.mram.events[ev].flags[MEvent.FlagSeconds0]
			seconds1[ev] = model.mram.events[ev].flags[MEvent.FlagSeconds1]
			timestamp_reset[ev] = model.mram.events[ev].flags[MEvent.FlagTimestampReset]
			timestamp_clock[ev] = model.mram.events[ev].flags[MEvent.FlagTimestampClk]

		self.tio.set_image('Ram', ram, 3, nevents)
		self.tio.set_spectrum('EventsFIFOSave', map(int, fifoSave))
		self.tio.set_spectrum('EventsLogSave', map(int, logSave))
		self.tio.set_spectrum('EventsLogStop', map(int, logStop))
		self.tio.set_spectrum('EventsForward', map(int, forward))
		self.tio.set_spectrum('EventsLed', map(int, led))
		self.tio.set_spectrum('EventsSeconds0', map(int, seconds0))
		self.tio.set_spectrum('EventsSeconds1', map(int, seconds1))
		self.tio.set_spectrum('EventsTimestampReset', map(int, timestamp_reset))
		self.tio.set_spectrum('EventsTimestampClock', map(int, timestamp_clock))

	def save_outputs_to_tango(self, model):
		num = len(model.moutputs)
		vals = num * [0]
		for n in xrange(num):
			vals[n] = int(model.moutputs[n].output)
		self.tio.set_spectrum('UnivOut', vals)

	def save_inputs_to_tango(self, model):
		num = len(model.minputs)
		backs = [[0 for i in range(4)] for j in range(num)]
		exts = [[0 for i in range(4)] for j in range(num)]
		extSensitivity = [[0 for i in range(3)] for j in range(num)]

		for n in range(num):

			if model.minputs[n].backEvent is None:
				backs[n] = [n, -1, 0, 0]
			else:
				backs[n] = [  n,
							model.minputs[n].backEvent,
							int(model.minputs[n].backEdge),
							int(model.minputs[n].backLevel) ]
			
			if model.minputs[n].extEvent is None:
				exts[n] = [n, -1, 0, 0]
			else:
				exts[n] = [ n,
							model.minputs[n].extEvent,
							int(model.minputs[n].extEdge),
							int(model.minputs[n].extLevel) ]

			extSensitivity[n] = [
						n,
						int(model.minputs[n].extEdgeSensitivity),
						int(model.minputs[n].extLevelSensitivity) ]

		self.tio.set_image('ExtBackEvent', backs, 4, num)
		self.tio.set_image('ExtEvent', exts, 4, num)
		self.tio.set_image('ExtSensitivity', extSensitivity, 3, num)

	def save_counters_to_tango(self, model):
		num = len(model.mcounters)
		vals = num * [0]
		for n in xrange(num):
			vals[n] = model.mcounters[n]
		self.tio.set_spectrum('Prescalers', vals)

	def save_fpoutputs_to_tango(self, model):
		num = len(model.fpoutputs)
		vals = num * [0]
		for n in xrange(num):
			vals[n] = int(model.fpoutputs[n].output)
		self.tio.set_spectrum('FPOut', vals)

	def save_cml_to_tango(self, model):
		num = len(model.cml)
		vals = num * [False]
		for n in xrange(num):
			vals[n] = model.cml[n].enable
		self.tio.set_spectrum('CMLEnable', vals)

	def save_fine_to_tango(self, model):
		num = len(model.fine_delays)
		vals = num * [0]
		for n in xrange(num):
			vals[n] = model.fine_delays[n].fine_delay
		self.tio.set_spectrum('FineDelay', vals)
