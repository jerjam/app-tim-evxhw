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


#updated meu

from auxeg import *


class ACControl(PseudoControl):
	controlName = 'ACControl'
	def __init__(self, ctrl):
		self.eva = ctrl.eva
		self.acprescaler = ctrl.acPrescaler
		self.acdelay = ctrl.acDelay
		self.acsyncmxc7 = ctrl.acSyncMXC7
		self.acbypass = ctrl.acByPass
		self.actrigger = ctrl.acTrigger
		for i in range(0, self.eva.TOTAL_TRIGGERS):
			self.actrigger.insertItem("tr" + str(i))
		self.actrigger.insertItem("None")

	def getFromDev(self):
		return self.eva.getOpsAC()
	
	def getFromForm(self):
		pr = self.acprescaler.text().toUInt()
		dl = self.acdelay.text().toUInt()
		synmx7 = self.acsyncmxc7.isChecked()
		bypass = self.acbypass.isChecked()
		trigger = self.actrigger.currentItem()
		if trigger >= self.eva.TOTAL_TRIGGERS: trigger = None
		
		presc = None
		delay = None
		if pr[1]: presc = pr[0]
		if dl[1]: delay = dl[0]
		return presc, delay, synmx7, bypass, trigger

	def set2Dev(self, presc, delay, synmx7, bypass, trigger):
		self.eva.setOpsAC(presc, delay, synmx7, bypass, trigger)

	def set2Form(self, presc, delay, synmx7, bypass, trigger):
		self.acprescaler.setText(str(presc))
		self.acdelay.setText(str(delay))
		self.acsyncmxc7.setChecked(synmx7)
		self.acbypass.setChecked(bypass)
		if(trigger):
			self.actrigger.setCurrentItem(trigger)
		else:
			self.actrigger.setCurrentItem(self.eva.TOTAL_TRIGGERS)





































