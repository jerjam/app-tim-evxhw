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

#TODO: test & assegurar que la nova versio de SetSize que em doni sigui compatible, allo de si cal dividir per 4 o no ...
#TODO: hi ha flags de databuffer que han d'anar a la finestra destatus
#TODO: el tal databuf trigger no lestic tractant i hauria d'anar aqui
from auxeg import *


class DataBufferControl(PseudoControl):
	controlName = 'DataBufferControl'
	def __init__(self, ctrl):
		self.eva = ctrl.eva
		self.dbtable = ctrl.dataBufData
		self.dbsize = ctrl.dataBufSize
		self.dbenable = ctrl.dataBufEnable
		self.dbmode = ctrl.dataBufMode

	###########################################
	#Control and status
	def getFromDev(self):
		evg = self.evg
		en = evg.DataBufferGetEnable()
		md = evg.DataBufferGetMode()
		sz = evg.DataBufferGetSize()
		bf = sz*[0]
		for i in range(0,sz):
			bf[i] = evg.DataBufferRead(i)
		return en, md, bf

	def getFromForm(self):
		tb = self.dbtable
		en = self.dbenable.isChecked()
		md = self.dbmode.isChecked()
		sz = self.dbsize.text().toUInt()
		if sz[1]: sz = sz[0]
		else: sz = 1
		bf = sz * [None]
		for i in range(0, sz):
			val = tb.text(i,0).toUInt()
			if val[1]: bf[i] = val[0]
		return en, md, bf
	
	def set2Dev(self, en, md, bf):
		evg = self.evg
		sz = len(bf)
		evg.DataBufferSetSize(sz)
		for i in range(0, sz):
			if bf[i]: evg.DataBufferWrite(i, bf[i])
		evg.DataBufferMode(md)
		evg.DataBufferEnable(en)
	
	def set2Form(self, en, md, bf):
		tb = self.dbtable
		self.dbenable.setChecked(en)
		self.dbmode.setChecked(md)
		sz = len(bf)
		self.dbsize.setText(str(sz))
		tb.setNumRows(sz)
		for i in range(0, sz):
			tb.setText(i,0, str(bf[i]))

	######################################################
	#Actions
	def changingSizeField(self):
		szct = self.dbsize
		tb = self.dbtable
		sz = szct.text().toUInt()
		if sz[1]: sz = sz[0]
		else: sz = 1
 		if sz < 1: sz=1
		if sz % 4 != 0: sz += (4 - sz % 4)
		szct.setText(str(sz))
		szct.selectAll()
		tb.setNumRows(sz)
		
	def sendDataBuf(self):
		evg = self.evg
		evg.DataBufferSend()
		


























