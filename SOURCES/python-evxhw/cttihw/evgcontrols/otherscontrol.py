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

class OthersControl(PseudoControl):
	controlName = 'OthersControl'
	def __init__(self, ctrl):
		self.eva = ctrl.eva
		self.enswev = ctrl.swEventEnable
		self.enmast = ctrl.masterEnable
		
	def getFromDev(self):
		return self.eva.getOpsOthers()
	
	def getFromForm(self):
		enswev = self.enswev.isChecked()
		enmast = self.enmast.isChecked()
		
		return enswev, enmast

	def set2Dev(self, enswev, enmast):
		self.eva.setOpsOthers(enswev, enmast)
		
	def set2Form(self, enswev, enmast):
		self.enswev.setChecked(enswev)
  		self.enmast.setChecked(enmast)













