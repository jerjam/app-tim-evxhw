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

import mevrconst

class MPulse:
	def __init__(self):
		self.delay = 0
		self.width = 1
		self.prescaler = None
		self.polarityActiveHigh = True
		self.tmaster = False
		self.tpulse = False
		self.tset = False
		self.tclear = False

	def set_trigger_enable(self, tmaster, tpulse, tset, tclear):
		self.tmaster = tmaster
		self.tpulse = tpulse
		self.tset = tset
		self.tclear = tclear

	def get_trigger_enable(self):
		return [ self.tmaster, self.tpulse, self.tset, self.tclear ]
		

class MPulseList:
	TotalPrescalers = 4
	def __init__(self):
		self.pulseNames = ['PULSE ' + str(i) for i in xrange(10)]
		self.pulses = [ MPulse() for x in xrange(10) ]
		for p in self.pulses[:MPulseList.TotalPrescalers]:
			p.prescaler = 1

class MEvent:
	FlagFIFOSaveEvent = 0
	FlagLogSaveEvent = 1
	FlagLogStopEvent = 2
	FlagLatchTimestamp = 3
	FlagLedEvent = 4
	FlagForwardEvent  = 5
	FlagHeartbeatEvent = 6
	FlagResetprescEvent = 7
	FlagTimestampReset = 8
	FlagTimestampClk = 9
	FlagSeconds1 = 10
	FlagSeconds0 = 11
	def __init__(self):
		self.trigger = 10*[False]
		self.set = 10*[False]
		self.clear = 10*[False]
		self.flags = 12*[False]

class MRam:
	def __init__(self):
		self.set_event_names( {} )
		self.events = [ MEvent() for x in xrange(256) ]

	def set_event_names(self, evNames):
		self.eventNames = [ 'EV-' + str(x) for x in xrange(256)]
		for k in evNames:
			self.eventNames [evNames[k]] = k
		self.eventNamesIndex = evNames
		# We also save, just for ease of use, a dict 'EVNAME' : evnumber
		# that contains all the events, also the unnamed ones (as EV-NUM)
		self.eventNamesIndexFull = dict(
							zip(self.eventNames, xrange(len(self.eventNames))) )

class MOutput:
	OutPulse0 = mevrconst.SIGNAL_MAP_PULSE
	OutDBus0 = mevrconst.SIGNAL_MAP_DBUS
	OutPresc0 = mevrconst.SIGNAL_MAP_PRESC
	OutHigh = mevrconst.SIGNAL_MAP_HIGH
	OutLow = mevrconst.SIGNAL_MAP_LOW
	def __init__(self, val=OutLow):
		self.output = val

class MInput:
	def __init__(self):
		# accept 0-255 or None
		self.backEvent = None
		self.backEdge = None
		self.backLevel = None
		self.extEvent = None
		self.extEdge = None
		self.extLevel = None
		self.extEdgeSensitivity = None
		self.extLevelSensitivity = None

class FPOutput:
	OutPulse0 = mevrconst.SIGNAL_MAP_PULSE
	OutDBus0 = mevrconst.SIGNAL_MAP_DBUS
	OutHigh = mevrconst.SIGNAL_MAP_HIGH
	OutLow = mevrconst.SIGNAL_MAP_LOW
	def __init__(self, val=OutLow):
		self.output = val

class CML:
	def __init__(self, value=False):
		self.enable = value

class FineDelay:
	def __init__(self, value=0):
		self.fine_delay = value

# Only get_* methods! See ReceiverConfigurableModel for set_* ones
class MReceiver:
	def __init__(self):
		#Common
		self.mpulses = MPulseList()
		self.mram = MRam()
		#EVR230 only
		self.moutputs = [ MOutput() for x in xrange(10)]
		self.minputs = [ MInput() for x in xrange(2)]
		self.mcounters = 3 * [0]
		#EVR300 only
		self.fpoutputs = [ FPOutput() for x in xrange(8)]
		self.cml = [ CML() for x in xrange(8)]
		self.fine_delays = [ FineDelay() for x in xrange(8)]

	def get_pulse_names(self):
		return self.mpulses.pulseNames

	def get_pulse_trigger_enable(self, pulseId):
		return self.mpulses.pulses[pulseId].get_trigger_enable()

	def get_pulse_polarity(self, pulseId):
		return self.mpulses.pulses[pulseId].polarityActiveHigh

	def get_pulse_delay(self, pulseId):
		return self.mpulses.pulses[pulseId].delay

	def get_pulse_width(self, pulseId):
		return self.mpulses.pulses[pulseId].width

	def get_pulse_prescaler(self, pulseId):
		return self.mpulses.pulses[pulseId].prescaler

	def get_event_name(self, ev):
		return self.mram.eventNames[ev]

	def get_event_id(self, name):
		name = str(name)
		if name in self.mram.eventNamesIndexFull:
			return self.mram.eventNamesIndexFull[name]
		return None

	def get_event_names(self):
		return self.mram.eventNamesIndex

