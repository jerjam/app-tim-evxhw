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

class ClockControl(PseudoControl):

	controlName = 'ClockControl'
	def __init__(self, ctrl):
		self.eva = ctrl.eva
		self.ckmode = ctrl.ckMode
		self.cksynth = ctrl.ckSynth
		
		self.fracbitsout = [
			(0x00DE816D, "125 MHz"),
			(0x00FE816D, "124.95 MHz"),
			(0x0C928166, "124.908 MHz"),
			(0x018741AD, "119 MHz"),
			(0x072F01AD, "114.24 MHz"),
			(0x049E81AD, "106.25 MHz"),
			(0x008201AD, "100 MHz"),
			(0x025B41ED, "99.956 MHz"),
			(0x023701f4, "99.929520 MHz*"),
			(0x0187422D, "89.25 MHz"),
			(0x0082822D, "81 MHz"),
			(0x0106822D, "80 MHz"),
			(0x019E822D, "78.900 MHz"),
			(0x01064200, "77 MHz**"),
			(0x09ae4200, "76.9 MHz*"),
			(0x0dc24200, "76.883721 MHz*"),
			(0x018742AD, "71.4 MHz"),
			(0x0C9282A6, "62.454 MHz"),
			(0x009743AD, "50 MHz"),
			(0x025B43AD, "49.978 MHz"),
			(0x0176C36D, "49.965 MHz")
		]

		self.typeint = 0
		self.typeext = 1

		self.rfclocks = [
			('RF Frac Synth', self.typeint, 0),
			#this must be tested I am not sure it changes the divider to 1
			('RF EXT div 1', self.typeext, 1-1),
			('RF EXT div 4', self.typeext, 4-1),
			('RF EXT div 5', self.typeext, 5-1),
			('RF EXT div 6', self.typeext, 6-1),
			('RF EXT div 8', self.typeext, 8-1),
			('RF EXT div 10', self.typeext, 10-1),
			('RF EXT div 12', self.typeext, 12-1)
			]
		for n, desc in self.fracbitsout:
			self.cksynth.insertItem(desc)
		for desc, p1, p2 in self.rfclocks:
			self.ckmode.insertItem(desc)

	def getFromDev(self):
		return self.eva.getOpsClock()

	def getFromForm(self):
		cm = self.ckmode
		cs = self.cksynth
		
		mode = self.rfclocks[cm.currentItem()]
		synth = self.fracbitsout[cs.currentItem()]
		
		rftype = mode[1]
		rfdiv = mode[2]
		syn = synth[0]
		return rftype, rfdiv, syn

	def set2Dev(self, rftype, rfdiv, syn):
		return self.eva.setOpsClock(rftype, rfdiv, syn)

	def set2Form(self, rftype, rfdiv, syn):
		cm = self.ckmode
		cs = self.cksynth
		rfclocks = self.rfclocks
		fracbitsout = self.fracbitsout
		for i in range(0, len(fracbitsout)):
			if fracbitsout[i][0] == syn:
				cs.setCurrentItem(i)
		if rftype == self.typeint:
			cm.setCurrentItem(0)
		else:
			for i in range(1, len(rfclocks)):
				if rfclocks[i][2] == rfdiv:
					cm.setCurrentItem(i)
					break


