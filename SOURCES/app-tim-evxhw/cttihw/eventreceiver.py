#!/usr/bin/env python

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

from qt import *
import pickle
from eventreceiverform import EventReceiverForm
from evrcontrols.ramcontrol import RamControl
from evrcontrols.pulsecontrol import PulseControl
from evrcontrols.interruptcontrol import InterruptControl
from evrcontrols.prescalercontrol import PrescalerControl
from evrcontrols.frontpanelcontrol import UnivOutControl
from evrcontrols.clockcontrol import ClockControl
from evrcontrols.otherscontrol import OthersControl


import time

import evaccess
#import access.evrtango
try:
	import access.evrlocal
except:
	print 'This expert GUI can only be run on the machine in which the EVR is installed'
	exit(-1)

import xml.dom.minidom

class EventReceiver(EventReceiverForm):
	def __init__(self, parent=None, name=None, fl=0):
		EventReceiverForm.__init__(self, parent, name, fl)

		self.eva = evaccess.OpenDevice(access.evr.evrAccessFactoryDict)

		caption = self.eva.deviceString() + '  -  Event Receiver'
		self.setCaption(caption)

		self.setDefaultBt.setEnabled(self.eva.canSetDefault())

		self.ram_control = RamControl(self)
		self.pulse_control = PulseControl(self)
		self.interrupt_control = InterruptControl(self)
		self.univ_out_control = UnivOutControl(self)
		self.clock_control = ClockControl(self)
		self.others_control = OthersControl(self)
		self.prescaler_control = PrescalerControl(self)

		self.myControls = [
			self.prescaler_control,
			self.ram_control,
			self.pulse_control,
# 			self.interrupt_control,
			self.univ_out_control,
			self.clock_control,
			self.others_control,
			]





	def clearInterrupts_clicked(self):
		self.eva.clearViolation()

	def ramClear_clicked(self):
		self.ram_control.clearMappings()
	def ramDel_clicked(self):
		self.ram_control.deleteMapping()
	def ramMod_clicked(self):
		self.ram_control.modifyMapping()
	def ramEnable_toggled(self, status):
		self.ram_control.changeEnable(status)
	def ramList_clicked(self, item):
		self.ram_control.changeSelected(item)
	def ramList_doubleClicked(self, item):
		if item:
			self.ram_control.changeSelected(item)
			self.ram_control.modifyMapping(item.text(0).toUInt()[0])
	def ramSel_activated(self, index):
		self.ram_control.changeRam(index)
		

		
	def listPulse_doubleClicked(self, item):
		self.pulse_control.modify(item)





	def onRestoreConfig(self, controls=None):
		self.setEnabled(False)
		try:
			if controls == None: controls=self.myControls
			for el in controls:
				try:
					el.restore()
				except:
					print 'restore error ('+ el.controlName +')'
					raise
		finally:
			self.setEnabled(True)

	def onApplyConfig(self):
		self.setEnabled(False)
		try:
			for el in self.myControls:
				try:
					el.applyConf()
					self.eva.clearViolation()
				except:
					print 'apply error ('+ el.controlName +')'
					raise
			#time.sleep(1)
			self.eva.clearViolation()
			self.onRestoreConfig()
		finally:
			self.setEnabled(True)


	def file_io(self, saving):
		if saving:
# 			doc = xml.dom.minidom.Document()
# 			doc2 = doc.createElement('document')
# 			doc.appendChild(doc2)
# 			for el in self.myControls:
# 				el.ioXML(doc, doc2, saving)
# 			print '#######################'
# 			filename = 'prova.xml'
# 			f = open(str(filename), 'w')
# 			#print doc.toxml()
# 			f.write(doc.toxml())
# 			f.close()
# 			return


			filename = QFileDialog.getSaveFileName('', "Configuracions EVR (*.erc)", self )
			if not filename:
				return
			f = open(str(filename), 'w')
			dict = {}
		else:
			filename = QFileDialog.getOpenFileName('', "Configuracions EVR (*.erc)", self )
			if not filename:
				return
			f = open(str(filename), 'r')
			dict = pickle.load(f)

		for el in self.myControls:
			el.io(dict, saving)
		if saving:
			pickle.dump(dict, f)
		f.close()
	def loadConfig_clicked(self):
		self.file_io(False)
	def saveConfig_clicked(self):
		self.file_io(True)


	def onSetConfigAsDefault(self):
		assert(self.eva.__class__ is access.evrtango.EvrAccessTango)
		if not QMessageBox.question(self, 'Overwritting default settings', 'This will overwrite default settings (the property values stored in the database) of the device server, every time the device is restarted those settings will be applied. \n\n Are you sure?', QMessageBox.No, QMessageBox.Yes) is QMessageBox.Yes:
			return

		self.setEnabled(False)
		try:
			evaconf = access.evrtango.EvrAccessTangoConfig(self.eva.dp)
			for el in self.myControls:
				try:
					exeva = el.eva
					el.eva = evaconf
					el.applyConf()
					self.eva.clearViolation()
				except:
					print 'apply (onSetConfigAsDefault) error ('+ el.controlName +')'
				el.eva = exeva
			print 'onSetConfigAsDefault OK'
		finally:
			self.setEnabled(True)



def main():
    import sys
    if (len(sys.argv) < 2) or (sys.argv[1] in ("-h", "--help")):
    	print "Usage:"
    	print "1) Direct hardware access:    ", sys.argv[0], "[local] sys_dev_name (i.e. /dev/evs/era)"
    	print "2) Tango device access:       ", sys.argv[0], "tango tango_dev_name (i.e. sr01/ti/evr-cdi0101-a)"
    	print "3) Tango configuration access:", sys.argv[0], "tangoconf tango_dev_name (i.e. sr01/ti/evr-cdi0101-a)"
    	exit(0)
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    try:
      w = EventReceiver()
    except:
      print '\n\n\n--------------------'
      raise
    else:
      a.setMainWidget(w)
      w.onRestoreConfig()
      w.show()
      a.exec_loop()


if __name__ == "__main__":
	main()
