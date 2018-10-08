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
import mevg
import time

class EvgAccessLocal(EvgAccess):
	def __init__(self, url = '/dev/evs/g12'):
		self.ev = mevg.new(url)
		self._url = url
	

	def deviceName(self):
		return self._url
	
	def deviceString(self):
		return 'local:' + self.deviceName()

	def runSequence(self, seq):
		self.ev.SeqRamSWTrig(seq)

	def sendSwEvent(self, ev):
		self.ev.SendSWEvent(ev)

	#############################################################
	####### ACControl
	def getOpsAC(self):
		ev = self.ev
		#presc = ev.GetACPrescaler()
		#delay = ev.GetACDelay()
		#synmx7 = ev.GetACSyncMXC()
		#bypass = ev.GetACByPass()
		bypass, synmx7, presc, delay = ev.GetACInput()
		trigger = ev.GetACMap()
		if trigger < 0: trigger = None
		return presc, delay, synmx7, bypass, trigger

	def setOpsAC(self, presc, delay, synmx7, bypass, trigger):
		ev = self.ev
		#ev.SetACPrescaler(presc)
		#ev.SetACDelay(delay)
		#ev.SetACSyncMXC(synmx7)
		ev.SetACInput(bypass, synmx7, presc, delay)
		if not trigger == None:
			ev.SetACMap(trigger)
		else:
			ev.ResetACMap()

	#############################################################
	####### ClockControl

	def getOpsClock(self):
		ev = self.ev
		rftype, rfdiv = ev.GetRFInput()
		syn = ev.GetInternalFrac()
		return rftype, rfdiv, syn

	def setOpsClock(self, rftype, rfdiv, syn):
		ev = self.ev
		ev.SetInternalFrac(syn)
		ev.SetRFInput(rftype, rfdiv)
		#Sequences and maybe other things wont be able to be enabled until the clock is locked
		retry = 10
		while not ev.ClockIsCGLocked():
			time.sleep(0.1)
			retry -= 1
			if retry < 0:
				raise "Problems setting clock"


	#############################################################
	####### DataBufferControl
	#TODO:  DataBufferControl


	
	#############################################################
	####### DBusControl
	def getOpsDBus(self):
		ev = self.ev
		dmap = self.TOTAL_DBUS_BITS*[None]

		for i in range(0, self.TOTAL_DBUS_BITS):
			aux = ev.GetDBusMap(i)
			if aux >= 0: dmap[i] = aux

		return (dmap,)


	def setOpsDBus(self, dmap):
		ev = self.ev
		for i in range(0, self.TOTAL_DBUS_BITS):
			if dmap[i]:
				ev.SetDBusMap(i, dmap[i])
			else:
				ev.SetDBusMap(i, self.DBUS_SEL_OFF)


	#############################################################
	####### Front Panel Univ I/O Control
	def getOpsUnivIn(self):
		ev = self.ev
		dbus = self.TOTAL_INPUT_PORTS * [-1]
		trig = self.TOTAL_INPUT_PORTS * [-1]
		
		for i in range(0, self.TOTAL_INPUT_PORTS):
			trig[i], dbus[i] = ev.GetUnivinMap(i)
		return (dbus,trig)

	def setOpsUnivIn(self, dbus, trig):
		ev = self.ev
		for i in range(0, self.TOTAL_INPUT_PORTS):
			ev.SetUnivinMap(i, trig[i], dbus[i])


	#############################################################
	####### MXCTableControl
	def getOpsMXCTable(self):
		ev = self.ev
		prescs = self.TOTAL_MXCS*[None]
		for i in range(0, len(prescs)):
			prescs[i] = ev.GetMXCPrescaler(i)
		#polarities = ev.GetMXCPolarity()
		#return (prescs,polarities,)
		trigmap = self.TOTAL_MXCS*[None]
		for i in range(0, len(trigmap)):
			trigmap[i] =  ev.GetMxcTrigMap(i)
			if trigmap[i] < 0: trigmap[i] = None;
		return (prescs,trigmap)

	def setOpsMXCTable(self, prescs, trigmap):
		ev = self.ev
		for i in range(0, len(prescs)):
			ev.SetMXCPrescaler(i, prescs[i])
			if trigmap[i] != None:
				ev.SetMxcTrigMap(i, trigmap[i])
			else:
				ev.ResetMxcTrigMap(i)
		#ev.SetMXCPolarity(polarities)

	#############################################################
	####### OthersControl
	def getOpsOthers(self):
		ev = self.ev
		enswev = ev.GetSWEventEnable()
		enmast = ev.GetEnable()
		
		return enswev, enmast

	def setOpsOthers(self, enswev, enmast):
		ev = self.ev
		ev.SWEventEnable(enswev)
		ev.Enable(enmast)

	#############################################################
	####### TriggersControl
	def getOpsTriggers(self):
		ev = self.ev
		eventcodes = self.TOTAL_TRIGGERS*[0]
		eventenables = self.TOTAL_TRIGGERS*[0]
		for i in range(0, len(eventcodes)):
			eventcodes[i], eventenables[i] = ev.GetTriggerEvent(i)
		return eventenables, eventcodes

	def setOpsTriggers(self, eventenables, eventcodes):
		ev = self.ev
		for i in range(0, len(eventcodes)):
			if eventcodes[i] != None:
				ev.SetTriggerEvent(i, eventcodes[i], eventenables[i])

	#############################################################
	####### SequenceEditor
	def getOpsSequenceEditor(self, rs):
		ev = self.ev
		seqen, single, recycle, trigsel = ev.SeqRamGetControl(rs)

		seq = []
		for i in range(0, self.MAX_SEQRAMEV):
			ts, ec = ev.GetSeqRamEvent(rs, i)
			#Just like in EvgSeqRamDump, event code 0 means do not show
			if ec != 0:
				seq += [(ts, ec)]

		return seq, seqen, trigsel, single, recycle

	def setOpsSequenceEditor(self, rs, seq, seqen, trigsel, single, recycle):
		ev = self.ev

		for i in range(0, len(seq)):
			ts = seq[i][0]
			ec = seq[i][1]
			ev.SetSeqRamEvent(rs, i, ts, ec)
		for i in range(len(seq), self.MAX_SEQRAMEV):
			ev.SetSeqRamEvent(rs, i, 0, 0)

		ev.SeqRamControl(rs, int(seqen), single, recycle, 0, trigsel)





evgAccessFactoryDict['_default'] = [EvgAccessLocal, (str, 'device')]
evgAccessFactoryDict['local'] = [EvgAccessLocal, (str, 'device')]

