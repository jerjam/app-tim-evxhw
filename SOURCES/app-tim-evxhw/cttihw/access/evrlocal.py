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
import mevr


class EvrAccessLocal(EvrAccess):
	def __init__(self, url = '/dev/evs/r13'):
		self.ev = mevr.new(url)
		self._url = url


	def clearViolation(self):
		self.ev.GetViolation(True)


	def deviceName(self):
		return self._url
	
	def deviceString(self):
		return 'local:' + self.deviceName()









	#############################################################
	####### RamControl
	def getOpsRam(self):
		return [ self._getOpsRam(0), self._getOpsRam(1) ]

	def setOpsRam(self, ram0, ram1):
		ev = self.ev
		self._setOpsRam(0, ram0[0], ram0[1])
		self._setOpsRam(1, ram1[0], ram1[1])
		#Only one enabled or disable all
		if ram0[1]:
			ev.MapRamEnable(0, True)
		elif ram1[1]:
			ev.MapRamEnable(1, True)
		else:
			ev.MapRamEnable(0, False)
	
	def _getOpsRam(self, ram):
		ev = self.ev
		ramEvents = {}
		for i in range(1,self.TOTAL_EVENT_CODE+1):
			trig, set, clear = ev.GetPulseMapEx(ram, i)
			ledev = ev.GetLedEvent(ram, i)
			if (trig | set | clear | ledev): aux = {'trigger' : trig, 'set' : set, 'clear' : clear, 'ledEvent' : ledev}
			else: aux = None
			if aux: ramEvents[i] = aux
		enable = ev.GetMapRamEnable(ram)
		return (ramEvents, enable)

	def _setOpsRam(self, ram, ramEvents, enable):
		ev = self.ev
		
		for k in range(1,self.TOTAL_EVENT_CODE+1):
			if ramEvents.has_key(k):
				v = ramEvents[k]
				ev.SetPulseMapEx(ram, k, v['trigger'], v['set'], v['clear'])
				ev.SetLedEvent(ram, k, v['ledEvent'])
			else:
				#The others go to 0, or they'll appear agein later
				ev.SetPulseMapEx(ram, k, 0, 0, 0)
				ev.SetLedEvent(ram, k, 0)






	#############################################################
	####### PulseControl
	def getOpsPulse(self):
		ev = self.ev
		#TODO: getFromDev enirq
		flags = self.TOTAL_PULSES*[[0,0,0,0,0,0]]
		delay = self.TOTAL_PULSES*[0]
		width = self.TOTAL_PULSES*[0]
		presc = self.TOTAL_PULSES*[0]
		enirq = 0
		for i in range(0, self.TOTAL_PULSES):
			presc[i], delay[i], width[i] = ev.GetPulseParams(i)
			polarity, enclean, enset, entrigger, enmaster = ev.GetPulseProperties(i)
			flags[i] = enmaster, enirq, entrigger, enset, enclean, polarity
		return flags, delay, width, presc
		
	def setOpsPulse(self, flags, delay, width, presc):
		ev = self.ev
		i=5
		#time.sleep(1)
		ev.GetViolation(1)
		print i, presc[i], delay[i], width[i]
		for i in range(0, self.TOTAL_PULSES):
			enmaster, enirq, entrigger, enset, enclean, polarity = flags[i]
			ev.SetPulseParams(i, presc[i], delay[i], width[i])
			ev.SetPulseProperties(i, polarity, enclean, enset, entrigger, enmaster)
		#TODO: set2Dev enirq!!






	#############################################################
	####### ClockControl
	def getOpsClock(self):
		ev = self.ev
		syn = ev.GetInternalFrac()
		return (syn,)

	def setOpsClock(self, syn):
		ev = self.ev
		ev.SetInternalFrac(syn)





	#############################################################
	####### UnivOutControl
	def getOpsUnivOut(self):
		ev = self.ev
		maps = self.TOTAL_OUTPUT_PORTS * [0]
		
		for i in range(0, self.TOTAL_OUTPUT_PORTS):
			maps[i] = ev.GetUnivOutMap(i)
		return (maps,)
		
	def setOpsUnivOut(self, maps):
		ev = self.ev
		for i in range(0, self.TOTAL_OUTPUT_PORTS):
			ev.SetUnivOutMap(i, maps[i])





	#############################################################
	####### PrescalerControl
	def getOpsPrescaler(self):
		ev = self.ev
		prescs = self.TOTAL_PRESCALERS*[0]
		for i in range(0, self.TOTAL_PRESCALERS):
			prescs[i] = ev.GetPrescaler(i)
		return (prescs,)
		
	def setOpsPrescaler(self, prescs):
		ev = self.ev
		for i in range(0, self.TOTAL_PRESCALERS):
			v = prescs[i]
			ev.SetPrescaler(i, v)




	#############################################################
	####### OthersControl
	def getOpsOthers(self):
		ev = self.ev
		enmaster = ev.GetEnable()
		return (enmaster,)

	def setOpsOthers(self, enmaster):
		ev = self.ev
		ev.Enable(enmaster)


evrAccessFactoryDict['_default'] = [EvrAccessLocal, (str, 'device')]
evrAccessFactoryDict['local'] = [EvrAccessLocal, (str, 'device')]


