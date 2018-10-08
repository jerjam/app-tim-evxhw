# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/sequenceeditorform.ui'
#
# Created: Thu Mar 5 11:44:25 2015
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *


class SequenceEditorForm(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("SequenceEditorForm")


        SequenceEditorFormLayout = QGridLayout(self,1,1,11,6,"SequenceEditorFormLayout")

        self.groupBox4 = QGroupBox(self,"groupBox4")
        self.groupBox4.setColumnLayout(0,Qt.Vertical)
        self.groupBox4.layout().setSpacing(6)
        self.groupBox4.layout().setMargin(11)
        groupBox4Layout = QGridLayout(self.groupBox4.layout())
        groupBox4Layout.setAlignment(Qt.AlignTop)

        self.timestamp_del = QPushButton(self.groupBox4,"timestamp_del")

        groupBox4Layout.addWidget(self.timestamp_del,1,2)
        spacer7 = QSpacerItem(122,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        groupBox4Layout.addItem(spacer7,1,0)

        self.timestamp_add = QPushButton(self.groupBox4,"timestamp_add")

        groupBox4Layout.addWidget(self.timestamp_add,1,1)

        layout33 = QHBoxLayout(None,0,6,"layout33")

        self.timestamp = QLineEdit(self.groupBox4,"timestamp")
        layout33.addWidget(self.timestamp)

        self.eventcode = QLineEdit(self.groupBox4,"eventcode")
        layout33.addWidget(self.eventcode)

        groupBox4Layout.addMultiCellLayout(layout33,0,0,0,2)

        SequenceEditorFormLayout.addWidget(self.groupBox4,0,0)

        self.list = QListView(self,"list")
        self.list.addColumn(self.__tr("Timestamp"))
        self.list.addColumn(self.__tr("EventCode"))
        self.list.setAllColumnsShowFocus(1)

        SequenceEditorFormLayout.addWidget(self.list,1,0)

        layout31 = QVBoxLayout(None,0,6,"layout31")

        self.seqEnable = QCheckBox(self,"seqEnable")
        layout31.addWidget(self.seqEnable)

        layout25 = QHBoxLayout(None,0,6,"layout25")

        self.textLabel1 = QLabel(self,"textLabel1")
        layout25.addWidget(self.textLabel1)
        spacer1 = QSpacerItem(20,22,QSizePolicy.Minimum,QSizePolicy.Minimum)
        layout25.addItem(spacer1)

        self.prescaler = QLineEdit(self,"prescaler")
        self.prescaler.setEnabled(0)
        self.prescaler.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed,0,0,self.prescaler.sizePolicy().hasHeightForWidth()))
        layout25.addWidget(self.prescaler)
        layout31.addLayout(layout25)

        layout30 = QHBoxLayout(None,0,6,"layout30")

        self.textLabel1_2 = QLabel(self,"textLabel1_2")
        layout30.addWidget(self.textLabel1_2)

        self.trigger = QComboBox(0,self,"trigger")
        layout30.addWidget(self.trigger)
        layout31.addLayout(layout30)

        self.single = QCheckBox(self,"single")
        self.single.setEnabled(1)
        layout31.addWidget(self.single)

        self.recycle = QCheckBox(self,"recycle")
        self.recycle.setEnabled(1)
        layout31.addWidget(self.recycle)
        spacer2 = QSpacerItem(190,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        layout31.addItem(spacer2)

        layout31_2 = QGridLayout(None,1,1,0,6,"layout31_2")

        self.cancel = QPushButton(self,"cancel")

        layout31_2.addWidget(self.cancel,1,0)

        self.ok = QPushButton(self,"ok")

        layout31_2.addWidget(self.ok,1,1)
        layout31.addLayout(layout31_2)

        SequenceEditorFormLayout.addMultiCellLayout(layout31,0,1,1,1)

        self.languageChange()

        self.resize(QSize(499,310).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.ok,SIGNAL("clicked()"),self.accept)
        self.connect(self.cancel,SIGNAL("clicked()"),self.close)
        self.connect(self.timestamp_add,SIGNAL("clicked()"),self.timestamp_add_clicked)
        self.connect(self.list,SIGNAL("clicked(QListViewItem*)"),self.list_clicked)
        self.connect(self.timestamp_del,SIGNAL("clicked()"),self.timestamp_del_clicked)

        self.setTabOrder(self.timestamp,self.eventcode)
        self.setTabOrder(self.eventcode,self.timestamp_add)
        self.setTabOrder(self.timestamp_add,self.timestamp_del)
        self.setTabOrder(self.timestamp_del,self.seqEnable)
        self.setTabOrder(self.seqEnable,self.prescaler)
        self.setTabOrder(self.prescaler,self.ok)
        self.setTabOrder(self.ok,self.cancel)


    def languageChange(self):
        self.setCaption(self.__tr("Sequence Editor"))
        self.groupBox4.setTitle(self.__tr("Timestamp and Event Code"))
        self.timestamp_del.setText(self.__tr("Delete"))
        self.timestamp_add.setText(self.__tr("Add"))
        self.list.header().setLabel(0,self.__tr("Timestamp"))
        self.list.header().setLabel(1,self.__tr("EventCode"))
        self.seqEnable.setText(self.__tr("Sequence enable"))
        self.textLabel1.setText(self.__tr("Prescaler:"))
        self.textLabel1_2.setText(self.__tr("Trigger"))
        self.single.setText(self.__tr("single"))
        self.recycle.setText(self.__tr("recycle"))
        self.cancel.setText(self.__tr("Cancel"))
        self.ok.setText(self.__tr("OK"))


    def trigger_cmode_toggled(self,a0):
        print "SequenceEditorForm.trigger_cmode_toggled(bool): Not implemented yet"

    def timestamp_add_clicked(self):
        print "SequenceEditorForm.timestamp_add_clicked(): Not implemented yet"

    def list_clicked(self,a0):
        print "SequenceEditorForm.list_clicked(QListViewItem*): Not implemented yet"

    def timestamp_del_clicked(self):
        print "SequenceEditorForm.timestamp_del_clicked(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("SequenceEditorForm",s,c)
