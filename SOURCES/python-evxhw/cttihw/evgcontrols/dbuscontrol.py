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

class DBusControl(PseudoControl):
	controlName = 'DBusControl'
	def __init__(self, ctrl):
		self.eva = ctrl.eva

		#Look at the dialog items it is controlling and
		#you will easily undertand why
		assert(self.eva.TOTAL_TRIGGERS == self.eva.TOTAL_DBUS_BITS)

		self.dbusMap = self.eva.TOTAL_DBUS_BITS * [None]
		sv = QScrollView(ctrl.gbDBus)
		fr = QGroupBox(sv.viewport())
		fr.setColumnLayout(0, Qt.Vertical)
		fr.setFlat(True)

		alt = 0
		for i in range(0,self.eva.TOTAL_DBUS_BITS):
			p = QButtonGroup("DBus" + str(i), fr)
			p.setFlat(True)
			p.setColumnLayout(0, Qt.Vertical)
			lo = QHBoxLayout(p.layout())
			lvd = QVBoxLayout(lo)
			lve = QVBoxLayout(lo)
			#The order is important: the id from selectedId()
			#comes from here. It must be the same as C_EVG_DBUS_SEL_*
			off = QRadioButton('off', p)
			ext = QRadioButton('ext', p)
			mxc = QRadioButton('mxc', p)
			fwd = QRadioButton('fwd', p)
			lvd.addWidget(off)
			lvd.addWidget(mxc)
			lve.addWidget(ext)
			lve.addWidget(fwd)
			fr.layout().add(p)
			alt += 0.85*p.frameSize().width()
			
			self.dbusMap[i] = p
		ctrl.gbDBus.layout().add(sv)
		fr.setGeometry(QRect(0,0,ctrl.gbDBus.frameSize().width()-50,alt))
		fr.updateGeometry()
		sz = fr.frameSize()
		sv.resizeContents(sz.width(), sz.height())
		sv.addChild(fr)
		sv.show()

	def getFromDev(self):
		return self.eva.getOpsDBus()

	def getFromForm(self):
		dbusMap = self.dbusMap
		dmap = self.eva.TOTAL_DBUS_BITS*[None]

		for i in range(0, self.eva.TOTAL_DBUS_BITS):
			aux = dbusMap[i].selectedId()
			if aux >= 0: dmap[i] = aux

		return (dmap,)


	def set2Dev(self, dmap):
		self.eva.setOpsDBus(dmap)
		
	def set2Form(self, dmap):
		dbusMap = self.dbusMap

		for i in range(0, self.eva.TOTAL_DBUS_BITS):
			if dmap[i]:
				dbusMap[i].setButton(dmap[i])
			else:
				dbusMap[i].setButton(0)












