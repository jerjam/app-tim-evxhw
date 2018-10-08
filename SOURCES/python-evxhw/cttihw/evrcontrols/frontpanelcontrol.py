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


class UnivOutControl (PseudoControl):
	controlName = 'UnivOutControl'
	
	def __init__(self, ctrl):
		self.eva = ctrl.eva
		mappings = []

		for i in range(self.eva.TOTAL_PULSES):
			mappings += [ ( 'PULSE ' + str(i), self.eva.SIGNAL_MAP_PULSE + i ) ]
		for i in range(8):
			mappings += [ ( 'DBUS ' + str(i), self.eva.SIGNAL_MAP_DBUS + i ) ]
		for i in range(self.eva.TOTAL_PRESCALERS):
			mappings += [ ( 'PRESC ' + str(i), self.eva.SIGNAL_MAP_PRESC + i ) ]

		self.mappings = mappings
        #EVR max outputs are 12
		self.ctPorts = [
			ctrl.fp0,
			ctrl.fp1,
			ctrl.fp2,
			ctrl.fp3,
			ctrl.fp4,
			ctrl.fp5,
			ctrl.fp6,
            ctrl.fp7,
            ctrl.fp8,
            ctrl.fp9,
            ctrl.fp10,
            ctrl.fp11 ]

		for i in range(0, self.eva.TOTAL_OUTPUT_PORTS):
			for m in mappings:
				self.ctPorts[i].insertItem(m[0])
		for i in range(self.eva.TOTAL_OUTPUT_PORTS, len(self.ctPorts)):
			self.ctPorts[i].setEnabled(False)
		
	def getFromDev(self):
		return self.eva.getOpsUnivOut()
	
	def getFromForm(self):
		ports = self.ctPorts
		mappings = self.mappings
		maps =  self.eva.TOTAL_OUTPUT_PORTS * [0]
		for i in range(0, self.eva.TOTAL_OUTPUT_PORTS):
			maps[i] = mappings[ports[i].currentItem()][1]
		return (maps,)
			
	def set2Dev(self, maps):
		self.eva.setOpsUnivOut(maps)
			
	def set2Form(self, maps):
		ports = self.ctPorts
		#rsune 20080304 
		for i in range(0, self.eva.TOTAL_OUTPUT_PORTS):
		#for i in range(0, len(maps)):
			ports[i].setCurrentItem(self.reverseMap(maps[i]))
			
	def reverseMap(self, mapp):
		mapping = self.mappings
		i = 0
		for m in mapping:
			if m[1] == mapp: return i
			i += 1
		return 0



