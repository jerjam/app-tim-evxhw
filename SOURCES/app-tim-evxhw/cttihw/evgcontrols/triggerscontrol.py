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


class TriggersControl(PseudoControl):
	controlName = 'TriggersControl'
	def __init__(self, ctrl):
		self.eva = ctrl.eva

		self.ctTriggers = [
			(ctrl.enev_0, ctrl.trigev_0),
			(ctrl.enev_1, ctrl.trigev_1),
			(ctrl.enev_2, ctrl.trigev_2),
			(ctrl.enev_3, ctrl.trigev_3),
			(ctrl.enev_4, ctrl.trigev_4),
			(ctrl.enev_5, ctrl.trigev_5),
			(ctrl.enev_6, ctrl.trigev_6),
			(ctrl.enev_7, ctrl.trigev_7)
			]
		#about the assert:
		#If False because a different self.eva.TOTAL_TRIGGERS, the
		#dialog may need to be re-designed. If the new value is
		#lower than len(...), then it can be done here, rethinking
		#this class to allow disable the unused widgets. If the
		#new values is greather, go to designer (or create it
		#here, dinamically)
		assert(len(self.ctTriggers) == self.eva.TOTAL_TRIGGERS)

	controlEnable = 0
	controlValue = 1
			
	def getFromDev(self):
		return self.eva.getOpsTriggers()

	def getFromForm(self):
		ct = self.ctTriggers
		ts = 0
		eventcodes = len(ct)*[None]
		eventenables = len(ct)*[None]
		for i in range(0, len(ct)):
			eventenables[i] = ct[i][self.controlEnable].isOn()
			n = ct[i][self.controlValue].text().toUInt()
			if n[1]:
				eventcodes[i] = n[0]
		return eventenables, eventcodes

	def set2Dev(self, eventenables, eventcodes):
		self.eva.setOpsTriggers(eventenables, eventcodes)

	def set2Form(self, eventenables, eventcodes):
		ct = self.ctTriggers

		for i in range(0, len(ct)):
			btSetState(ct[i][self.controlEnable], eventenables[i])
			ct[i][self.controlValue].setText(str(eventcodes[i]))









