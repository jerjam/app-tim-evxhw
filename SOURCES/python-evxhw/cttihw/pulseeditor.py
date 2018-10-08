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
from pulseeditorform import PulseEditorForm

class PulseEditor (PulseEditorForm):
	def __init__(self, parent=None, name=None, fl=0, pulseid=0):
		PulseEditorForm.__init__(self, parent, name, fl)
		self.setCaption('Pulse(' + str(pulseid)+ ') editor')
		
	def loadValues(self, flags, delay, width, presc):
		enmaster, enirq, entrigger, enset, enclear, polarity = flags
		self.enMaster.setChecked(enmaster)
		self.enIrq.setChecked(enirq)
		self.enTrigger.setChecked(entrigger)
		self.enSet.setChecked(enset)
		self.enClear.setChecked(enclear)
		self.polarity.setButton(polarity)

		self.delay.setText(str(delay))
		self.width.setText(str(width))
		self.prescaler.setText(str(presc))
		
	
	def getValues(self):
		enmaster = self.enMaster.isChecked()
		enirq = self.enIrq.isChecked()
		entrigger = self.enTrigger.isChecked()
		enset = self.enSet.isChecked()
		enclear = self.enClear.isChecked()
		polarity = self.polarity.selectedId()
		flags = enmaster, enirq, entrigger, enset, enclear, polarity
		
		delay = self.delay.text().toUInt()
		width = self.width.text().toUInt()
		presc = self.prescaler.text().toUInt()
		
		if not (delay[1] and width[1] and presc[1]):
			return None
		delay = delay[0]
		width = width[0]
		presc =  presc[0]
		
		return flags, delay, width, presc
	
	def accept(self):
		if self.getValues():
			PulseEditorForm.accept(self)



















