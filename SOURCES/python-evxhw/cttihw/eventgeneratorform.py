# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/eventgeneratorform.ui'
#
# Created: Thu Mar 5 11:44:25 2015
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *
from qttable import QTable


class EventGeneratorForm(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        if not name:
            self.setName("EventGeneratorForm")


        self.setCentralWidget(QWidget(self,"qt_central_widget"))
        EventGeneratorFormLayout = QHBoxLayout(self.centralWidget(),11,6,"EventGeneratorFormLayout")

        layout9 = QVBoxLayout(None,0,6,"layout9")

        self.groupBox4 = QGroupBox(self.centralWidget(),"groupBox4")
        self.groupBox4.setColumnLayout(0,Qt.Vertical)
        self.groupBox4.layout().setSpacing(6)
        self.groupBox4.layout().setMargin(11)
        groupBox4Layout = QGridLayout(self.groupBox4.layout())
        groupBox4Layout.setAlignment(Qt.AlignTop)

        self.mxcTable = QTable(self.groupBox4,"mxcTable")
        self.mxcTable.setNumCols(self.mxcTable.numCols() + 1)
        self.mxcTable.horizontalHeader().setLabel(self.mxcTable.numCols() - 1,self.__tr("Prescaler"))
        self.mxcTable.setNumCols(self.mxcTable.numCols() + 1)
        self.mxcTable.horizontalHeader().setLabel(self.mxcTable.numCols() - 1,self.__tr("Trigger"))
        self.mxcTable.setNumRows(self.mxcTable.numRows() + 1)
        self.mxcTable.verticalHeader().setLabel(self.mxcTable.numRows() - 1,self.__tr("0"))
        self.mxcTable.setNumRows(self.mxcTable.numRows() + 1)
        self.mxcTable.verticalHeader().setLabel(self.mxcTable.numRows() - 1,self.__tr("1"))
        self.mxcTable.setNumRows(self.mxcTable.numRows() + 1)
        self.mxcTable.verticalHeader().setLabel(self.mxcTable.numRows() - 1,self.__tr("2"))
        self.mxcTable.setNumRows(self.mxcTable.numRows() + 1)
        self.mxcTable.verticalHeader().setLabel(self.mxcTable.numRows() - 1,self.__tr("3"))
        self.mxcTable.setNumRows(self.mxcTable.numRows() + 1)
        self.mxcTable.verticalHeader().setLabel(self.mxcTable.numRows() - 1,self.__tr("4"))
        self.mxcTable.setNumRows(self.mxcTable.numRows() + 1)
        self.mxcTable.verticalHeader().setLabel(self.mxcTable.numRows() - 1,self.__tr("5"))
        self.mxcTable.setNumRows(self.mxcTable.numRows() + 1)
        self.mxcTable.verticalHeader().setLabel(self.mxcTable.numRows() - 1,self.__tr("6"))
        self.mxcTable.setNumRows(self.mxcTable.numRows() + 1)
        self.mxcTable.verticalHeader().setLabel(self.mxcTable.numRows() - 1,self.__tr("7"))
        self.mxcTable.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding,0,0,self.mxcTable.sizePolicy().hasHeightForWidth()))
        self.mxcTable.setNumRows(8)
        self.mxcTable.setNumCols(2)

        groupBox4Layout.addWidget(self.mxcTable,0,0)
        layout9.addWidget(self.groupBox4)

        self.groupBox6 = QGroupBox(self.centralWidget(),"groupBox6")
        self.groupBox6.setColumnLayout(0,Qt.Vertical)
        self.groupBox6.layout().setSpacing(0)
        self.groupBox6.layout().setMargin(11)
        groupBox6Layout = QGridLayout(self.groupBox6.layout())
        groupBox6Layout.setAlignment(Qt.AlignTop)

        self.enev_1 = QPushButton(self.groupBox6,"enev_1")
        self.enev_1.setToggleButton(1)

        groupBox6Layout.addMultiCellWidget(self.enev_1,1,2,0,0)

        self.enev_2 = QPushButton(self.groupBox6,"enev_2")
        self.enev_2.setToggleButton(1)

        groupBox6Layout.addWidget(self.enev_2,3,0)

        self.enev_5 = QPushButton(self.groupBox6,"enev_5")
        self.enev_5.setToggleButton(1)

        groupBox6Layout.addWidget(self.enev_5,6,0)

        self.enev_6 = QPushButton(self.groupBox6,"enev_6")
        self.enev_6.setToggleButton(1)

        groupBox6Layout.addWidget(self.enev_6,7,0)

        self.enev_7 = QPushButton(self.groupBox6,"enev_7")
        self.enev_7.setToggleButton(1)

        groupBox6Layout.addWidget(self.enev_7,8,0)

        self.enev_4 = QPushButton(self.groupBox6,"enev_4")
        self.enev_4.setToggleButton(1)

        groupBox6Layout.addWidget(self.enev_4,5,0)

        self.enev_3 = QPushButton(self.groupBox6,"enev_3")
        self.enev_3.setToggleButton(1)

        groupBox6Layout.addWidget(self.enev_3,4,0)

        self.enev_0 = QPushButton(self.groupBox6,"enev_0")
        self.enev_0.setToggleButton(1)

        groupBox6Layout.addWidget(self.enev_0,0,0)

        self.trigev_1 = QLineEdit(self.groupBox6,"trigev_1")

        groupBox6Layout.addWidget(self.trigev_1,2,2)

        self.trigev_2 = QLineEdit(self.groupBox6,"trigev_2")

        groupBox6Layout.addWidget(self.trigev_2,3,2)

        self.trigev_3 = QLineEdit(self.groupBox6,"trigev_3")

        groupBox6Layout.addWidget(self.trigev_3,4,2)

        self.trigev_4 = QLineEdit(self.groupBox6,"trigev_4")

        groupBox6Layout.addWidget(self.trigev_4,5,2)

        self.trigev_5 = QLineEdit(self.groupBox6,"trigev_5")

        groupBox6Layout.addWidget(self.trigev_5,6,2)

        self.trigev_6 = QLineEdit(self.groupBox6,"trigev_6")

        groupBox6Layout.addWidget(self.trigev_6,7,2)

        self.trigev_7 = QLineEdit(self.groupBox6,"trigev_7")

        groupBox6Layout.addWidget(self.trigev_7,8,2)

        self.trigev_0 = QLineEdit(self.groupBox6,"trigev_0")

        groupBox6Layout.addWidget(self.trigev_0,0,2)
        layout9.addWidget(self.groupBox6)

        self.groupBox9 = QGroupBox(self.centralWidget(),"groupBox9")
        self.groupBox9.setColumnLayout(0,Qt.Vertical)
        self.groupBox9.layout().setSpacing(6)
        self.groupBox9.layout().setMargin(11)
        groupBox9Layout = QGridLayout(self.groupBox9.layout())
        groupBox9Layout.setAlignment(Qt.AlignTop)

        self.textLabel2_2 = QLabel(self.groupBox9,"textLabel2_2")

        groupBox9Layout.addWidget(self.textLabel2_2,0,0)

        self.ckMode = QComboBox(0,self.groupBox9,"ckMode")

        groupBox9Layout.addWidget(self.ckMode,0,1)

        self.ckSynth = QComboBox(0,self.groupBox9,"ckSynth")

        groupBox9Layout.addWidget(self.ckSynth,1,1)

        self.textLabel4 = QLabel(self.groupBox9,"textLabel4")

        groupBox9Layout.addWidget(self.textLabel4,1,0)
        layout9.addWidget(self.groupBox9)
        EventGeneratorFormLayout.addLayout(layout9)

        layout8 = QVBoxLayout(None,0,6,"layout8")

        self.gbDBus = QGroupBox(self.centralWidget(),"gbDBus")
        self.gbDBus.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Preferred,0,0,self.gbDBus.sizePolicy().hasHeightForWidth()))
        self.gbDBus.setMinimumSize(QSize(250,0))
        self.gbDBus.setColumnLayout(0,Qt.Vertical)
        self.gbDBus.layout().setSpacing(6)
        self.gbDBus.layout().setMargin(11)
        gbDBusLayout = QVBoxLayout(self.gbDBus.layout())
        gbDBusLayout.setAlignment(Qt.AlignTop)
        layout8.addWidget(self.gbDBus)

        self.groupBox3 = QGroupBox(self.centralWidget(),"groupBox3")
        self.groupBox3.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Maximum,0,0,self.groupBox3.sizePolicy().hasHeightForWidth()))
        self.groupBox3.setColumnLayout(0,Qt.Vertical)
        self.groupBox3.layout().setSpacing(6)
        self.groupBox3.layout().setMargin(11)
        groupBox3Layout = QGridLayout(self.groupBox3.layout())
        groupBox3Layout.setAlignment(Qt.AlignTop)

        self.textLabel2 = QLabel(self.groupBox3,"textLabel2")

        groupBox3Layout.addWidget(self.textLabel2,1,0)

        self.textLabel1 = QLabel(self.groupBox3,"textLabel1")

        groupBox3Layout.addWidget(self.textLabel1,0,0)

        self.acSyncMXC7 = QCheckBox(self.groupBox3,"acSyncMXC7")

        groupBox3Layout.addMultiCellWidget(self.acSyncMXC7,3,3,0,1)

        self.acByPass = QCheckBox(self.groupBox3,"acByPass")

        groupBox3Layout.addWidget(self.acByPass,3,2)

        self.acDelay = QLineEdit(self.groupBox3,"acDelay")

        groupBox3Layout.addMultiCellWidget(self.acDelay,1,1,1,2)

        self.acPrescaler = QLineEdit(self.groupBox3,"acPrescaler")

        groupBox3Layout.addMultiCellWidget(self.acPrescaler,0,0,1,2)

        self.textLabel1_3 = QLabel(self.groupBox3,"textLabel1_3")

        groupBox3Layout.addWidget(self.textLabel1_3,2,0)

        self.acTrigger = QComboBox(0,self.groupBox3,"acTrigger")

        groupBox3Layout.addMultiCellWidget(self.acTrigger,2,2,1,2)
        layout8.addWidget(self.groupBox3)

        self.groupBox9_2 = QGroupBox(self.centralWidget(),"groupBox9_2")
        self.groupBox9_2.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Maximum,0,0,self.groupBox9_2.sizePolicy().hasHeightForWidth()))
        self.groupBox9_2.setColumnLayout(0,Qt.Vertical)
        self.groupBox9_2.layout().setSpacing(6)
        self.groupBox9_2.layout().setMargin(11)
        groupBox9_2Layout = QGridLayout(self.groupBox9_2.layout())
        groupBox9_2Layout.setAlignment(Qt.AlignTop)

        self.fp0 = QComboBox(0,self.groupBox9_2,"fp0")

        groupBox9_2Layout.addWidget(self.fp0,1,0)

        self.fp1 = QComboBox(0,self.groupBox9_2,"fp1")

        groupBox9_2Layout.addWidget(self.fp1,1,1)

        self.fp2 = QComboBox(0,self.groupBox9_2,"fp2")

        groupBox9_2Layout.addWidget(self.fp2,2,0)

        self.fp3 = QComboBox(0,self.groupBox9_2,"fp3")

        groupBox9_2Layout.addWidget(self.fp3,2,1)

        self.fp4 = QComboBox(0,self.groupBox9_2,"fp4")

        groupBox9_2Layout.addWidget(self.fp4,3,0)

        self.fp5 = QComboBox(0,self.groupBox9_2,"fp5")

        groupBox9_2Layout.addWidget(self.fp5,3,1)

        self.fp6 = QComboBox(0,self.groupBox9_2,"fp6")

        groupBox9_2Layout.addWidget(self.fp6,4,0)

        self.fp7 = QComboBox(0,self.groupBox9_2,"fp7")

        groupBox9_2Layout.addWidget(self.fp7,4,1)

        self.fp8 = QComboBox(0,self.groupBox9_2,"fp8")

        groupBox9_2Layout.addWidget(self.fp8,5,0)

        self.fp9 = QComboBox(0,self.groupBox9_2,"fp9")

        groupBox9_2Layout.addWidget(self.fp9,5,1)

        self.fp10 = QComboBox(0,self.groupBox9_2,"fp10")

        groupBox9_2Layout.addWidget(self.fp10,6,0)

        self.fp11 = QComboBox(0,self.groupBox9_2,"fp11")

        groupBox9_2Layout.addWidget(self.fp11,6,1)

        self.fp12 = QComboBox(0,self.groupBox9_2,"fp12")

        groupBox9_2Layout.addWidget(self.fp12,7,0)

        self.fp13 = QComboBox(0,self.groupBox9_2,"fp13")

        groupBox9_2Layout.addWidget(self.fp13,7,1)

        self.fp14 = QComboBox(0,self.groupBox9_2,"fp14")

        groupBox9_2Layout.addWidget(self.fp14,8,0)

        self.fp15 = QComboBox(0,self.groupBox9_2,"fp15")

        groupBox9_2Layout.addWidget(self.fp15,8,1)

        self.fp16 = QComboBox(0,self.groupBox9_2,"fp16")

        groupBox9_2Layout.addWidget(self.fp16,9,0)

        self.fp17 = QComboBox(0,self.groupBox9_2,"fp17")

        groupBox9_2Layout.addWidget(self.fp17,9,1)

        self.fp18 = QComboBox(0,self.groupBox9_2,"fp18")

        groupBox9_2Layout.addWidget(self.fp18,10,0)

        self.fp19 = QComboBox(0,self.groupBox9_2,"fp19")

        groupBox9_2Layout.addWidget(self.fp19,10,1)

        self.textLabel2_3 = QLabel(self.groupBox9_2,"textLabel2_3")

        groupBox9_2Layout.addMultiCellWidget(self.textLabel2_3,0,0,0,1)
        layout8.addWidget(self.groupBox9_2)
        EventGeneratorFormLayout.addLayout(layout8)

        layout11 = QVBoxLayout(None,0,6,"layout11")

        self.groupBox8 = QGroupBox(self.centralWidget(),"groupBox8")
        self.groupBox8.setEnabled(0)
        self.groupBox8.setColumnLayout(0,Qt.Vertical)
        self.groupBox8.layout().setSpacing(6)
        self.groupBox8.layout().setMargin(11)
        groupBox8Layout = QGridLayout(self.groupBox8.layout())
        groupBox8Layout.setAlignment(Qt.AlignTop)

        self.dataBufData = QTable(self.groupBox8,"dataBufData")
        self.dataBufData.setNumRows(self.dataBufData.numRows() + 1)
        self.dataBufData.verticalHeader().setLabel(self.dataBufData.numRows() - 1,self.__tr("0"))
        self.dataBufData.setNumRows(1)
        self.dataBufData.setNumCols(1)

        groupBox8Layout.addMultiCellWidget(self.dataBufData,2,2,0,2)

        self.dataBufSize = QLineEdit(self.groupBox8,"dataBufSize")

        groupBox8Layout.addWidget(self.dataBufSize,1,2)

        self.textLabel1_2 = QLabel(self.groupBox8,"textLabel1_2")

        groupBox8Layout.addWidget(self.textLabel1_2,1,1)

        self.dataBufEnable = QCheckBox(self.groupBox8,"dataBufEnable")

        groupBox8Layout.addMultiCellWidget(self.dataBufEnable,0,0,0,1)

        self.dataBuffTrigger = QCheckBox(self.groupBox8,"dataBuffTrigger")

        groupBox8Layout.addWidget(self.dataBuffTrigger,1,0)

        self.dataBufMode = QCheckBox(self.groupBox8,"dataBufMode")

        groupBox8Layout.addWidget(self.dataBufMode,0,2)
        layout11.addWidget(self.groupBox8)

        self.groupBox7 = QGroupBox(self.centralWidget(),"groupBox7")
        self.groupBox7.setColumnLayout(0,Qt.Vertical)
        self.groupBox7.layout().setSpacing(6)
        self.groupBox7.layout().setMargin(11)
        groupBox7Layout = QVBoxLayout(self.groupBox7.layout())
        groupBox7Layout.setAlignment(Qt.AlignTop)

        layout7 = QHBoxLayout(None,0,6,"layout7")

        self.triggerSeq1 = QPushButton(self.groupBox7,"triggerSeq1")
        layout7.addWidget(self.triggerSeq1)

        self.triggerSeq2 = QPushButton(self.groupBox7,"triggerSeq2")
        layout7.addWidget(self.triggerSeq2)
        groupBox7Layout.addLayout(layout7)

        layout11_2 = QHBoxLayout(None,0,6,"layout11_2")

        self.swEvent = QLineEdit(self.groupBox7,"swEvent")
        layout11_2.addWidget(self.swEvent)

        self.sendSwEvent = QPushButton(self.groupBox7,"sendSwEvent")
        layout11_2.addWidget(self.sendSwEvent)
        groupBox7Layout.addLayout(layout11_2)
        layout11.addWidget(self.groupBox7)

        layout10 = QHBoxLayout(None,0,6,"layout10")

        self.masterEnable = QCheckBox(self.centralWidget(),"masterEnable")
        layout10.addWidget(self.masterEnable)

        self.swEventEnable = QCheckBox(self.centralWidget(),"swEventEnable")
        layout10.addWidget(self.swEventEnable)
        layout11.addLayout(layout10)

        layout12 = QGridLayout(None,1,1,0,6,"layout12")

        self.editSeq1 = QPushButton(self.centralWidget(),"editSeq1")

        layout12.addWidget(self.editSeq1,0,0)

        self.loadConfig = QPushButton(self.centralWidget(),"loadConfig")

        layout12.addWidget(self.loadConfig,0,1)

        self.saveConfig = QPushButton(self.centralWidget(),"saveConfig")

        layout12.addWidget(self.saveConfig,1,1)

        self.editSeq2 = QPushButton(self.centralWidget(),"editSeq2")

        layout12.addWidget(self.editSeq2,1,0)

        self.restoreConfig = QPushButton(self.centralWidget(),"restoreConfig")

        layout12.addWidget(self.restoreConfig,0,2)

        self.applyConfig = QPushButton(self.centralWidget(),"applyConfig")

        layout12.addWidget(self.applyConfig,1,2)
        layout11.addLayout(layout12)
        EventGeneratorFormLayout.addLayout(layout11)



        self.languageChange()

        self.resize(QSize(795,520).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.restoreConfig,SIGNAL("clicked()"),self.onRestoreConfig)
        self.connect(self.applyConfig,SIGNAL("clicked()"),self.onApplyConfig)
        self.connect(self.loadConfig,SIGNAL("clicked()"),self.loadConfig_clicked)
        self.connect(self.saveConfig,SIGNAL("clicked()"),self.saveConfig_clicked)
        self.connect(self.dataBufSize,SIGNAL("returnPressed()"),self.dataBufSize_returnPressed)
        self.connect(self.dataBufSize,SIGNAL("lostFocus()"),self.dataBufSize_returnPressed)
        self.connect(self.editSeq1,SIGNAL("clicked()"),self.editSeq1_clicked)
        self.connect(self.editSeq2,SIGNAL("clicked()"),self.editSeq2_clicked)
        self.connect(self.sendSwEvent,SIGNAL("clicked()"),self.sendSwEvent_clicked)
        self.connect(self.mxcTable,SIGNAL("valueChanged(int,int)"),self.mxcTable_valueChanged)
        self.connect(self.triggerSeq2,SIGNAL("clicked()"),self.triggerSeq2_clicked)
        self.connect(self.triggerSeq1,SIGNAL("clicked()"),self.triggerSeq1_clicked)

        self.textLabel1_3.setBuddy(self.acTrigger)


    def languageChange(self):
        self.setCaption(self.__tr("Event Generator"))
        self.groupBox4.setTitle(self.__tr("MXC"))
        self.mxcTable.horizontalHeader().setLabel(0,self.__tr("Prescaler"))
        self.mxcTable.horizontalHeader().setLabel(1,self.__tr("Trigger"))
        self.mxcTable.verticalHeader().setLabel(0,self.__tr("0"))
        self.mxcTable.verticalHeader().setLabel(1,self.__tr("1"))
        self.mxcTable.verticalHeader().setLabel(2,self.__tr("2"))
        self.mxcTable.verticalHeader().setLabel(3,self.__tr("3"))
        self.mxcTable.verticalHeader().setLabel(4,self.__tr("4"))
        self.mxcTable.verticalHeader().setLabel(5,self.__tr("5"))
        self.mxcTable.verticalHeader().setLabel(6,self.__tr("6"))
        self.mxcTable.verticalHeader().setLabel(7,self.__tr("7"))
        self.groupBox6.setTitle(self.__tr("Trigger Enable / Event Sent"))
        self.enev_1.setText(self.__tr("tr1"))
        self.enev_2.setText(self.__tr("tr2"))
        self.enev_5.setText(self.__tr("tr5"))
        self.enev_6.setText(self.__tr("tr6"))
        self.enev_7.setText(self.__tr("tr7"))
        self.enev_4.setText(self.__tr("tr4"))
        self.enev_3.setText(self.__tr("tr3"))
        self.enev_0.setText(self.__tr("tr0"))
        self.groupBox9.setTitle(self.__tr("Clock"))
        self.textLabel2_2.setText(self.__tr("tipus"))
        self.textLabel4.setText(self.__tr("frac synth"))
        self.gbDBus.setTitle(self.__tr("Distrib Bus"))
        self.groupBox3.setTitle(self.__tr("AC"))
        self.textLabel2.setText(self.__tr("delay"))
        self.textLabel1.setText(self.__tr("prescaler"))
        self.acSyncMXC7.setText(self.__tr("SYNCMXC7"))
        self.acByPass.setText(self.__tr("BYPASS"))
        self.textLabel1_3.setText(self.__tr("trigger"))
        self.groupBox9_2.setTitle(self.__tr("Front Panel Univ In"))
        self.textLabel2_3.setText(self.__tr("0 (dbus, trig) .. 1.. 2"))
        self.groupBox8.setTitle(self.__tr("Data Buffer"))
        self.dataBufData.verticalHeader().setLabel(0,self.__tr("0"))
        self.dataBufSize.setText(self.__tr("4"))
        self.textLabel1_2.setText(self.__tr("size"))
        self.dataBufEnable.setText(self.__tr("enable dbuf"))
        self.dataBuffTrigger.setText(self.__tr("trigger"))
        self.dataBufMode.setText(self.__tr("Mode"))
        self.groupBox7.setTitle(self.__tr("Actions"))
        self.triggerSeq1.setText(self.__tr("Tr Seq 1"))
        QToolTip.add(self.triggerSeq1,self.__tr("Trigger Seq 1"))
        self.triggerSeq2.setText(self.__tr("Tr Seq 2"))
        QToolTip.add(self.triggerSeq2,self.__tr("Trigger Sequence 2"))
        self.sendSwEvent.setText(self.__tr("Send SW event:"))
        self.masterEnable.setText(self.__tr("enable"))
        self.swEventEnable.setText(self.__tr("SW event enable"))
        self.editSeq1.setText(self.__tr("Edit Seq 1"))
        self.loadConfig.setText(self.__tr("Load"))
        self.saveConfig.setText(self.__tr("Save"))
        self.editSeq2.setText(self.__tr("Edit Seq 2"))
        self.restoreConfig.setText(self.__tr("Restore"))
        self.applyConfig.setText(self.__tr("Apply"))


    def onRestoreConfig(self):
        print "EventGeneratorForm.onRestoreConfig(): Not implemented yet"

    def onApplyConfig(self):
        print "EventGeneratorForm.onApplyConfig(): Not implemented yet"

    def loadConfig_clicked(self):
        print "EventGeneratorForm.loadConfig_clicked(): Not implemented yet"

    def saveConfig_clicked(self):
        print "EventGeneratorForm.saveConfig_clicked(): Not implemented yet"

    def dataBufSize_returnPressed(self):
        print "EventGeneratorForm.dataBufSize_returnPressed(): Not implemented yet"

    def editSeq1_clicked(self):
        print "EventGeneratorForm.editSeq1_clicked(): Not implemented yet"

    def editSeq2_clicked(self):
        print "EventGeneratorForm.editSeq2_clicked(): Not implemented yet"

    def sendDataBuf_clicked(self):
        print "EventGeneratorForm.sendDataBuf_clicked(): Not implemented yet"

    def resetEvan_clicked(self):
        print "EventGeneratorForm.resetEvan_clicked(): Not implemented yet"

    def resetFifo_clicked(self):
        print "EventGeneratorForm.resetFifo_clicked(): Not implemented yet"

    def resetRXVio_clicked(self):
        print "EventGeneratorForm.resetRXVio_clicked(): Not implemented yet"

    def mxrs7_clicked(self):
        print "EventGeneratorForm.mxrs7_clicked(): Not implemented yet"

    def mxrs6_clicked(self):
        print "EventGeneratorForm.mxrs6_clicked(): Not implemented yet"

    def mxrs5_clicked(self):
        print "EventGeneratorForm.mxrs5_clicked(): Not implemented yet"

    def mxrs4_clicked(self):
        print "EventGeneratorForm.mxrs4_clicked(): Not implemented yet"

    def mxrs3_clicked(self):
        print "EventGeneratorForm.mxrs3_clicked(): Not implemented yet"

    def mxrs2_clicked(self):
        print "EventGeneratorForm.mxrs2_clicked(): Not implemented yet"

    def mxrs1_clicked(self):
        print "EventGeneratorForm.mxrs1_clicked(): Not implemented yet"

    def mxrs0_clicked(self):
        print "EventGeneratorForm.mxrs0_clicked(): Not implemented yet"

    def sendSwEvent_clicked(self):
        print "EventGeneratorForm.sendSwEvent_clicked(): Not implemented yet"

    def mxcTable_valueChanged(self,a0,a1):
        print "EventGeneratorForm.mxcTable_valueChanged(int,int): Not implemented yet"

    def triggerSeq2_clicked(self):
        print "EventGeneratorForm.triggerSeq2_clicked(): Not implemented yet"

    def triggerSeq1_clicked(self):
        print "EventGeneratorForm.triggerSeq1_clicked(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("EventGeneratorForm",s,c)
