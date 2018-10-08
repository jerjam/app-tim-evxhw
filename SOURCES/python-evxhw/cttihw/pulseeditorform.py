# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/pulseeditorform.ui'
#
# Created: Thu Mar 5 11:44:25 2015
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *


class PulseEditorForm(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("PulseEditorForm")

        self.setModal(1)

        PulseEditorFormLayout = QVBoxLayout(self,11,6,"PulseEditorFormLayout")

        layout18 = QGridLayout(None,1,1,0,6,"layout18")

        self.textLabel2 = QLabel(self,"textLabel2")

        layout18.addWidget(self.textLabel2,1,0)

        self.prescaler = QLineEdit(self,"prescaler")

        layout18.addWidget(self.prescaler,2,1)

        self.textLabel1 = QLabel(self,"textLabel1")

        layout18.addWidget(self.textLabel1,0,0)

        self.textLabel3 = QLabel(self,"textLabel3")

        layout18.addWidget(self.textLabel3,2,0)

        self.delay = QLineEdit(self,"delay")

        layout18.addWidget(self.delay,0,1)

        self.width = QLineEdit(self,"width")

        layout18.addWidget(self.width,1,1)
        PulseEditorFormLayout.addLayout(layout18)

        self.groupBox13 = QGroupBox(self,"groupBox13")
        self.groupBox13.setColumnLayout(0,Qt.Vertical)
        self.groupBox13.layout().setSpacing(6)
        self.groupBox13.layout().setMargin(11)
        groupBox13Layout = QVBoxLayout(self.groupBox13.layout())
        groupBox13Layout.setAlignment(Qt.AlignTop)

        self.enMaster = QCheckBox(self.groupBox13,"enMaster")
        groupBox13Layout.addWidget(self.enMaster)

        self.enIrq = QCheckBox(self.groupBox13,"enIrq")
        self.enIrq.setEnabled(0)
        groupBox13Layout.addWidget(self.enIrq)

        self.enTrigger = QCheckBox(self.groupBox13,"enTrigger")
        groupBox13Layout.addWidget(self.enTrigger)

        self.enSet = QCheckBox(self.groupBox13,"enSet")
        groupBox13Layout.addWidget(self.enSet)

        self.enClear = QCheckBox(self.groupBox13,"enClear")
        groupBox13Layout.addWidget(self.enClear)
        PulseEditorFormLayout.addWidget(self.groupBox13)

        self.polarity = QButtonGroup(self,"polarity")
        self.polarity.setProperty("selectedId",QVariant(0))
        self.polarity.setColumnLayout(0,Qt.Vertical)
        self.polarity.layout().setSpacing(6)
        self.polarity.layout().setMargin(11)
        polarityLayout = QVBoxLayout(self.polarity.layout())
        polarityLayout.setAlignment(Qt.AlignTop)

        self.polarLow = QRadioButton(self.polarity,"polarLow")
        self.polarity.insert( self.polarLow,1)
        polarityLayout.addWidget(self.polarLow)

        self.polarHigh = QRadioButton(self.polarity,"polarHigh")
        self.polarHigh.setChecked(1)
        self.polarity.insert( self.polarHigh,0)
        polarityLayout.addWidget(self.polarHigh)
        PulseEditorFormLayout.addWidget(self.polarity)

        layout17 = QHBoxLayout(None,0,6,"layout17")
        spacer1 = QSpacerItem(61,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout17.addItem(spacer1)

        self.btCancel = QPushButton(self,"btCancel")
        layout17.addWidget(self.btCancel)

        self.btOK = QPushButton(self,"btOK")
        layout17.addWidget(self.btOK)
        PulseEditorFormLayout.addLayout(layout17)

        self.languageChange()

        self.resize(QSize(196,380).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.btOK,SIGNAL("clicked()"),self.accept)
        self.connect(self.btCancel,SIGNAL("clicked()"),self.close)

        self.setTabOrder(self.btCancel,self.btOK)
        self.setTabOrder(self.btOK,self.delay)
        self.setTabOrder(self.delay,self.width)
        self.setTabOrder(self.width,self.prescaler)
        self.setTabOrder(self.prescaler,self.enMaster)
        self.setTabOrder(self.enMaster,self.enIrq)
        self.setTabOrder(self.enIrq,self.enTrigger)
        self.setTabOrder(self.enTrigger,self.enSet)
        self.setTabOrder(self.enSet,self.enClear)
        self.setTabOrder(self.enClear,self.polarHigh)


    def languageChange(self):
        self.setCaption(self.__tr("Pulse Editor"))
        self.textLabel2.setText(self.__tr("Width"))
        self.textLabel1.setText(self.__tr("Delay"))
        self.textLabel3.setText(self.__tr("Prescaler"))
        self.groupBox13.setTitle(self.__tr("Enable"))
        self.enMaster.setText(self.__tr("master"))
        self.enIrq.setText(self.__tr("irq"))
        self.enTrigger.setText(self.__tr("trigger"))
        self.enSet.setText(self.__tr("set"))
        self.enClear.setText(self.__tr("clear"))
        self.polarity.setTitle(self.__tr("Polarity"))
        self.polarLow.setText(self.__tr("Active Low"))
        self.polarHigh.setText(self.__tr("Active High"))
        self.btCancel.setText(self.__tr("Cancel"))
        self.btOK.setText(self.__tr("OK"))


    def __tr(self,s,c = None):
        return qApp.translate("PulseEditorForm",s,c)
