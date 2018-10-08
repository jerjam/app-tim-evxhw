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


import MrfFanOut
from mevrconst import *
import evr_map

class _RealUDPEvr(object):
    def __init__(self, host, port=2000):
        self._base = 0x7a000000
        self._real = MrfFanOut.FanOut(host, port)

    def GetVal32(self, address):
        rh = self._real.read_register(self._base + address)
        rl = self._real.read_register(self._base + address + 2)
        return rl | (rh << 16)
        
    def SetVal32(self, address, value):
        rh = self._real.write_register(self._base + address, value >> 16)
        rl = self._real.write_register(self._base + address + 2, 0xffff & value)
        return rl | (rh << 16)
        
    def GetVal16(self, address):
        return self._real.read_register(self._base + address)
        
    def SetVal16(self, address, value):
        return self._real.write_register(self._base + address, value)

class PyEvr(object):
    def __init__(self, mapdev):
        self.map = mapdev
        
    def Enable(self, en):
        r = self.map.Control
        if en:
            r = r | (1 << 31)
        else:
            r = r & ~(1 << 31)
        self.map.Control = r
            
    def ClearViolation(self):
        r = (1 << 16)
        self.map.Status = r
        
    def EnableRam(self, ram_no):
        r = self.map.Control
        if ram_no is None:
            r = r & ~(1 << 9)
        elif ram_no == 1:
            r = (r | (1 << 9)) & ~(1 << 8)
        elif ram_no == 2:
            r = r | (1 << 9) | (1 << 8)
        else:
            raise IndexError("Ram must be 1 or 2")
        self.map.Control = r
        
    def OutputEnable(self, en):
        r = self.map.Control
        if en:
            r = r | (1 << 27)
        else:
            r = r & ~(1 << 27)
        self.map.Control = r
    
    def CMLEnable(self, out_id, en):
        C_EVR_CMLCTRL_RESET = 2
        C_EVR_CMLCTRL_POWERDOWN = 1
        C_EVR_CMLCTRL_ENABLE = 0
        
        cml = self.map.CML[out_id]
        ctrl = cml.Control
        
        if en:
            ctrl &= ~((1 << C_EVR_CMLCTRL_RESET) | (1 << C_EVR_CMLCTRL_POWERDOWN))
            ctrl |= (1 << C_EVR_CMLCTRL_ENABLE)
        else:
            ctrl |= (1 << C_EVR_CMLCTRL_RESET) | (1 << C_EVR_CMLCTRL_POWERDOWN)
            ctrl &= ~(1 << C_EVR_CMLCTRL_ENABLE)

        cml.Control = ctrl
        return cml.Control
    
    def SetFPOutMap(self, out_id, map):
        self.map.FPOutMap[out_id] = map
    
    def SetFineDelay(self, out_id, delay):
        self.map.FineDelay[out_id] = delay
        
    def SetPulseMap(self, ram, code, trig, set, clear):
        if trig >= 0:
            self.map.MapRam[ram-1][code].PulseTrigger |= (1 << trig)
        if set >= 0:
            self.map.MapRam[ram-1][code].PulseSet |= (1 << trig)
        if clear >= 0:
            self.map.MapRam[ram-1][code].PulseClear |= (1 << trig)
            
    def SetPulseParams(self, pulse, presc, delay, width):
        self.map.Pulse[pulse].Prescaler = presc
        self.map.Pulse[pulse].Delay = delay
        self.map.Pulse[pulse].Width = width
        
    def SetPulseProperties(self, pulse, polarity, map_reset_ena, map_set_ena, map_trigger_ena, enable):
        r = self.map.Pulse[pulse].Control
        def _aux(r, var, pos):
            if var is not None:
                if var:
                    r |= (1 << pos)
                else:
                    r &= ~(1 << pos)
            return r
                
        C_EVR_PULSE_POLARITY = 4
        C_EVR_PULSE_MAP_RESET_ENA = 3
        C_EVR_PULSE_MAP_SET_ENA = 2
        C_EVR_PULSE_MAP_TRIG_ENA = 1
        C_EVR_PULSE_ENA = 0
        r = _aux(r, polarity, C_EVR_PULSE_POLARITY)
        r = _aux(r, map_reset_ena, C_EVR_PULSE_MAP_RESET_ENA)
        r = _aux(r, map_set_ena, C_EVR_PULSE_MAP_SET_ENA)
        r = _aux(r, map_trigger_ena, C_EVR_PULSE_MAP_TRIG_ENA)
        r = _aux(r, enable, C_EVR_PULSE_ENA)
        self.map.Pulse[pulse].Control = r

def new(host, port=2000):
    fout_api = _RealUDPEvr(host, port)
    mapped_evr = evr_map.EVRMap(fout_api, 0)
    py_evr_api = PyEvr(mapped_evr)
    return py_evr_api

