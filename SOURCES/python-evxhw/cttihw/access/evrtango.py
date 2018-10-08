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

from access.evr import *
import PyTango


class EvrAccessTango(EvrAccess):
	def __init__(self, url = 'timing/EventR/rec1'):
		self.dp = PyTango.DeviceProxy(url)

	def deviceName(self):
		return self.dp.name()
	
	def deviceString(self):
		return 'tango:' + self.deviceName()


	def clearViolation(self):
		self.dp.ClearViolation()

	def canSetDefault(self):
		return True

	def writeAttribute(self, attrname, val, dim_x = None, dim_y = None):
		av = PyTango.AttributeValue()
		av.name = attrname
		av.value = val

		if dim_x: av.dim_x = dim_x
		elif type(val) is list: av.dim_x = len(val)
		else: av.dim_x = 1

		if dim_y: av.dim_y = dim_y
		else: av.dim_y = 0
		self.dp.write_attribute(av)


	#############################################################
	####### RamControl
	def getOpsRam(self):
		return [ self._getOpsRam(0), self._getOpsRam(1) ]
	
	def setOpsRam(self, ram0, ram1):
		self._setOpsRam(0, ram0[0], ram0[1])
		self._setOpsRam(1, ram1[0], ram1[1])
		#Only one enabled or disable all
		#Important, at the end
		ram = 0
		if ram0[1]:
			ram = 1
		elif ram1[1]:
			ram = 2

		self.writeAttribute('Ram', ram)


	def _getOpsRam(self, ram):
		assert(ram in range(2))
		attr_name = 'Ram' + str(ram)
		attr_val = self.dp.read_attribute(attr_name)
		ramval = attr_val.value #NO, xq value=[loquetorna lultimqueheescrit]
		ramval = ramval[:attr_val.dim_x * attr_val.dim_y]
		assert(attr_val.dim_x == 3)
		sz = len(ramval)/3

		attr_val = self.dp.read_attribute('Ram')
		enable = False
		if attr_val.value == ram + 1:
			enable = True
		ramEvents = {}
		for i in range(0, self.TOTAL_EVENT_CODE):
			ledev = 0 #TODO
			if (i < sz):
				trig, set, clear = ramval[3*i : 3*(i+1)]
			else:
				trig, set, clear = [0,0,0]
			if (trig | set | clear | ledev): aux = {'trigger' : trig, 'set' : set, 'clear' : clear, 'ledEvent' : ledev}
			else: aux = None
			if aux: ramEvents[i] = aux
		return (ramEvents, enable)

	def _setOpsRam(self, ram, ramEvents, enable):
		assert(ram in range(2))
		attr_name = 'Ram' + str(ram)
		
		val = []
		zeros = []
		for k in range(self.TOTAL_EVENT_CODE + 1):
			if ramEvents.has_key(k):
				v = ramEvents[k]
				val = val + zeros + [v['trigger'], v['set'], v['clear']]
				zeros = []
			else:
				#The others go to 0, or they'll appear agein later
				zeros += [0,0,0]

		if val == []:
			val = [0,0,0]
		
		self.writeAttribute(
			attr_name, val,
			dim_x=3,
			dim_y=len(val)/3 )
		







	#############################################################
	####### PulseControl
	def getOpsPulse(self):
		#TODO: Molts cmaps no son reals!!
		#TODO: getFromDev enirq
		flags = self.TOTAL_PULSES*[[0,0,0,0,0,0]]
		delay = self.TOTAL_PULSES*[0]
		width = self.TOTAL_PULSES*[0]
		presc = self.TOTAL_PULSES*[0]
		enirq = 0
		
		avparams = self.dp.read_attribute('PulseParams')
		dataparams = avparams.value
		widthparams = 3
		
		avprop = self.dp.read_attribute('PulseProperties')
		dataprop = avprop.value
		widthprop = 5
		
		def getPulseParams(index):
			presc = data[3*index + 0]
			delay = data[3*index + 1]
			width = data[3*index + 2]
			return presc, delay, width
		
		for i in range(0, self.TOTAL_PULSES):
			presc[i], delay[i], width[i] = dataparams[widthparams*i : widthparams*(i+1)]
			polarity, map_reset_ena, map_set_ena, map_trigger_ena, enable = dataprop [ i*widthprop : (i+1)*widthprop ]
			flags[i] = enable, enirq, map_trigger_ena, map_set_ena, map_reset_ena, polarity
		return flags, delay, width, presc
		
	def setOpsPulse(self, flags, delay, width, presc):
		#TODO: Mols valors no els escric de debo!!
		vpulseparams = []
		vpulseproperties = []
		for i in range(self.TOTAL_PULSES):
			enable, enirq, map_trigger_ena, map_set_ena, map_reset_ena, polarity = flags[i]
			vpulseproperties += [polarity, map_reset_ena, map_set_ena, map_trigger_ena, enable]
			vpulseparams += [presc[i], delay[i], width[i]]
# 		#TODO: set2Dev enirq!!

		self.writeAttribute(
			'PulseParams', vpulseparams,
			dim_x = 3, dim_y = len(vpulseparams) / 3 )

		self.writeAttribute(
			'PulseProperties', vpulseproperties,
			dim_x = 5, dim_y = len(vpulseproperties) / 5)










	#############################################################
	####### ClockControl
	def getOpsClock(self):
		av = self.dp.read_attribute('InternalFrac')
		return (av.value,)

	def setOpsClock(self, syn):
		self.writeAttribute('InternalFrac', syn)





	#############################################################
	####### UnivOutControl
	def getOpsUnivOut(self):
		av = self.dp.read_attribute('UnivOut')
		return (av.value,)
		
	def setOpsUnivOut(self, maps):
		self.writeAttribute('UnivOut', maps)





	#############################################################
	####### PrescalerControl
	def getOpsPrescaler(self):
		av = self.dp.read_attribute('Prescalers')
		return (av.value,)
		
	def setOpsPrescaler(self, prescs):
		self.writeAttribute('Prescalers', prescs)




	#############################################################
	####### OthersControl
	def getOpsOthers(self):
		print self.dp.state()
		enmaster =  (self.dp.state() != PyTango.DevState.OFF)
		return (enmaster,)

	def setOpsOthers(self, enmaster):
		if enmaster:
			self.dp.On()
		else:
			self.dp.Off()







































class EvrAccessTangoConfig(EvrAccess):
	def __init__(self, url = 'timing/EventR/rec1'):
		if type(url) is PyTango.DeviceProxy:
			self.dp = url
		else:
			self.dp = PyTango.DeviceProxy(url)

	def deviceName(self):
		return self.dp.name()
	
	def deviceString(self):
		return 'tango-config:' + self.deviceName()


	def clearViolation(self):
		#we are just setting the default values, this method has no sense here
		pass


	#############################################################
	####### RamControl
	def getOpsRam(self):
		return [ self._getOpsRam(0), self._getOpsRam(1) ]
	
	def setOpsRam(self, ram0, ram1):
		self._setOpsRam(0, ram0[0], ram0[1])
		self._setOpsRam(1, ram1[0], ram1[1])

	def _getOpsRam(self, ram):
		assert(ram in range(2))
		prop_name = 'Ram' + str(ram)
		print prop_name
		prop_val = self.dp.get_property([prop_name])
		ramval = map(int, prop_val[prop_name])
		print ramval
		assert len(ramval) % 3 == 0
		sz = len(ramval)/3

		enable = True #TODO Ram enable
		ramEvents = {}
		for i in range(0, self.TOTAL_EVENT_CODE):
			ledev = 0 #TODO
			if (i < sz):
				trig, set, clear = ramval[3*i : 3*(i+1)]
			else:
				trig, set, clear = [0,0,0]
			if (trig | set | clear | ledev): aux = {'trigger' : trig, 'set' : set, 'clear' : clear, 'ledEvent' : ledev}
			else: aux = None
			if aux: ramEvents[i] = aux
		return (ramEvents, enable)

	def _setOpsRam(self, ram, ramEvents, enable):
		assert(ram in range(2))
		prop_name = 'Ram' + str(ram)

		val = []
		zeros = []
		for k in range(self.TOTAL_EVENT_CODE + 1):
			if ramEvents.has_key(k):
				v = ramEvents[k]
				val = val + zeros + [v['trigger'], v['set'], v['clear']]
				zeros = []
			else:
				#The others go to 0, or they'll appear agein later
				zeros += [0,0,0]

		if val == []:
			val = [0,0,0]
		prop_val={prop_name:val}
		self.dp.put_property(prop_val)



		

	#############################################################
	####### PulseControl
	def getOpsPulse(self):
		#TODO: Molts cmaps no son reals!!
		#TODO: getFromDev enirq
		flags = self.TOTAL_PULSES*[[0,0,0,0,0,0]]
		delay = self.TOTAL_PULSES*[0]
		width = self.TOTAL_PULSES*[0]
		presc = self.TOTAL_PULSES*[0]
		enirq = 0

		props = self.dp.get_property(['PulseParams', 'PulseProperties'])

		dataparams =  map(int,props['PulseParams'])
		widthparams = 3

		dataprop =  map(int,props['PulseProperties'])
		widthprop = 5

		def getPulseParams(index):
			presc = data[3*index + 0]
			delay = data[3*index + 1]
			width = data[3*index + 2]
			return presc, delay, width

# 		for i in range(0, self.TOTAL_PULSES):
		
		for i in range(0, len(dataparams)/3):
			presc[i], delay[i], width[i] = dataparams[widthparams*i : widthparams*(i+1)]
			polarity, map_reset_ena, map_set_ena, map_trigger_ena, enable = 0,0,0,0,0
			if len(dataprop) >= (i+1)*widthprop:
				polarity, map_reset_ena, map_set_ena, map_trigger_ena, enable = dataprop [ i*widthprop : (i+1)*widthprop ]
			flags[i] = enable, enirq, map_trigger_ena, map_set_ena, map_reset_ena, polarity
		return flags, delay, width, presc

	def setOpsPulse(self, flags, delay, width, presc):
		#TODO: Mols valors no els escric de debo!!
		vpulseparams = []
		vpulseproperties = []
		for i in range(self.TOTAL_PULSES):
			enable, enirq, map_trigger_ena, map_set_ena, map_reset_ena, polarity = flags[i]
			vpulseproperties += [polarity, map_reset_ena, map_set_ena, map_trigger_ena, enable]
			vpulseparams += [presc[i], delay[i], width[i]]
# 		#TODO: set2Dev enirq!!

		props = {'PulseParams':vpulseparams, 'PulseProperties':map(int,vpulseproperties)}
		self.dp.put_property(props)








	#############################################################
	####### ClockControl
	def getOpsClock(self):
		props = self.dp.get_property(['InternalFrac'])
		syn =  map(int, props['InternalFrac'])
		if len(syn):
			return(syn[0],)
		return (None,)

	def setOpsClock(self, syn):
		props = {'InternalFrac':[syn]}
		self.dp.put_property(props)





	#############################################################
	####### UnivOutControl
	def getOpsUnivOut(self):
		props = self.dp.get_property(['UnivOut'])
		maps = map(int, props['UnivOut'])
		if len(maps) < self.TOTAL_OUTPUT_PORTS:
			maps += (self.TOTAL_OUTPUT_PORTS-len(maps))*[0]
		return (maps,)

	def setOpsUnivOut(self, maps):
		props = {'UnivOut':maps}
		self.dp.put_property(props)





	#############################################################
	####### PrescalerControl
	def getOpsPrescaler(self):
		props = self.dp.get_property(['Prescalers'])
		prescs = map(int, props['Prescalers'])
		sz = len(prescs)
		if sz < self.TOTAL_PRESCALERS:
			prescs += (self.TOTAL_PRESCALERS-sz)*[0]
		return (prescs,)

	def setOpsPrescaler(self, prescs):
		props = {'Prescalers':prescs}
		self.dp.put_property(props)




	#############################################################
	####### OthersControl
	def getOpsOthers(self):
		props = self.dp.get_property(['MasterEnable'])
		enmaster = False
		if props['MasterEnable'] == ['true']:
			enmaster = True
		return (enmaster,)

	def setOpsOthers(self, enmaster):
		if enmaster:
			props = {'MasterEnable':['true']}
		else:
			props = {'MasterEnable':['false']}
		self.dp.put_property(props)


evrAccessFactoryDict['_default'] = [EvrAccessTango, (str, 'url')]
evrAccessFactoryDict['tango'] = [EvrAccessTango, (str, 'url')]
evrAccessFactoryDict['tangoconf'] = [EvrAccessTangoConfig, (str, 'url')]
