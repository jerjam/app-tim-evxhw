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

from auxer import *
from pulseeditor import PulseEditor
import time
class PulseControl (PseudoControl):
	controlName = 'PulseControl'
	
	def __init__(self, ctrl):
		self.eva = ctrl.eva
		self.ctList = ctrl.listPulse
		
		ctlist = self.ctList
		for i in range(0, self.eva.TOTAL_PULSES):
			it = QListViewItem(ctlist, self.mapName(i))
# 			it.setText(1, self.toFlagString(0,0,0,0,0,0))
			ctlist.insertItem(it)
	
	def getFromDev(self):
		return self.eva.getOpsPulse()

	def getFromForm(self):
		ctlist = self.ctList
		flags = self.eva.TOTAL_PULSES*[0]
		delay = self.eva.TOTAL_PULSES*[0]
		width = self.eva.TOTAL_PULSES*[0]
		presc = self.eva.TOTAL_PULSES*[0]
		
		it = ctlist.firstChild()
		i = 0
		while (it):
			flags[i], delay[i], width[i], presc[i] = self.getFromFormItem(it)
			it = it.nextSibling()
			i += 1
		return flags, delay, width, presc
		
	def set2Dev(self, flags, delay, width, presc):
		self.eva.setOpsPulse(flags, delay, width, presc)
		
	def set2Form(self, flags, delay, width, presc):
		ctlist = self.ctList
		
		it = ctlist.firstChild()
		i = 0
		while(it):
			self.set2FormItem(it, flags[i], delay[i], width[i], presc[i])
			it = it.nextSibling()
			i += 1
		

	def getFromFormItem(self, it):
		flags = self.fromFlagString(it.text(1))
		delay = it.text(2).toUInt()[0]
		width = it.text(3).toUInt()[0]
		presc = it.text(4).toUInt()[0]
		return flags, delay, width, presc
	
	def set2FormItem(self, it, flags, delay, width, presc):
		it.setText(1, apply(self.toFlagString, flags))
		it.setText(2, str(delay))
		it.setText(3, str(width))
		it.setText(4, str(presc))
		
		
		
	def modify(self, item):
		num = item.text(0).toUInt()[0]
		dlg = PulseEditor(pulseid=num)
		apply(dlg.loadValues, self.getFromFormItem(item))
		if not dlg.exec_loop():
			return None
		apply(self.set2FormItem, (item,) + dlg.getValues())
		
		
		
	def mapName(self, mapid):
		return "%02d" % mapid
	
	def toFlagString(self, enmaster, enirq, entrigger, enset, enclean, polarity):
		r = ''
		if enmaster: r+= 'm'
		else: r+='-'
		if enirq: r+= 'i'
		else: r+='-'
		if entrigger: r+= 't'
		else: r+='-'
		if enset: r+= 's'
		else: r+='-'
		if enclean: r+= 'c'
		else: r+='-'
		if polarity: r+= 'l' #TODO: no se quina era low i quina high, arreglar
		else: r+='h'
		return r
	def fromFlagString(self, etscp):
		enmaster = etscp[0] != '-'
		enirq = etscp[1] != '-'
		entrigger = etscp[2] != '-'
		enset = etscp[3] != '-'
		enclean = etscp[4] != '-'
		polarity = etscp[5] != 'h' #TODO: Quan es low i quan es high?
		return enmaster, enirq, entrigger, enset, enclean, polarity