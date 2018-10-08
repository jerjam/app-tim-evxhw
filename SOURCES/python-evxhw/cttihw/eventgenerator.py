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

from auxiliar import *

from eventgeneratorform import EventGeneratorForm
import pickle
from evgcontrols.dbuscontrol import DBusControl
from evgcontrols.triggerscontrol import TriggersControl
from evgcontrols.mxctablecontrol import MXCTableControl
from evgcontrols.databuffercontrol import DataBufferControl
from evgcontrols.accontrol import ACControl
from evgcontrols.clockcontrol import ClockControl
from evgcontrols.frontpanelcontrol import UnivInControl
from sequenceeditor import SequenceEditor
from evgcontrols.otherscontrol import OthersControl

import evaccess
#import access.evgtango

try:
    import access.evglocal
except:
    print 'This expert GUI can only be run on the machine in which the EVG is installed'
    exit(-1)

import time


class EventGenerator(EventGeneratorForm):
    def __init__(self, parent=None, name=None, fl=0):
        EventGeneratorForm.__init__(self, parent, name, fl)
        self.othercontrols = None

        self.eva = evaccess.OpenDevice(access.evg.evgAccessFactoryDict)

        caption = self.eva.deviceString() + '  -  Event Generator'
        self.setCaption(caption)

        self.triggerscontrol = TriggersControl(self)
        self.dbuscontrol = DBusControl(self)
        self.mxctablecontrol = MXCTableControl(self)
        self.accontrol = ACControl(self)
        self.clockcontrol = ClockControl(self)
        # self.databuffercontrol = DataBufferControl(self)
        self.univincontrol = UnivInControl(self)
        self.sequenceeditor1 = SequenceEditor(self, seq=self.eva.SEQ1)
        self.sequenceeditor2 = SequenceEditor(self, seq=self.eva.SEQ2)
        self.otherscontrol = OthersControl(self)

        #ClockControl must be the first to apply, as
        #its changes affect the time of everything
        #else: in particular, all sequence get
        #disabled after writting InternalFrac
        self.myControls = [
            self.clockcontrol,
            self.sequenceeditor1,
            self.sequenceeditor2,
            self.triggerscontrol,
            self.dbuscontrol,
            self.mxctablecontrol,
            self.accontrol,
            ##          self.databuffercontrol,
            self.univincontrol,
            self.otherscontrol
        ]
        self.onRestoreConfig()


    def dataBufSize_returnPressed(self):
        self.databuffercontrol.changingSizeField()

    def onRestoreConfig(self, controls=None):
        # evg = self.evg

        if controls == None: controls = self.myControls
        for el in controls:
            try:
                el.restore()
            except:
                print 'restore error (' + el.controlName + ')'
                raise
            # 		rxv = evg.GetRXViolation()
            # 		if rxv: rxv = 'Yes'
            # 		else: rxv = 'No'
            # 		self.rxvio.setText('RX Violation: ' + rxv)

    def onApplyConfig(self):
        for el in self.myControls:
            try:
                el.applyConf()
            # print 'juer',el.controlName, self.eva.ev.SeqRamGetControl(0), self.eva.ev.GetVal(0x50)
            except:
                print 'apply error (' + el.controlName + ')'
                raise
            # time.sleep(0.5)
        self.onRestoreConfig()

    def file_io(self, saving):
        if saving:
            filename = QFileDialog.getSaveFileName('', "Configuracions EVG (*.egc)", self)
            if not filename:
                return
            f = open(str(filename), 'w')
            dict = {}
        else:
            filename = QFileDialog.getOpenFileName('', "Configuracions EVG (*.egc)", self)
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

    def editSeq1_clicked(self):
        self.sequenceeditor1.editSequence()

    def editSeq2_clicked(self):
        self.sequenceeditor2.editSequence()

    def mxcTable_valueChanged(self, row, col):
        self.mxctablecontrol.valueChanged(row, col)


    def sendDataBuf_clicked(self):
        self.databuffercontrol.sendDataBuf()

    def resetRXVio_clicked(self):
        self.evg.ResetRXViolation()

    # def mxrs0_clicked(self): self.evg.ResetMXC(1 << 0)
    # 	def mxrs1_clicked(self): self.evg.ResetMXC(1 << 1)
    # 	def mxrs2_clicked(self): self.evg.ResetMXC(1 << 2)
    # 	def mxrs3_clicked(self): self.evg.ResetMXC(1 << 3)
    # 	def mxrs4_clicked(self): self.evg.ResetMXC(1 << 4)
    # 	def mxrs5_clicked(self): self.evg.ResetMXC(1 << 5)
    # 	def mxrs6_clicked(self): self.evg.ResetMXC(1 << 6)
    # 	def mxrs7_clicked(self): self.evg.ResetMXC(1 << 7)

    def triggerSeq1_clicked(self):
        self.eva.runSequence(self.eva.SEQ1)

    def triggerSeq2_clicked(self):
        self.eva.runSequence(self.eva.SEQ2)

    def sendSwEvent_clicked(self):
        ct = self.swEvent
        ev = ct.text().toUInt()
        if (not ev[1]) or ev[0] > 255:
            ct.selectAll()
            ct.setFocus()
            return
        ev = ev[0]
        self.eva.sendSwEvent(ev)


def main():
    import sys

    if (len(sys.argv) < 2) or (sys.argv[1] in ("-h", "--help")):
        print "Usage:"
        print "1) Direct hardware access:    ", sys.argv[0], "[local] sys_dev_name (i.e. /dev/evs/ega)"
        print "2) Tango device access:       ", sys.argv[0], "tango tango_dev_name (i.e. al/ti/evg)"
        print "3) Tango configuration access:", sys.argv[0], "tangoconf tango_dev_name (i.e. al/ti/evg)"
        exit(0)

    a = QApplication(sys.argv)
    QObject.connect(a, SIGNAL("lastWindowClosed()"), a, SLOT("quit()"))
    w = EventGenerator()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()


if __name__ == "__main__":
    main()
