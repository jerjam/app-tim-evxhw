# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/pulsemapform.ui'
#
# Created: Thu Mar 5 11:44:25 2015
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *


class PulseMapForm(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("PulseMapForm")


        PulseMapFormLayout = QVBoxLayout(self,11,6,"PulseMapFormLayout")

        self.triggers = QGroupBox(self,"triggers")
        self.triggers.setColumnLayout(0,Qt.Vertical)
        self.triggers.layout().setSpacing(0)
        self.triggers.layout().setMargin(11)
        triggersLayout = QGridLayout(self.triggers.layout())
        triggersLayout.setAlignment(Qt.AlignTop)

        self.trig_25 = QPushButton(self.triggers,"trig_25")
        self.trig_25.setToggleButton(1)

        triggersLayout.addWidget(self.trig_25,2,3)

        self.trig_2 = QPushButton(self.triggers,"trig_2")
        self.trig_2.setToggleButton(1)

        triggersLayout.addWidget(self.trig_2,0,2)

        self.trig_18 = QPushButton(self.triggers,"trig_18")
        self.trig_18.setToggleButton(1)

        triggersLayout.addWidget(self.trig_18,1,7)

        self.trig_6 = QPushButton(self.triggers,"trig_6")
        self.trig_6.setToggleButton(1)

        triggersLayout.addWidget(self.trig_6,0,6)

        self.trig_4 = QPushButton(self.triggers,"trig_4")
        self.trig_4.setToggleButton(1)

        triggersLayout.addWidget(self.trig_4,0,4)

        self.trig_11 = QPushButton(self.triggers,"trig_11")
        self.trig_11.setToggleButton(1)

        triggersLayout.addWidget(self.trig_11,1,0)

        self.trig_17 = QPushButton(self.triggers,"trig_17")
        self.trig_17.setToggleButton(1)

        triggersLayout.addWidget(self.trig_17,1,6)

        self.trig_5 = QPushButton(self.triggers,"trig_5")
        self.trig_5.setToggleButton(1)

        triggersLayout.addWidget(self.trig_5,0,5)

        self.trig_21 = QPushButton(self.triggers,"trig_21")
        self.trig_21.setToggleButton(1)

        triggersLayout.addWidget(self.trig_21,1,10)

        self.trig_16 = QPushButton(self.triggers,"trig_16")
        self.trig_16.setToggleButton(1)

        triggersLayout.addWidget(self.trig_16,1,5)

        self.trig_20 = QPushButton(self.triggers,"trig_20")
        self.trig_20.setToggleButton(1)

        triggersLayout.addWidget(self.trig_20,1,9)

        self.trig_8 = QPushButton(self.triggers,"trig_8")
        self.trig_8.setToggleButton(1)

        triggersLayout.addWidget(self.trig_8,0,8)

        self.trig_12 = QPushButton(self.triggers,"trig_12")
        self.trig_12.setToggleButton(1)

        triggersLayout.addWidget(self.trig_12,1,1)

        self.trig_9 = QPushButton(self.triggers,"trig_9")
        self.trig_9.setToggleButton(1)

        triggersLayout.addWidget(self.trig_9,0,9)

        self.trig_27 = QPushButton(self.triggers,"trig_27")
        self.trig_27.setToggleButton(1)

        triggersLayout.addWidget(self.trig_27,2,5)

        self.trig_13 = QPushButton(self.triggers,"trig_13")
        self.trig_13.setToggleButton(1)

        triggersLayout.addWidget(self.trig_13,1,2)

        self.trig_22 = QPushButton(self.triggers,"trig_22")
        self.trig_22.setToggleButton(1)

        triggersLayout.addWidget(self.trig_22,2,0)

        self.trig_15 = QPushButton(self.triggers,"trig_15")
        self.trig_15.setToggleButton(1)

        triggersLayout.addWidget(self.trig_15,1,4)

        self.trig_7 = QPushButton(self.triggers,"trig_7")
        self.trig_7.setToggleButton(1)

        triggersLayout.addWidget(self.trig_7,0,7)

        self.trig_1 = QPushButton(self.triggers,"trig_1")
        self.trig_1.setToggleButton(1)

        triggersLayout.addWidget(self.trig_1,0,1)

        self.trig_29 = QPushButton(self.triggers,"trig_29")
        self.trig_29.setToggleButton(1)

        triggersLayout.addWidget(self.trig_29,2,7)

        self.trig_14 = QPushButton(self.triggers,"trig_14")
        self.trig_14.setToggleButton(1)

        triggersLayout.addWidget(self.trig_14,1,3)

        self.trig_19 = QPushButton(self.triggers,"trig_19")
        self.trig_19.setToggleButton(1)

        triggersLayout.addWidget(self.trig_19,1,8)

        self.trig_30 = QPushButton(self.triggers,"trig_30")
        self.trig_30.setToggleButton(1)

        triggersLayout.addWidget(self.trig_30,2,8)

        self.trig_23 = QPushButton(self.triggers,"trig_23")
        self.trig_23.setToggleButton(1)

        triggersLayout.addWidget(self.trig_23,2,1)

        self.trig_31 = QPushButton(self.triggers,"trig_31")
        self.trig_31.setToggleButton(1)

        triggersLayout.addWidget(self.trig_31,2,9)

        self.trig_24 = QPushButton(self.triggers,"trig_24")
        self.trig_24.setToggleButton(1)

        triggersLayout.addWidget(self.trig_24,2,2)

        self.trig_28 = QPushButton(self.triggers,"trig_28")
        self.trig_28.setToggleButton(1)

        triggersLayout.addWidget(self.trig_28,2,6)

        self.trig_26 = QPushButton(self.triggers,"trig_26")
        self.trig_26.setToggleButton(1)

        triggersLayout.addWidget(self.trig_26,2,4)

        self.trig_3 = QPushButton(self.triggers,"trig_3")
        self.trig_3.setToggleButton(1)

        triggersLayout.addWidget(self.trig_3,0,3)

        self.trig_0 = QPushButton(self.triggers,"trig_0")
        self.trig_0.setToggleButton(1)

        triggersLayout.addWidget(self.trig_0,0,0)

        self.trig_10 = QPushButton(self.triggers,"trig_10")
        self.trig_10.setToggleButton(1)

        triggersLayout.addWidget(self.trig_10,0,10)
        PulseMapFormLayout.addWidget(self.triggers)

        self.set = QGroupBox(self,"set")
        self.set.setColumnLayout(0,Qt.Vertical)
        self.set.layout().setSpacing(0)
        self.set.layout().setMargin(11)
        setLayout = QGridLayout(self.set.layout())
        setLayout.setAlignment(Qt.AlignTop)

        self.set_25 = QPushButton(self.set,"set_25")
        self.set_25.setToggleButton(1)

        setLayout.addWidget(self.set_25,2,3)

        self.set_2 = QPushButton(self.set,"set_2")
        self.set_2.setToggleButton(1)

        setLayout.addWidget(self.set_2,0,2)

        self.set_18 = QPushButton(self.set,"set_18")
        self.set_18.setToggleButton(1)

        setLayout.addWidget(self.set_18,1,7)

        self.set_6 = QPushButton(self.set,"set_6")
        self.set_6.setToggleButton(1)

        setLayout.addWidget(self.set_6,0,6)

        self.set_4 = QPushButton(self.set,"set_4")
        self.set_4.setToggleButton(1)

        setLayout.addWidget(self.set_4,0,4)

        self.set_11 = QPushButton(self.set,"set_11")
        self.set_11.setToggleButton(1)

        setLayout.addWidget(self.set_11,1,0)

        self.set_17 = QPushButton(self.set,"set_17")
        self.set_17.setToggleButton(1)

        setLayout.addWidget(self.set_17,1,6)

        self.set_5 = QPushButton(self.set,"set_5")
        self.set_5.setToggleButton(1)

        setLayout.addWidget(self.set_5,0,5)

        self.set_21 = QPushButton(self.set,"set_21")
        self.set_21.setToggleButton(1)

        setLayout.addWidget(self.set_21,1,10)

        self.set_16 = QPushButton(self.set,"set_16")
        self.set_16.setToggleButton(1)

        setLayout.addWidget(self.set_16,1,5)

        self.set_20 = QPushButton(self.set,"set_20")
        self.set_20.setToggleButton(1)

        setLayout.addWidget(self.set_20,1,9)

        self.set_8 = QPushButton(self.set,"set_8")
        self.set_8.setToggleButton(1)

        setLayout.addWidget(self.set_8,0,8)

        self.set_12 = QPushButton(self.set,"set_12")
        self.set_12.setToggleButton(1)

        setLayout.addWidget(self.set_12,1,1)

        self.set_9 = QPushButton(self.set,"set_9")
        self.set_9.setToggleButton(1)

        setLayout.addWidget(self.set_9,0,9)

        self.set_27 = QPushButton(self.set,"set_27")
        self.set_27.setToggleButton(1)

        setLayout.addWidget(self.set_27,2,5)

        self.set_13 = QPushButton(self.set,"set_13")
        self.set_13.setToggleButton(1)

        setLayout.addWidget(self.set_13,1,2)

        self.set_22 = QPushButton(self.set,"set_22")
        self.set_22.setToggleButton(1)

        setLayout.addWidget(self.set_22,2,0)

        self.set_15 = QPushButton(self.set,"set_15")
        self.set_15.setToggleButton(1)

        setLayout.addWidget(self.set_15,1,4)

        self.set_7 = QPushButton(self.set,"set_7")
        self.set_7.setToggleButton(1)

        setLayout.addWidget(self.set_7,0,7)

        self.set_1 = QPushButton(self.set,"set_1")
        self.set_1.setToggleButton(1)

        setLayout.addWidget(self.set_1,0,1)

        self.set_29 = QPushButton(self.set,"set_29")
        self.set_29.setToggleButton(1)

        setLayout.addWidget(self.set_29,2,7)

        self.set_14 = QPushButton(self.set,"set_14")
        self.set_14.setToggleButton(1)

        setLayout.addWidget(self.set_14,1,3)

        self.set_19 = QPushButton(self.set,"set_19")
        self.set_19.setToggleButton(1)

        setLayout.addWidget(self.set_19,1,8)

        self.set_30 = QPushButton(self.set,"set_30")
        self.set_30.setToggleButton(1)

        setLayout.addWidget(self.set_30,2,8)

        self.set_23 = QPushButton(self.set,"set_23")
        self.set_23.setToggleButton(1)

        setLayout.addWidget(self.set_23,2,1)

        self.set_31 = QPushButton(self.set,"set_31")
        self.set_31.setToggleButton(1)

        setLayout.addWidget(self.set_31,2,9)

        self.set_24 = QPushButton(self.set,"set_24")
        self.set_24.setToggleButton(1)

        setLayout.addWidget(self.set_24,2,2)

        self.set_28 = QPushButton(self.set,"set_28")
        self.set_28.setToggleButton(1)

        setLayout.addWidget(self.set_28,2,6)

        self.set_26 = QPushButton(self.set,"set_26")
        self.set_26.setToggleButton(1)

        setLayout.addWidget(self.set_26,2,4)

        self.set_3 = QPushButton(self.set,"set_3")
        self.set_3.setToggleButton(1)

        setLayout.addWidget(self.set_3,0,3)

        self.set_0 = QPushButton(self.set,"set_0")
        self.set_0.setToggleButton(1)

        setLayout.addWidget(self.set_0,0,0)

        self.set_10 = QPushButton(self.set,"set_10")
        self.set_10.setToggleButton(1)

        setLayout.addWidget(self.set_10,0,10)
        PulseMapFormLayout.addWidget(self.set)

        self.clear = QGroupBox(self,"clear")
        self.clear.setColumnLayout(0,Qt.Vertical)
        self.clear.layout().setSpacing(0)
        self.clear.layout().setMargin(11)
        clearLayout = QGridLayout(self.clear.layout())
        clearLayout.setAlignment(Qt.AlignTop)

        self.clear_25 = QPushButton(self.clear,"clear_25")
        self.clear_25.setToggleButton(1)

        clearLayout.addWidget(self.clear_25,2,3)

        self.clear_2 = QPushButton(self.clear,"clear_2")
        self.clear_2.setToggleButton(1)

        clearLayout.addWidget(self.clear_2,0,2)

        self.clear_18 = QPushButton(self.clear,"clear_18")
        self.clear_18.setToggleButton(1)

        clearLayout.addWidget(self.clear_18,1,7)

        self.clear_6 = QPushButton(self.clear,"clear_6")
        self.clear_6.setToggleButton(1)

        clearLayout.addWidget(self.clear_6,0,6)

        self.clear_4 = QPushButton(self.clear,"clear_4")
        self.clear_4.setToggleButton(1)

        clearLayout.addWidget(self.clear_4,0,4)

        self.clear_11 = QPushButton(self.clear,"clear_11")
        self.clear_11.setToggleButton(1)

        clearLayout.addWidget(self.clear_11,1,0)

        self.clear_17 = QPushButton(self.clear,"clear_17")
        self.clear_17.setToggleButton(1)

        clearLayout.addWidget(self.clear_17,1,6)

        self.clear_5 = QPushButton(self.clear,"clear_5")
        self.clear_5.setToggleButton(1)

        clearLayout.addWidget(self.clear_5,0,5)

        self.clear_21 = QPushButton(self.clear,"clear_21")
        self.clear_21.setToggleButton(1)

        clearLayout.addWidget(self.clear_21,1,10)

        self.clear_16 = QPushButton(self.clear,"clear_16")
        self.clear_16.setToggleButton(1)

        clearLayout.addWidget(self.clear_16,1,5)

        self.clear_20 = QPushButton(self.clear,"clear_20")
        self.clear_20.setToggleButton(1)

        clearLayout.addWidget(self.clear_20,1,9)

        self.clear_8 = QPushButton(self.clear,"clear_8")
        self.clear_8.setToggleButton(1)

        clearLayout.addWidget(self.clear_8,0,8)

        self.clear_12 = QPushButton(self.clear,"clear_12")
        self.clear_12.setToggleButton(1)

        clearLayout.addWidget(self.clear_12,1,1)

        self.clear_9 = QPushButton(self.clear,"clear_9")
        self.clear_9.setToggleButton(1)

        clearLayout.addWidget(self.clear_9,0,9)

        self.clear_27 = QPushButton(self.clear,"clear_27")
        self.clear_27.setToggleButton(1)

        clearLayout.addWidget(self.clear_27,2,5)

        self.clear_13 = QPushButton(self.clear,"clear_13")
        self.clear_13.setToggleButton(1)

        clearLayout.addWidget(self.clear_13,1,2)

        self.clear_22 = QPushButton(self.clear,"clear_22")
        self.clear_22.setToggleButton(1)

        clearLayout.addWidget(self.clear_22,2,0)

        self.clear_15 = QPushButton(self.clear,"clear_15")
        self.clear_15.setToggleButton(1)

        clearLayout.addWidget(self.clear_15,1,4)

        self.clear_7 = QPushButton(self.clear,"clear_7")
        self.clear_7.setToggleButton(1)

        clearLayout.addWidget(self.clear_7,0,7)

        self.clear_1 = QPushButton(self.clear,"clear_1")
        self.clear_1.setToggleButton(1)

        clearLayout.addWidget(self.clear_1,0,1)

        self.clear_29 = QPushButton(self.clear,"clear_29")
        self.clear_29.setToggleButton(1)

        clearLayout.addWidget(self.clear_29,2,7)

        self.clear_14 = QPushButton(self.clear,"clear_14")
        self.clear_14.setToggleButton(1)

        clearLayout.addWidget(self.clear_14,1,3)

        self.clear_19 = QPushButton(self.clear,"clear_19")
        self.clear_19.setToggleButton(1)

        clearLayout.addWidget(self.clear_19,1,8)

        self.clear_30 = QPushButton(self.clear,"clear_30")
        self.clear_30.setToggleButton(1)

        clearLayout.addWidget(self.clear_30,2,8)

        self.clear_23 = QPushButton(self.clear,"clear_23")
        self.clear_23.setToggleButton(1)

        clearLayout.addWidget(self.clear_23,2,1)

        self.clear_31 = QPushButton(self.clear,"clear_31")
        self.clear_31.setToggleButton(1)

        clearLayout.addWidget(self.clear_31,2,9)

        self.clear_24 = QPushButton(self.clear,"clear_24")
        self.clear_24.setToggleButton(1)

        clearLayout.addWidget(self.clear_24,2,2)

        self.clear_28 = QPushButton(self.clear,"clear_28")
        self.clear_28.setToggleButton(1)

        clearLayout.addWidget(self.clear_28,2,6)

        self.clear_26 = QPushButton(self.clear,"clear_26")
        self.clear_26.setToggleButton(1)

        clearLayout.addWidget(self.clear_26,2,4)

        self.clear_3 = QPushButton(self.clear,"clear_3")
        self.clear_3.setToggleButton(1)

        clearLayout.addWidget(self.clear_3,0,3)

        self.clear_0 = QPushButton(self.clear,"clear_0")
        self.clear_0.setToggleButton(1)

        clearLayout.addWidget(self.clear_0,0,0)

        self.clear_10 = QPushButton(self.clear,"clear_10")
        self.clear_10.setToggleButton(1)

        clearLayout.addWidget(self.clear_10,0,10)
        PulseMapFormLayout.addWidget(self.clear)

        self.led_event = QCheckBox(self,"led_event")
        PulseMapFormLayout.addWidget(self.led_event)

        layout16 = QHBoxLayout(None,0,6,"layout16")
        spacer3 = QSpacerItem(221,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout16.addItem(spacer3)

        self.btCancel = QPushButton(self,"btCancel")
        layout16.addWidget(self.btCancel)

        self.btOK = QPushButton(self,"btOK")
        layout16.addWidget(self.btOK)
        PulseMapFormLayout.addLayout(layout16)

        self.languageChange()

        self.resize(QSize(524,395).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.btOK,SIGNAL("clicked()"),self.accept)
        self.connect(self.btCancel,SIGNAL("clicked()"),self.reject)

        self.setTabOrder(self.btCancel,self.btOK)
        self.setTabOrder(self.btOK,self.trig_0)
        self.setTabOrder(self.trig_0,self.trig_1)
        self.setTabOrder(self.trig_1,self.trig_2)
        self.setTabOrder(self.trig_2,self.trig_3)
        self.setTabOrder(self.trig_3,self.trig_4)
        self.setTabOrder(self.trig_4,self.trig_5)
        self.setTabOrder(self.trig_5,self.trig_6)
        self.setTabOrder(self.trig_6,self.trig_7)
        self.setTabOrder(self.trig_7,self.trig_8)
        self.setTabOrder(self.trig_8,self.trig_9)
        self.setTabOrder(self.trig_9,self.trig_10)
        self.setTabOrder(self.trig_10,self.trig_11)
        self.setTabOrder(self.trig_11,self.trig_12)
        self.setTabOrder(self.trig_12,self.trig_13)
        self.setTabOrder(self.trig_13,self.trig_14)
        self.setTabOrder(self.trig_14,self.trig_15)
        self.setTabOrder(self.trig_15,self.trig_16)
        self.setTabOrder(self.trig_16,self.trig_17)
        self.setTabOrder(self.trig_17,self.trig_18)
        self.setTabOrder(self.trig_18,self.trig_19)
        self.setTabOrder(self.trig_19,self.trig_20)
        self.setTabOrder(self.trig_20,self.trig_21)
        self.setTabOrder(self.trig_21,self.trig_22)
        self.setTabOrder(self.trig_22,self.trig_23)
        self.setTabOrder(self.trig_23,self.trig_24)
        self.setTabOrder(self.trig_24,self.trig_25)
        self.setTabOrder(self.trig_25,self.trig_26)
        self.setTabOrder(self.trig_26,self.trig_27)
        self.setTabOrder(self.trig_27,self.trig_28)
        self.setTabOrder(self.trig_28,self.trig_29)
        self.setTabOrder(self.trig_29,self.trig_30)
        self.setTabOrder(self.trig_30,self.trig_31)
        self.setTabOrder(self.trig_31,self.set_0)
        self.setTabOrder(self.set_0,self.set_1)
        self.setTabOrder(self.set_1,self.set_2)
        self.setTabOrder(self.set_2,self.set_3)
        self.setTabOrder(self.set_3,self.set_4)
        self.setTabOrder(self.set_4,self.set_5)
        self.setTabOrder(self.set_5,self.set_6)
        self.setTabOrder(self.set_6,self.set_7)
        self.setTabOrder(self.set_7,self.set_8)
        self.setTabOrder(self.set_8,self.set_9)
        self.setTabOrder(self.set_9,self.set_10)
        self.setTabOrder(self.set_10,self.set_11)
        self.setTabOrder(self.set_11,self.set_12)
        self.setTabOrder(self.set_12,self.set_13)
        self.setTabOrder(self.set_13,self.set_14)
        self.setTabOrder(self.set_14,self.set_15)
        self.setTabOrder(self.set_15,self.set_16)
        self.setTabOrder(self.set_16,self.set_17)
        self.setTabOrder(self.set_17,self.set_18)
        self.setTabOrder(self.set_18,self.set_19)
        self.setTabOrder(self.set_19,self.set_20)
        self.setTabOrder(self.set_20,self.set_21)
        self.setTabOrder(self.set_21,self.set_22)
        self.setTabOrder(self.set_22,self.set_23)
        self.setTabOrder(self.set_23,self.set_24)
        self.setTabOrder(self.set_24,self.set_25)
        self.setTabOrder(self.set_25,self.set_26)
        self.setTabOrder(self.set_26,self.set_27)
        self.setTabOrder(self.set_27,self.set_28)
        self.setTabOrder(self.set_28,self.set_29)
        self.setTabOrder(self.set_29,self.set_30)
        self.setTabOrder(self.set_30,self.set_31)
        self.setTabOrder(self.set_31,self.clear_0)
        self.setTabOrder(self.clear_0,self.clear_1)
        self.setTabOrder(self.clear_1,self.clear_2)
        self.setTabOrder(self.clear_2,self.clear_3)
        self.setTabOrder(self.clear_3,self.clear_4)
        self.setTabOrder(self.clear_4,self.clear_5)
        self.setTabOrder(self.clear_5,self.clear_6)
        self.setTabOrder(self.clear_6,self.clear_7)
        self.setTabOrder(self.clear_7,self.clear_8)
        self.setTabOrder(self.clear_8,self.clear_9)
        self.setTabOrder(self.clear_9,self.clear_10)
        self.setTabOrder(self.clear_10,self.clear_11)
        self.setTabOrder(self.clear_11,self.clear_12)
        self.setTabOrder(self.clear_12,self.clear_13)
        self.setTabOrder(self.clear_13,self.clear_14)
        self.setTabOrder(self.clear_14,self.clear_15)
        self.setTabOrder(self.clear_15,self.clear_16)
        self.setTabOrder(self.clear_16,self.clear_17)
        self.setTabOrder(self.clear_17,self.clear_18)
        self.setTabOrder(self.clear_18,self.clear_19)
        self.setTabOrder(self.clear_19,self.clear_20)
        self.setTabOrder(self.clear_20,self.clear_21)
        self.setTabOrder(self.clear_21,self.clear_22)
        self.setTabOrder(self.clear_22,self.clear_23)
        self.setTabOrder(self.clear_23,self.clear_24)
        self.setTabOrder(self.clear_24,self.clear_25)
        self.setTabOrder(self.clear_25,self.clear_26)
        self.setTabOrder(self.clear_26,self.clear_27)
        self.setTabOrder(self.clear_27,self.clear_28)
        self.setTabOrder(self.clear_28,self.clear_29)
        self.setTabOrder(self.clear_29,self.clear_30)
        self.setTabOrder(self.clear_30,self.clear_31)
        self.setTabOrder(self.clear_31,self.led_event)


    def languageChange(self):
        self.setCaption(self.__tr("Pulse Map"))
        self.triggers.setTitle(self.__tr("Trigger"))
        self.trig_25.setText(self.__tr("25"))
        self.trig_2.setText(self.__tr("2"))
        self.trig_18.setText(self.__tr("18"))
        self.trig_6.setText(self.__tr("6"))
        self.trig_4.setText(self.__tr("4"))
        self.trig_11.setText(self.__tr("11"))
        self.trig_17.setText(self.__tr("17"))
        self.trig_5.setText(self.__tr("5"))
        self.trig_21.setText(self.__tr("21"))
        self.trig_16.setText(self.__tr("16"))
        self.trig_20.setText(self.__tr("20"))
        self.trig_8.setText(self.__tr("8"))
        self.trig_12.setText(self.__tr("12"))
        self.trig_9.setText(self.__tr("9"))
        self.trig_27.setText(self.__tr("27"))
        self.trig_13.setText(self.__tr("13"))
        self.trig_22.setText(self.__tr("22"))
        self.trig_15.setText(self.__tr("15"))
        self.trig_7.setText(self.__tr("7"))
        self.trig_1.setText(self.__tr("1"))
        self.trig_29.setText(self.__tr("29"))
        self.trig_14.setText(self.__tr("14"))
        self.trig_19.setText(self.__tr("19"))
        self.trig_30.setText(self.__tr("30"))
        self.trig_23.setText(self.__tr("23"))
        self.trig_31.setText(self.__tr("31"))
        self.trig_24.setText(self.__tr("24"))
        self.trig_28.setText(self.__tr("28"))
        self.trig_26.setText(self.__tr("26"))
        self.trig_3.setText(self.__tr("3"))
        self.trig_0.setText(self.__tr("0"))
        self.trig_10.setText(self.__tr("10"))
        self.set.setTitle(self.__tr("Set"))
        self.set_25.setText(self.__tr("25"))
        self.set_2.setText(self.__tr("2"))
        self.set_18.setText(self.__tr("18"))
        self.set_6.setText(self.__tr("6"))
        self.set_4.setText(self.__tr("4"))
        self.set_11.setText(self.__tr("11"))
        self.set_17.setText(self.__tr("17"))
        self.set_5.setText(self.__tr("5"))
        self.set_21.setText(self.__tr("21"))
        self.set_16.setText(self.__tr("16"))
        self.set_20.setText(self.__tr("20"))
        self.set_8.setText(self.__tr("8"))
        self.set_12.setText(self.__tr("12"))
        self.set_9.setText(self.__tr("9"))
        self.set_27.setText(self.__tr("27"))
        self.set_13.setText(self.__tr("13"))
        self.set_22.setText(self.__tr("22"))
        self.set_15.setText(self.__tr("15"))
        self.set_7.setText(self.__tr("7"))
        self.set_1.setText(self.__tr("1"))
        self.set_29.setText(self.__tr("29"))
        self.set_14.setText(self.__tr("14"))
        self.set_19.setText(self.__tr("19"))
        self.set_30.setText(self.__tr("30"))
        self.set_23.setText(self.__tr("23"))
        self.set_31.setText(self.__tr("31"))
        self.set_24.setText(self.__tr("24"))
        self.set_28.setText(self.__tr("28"))
        self.set_26.setText(self.__tr("26"))
        self.set_3.setText(self.__tr("3"))
        self.set_0.setText(self.__tr("0"))
        self.set_10.setText(self.__tr("10"))
        self.clear.setTitle(self.__tr("Clear"))
        self.clear_25.setText(self.__tr("25"))
        self.clear_2.setText(self.__tr("2"))
        self.clear_18.setText(self.__tr("18"))
        self.clear_6.setText(self.__tr("6"))
        self.clear_4.setText(self.__tr("4"))
        self.clear_11.setText(self.__tr("11"))
        self.clear_17.setText(self.__tr("17"))
        self.clear_5.setText(self.__tr("5"))
        self.clear_21.setText(self.__tr("21"))
        self.clear_16.setText(self.__tr("16"))
        self.clear_20.setText(self.__tr("20"))
        self.clear_8.setText(self.__tr("8"))
        self.clear_12.setText(self.__tr("12"))
        self.clear_9.setText(self.__tr("9"))
        self.clear_27.setText(self.__tr("27"))
        self.clear_13.setText(self.__tr("13"))
        self.clear_22.setText(self.__tr("22"))
        self.clear_15.setText(self.__tr("15"))
        self.clear_7.setText(self.__tr("7"))
        self.clear_1.setText(self.__tr("1"))
        self.clear_29.setText(self.__tr("29"))
        self.clear_14.setText(self.__tr("14"))
        self.clear_19.setText(self.__tr("19"))
        self.clear_30.setText(self.__tr("30"))
        self.clear_23.setText(self.__tr("23"))
        self.clear_31.setText(self.__tr("31"))
        self.clear_24.setText(self.__tr("24"))
        self.clear_28.setText(self.__tr("28"))
        self.clear_26.setText(self.__tr("26"))
        self.clear_3.setText(self.__tr("3"))
        self.clear_0.setText(self.__tr("0"))
        self.clear_10.setText(self.__tr("10"))
        self.led_event.setText(self.__tr("Led event"))
        self.btCancel.setText(self.__tr("Cancel"))
        self.btOK.setText(self.__tr("OK"))


    def __tr(self,s,c = None):
        return qApp.translate("PulseMapForm",s,c)
