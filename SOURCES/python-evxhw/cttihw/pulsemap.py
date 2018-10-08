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


from auxer import *
from pulsemapform import PulseMapForm

#Used to edit the mapping between an event and the triggers it generates. It's only intended to be called from the runMappingDialog() function of evrcontrols.ramcontrol

class PulseMap(PulseMapForm):
	def __init__(self, parent=None, name=None, fl=0):
		PulseMapForm.__init__(self, parent, name, fl)
		
		self.TOTAL_PULSES = 10
		
		self.ctTrig = [
			self.trig_0,self.trig_1,
			self.trig_2,self.trig_3,
			self.trig_4,self.trig_5,
			self.trig_6,self.trig_7,
			self.trig_8,self.trig_9,
			self.trig_10,self.trig_11,
			self.trig_12,self.trig_13,
			self.trig_14,self.trig_15,
			self.trig_16,self.trig_17,
			self.trig_18,self.trig_19,
			self.trig_20,self.trig_21,
			self.trig_22,self.trig_23,
			self.trig_24,self.trig_25,
			self.trig_26,self.trig_27,
			self.trig_28,self.trig_29,
			self.trig_30,self.trig_31 ]
			
		self.ctSet = [
			self.set_0,self.set_1,
			self.set_2,self.set_3,
			self.set_4,self.set_5,
			self.set_6,self.set_7,
			self.set_8,self.set_9,
			self.set_10,self.set_11,
			self.set_12,self.set_13,
			self.set_14,self.set_15,
			self.set_16,self.set_17,
			self.set_18,self.set_19,
			self.set_20,self.set_21,
			self.set_22,self.set_23,
			self.set_24,self.set_25,
			self.set_26,self.set_27,
			self.set_28,self.set_29,
			self.set_30,self.set_31 ]
			
		self.ctClear = [
			self.clear_0,self.clear_1,
			self.clear_2,self.clear_3,
			self.clear_4,self.clear_5,
			self.clear_6,self.clear_7,
			self.clear_8,self.clear_9,
			self.clear_10,self.clear_11,
			self.clear_12,self.clear_13,
			self.clear_14,self.clear_15,
			self.clear_16,self.clear_17,
			self.clear_18,self.clear_19,
			self.clear_20,self.clear_21,
			self.clear_22,self.clear_23,
			self.clear_24,self.clear_25,
			self.clear_26,self.clear_27,
			self.clear_28,self.clear_29,
			self.clear_30,self.clear_31 ]
			
		for i in range (self.TOTAL_PULSES, len(self.ctClear)):
			self.ctTrig[i].hide()
			self.ctSet[i].hide()
			self.ctClear[i].hide()
			
			
		self.ctLed = self.led_event
	
	def loadValues(self, trig, set, clear, led):
		for i in range(0, self.TOTAL_PULSES):
			btSetState(self.ctTrig[i], trig & (1 << i))
		for i in range(0, self.TOTAL_PULSES):
			btSetState(self.ctSet[i], set & (1 << i))
		for i in range(0, self.TOTAL_PULSES):
			btSetState(self.ctClear[i], clear & (1 << i))
		self.ctLed.setChecked(led)

	def getValues(self):
		trig = 0
		set = 0
		clear = 0
		for i in range(0, self.TOTAL_PULSES):
			if self.ctTrig[i].isOn(): trig |= (1 << i)
		for i in range(0, self.TOTAL_PULSES):
			if self.ctSet[i].isOn(): set |= (1 << i)
		for i in range(0, self.TOTAL_PULSES):
			if self.ctClear[i].isOn(): clear |= (1 << i)
		led = self.ctLed.isChecked()
		return trig, set, clear, led

































