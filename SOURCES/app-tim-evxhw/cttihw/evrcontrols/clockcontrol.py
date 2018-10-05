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


class ClockControl(PseudoControl):

    controlName = 'ClockControl'

    def __init__(self, ctrl):

        self.eva = ctrl.eva
        self.ctSynth = ctrl.ckSynthesiser
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

        for n,desc in self.fracbitsout:
            self.ctSynth.insertItem(desc)

    def getFromDev(self):
        return self.eva.getOpsClock()

    def getFromForm(self):
        cs = self.ctSynth
        synth = self.fracbitsout[cs.currentItem()]
        syn = synth[0]
        return (syn, )

    def set2Dev(self, syn):
        self.eva.setOpsClock(syn)

    def set2Form(self, syn):
        cs = self.ctSynth
        fracbitsout = self.fracbitsout
        for i in range(0, len(fracbitsout)):
            if fracbitsout[i][0] == syn:
                cs.setCurrentItem(i)

