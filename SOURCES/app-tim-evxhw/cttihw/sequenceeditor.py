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

from auxeg import *
from sequenceeditorform import SequenceEditorForm


# seq = 0
class SequenceEditor(SequenceEditorForm):
	def __init__(self, parent=None, name=None, fl=0, seq=1):
		SequenceEditorForm.__init__(self,parent,name,fl)
		self.controlName = 'SequenceEditor' + str(seq)
		self.sequence = seq
		self.eva = parent.eva
		self.setCaption('Sequence Editor: RAM ' + str(seq))
		
		self.mappings = []
		for i in range(0, self.eva.TOTAL_MXCS):
			self.mappings += [ ('MXC ' + str(i), i + self.eva.SEQTRIG_MXC_BASE ) ];
		self.mappings += [ ('ACINPUT', self.eva.SEQTRIG_ACINPUT ) ];
		self.mappings += [ ('SWTRIGGER1', self.eva.SEQTRIG_SWTRIGGER1 ) ];
		self.mappings += [ ('SWTRIGGER2', self.eva.SEQTRIG_SWTRIGGER2 ) ];
		
		for m in self.mappings:
			self.trigger.insertItem(m[0])
		
		self.list.setSorting(0)
# 		self.lastvals = self.getFromDev()

	def editSequence(self):
		apply(self.set2Form, self.lastvals)
		if self.exec_loop():
			r = self.getFromForm()
			if type(r) is str:
				QMessageBox.critical(self, 'Bad last EC', r,QMessageBox.Ok)
			else:
				self.lastvals = r

	def getFromDev(self):
		return self.eva.getOpsSequenceEditor(self.sequence)
		
	def getFromForm(self):
		rs = self.sequence
		l = self.list
		trigsel = 0
		END_SEQUENCE_EVENT_CODE = 127 #TDOD: Asseugrarse que es 127 i moure la cosntant a un altre lloc(mevgconst?)
		ec = END_SEQUENCE_EVENT_CODE
		
		seqen = self.seqEnable.isChecked()
		single = self.single.isChecked()
		recycle = self.recycle.isChecked()
		
		trigsel = self.mappings[self.trigger.currentItem()][1]
		seq = []
		l.setSorting(0)
		it = l.firstChild()
		while it:
			ts = int(str(it.text(0)))
			ec = int(str(it.text(1)))
			seq += [(ts, ec)]
			it = it.nextSibling()
		if ec != END_SEQUENCE_EVENT_CODE:
			return "The last event code in the RAM must be 127"
		return seq, seqen, trigsel, single, recycle
	def set2Dev(self, seq, seqen, trigsel, single, recycle):
		self.eva.setOpsSequenceEditor(self.sequence, seq, seqen, trigsel, single, recycle)
		
	def set2Form(self, seq, seqen, trigsel, single, recycle):
		l = self.list
		self.seqEnable.setChecked(seqen)
		self.single.setChecked(single)
		self.recycle.setChecked(recycle)
		
		self.trigger.setCurrentItem(self.reverseMap(trigsel))

		l.setSorting(0)
		l.clear()
		for i in range(0, len(seq)):
			ts = '%.8d' % seq[i][0]
			ec = seq[i][1]
			l.insertItem(QListViewItem(self.list, ts, str(ec)))









	def restore(self):
		r = self.getFromDev()
		self.lastvals = r
		#apply(self.set2Form, r)

	def applyConf(self):
# 		r = self.getFromForm()
		r = self.lastvals
		apply(self.set2Dev, r)
	
	def io(self, dict, saving):
		if saving:
			vals = self.getFromDev()
			dict[self.controlName] = vals
		else:
			self.lastvals = dict[self.controlName]
	
	def list_clicked(self, it):
		if it:
			self.timestamp.setText(str(it.text(0).toInt()[0]))
			self.eventcode.setText(it.text(1))
			self.eventcode.setFocus()
			self.eventcode.selectAll()
	
	def trigger_cmode_toggled(self, stat):
		self.triggers.setEnabled(not stat)

	def get_timestamp_eventcode(self):
		ts = str(self.timestamp.text())
		ec = str(self.eventcode.text())
		try:
			ts = int(ts)
			ec = int(ec)
		except:
			return None, None
		return ts, ec

	def timestamp_add_clicked(self):
		ts, ec = self.get_timestamp_eventcode()
		if ts:
			if ts < 0:
				self.timestamp.setFocus()
				self.timestamp.selectAll()
			elif not ec in range (0, 256):
				self.eventcode.setFocus()
				self.eventcode.selectAll()
			else:
				l = self.list
				ts2 = '%.8d' % ts
				it = l.findItem(ts2, 0)
				if it:
					it.setText(1, str(ec))
				else:
					l.insertItem(QListViewItem(self.list, ts2, str(ec)))
	    			self.timestamp.setFocus()
	    			self.timestamp.selectAll()
    
    
	def timestamp_del_clicked(self):
		ts, ec = self.get_timestamp_eventcode()
		if ts:
			l = self.list
			ts2 = '%.8d' % ts
			it = l.findItem(ts2, 0)
			print it, l.childCount()
			if it:
				l.takeItem(it)
       

      
	def accept(self):
		#self.set2Dev(seqen, presc, cmode, trmxc, trac, seq)
		SequenceEditorForm.accept(self)


		
	def reverseMap(self, mapp):
		mapping = self.mappings
		i = 0
		for m in mapping:
			if m[1] == mapp: return i
			i += 1
		return 0

