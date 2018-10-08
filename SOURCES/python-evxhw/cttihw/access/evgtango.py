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


from access.evg import *
import PyTango
import numpy

import time


class EvgAccessTango(EvgAccess):
	def __init__(self, url = 'timing/EventG/gen1'):
		self.dp = PyTango.DeviceProxy(url)

	def deviceName(self):
		return self.dp.name()
	
	def deviceString(self):
		return 'tango:' + self.deviceName()

	def runSequence(self, seq):
		self.dp.RunSequence(seq)

	def sendSwEvent(self, ev):
		self.dp.SendSwEvent(ev)

	def canSetDefault(self):
		return True

	def writeAttribute(self, attrname, val, dim_x = None, dim_y = None):
		self.dp.write_attribute(attrname, val)

	#############################################################
	####### ACControl
	def getOpsAC(self):
		ac = self.dp.read_attribute('AC')
		bypass, synmx7, presc, delay, trigger = ac.value

		if trigger < 0: trigger = None
		return presc, delay, synmx7, bypass, trigger

	def setOpsAC(self, presc, delay, synmx7, bypass, trigger):
		if trigger == None: trigger = -1
		r = [ bypass, synmx7, presc, delay, trigger ]
		self.writeAttribute('AC', r)

	#############################################################
	####### ClockControl

	def getOpsClock(self):
		rftype, rfdiv, syn = self.dp.GetClockParameters()
		return rftype, rfdiv, syn

	def setOpsClock(self, rftype, rfdiv, syn):
		arg = [rftype, rfdiv, syn]
		old = list(self.getOpsClock())
		if old != arg:
			self.dp.SetClockParameters(arg)


# 	#############################################################
# 	####### DataBufferControl
# 	#TODO:  DataBufferControl
# 
# 
# 	
	#############################################################
	####### DBusControl
	def getOpsDBus(self):
		dbusmap = self.dp.read_attribute('DBus')
		dmap = dbusmap.value
		assert len(dmap) == self.TOTAL_DBUS_BITS

		return (dmap,)


	def setOpsDBus(self, dmap):
		assert len(dmap) == self.TOTAL_DBUS_BITS
		self.writeAttribute('DBus', dmap)

	#############################################################
	####### Front Panel Univ I/O Control
	def getOpsUnivIn(self):
		fpattr = self.dp.read_attribute('UnivIn')
		fp = fpattr.value

		assert fp.shape == (self.TOTAL_INPUT_PORTS, 2)

		trig = fp.transpose()[0]
		dbus = fp.transpose()[1]

		return (dbus,trig)

	def setOpsUnivIn(self, dbus, trig):
		assert len(dbus) == self.TOTAL_INPUT_PORTS
		assert len(trig) == self.TOTAL_INPUT_PORTS

		a = numpy.ndarray(shape=(self.TOTAL_INPUT_PORTS,2), dtype=numpy.int32)

		a.transpose()[0] = trig
		a.transpose()[1] = dbus

		self.writeAttribute('UnivIn', a)


	#############################################################
	####### MXCTableControl
	def getOpsMXCTable(self):
		mxcattr = self.dp.read_attribute('MXC')
		mxc = mxcattr.value
		assert mxc.shape == (self.TOTAL_MXCS, 2)

		prescs = self.TOTAL_MXCS*[None]
		trigmap = self.TOTAL_MXCS*[None]
		for i in range(self.TOTAL_MXCS):
			prescs[i] = mxc[i, 0]
			t = mxc[i, 1]
			#TODO: Documenta a form.set/get tots els parametres de tots els metodes, es alla on ho aire a buscar. En aquest cas per exemple, comentar que tornen None per a invalids i tal...
			if t in range(self.MAX_MXCS): trigmap[i] = t

		return (prescs,trigmap)

	def setOpsMXCTable(self, prescs, trigmap):
		assert len(prescs) == self.TOTAL_MXCS
		assert len(trigmap) == self.TOTAL_MXCS

		mxc = numpy.ndarray(shape=(self.TOTAL_MXCS,2), dtype=numpy.int32)

		for i in xrange(self.TOTAL_MXCS):
			if trigmap[i] is None:
				tr = -1
			else:
				tr = trigmap[i]
			if prescs[i] is None:
				pr = 0
			else:
				pr = prescs[i]
			mxc[i] = [pr, tr]

		self.writeAttribute('MXC', mxc)



	#############################################################
	####### OthersControl
	def getOpsOthers(self):
		print self.dp.state()

		enmast = (self.dp.state() != PyTango.DevState.OFF)
		swen = self.dp.read_attribute('SwEvent')
		enswev = swen.value

		return enswev, enmast

	def setOpsOthers(self, enswev, enmast):
		self.writeAttribute('SwEvent', enswev)
		if enmast:
			self.dp.On()
		else:
			self.dp.Off()
		


	#############################################################
	####### TriggersControl
	def getOpsTriggers(self):
		ten = self.dp.read_attribute('TriggerEnable')
		tev = self.dp.read_attribute('TriggerEvent')

		eventenables = ten.value
		eventcodes = tev.value

		assert len(eventcodes) == self.TOTAL_TRIGGERS
		assert len(eventenables) == self.TOTAL_TRIGGERS
		
		return eventenables, eventcodes

	def setOpsTriggers(self, eventenables, eventcodes):
		assert len(eventcodes) == self.TOTAL_TRIGGERS
		assert len(eventenables) == self.TOTAL_TRIGGERS

		self.writeAttribute('TriggerEvent', eventcodes)
		self.writeAttribute('TriggerEnable', eventenables)


	#############################################################
	####### SequenceEditor
	def getOpsSequenceEditor(self, rs):
		seqattrname = 'Sequence' + str(rs)
		seqval = self.dp.read_attribute(seqattrname)
		seq = seqval.value

		sc = self.dp.read_attribute(seqattrname+'Control')
		assert sc.dim_x == 4
		scv = sc.value
		seqen, single, recycle, trigsel = scv

		return seq, seqen, trigsel, single, recycle

	def setOpsSequenceEditor(self, rs, seq, seqen, trigsel, single, recycle):
		"""
		rs : Sequence id (0 or 1)
		seq: [(ts0, ec0), (ts1, ec1), ... MAX_SEQRAMEV ]
		seqen : Sequence enabled, disabled
		trigsel : Sequence trigger selector see doc *** (TODO)
		single:
		recycle:
		""" #TODO: moure aquesta doc al form...

		retry = 30
		while self.dp.state() == PyTango.DevState.STANDBY:
			time.sleep(0.1)
			retry -= 1
			if retry < 0:
				raise "Problems setting clock"

		seqattrname = 'Sequence' + str(rs)

		if len(seq) == 0: seq = [ [0, 0] ] # minimum required
		self.writeAttribute(seqattrname, seq)

		self.writeAttribute(seqattrname+'Control', [int(seqen), int(single), int(recycle), trigsel])






































class EvgAccessTangoConfig(EvgAccess):
	def __init__(self, url = 'timing/EventG/gen1'):
		if type(url) is PyTango.DeviceProxy:
			self.dp = url
		else:
			self.dp = PyTango.DeviceProxy(url)

	def deviceName(self):
		return self.dp.name()
	
	def deviceString(self):
		return 'tango-config:' + self.deviceName()

	def runSequence(self, seq):
		#self.dp.RunSequence(seq)
		pass

	def sendSwEvent(self, ev):
		#self.dp.SendSwEvent(ev)
		pass

	def writeProperty(self, propname, val, dim_x = None, dim_y = None, _type=int):
		print 'write', propname, val
		prop_val = {propname:map(_type,val)}
		self.dp.put_property(prop_val)

	def readProperty(self, propname, proptype = None, length = None, default = 0):
		val = self.dp.get_property([propname])[propname]

		if proptype is bool: proptype = lambda x: bool(int(x))
		if proptype: val = map(proptype, val)

		if not length == None:
			aux = val
			val = length * [default]
			val[:len(aux)] = aux
			assert len(val) == length

		print 'read', propname, val

		return val

# 	#############################################################
# 	####### ACControl
	def getOpsAC(self):
		bypass, synmx7, presc, delay, trigger = self.readProperty('AC', int, length=5, default=0)
		if trigger < 0: trigger = None
		return presc, delay, synmx7, bypass, trigger

	def setOpsAC(self, presc, delay, synmx7, bypass, trigger):
		if trigger == None: trigger = -1
		r = [ bypass, synmx7, presc, delay, trigger ]
		self.writeProperty('AC', r)


	#############################################################
	####### ClockControl

	def getOpsClock(self):
		rftype, rfdiv, syn = self.readProperty(
			'ClockParams', int, length=3, default=0)
		return rftype, rfdiv, syn


	def setOpsClock(self, rftype, rfdiv, syn):
		arg = [rftype, rfdiv, syn]
		self.writeProperty('ClockParams', arg)


# # 	#############################################################
# # 	####### DataBufferControl
# # 	#TODO:  DataBufferControl
# # 
# # 
# # 	
	#############################################################
	####### DBusControl
	def getOpsDBus(self):
		dmap = self.readProperty(
			'DBus', int,
			length = self.TOTAL_DBUS_BITS,
			default = 0)

		return (dmap,)


	def setOpsDBus(self, dmap):
		assert len(dmap) == self.TOTAL_DBUS_BITS
		self.writeProperty('DBus', dmap)

	#############################################################
	####### Front Panel Univ I/O Control
	def getOpsUnivIn(self):
		fpattr = self.dp.read_attribute('UnivIn')
		fp = fpattr.value[:fpattr.dim_x * fpattr.dim_y]

		fp = self.readProperty(
			'UnivIn', int,
			length = 2 * self.TOTAL_INPUT_PORTS,
			default = -1)

		trig = fp[::2]
		dbus = fp[1::2]

		return (dbus,trig)
# 
	def setOpsUnivIn(self, dbus, trig):
		assert len(dbus) == self.TOTAL_INPUT_PORTS
		assert len(trig) == self.TOTAL_INPUT_PORTS

		r = 2 * self.TOTAL_INPUT_PORTS * [0]
		r[::2] = trig
		r[1::2] = dbus

		self.writeProperty('UnivIn', r, 2, len(r)/2)


	#############################################################
	####### MXCTableControl
	def getOpsMXCTable(self):
		prescs = self.readProperty(
			'MXCPrescaler', int,
			length = self.TOTAL_MXCS,
			default = 0 )

		trigmap = self.readProperty(
			'MXCTriggerMap', int,
			length = self.TOTAL_MXCS,
			default = None )

		return (prescs,trigmap)

	def setOpsMXCTable(self, prescs, trigmap):
		assert len(prescs) == self.TOTAL_MXCS
		assert len(trigmap) == self.TOTAL_MXCS

		def __noNone(x):
			if x == None: return self.MAX_MXCS - 1
			return x
		trigmap = [__noNone(x) for x in trigmap]

		self.writeProperty('MXCPrescaler', prescs)
		self.writeProperty('MXCTriggerMap', trigmap)


	#############################################################
	####### OthersControl
	def getOpsOthers(self):
		enmast = True
		enswev = self.readProperty(
			'SwEventEnable', str,
			length = 1,
			default = False)[0]

		if enswev == 'True':
			enswev = True
		else:
			enswev = False
		return enswev, enmast

	def setOpsOthers(self, enswev, enmast):
		self.writeProperty('SwEventEnable', [bool(enswev)], _type=str)



	#############################################################
	####### TriggersControl
	def getOpsTriggers(self):

		eventenables =  self.readProperty(
			'TriggerEnable', bool,
			length = self.TOTAL_TRIGGERS )
		eventcodes =  self.readProperty(
			'TriggerEvent', int,
			length = self.TOTAL_TRIGGERS )
		return eventenables, eventcodes
# 
	def setOpsTriggers(self, eventenables, eventcodes):
		assert len(eventcodes) == self.TOTAL_TRIGGERS
		assert len(eventenables) == self.TOTAL_TRIGGERS

		self.writeProperty('TriggerEvent', eventcodes)
		self.writeProperty('TriggerEnable', eventenables)


	#############################################################
	####### SequenceEditor
	def getOpsSequenceEditor(self, rs):
		seqen = True
		trigsel = 0x0

		seqattrname = 'Sequence' + str(rs)
		s = self.readProperty(seqattrname, int)
		
		assert len(s) % 2 == 0
		# change format, from [ts0, ec0, ts1, ec1... MAX_SEQRAMEV]
		# to [(ts0, ec0), (ts1, ec1), ... MAX_SEQRAMEV]
		seq = map(lambda x,y: (x,y) , s[::2], s[1::2])

		seqctrl = seqattrname + 'Control'
		seqen, single, recycle, trigsel = self.readProperty(seqctrl, int, length=4, default=0)

		return seq, seqen, trigsel, single, recycle
# 
	def setOpsSequenceEditor(self, rs, seq, seqen, trigsel, single, recycle):
		"""
		rs : Sequence id (0 or 1)
		seq: [(ts0, ec0), (ts1, ec1), ... MAX_SEQRAMEV ]
		seqen : Sequence enabled, disabled
		trigsel : Sequence trigger selector see doc
		single :
		recylce :
		""" #TODO: moure aquesta doc al form...
		seqattrname = 'Sequence' + str(rs)
		seqcp = []
		# change format, from [(ts0, ec0), (ts1, ec1)...MAX_SEQRAMEV]
		# tots0, ec0, ts1, ec1... MAX_SEQRAMEV]
		for i in seq:
			seqcp += [ i[0], i[1] ]
		if seqcp == []: seqcp = [0, 0] #minimum required
		self.writeProperty(seqattrname, seqcp, 2, len(seqcp)/2)

		seqctrl = seqattrname + 'Control'
		scv = [ seqen, single, recycle, trigsel ]
		self.writeProperty(seqctrl, scv, dim_x=len(scv))

















evgAccessFactoryDict['_default'] = [EvgAccessTango, (str, 'url')]
evgAccessFactoryDict['tango'] = [EvgAccessTango, (str, 'url')]
evgAccessFactoryDict['tangoconf'] = [EvgAccessTangoConfig, (str, 'url')]

