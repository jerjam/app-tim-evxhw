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
# from qttable import QTable

#Older versions of the EVR had a polarity flag for the MXCs. If this feature came back, just uncomment some lines here


class MXCTableControl(PseudoControl):
	controlName = 'MXCTableControl'

	def __init__(self, ctrl):
		self.eva = ctrl.eva
		self.table = ctrl.mxcTable
	
	columnPrescaler = 0
	#columnPolarity = 1
	columnTrigger = 1 #2

	def getFromDev(self):
		return self.eva.getOpsMXCTable()

	def getFromForm(self):
		tb = self.table
		prescs = self.eva.TOTAL_MXCS*[None]
		trigmap = self.eva.TOTAL_MXCS*[None]
		#polarities = 0
		for i in range(0, len(prescs)):
			val = tb.text(i, self.columnPrescaler).toUInt()
			if val[1]: prescs[i] = val[0]
			
			#pol = str(tb.text(i, self.columnPolarity))
			#if pol == "1": polarities |= (1 << i)
			
			val = tb.text(i, self.columnTrigger).toUInt()
			if val[1]: trigmap[i] = val[0]

		return (prescs,trigmap)

	def set2Dev(self, prescs, trigmap):
		self.eva.setOpsMXCTable(prescs, trigmap)
	
	def set2Form(self, prescs, trigmap):
		tb = self.table
		for i in range(0, len(prescs)):
			v = prescs[i]
			tb.setText(i,self.columnPrescaler, str(v))
			#if polarities & (1 << i):
			#	tb.setText(i,self.columnPolarity,"1")
			#else:
			#	tb.setText(i,self.columnPolarity,"0")
			v = trigmap[i]
			tb.setText(i,self.columnTrigger, str(v))
	
	def valueChanged(self, row, col ):
		tb = self.table
		txt = tb.text(row,col)
		tv = txt.toUInt()
		if col == self.columnPrescaler:
			if not tv[1]:
				return tbSetError(tb, row, col)
# 		elif col == self.columnPolarity:
# 			if not tv[1] or tv[0] not in range(0,2):
# 				return tbSetError(tb, row, col)
		elif col == self.columnTrigger:
			if not tv[1] or tv[0] not in range(self.eva.TOTAL_TRIGGERS):
				return tbSetError(tb, row, col)
	




















