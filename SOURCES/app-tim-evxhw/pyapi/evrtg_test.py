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

"""
This script was made just to test the new EVR300TG, and see if we can
make it generate pulses.

It can be used both for testing normal PCI API and new UDP API
"""

from mevrconst import *
import mevr_udp
import mevr

def example_a(evr):
    evr.Enable(True)
    
    #evr.EnableRam(1)
    for i in xrange(1,11):
        evr.SetPulseMap(1, i, i-1, -1, -1)
        
        evr.SetPulseParams(i-1, 1, 0, 100)
        evr.SetPulseProperties(i-1, 0, 0, 0, 1, 1)
    
    # If I put it here, does not work!
    #evr.EnableRam(1)
    evr.Enable(True)

def example_b(evr):
    import time
    evr.Enable(True)
    evr.OutputEnable(True)
    for i in xrange(8):
        evr.CMLEnable(i, True)

    for i in xrange(8):
        evr.SetFPOutMap(i, 0)
        
    #time.sleep(3)
    evr.Enable(True)

    evr.SetFineDelay(0, 0)
    for i in xrange(1024):
        #evr.SetFineDelay(0, i)
        time.sleep(0.01)
    return evr

def example_c(evr):
    evr.Enable(True)

    #evr.EnableRam(1)
    #evr.EnableRam(2)
    evr.MapRamEnable(0,True)
    evr.MapRamEnable(1,True)
    for i in xrange(1,11):
        #evr.SetPulseMap(1, i, i-1, -1, -1)
        #evr.SetPulseMap(0, i, i-1, -1, -1)
        evr.SetPulseMap(1, 1, 0, -1, -1)
        evr.SetPulseMap(0, 1, 0, -1, -1)
        #evr.SetPulseParams(i-1, 1, 0, 2)
        evr.SetPulseParams(0, 1, 0, 1)
        evr.SetPulseProperties(0, 0, 0, 0, 1, 1)

    # If I put it here, does not work!
    evr.Enable(True)

    import time
    evr.Enable(True)
    evr.OutputEnable(1)
    for i in xrange(8):
        evr.CMLEnable(i, True)
        #evr.SetUnivOutMap(i, 0)
        #evr.SetFPOutMap(i, 0)
        #evr.SetTBOutMap(i, 0)
        evr.SetFPOutMap(i, 0)

    #time.sleep(3)
    evr.Enable(True)

    #evr.SetFineDelay(0, 0)
    #for i in xrange(1024):
        #evr.SetFineDelay(0, i)
        #time.sleep(0.01)
    #return evr

def main():
    # 0xc908146

    #Can be used both for testing "normal" pci API and new UDP API
    #Just comment/uncomment the necessary lines below

    #evr = mevr_udp.new('evr300lab01', 2000)
    evr = mevr.new('/dev/evrtga3')

    #example_a(evr)
    #example_b(evr)
    example_c(evr)

    #evr.map.Pulse[0].Width = 1
    #evr.SetFineDelay(0, 0)

    #evr.Enable(True)

    #print evr.map._parent._real.read_register(evr.map._parent._base + 0x200)

    return evr

evr = main()
