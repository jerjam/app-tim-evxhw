# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/eventreceiverform.ui'
#
# Created: Thu Mar 5 11:44:25 2015
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *
from qttable import QTable


class EventReceiverForm(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("EventReceiverForm")

        self.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum,0,0,self.sizePolicy().hasHeightForWidth()))

        EventReceiverFormLayout = QHBoxLayout(self,11,6,"EventReceiverFormLayout")

        layout20 = QVBoxLayout(None,0,6,"layout20")

        self.groupBox6 = QGroupBox(self,"groupBox6")
        self.groupBox6.setColumnLayout(0,Qt.Vertical)
        self.groupBox6.layout().setSpacing(6)
        self.groupBox6.layout().setMargin(11)
        groupBox6Layout = QVBoxLayout(self.groupBox6.layout())
        groupBox6Layout.setAlignment(Qt.AlignTop)

        self.irqMasterEnable = QCheckBox(self.groupBox6,"irqMasterEnable")
        groupBox6Layout.addWidget(self.irqMasterEnable)

        self.irqViolation = QCheckBox(self.groupBox6,"irqViolation")
        groupBox6Layout.addWidget(self.irqViolation)

        self.irqFifoFull = QCheckBox(self.groupBox6,"irqFifoFull")
        groupBox6Layout.addWidget(self.irqFifoFull)

        self.irqHeartBeat = QCheckBox(self.groupBox6,"irqHeartBeat")
        groupBox6Layout.addWidget(self.irqHeartBeat)

        self.irqEvent = QCheckBox(self.groupBox6,"irqEvent")
        groupBox6Layout.addWidget(self.irqEvent)

        self.irqPulse = QCheckBox(self.groupBox6,"irqPulse")
        groupBox6Layout.addWidget(self.irqPulse)

        self.irqDataBuf = QCheckBox(self.groupBox6,"irqDataBuf")
        groupBox6Layout.addWidget(self.irqDataBuf)

        self.clearInterrupts = QPushButton(self.groupBox6,"clearInterrupts")
        groupBox6Layout.addWidget(self.clearInterrupts)
        layout20.addWidget(self.groupBox6)

        self.groupBox9 = QGroupBox(self,"groupBox9")
        self.groupBox9.setColumnLayout(0,Qt.Vertical)
        self.groupBox9.layout().setSpacing(6)
        self.groupBox9.layout().setMargin(11)
        groupBox9Layout = QGridLayout(self.groupBox9.layout())
        groupBox9Layout.setAlignment(Qt.AlignTop)

        self.fp0 = QComboBox(0,self.groupBox9,"fp0")

        groupBox9Layout.addWidget(self.fp0,1,0)

        self.fp1 = QComboBox(0,self.groupBox9,"fp1")

        groupBox9Layout.addWidget(self.fp1,1,1)

        self.fp2 = QComboBox(0,self.groupBox9,"fp2")

        groupBox9Layout.addWidget(self.fp2,2,0)

        self.fp3 = QComboBox(0,self.groupBox9,"fp3")

        groupBox9Layout.addWidget(self.fp3,2,1)

        self.fp4 = QComboBox(0,self.groupBox9,"fp4")

        groupBox9Layout.addWidget(self.fp4,3,0)

        self.fp5 = QComboBox(0,self.groupBox9,"fp5")

        groupBox9Layout.addWidget(self.fp5,3,1)

        self.fp6 = QComboBox(0,self.groupBox9,"fp6")

        groupBox9Layout.addWidget(self.fp6,4,0)

        self.fp7 = QComboBox(0,self.groupBox9,"fp7")

        groupBox9Layout.addWidget(self.fp7,4,1)

        self.fp8 = QComboBox(0,self.groupBox9,"fp8")

        groupBox9Layout.addWidget(self.fp8,5,0)

        self.fp9 = QComboBox(0,self.groupBox9,"fp9")

        groupBox9Layout.addWidget(self.fp9,5,1)

        self.fp10 = QComboBox(0,self.groupBox9,"fp10")

        groupBox9Layout.addWidget(self.fp10,6,0)

        self.fp11 = QComboBox(0,self.groupBox9,"fp11")

        groupBox9Layout.addWidget(self.fp11,6,1)

        self.textLabel2 = QLabel(self.groupBox9,"textLabel2")

        groupBox9Layout.addMultiCellWidget(self.textLabel2,0,0,0,1)
        layout20.addWidget(self.groupBox9)

        layout16 = QGridLayout(None,1,1,0,6,"layout16")

        self.evcountPresc = QLineEdit(self,"evcountPresc")
        self.evcountPresc.setEnabled(0)

        layout16.addWidget(self.evcountPresc,0,1)

        self.textLabel5 = QLabel(self,"textLabel5")

        layout16.addWidget(self.textLabel5,0,0)
        layout20.addLayout(layout16)

        layout24 = QHBoxLayout(None,0,6,"layout24")

        self.textLabel4 = QLabel(self,"textLabel4")
        layout24.addWidget(self.textLabel4)

        self.ckSynthesiser = QComboBox(0,self,"ckSynthesiser")
        layout24.addWidget(self.ckSynthesiser)
        layout20.addLayout(layout24)
        EventReceiverFormLayout.addLayout(layout20)

        layout13 = QVBoxLayout(None,0,6,"layout13")

        self.groupBox18 = QGroupBox(self,"groupBox18")
        self.groupBox18.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Fixed,0,0,self.groupBox18.sizePolicy().hasHeightForWidth()))
        self.groupBox18.setColumnLayout(0,Qt.Vertical)
        self.groupBox18.layout().setSpacing(6)
        self.groupBox18.layout().setMargin(11)
        groupBox18Layout = QGridLayout(self.groupBox18.layout())
        groupBox18Layout.setAlignment(Qt.AlignTop)

        self.prescalerOutputs = QTable(self.groupBox18,"prescalerOutputs")
        self.prescalerOutputs.setNumCols(self.prescalerOutputs.numCols() + 1)
        self.prescalerOutputs.horizontalHeader().setLabel(self.prescalerOutputs.numCols() - 1,self.__tr("Prescaler"))
        self.prescalerOutputs.setNumRows(self.prescalerOutputs.numRows() + 1)
        self.prescalerOutputs.verticalHeader().setLabel(self.prescalerOutputs.numRows() - 1,self.__tr("0"))
        self.prescalerOutputs.setNumRows(self.prescalerOutputs.numRows() + 1)
        self.prescalerOutputs.verticalHeader().setLabel(self.prescalerOutputs.numRows() - 1,self.__tr("1"))
        self.prescalerOutputs.setNumRows(self.prescalerOutputs.numRows() + 1)
        self.prescalerOutputs.verticalHeader().setLabel(self.prescalerOutputs.numRows() - 1,self.__tr("2"))
        self.prescalerOutputs.setNumRows(self.prescalerOutputs.numRows() + 1)
        self.prescalerOutputs.verticalHeader().setLabel(self.prescalerOutputs.numRows() - 1,self.__tr("3"))
        self.prescalerOutputs.setNumRows(4)
        self.prescalerOutputs.setNumCols(1)

        groupBox18Layout.addWidget(self.prescalerOutputs,0,0)
        layout13.addWidget(self.groupBox18)

        self.groupBox3 = QGroupBox(self,"groupBox3")
        self.groupBox3.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum,0,0,self.groupBox3.sizePolicy().hasHeightForWidth()))
        self.groupBox3.setColumnLayout(0,Qt.Vertical)
        self.groupBox3.layout().setSpacing(6)
        self.groupBox3.layout().setMargin(11)
        groupBox3Layout = QVBoxLayout(self.groupBox3.layout())
        groupBox3Layout.setAlignment(Qt.AlignTop)

        self.listPulse = QListView(self.groupBox3,"listPulse")
        self.listPulse.addColumn(self.__tr("id"))
        self.listPulse.header().setClickEnabled(0,self.listPulse.header().count() - 1)
        self.listPulse.header().setResizeEnabled(0,self.listPulse.header().count() - 1)
        self.listPulse.addColumn(self.__tr("eitscp"))
        self.listPulse.header().setClickEnabled(0,self.listPulse.header().count() - 1)
        self.listPulse.header().setResizeEnabled(0,self.listPulse.header().count() - 1)
        self.listPulse.addColumn(self.__tr("Delay"))
        self.listPulse.header().setClickEnabled(0,self.listPulse.header().count() - 1)
        self.listPulse.header().setResizeEnabled(0,self.listPulse.header().count() - 1)
        self.listPulse.addColumn(self.__tr("Width"))
        self.listPulse.header().setClickEnabled(0,self.listPulse.header().count() - 1)
        self.listPulse.header().setResizeEnabled(0,self.listPulse.header().count() - 1)
        self.listPulse.addColumn(self.__tr("Prescaler"))
        self.listPulse.header().setClickEnabled(0,self.listPulse.header().count() - 1)
        self.listPulse.header().setResizeEnabled(0,self.listPulse.header().count() - 1)
        listPulse_font = QFont(self.listPulse.font())
        listPulse_font.setFamily("Courier")
        self.listPulse.setFont(listPulse_font)
        groupBox3Layout.addWidget(self.listPulse)
        layout13.addWidget(self.groupBox3)
        EventReceiverFormLayout.addLayout(layout13)

        layout11 = QVBoxLayout(None,0,6,"layout11")

        self.groupBox7 = QGroupBox(self,"groupBox7")
        self.groupBox7.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum,0,0,self.groupBox7.sizePolicy().hasHeightForWidth()))
        self.groupBox7.setColumnLayout(0,Qt.Vertical)
        self.groupBox7.layout().setSpacing(6)
        self.groupBox7.layout().setMargin(11)
        groupBox7Layout = QVBoxLayout(self.groupBox7.layout())
        groupBox7Layout.setAlignment(Qt.AlignTop)

        layout7 = QHBoxLayout(None,0,6,"layout7")

        self.ramSel = QComboBox(0,self.groupBox7,"ramSel")
        layout7.addWidget(self.ramSel)

        self.ramEnable = QCheckBox(self.groupBox7,"ramEnable")
        layout7.addWidget(self.ramEnable)
        groupBox7Layout.addLayout(layout7)

        layout21 = QHBoxLayout(None,0,6,"layout21")

        self.ramEvent = QLineEdit(self.groupBox7,"ramEvent")
        layout21.addWidget(self.ramEvent)

        self.ramMod = QPushButton(self.groupBox7,"ramMod")
        layout21.addWidget(self.ramMod)

        self.ramDel = QPushButton(self.groupBox7,"ramDel")
        layout21.addWidget(self.ramDel)
        groupBox7Layout.addLayout(layout21)

        self.ramList = QListView(self.groupBox7,"ramList")
        self.ramList.addColumn(self.__tr("Event"))
        self.ramList.header().setClickEnabled(0,self.ramList.header().count() - 1)
        self.ramList.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding,0,0,self.ramList.sizePolicy().hasHeightForWidth()))
        ramList_font = QFont(self.ramList.font())
        ramList_font.setFamily("Courier")
        self.ramList.setFont(ramList_font)
        groupBox7Layout.addWidget(self.ramList)

        layout19 = QHBoxLayout(None,0,6,"layout19")
        spacer4 = QSpacerItem(81,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout19.addItem(spacer4)

        self.ramClear = QPushButton(self.groupBox7,"ramClear")
        layout19.addWidget(self.ramClear)
        groupBox7Layout.addLayout(layout19)
        layout11.addWidget(self.groupBox7)

        layout10 = QGridLayout(None,1,1,0,6,"layout10")

        self.restoreConfig = QPushButton(self,"restoreConfig")

        layout10.addWidget(self.restoreConfig,0,2)

        self.saveConfig = QPushButton(self,"saveConfig")

        layout10.addWidget(self.saveConfig,1,1)

        self.applyConfig = QPushButton(self,"applyConfig")

        layout10.addWidget(self.applyConfig,1,2)

        self.masterEnable = QCheckBox(self,"masterEnable")

        layout10.addWidget(self.masterEnable,1,0)

        self.loadConfig = QPushButton(self,"loadConfig")

        layout10.addWidget(self.loadConfig,0,1)

        self.setDefaultBt = QPushButton(self,"setDefaultBt")
        self.setDefaultBt.setEnabled(0)

        layout10.addWidget(self.setDefaultBt,0,0)
        layout11.addLayout(layout10)
        EventReceiverFormLayout.addLayout(layout11)

        self.languageChange()

        self.resize(QSize(816,484).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.ramList,SIGNAL("clicked(QListViewItem*)"),self.ramList_clicked)
        self.connect(self.ramList,SIGNAL("doubleClicked(QListViewItem*)"),self.ramList_doubleClicked)
        self.connect(self.ramEnable,SIGNAL("toggled(bool)"),self.ramEnable_toggled)
        self.connect(self.ramMod,SIGNAL("clicked()"),self.ramMod_clicked)
        self.connect(self.ramDel,SIGNAL("clicked()"),self.ramDel_clicked)
        self.connect(self.ramClear,SIGNAL("clicked()"),self.ramClear_clicked)
        self.connect(self.ramSel,SIGNAL("activated(int)"),self.ramSel_activated)
        self.connect(self.listPulse,SIGNAL("doubleClicked(QListViewItem*)"),self.listPulse_doubleClicked)
        self.connect(self.restoreConfig,SIGNAL("clicked()"),self.onRestoreConfig)
        self.connect(self.loadConfig,SIGNAL("clicked()"),self.loadConfig_clicked)
        self.connect(self.saveConfig,SIGNAL("clicked()"),self.saveConfig_clicked)
        self.connect(self.applyConfig,SIGNAL("clicked()"),self.onApplyConfig)
        self.connect(self.setDefaultBt,SIGNAL("clicked()"),self.onSetConfigAsDefault)
        self.connect(self.ramEvent,SIGNAL("returnPressed()"),self.ramMod_clicked)
        self.connect(self.clearInterrupts,SIGNAL("clicked()"),self.clearInterrupts_clicked)

        self.setTabOrder(self.ramEnable,self.ramEvent)
        self.setTabOrder(self.ramEvent,self.ramMod)
        self.setTabOrder(self.ramMod,self.ramList)
        self.setTabOrder(self.ramList,self.ramClear)
        self.setTabOrder(self.ramClear,self.listPulse)
        self.setTabOrder(self.listPulse,self.ckSynthesiser)
        self.setTabOrder(self.ckSynthesiser,self.evcountPresc)
        self.setTabOrder(self.evcountPresc,self.irqMasterEnable)
        self.setTabOrder(self.irqMasterEnable,self.irqViolation)
        self.setTabOrder(self.irqViolation,self.irqHeartBeat)
        self.setTabOrder(self.irqHeartBeat,self.irqFifoFull)
        self.setTabOrder(self.irqFifoFull,self.irqEvent)
        self.setTabOrder(self.irqEvent,self.fp0)
        self.setTabOrder(self.fp0,self.fp1)
        self.setTabOrder(self.fp1,self.fp2)
        self.setTabOrder(self.fp2,self.fp3)
        self.setTabOrder(self.fp3,self.fp4)
        self.setTabOrder(self.fp4,self.fp5)
        self.setTabOrder(self.fp5,self.fp6)


    def languageChange(self):
        self.setCaption(self.__tr("Event Receiver"))
        self.groupBox6.setTitle(self.__tr("Interrupts"))
        self.irqMasterEnable.setText(self.__tr("Enable"))
        self.irqViolation.setText(self.__tr("Violation"))
        self.irqFifoFull.setText(self.__tr("Fifo Full"))
        self.irqHeartBeat.setText(self.__tr("HeartBeat"))
        self.irqEvent.setText(self.__tr("Event?"))
        self.irqPulse.setText(self.__tr("Pulse master (see pulses)"))
        self.irqDataBuf.setText(self.__tr("data buffer?"))
        self.clearInterrupts.setText(self.__tr("Clear"))
        self.groupBox9.setTitle(self.__tr("Front Panel Univ Out"))
        self.textLabel2.setText(self.__tr("STDDLY(0,1,2,3,4,5,6,7),FINEDLY(8,9,10,11)"))
        self.textLabel5.setText(self.__tr("Event Counter Presc"))
        self.textLabel4.setText(self.__tr("Event Clock[RF]"))
        self.groupBox18.setTitle(self.__tr("Prescalers"))
        self.prescalerOutputs.horizontalHeader().setLabel(0,self.__tr("Prescaler"))
        self.prescalerOutputs.verticalHeader().setLabel(0,self.__tr("0"))
        self.prescalerOutputs.verticalHeader().setLabel(1,self.__tr("1"))
        self.prescalerOutputs.verticalHeader().setLabel(2,self.__tr("2"))
        self.prescalerOutputs.verticalHeader().setLabel(3,self.__tr("3"))
        self.groupBox3.setTitle(self.__tr("Pulses"))
        self.listPulse.header().setLabel(0,self.__tr("id"))
        self.listPulse.header().setLabel(1,self.__tr("eitscp"))
        self.listPulse.header().setLabel(2,self.__tr("Delay"))
        self.listPulse.header().setLabel(3,self.__tr("Width"))
        self.listPulse.header().setLabel(4,self.__tr("Prescaler"))
        self.groupBox7.setTitle(self.__tr("Ram"))
        self.ramSel.clear()
        self.ramSel.insertItem(self.__tr("Ram 1"))
        self.ramSel.insertItem(self.__tr("Ram 2"))
        self.ramEnable.setText(self.__tr("enable"))
        self.ramMod.setText(self.__tr("+"))
        self.ramDel.setText(self.__tr("-"))
        self.ramList.header().setLabel(0,self.__tr("Event"))
        self.ramClear.setText(self.__tr("Clear"))
        self.restoreConfig.setText(self.__tr("Restore"))
        self.saveConfig.setText(self.__tr("Save"))
        self.applyConfig.setText(self.__tr("Apply"))
        self.masterEnable.setText(self.__tr("Enable"))
        self.loadConfig.setText(self.__tr("Load"))
        self.setDefaultBt.setText(self.__tr("Set As Default"))


    def ramList_clicked(self,a0):
        print "EventReceiverForm.ramList_clicked(QListViewItem*): Not implemented yet"

    def ramList_doubleClicked(self,a0):
        print "EventReceiverForm.ramList_doubleClicked(QListViewItem*): Not implemented yet"

    def ramEnable_toggled(self,a0):
        print "EventReceiverForm.ramEnable_toggled(bool): Not implemented yet"

    def ramMod_clicked(self):
        print "EventReceiverForm.ramMod_clicked(): Not implemented yet"

    def ramDel_clicked(self):
        print "EventReceiverForm.ramDel_clicked(): Not implemented yet"

    def ramClear_clicked(self):
        print "EventReceiverForm.ramClear_clicked(): Not implemented yet"

    def ramSel_activated(self,a0):
        print "EventReceiverForm.ramSel_activated(int): Not implemented yet"

    def listPulse_doubleClicked(self,a0):
        print "EventReceiverForm.listPulse_doubleClicked(QListViewItem*): Not implemented yet"

    def loadConfig_clicked(self):
        print "EventReceiverForm.loadConfig_clicked(): Not implemented yet"

    def onRestoreConfig(self):
        print "EventReceiverForm.onRestoreConfig(): Not implemented yet"

    def onApplyConfig(self):
        print "EventReceiverForm.onApplyConfig(): Not implemented yet"

    def saveConfig_clicked(self):
        print "EventReceiverForm.saveConfig_clicked(): Not implemented yet"

    def statusUpdate_clicked(self):
        print "EventReceiverForm.statusUpdate_clicked(): Not implemented yet"

    def statusViolation_clicked(self):
        print "EventReceiverForm.statusViolation_clicked(): Not implemented yet"

    def onSetConfigAsDefault(self):
        print "EventReceiverForm.onSetConfigAsDefault(): Not implemented yet"

    def clearInterrupts_clicked(self):
        print "EventReceiverForm.clearInterrupts_clicked(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("EventReceiverForm",s,c)
