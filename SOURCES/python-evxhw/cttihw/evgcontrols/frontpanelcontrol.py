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



from auxeg import *


class UnivInControl (PseudoControl):
	controlName = 'UnivInControl'
	
	def __init__(self, ctrl):
		self.eva = ctrl.eva


		self.ctPorts = [
			(ctrl.fp0,  ctrl.fp1),
			(ctrl.fp2,  ctrl.fp3),
			(ctrl.fp4,  ctrl.fp5),
			(ctrl.fp6,  ctrl.fp7),
			(ctrl.fp8,  ctrl.fp9),
			(ctrl.fp10, ctrl.fp11),
			(ctrl.fp12, ctrl.fp13),
			(ctrl.fp14, ctrl.fp15),
			(ctrl.fp16, ctrl.fp17),
			(ctrl.fp18, ctrl.fp19)
		]
		for i in range(0, self.eva.TOTAL_INPUT_PORTS):
			for n in range(0, self.eva.TOTAL_DBUS_BITS):
				self.ctPorts[i][0].insertItem('DBUS ' + str(n))
			for n in range(0, self.eva.TOTAL_TRIGGERS):
				self.ctPorts[i][1].insertItem('TRIG ' + str(n))
			self.ctPorts[i][0].insertItem('NONE')
			self.ctPorts[i][1].insertItem('NONE')
		for i in range(self.eva.TOTAL_INPUT_PORTS, len(self.ctPorts)):
			self.ctPorts[i][0].setEnabled(False)
			self.ctPorts[i][1].setEnabled(False)
		
	def getFromDev(self):
		return self.eva.getOpsUnivIn()
	
	def getFromForm(self):
		ports = self.ctPorts
		dbus =  self.eva.TOTAL_INPUT_PORTS * [0]
		trig =  self.eva.TOTAL_INPUT_PORTS * [0]
		for i in range(0, self.eva.TOTAL_INPUT_PORTS):
			dbus[i] = ports[i][0].currentItem()
			if dbus[i] == self.eva.TOTAL_DBUS_BITS:
				dbus[i]=-1
			trig[i] = ports[i][1].currentItem()
			if trig[i] == self.eva.TOTAL_TRIGGERS:
				trig[i]=-1
		return (dbus,trig,)
			
	def set2Dev(self, dbus, trig):
		self.eva.setOpsUnivIn(dbus, trig)
			
	def set2Form(self, dbus, trig):
		ports = self.ctPorts
		for i in range(0, self.eva.TOTAL_INPUT_PORTS):
			if dbus[i] not in range(0, self.eva.TOTAL_DBUS_BITS):
				ports[i][0].setCurrentItem(self.eva.TOTAL_DBUS_BITS)
			else:
				ports[i][0].setCurrentItem(dbus[i])

			if trig[i] not in range(0, self.eva.TOTAL_TRIGGERS):
				ports[i][1].setCurrentItem(self.eva.TOTAL_DBUS_BITS)
			else:
				ports[i][1].setCurrentItem(trig[i])
			


























