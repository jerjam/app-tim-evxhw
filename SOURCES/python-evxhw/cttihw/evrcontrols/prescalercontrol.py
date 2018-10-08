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


class PrescalerControl(PseudoControl):
	controlName = 'PrescalerControl'
	
	def __init__(self, ctrl):
		self.eva = ctrl.eva
		self.ctList = ctrl.prescalerOutputs
		
		self.ctList.setNumRows(self.eva.TOTAL_PRESCALERS)
		for i in range(0, self.eva.TOTAL_PRESCALERS):
			self.ctList.verticalHeader().setLabel(i, str(i))
		
	def getFromDev(self):
		return self.eva.getOpsPrescaler()
		
	def getFromForm(self):
		ctlist = self.ctList
		prescs = self.eva.TOTAL_PRESCALERS*[0]
		for i in range(0, self.eva.TOTAL_PRESCALERS):
			aux = ctlist.text(i,0).toUInt()
			if not aux[1]:
				ctlist.setText(i,0,'ERROR')
			prescs[i] = aux[0]
		return (prescs,)
		
	def set2Dev(self, prescs):
		self.eva.setOpsPrescaler(prescs)
	
	def set2Form(self, prescs):
		ctlist = self.ctList
		for i in range(0, self.eva.TOTAL_PRESCALERS):
			ctlist.setText(i,0,str(prescs[i]))






