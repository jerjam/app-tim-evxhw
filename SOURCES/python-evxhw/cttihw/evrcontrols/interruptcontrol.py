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

#TODO: OLD! Its accessing directly the local device!!

#TODO: Delete this from here
class falsemevr:
	def __getattr__(self, name):
		return 0
mevr = falsemevr()
#TODO: delete to here

class InterruptControl (PseudoControl):
	controlName = 'InterruptControl'
	
	def __init__(self, ctrl):
		self.eva = ctrl.eva
		self.ctInterrupts = [
			(ctrl.irqMasterEnable, mevr.IRQ_MASTER_ENABLE),
			(ctrl.irqDataBuf, mevr.IRQFLAG_DATABUF),
			(ctrl.irqPulse, mevr.IRQFLAG_PULSE),
			(ctrl.irqEvent, mevr.IRQFLAG_EVENT),
			(ctrl.irqHeartBeat, mevr.IRQFLAG_HEARTBEAT),
			(ctrl.irqFifoFull, mevr.IRQFLAG_FIFOFULL),
			(ctrl.irqViolation, mevr.IRQFLAG_VIOLATION) ]
		for ct, irq in self.ctInterrupts:
			ct.setEnabled(False)
			
	def getFromDev(self):
		ev = self.ev
		ctints = self.ctInterrupts
		ints = len(ctints) * [False]
		reg = ev.GetIrqEnable()
		for i in range(0, len(ctints)):
			if reg & (1 << ctints[i][1]):
				ints[i] = True
		return (ints,)
	
	def getFromForm(self):
		ctints = self.ctInterrupts
		ints = len(ctints) * [False]
		for i in range(0, len(ctints)):
			if ctints[i][0].isChecked():
				ints[i] = True
		return (ints,)

	def set2Dev(self, ints):
		ev = self.ev
		ctints = self.ctInterrupts
		mask = 0
		for i in range(0, len(ints)):
			if ints[i]:
				mask |= (1 << ctints[i][1])
		ev.IrqEnable(mask)
		
	def set2Form(self, ints):
		ctints = self.ctInterrupts
		for i in range(0, len(ctints)):
			ctints[i][0].setChecked(ints[i])



	def clearIrq(self, mask=~0):
		ev = self.ev
		ev.ClearIrqFlags(mask)
		






























