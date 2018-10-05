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



from extra import _ExtraStruct, _ExtraArray
from mevrconst import *

class _PulseStruct(_ExtraStruct):
  ORIGIN = 0x0200
  TOTAL_BYTES = 16
  FIELDS = {
    # 'name' : (bytes_offset, bytes_width, [dims])
    'Control': (0, 4, []),
    'Prescaler': (4, 4, []),
    'Delay': (8, 4, []),
    'Width': (12, 4, []),
  }
  __slots__ = [x for x in FIELDS]

class _CMLStruct(_ExtraStruct):
  ORIGIN = 0x0600
  TOTAL_BYTES = 32
  FIELDS = {
    # 'name' : (bytes_offset, bytes_width, [dims])
    'Pattern00': (0, 4, []),
    'Pattern01': (4, 4, []),
    'Pattern10': (8, 4, []),
    'Pattern11': (12, 4, []),
    'TrigPos': (16, 2, []),
    'Control': (18, 2, []),
    'HighPeriod': (20, 2, []),
    'LowPeriod': (22, 2, []),
    'SamplePos': (24, 4, []),
    'Reserved': (28, 4, []),
  }
  __slots__ = [x for x in FIELDS]

class _MapRamItemStruct(_ExtraStruct):
  ORIGIN = 0x4000
  TOTAL_BYTES = 16
  FIELDS = {
    # 'name' : (bytes_offset, bytes_width, [dims])
    'IntEvent': (0, 4, []),
    'PulseTrigger': (4, 4, []),
    'PulseSet': (8, 4, []),
    'PulseClear': (12, 4, []),
  }
  __slots__ = [x for x in FIELDS]

class _FIFOEvent(_ExtraStruct):
  ORIGIN = 0x2000
  TOTAL_BYTES = 16
  FIELDS = {
    # 'name' : (bytes_offset, bytes_width, [dims])
    'TimestampHigh': (0, 4, []),
    'TimestampLow': (4, 4, []),
    'Eventcode': (8, 4, []),
    'Reserved': (12, 4, []),
  }
  __slots__ = [x for x in FIELDS]


        
class EVRMap(_ExtraStruct):
    ORIGIN = 0x0
    TOTAL_BYTES = 0x01ff
    FIELDS = {
        # 'name' : (bytes_offset, bytes_width, [dims])
        'Status'            : (0x0000, 4, []),
        'Control'           : (0x0004, 4, []),
        'IrqFlag'           : (0x0008, 4, []),
        'IrqEnable'         : (0x000C, 4, []),
        'PulseIrqMap'       : (0x0010, 4, []),
        'Resv0x0014'        : (0x0014, 4, []),
        'Resv0x0018'        : (0x0018, 4, []),
        'Resv0x001c'        : (0x001c, 4, []),
        'DataBufControl'    : (0x0020, 4, []),
        'TxDataBufControl'  : (0x0024, 4, []),
        'Resv0x0028'        : (0x0028, 4, []),
        'FPGAVersion'       : (0x002c, 4, []),
        'Resv0x0030'        : (0x0030, 4, [(0x040-0x030)/4]),
        'EvCntPresc'        : (0x0040, 4, []),
        'EvCntControl'      : (0x0044, 4, []),
        'Resv0x0048'        : (0x0048, 4, []),
        'UsecDiv'           : (0x004c, 4, []),
        'ClockControl'      : (0x0050, 4, []),
        'Resv0x0054'        : (0x0054, 4, [(0x05C-0x054)/4]),
        'SecondsShift'      : (0x005c, 4, []),
        'SecondsCounter'    : (0x0060, 4, []),
        'TimestampEventCounter': (0x0064, 4, []),
        'SecondsLatch'      : (0x0068, 4, []),
        'TimestampLatch'    : (0x006c, 4, []),
        'FIFOSeconds'       : (0x0070, 4, []),
        'FIFOTimestamp'     : (0x0074, 4, []),
        'FIFOEvent'         : (0x0078, 4, []),
        'LogStatus'         : (0x007c, 4, []),
        'FracDiv'           : (0x0080, 4, []),
        'Resv0x0084'        : (0x0084, 4, []),
        'RxInitPS'          : (0x0088, 4, []),
        'Resv0x008C'        : (0x008c, 4, []),
        'GPIODir'           : (0x0090, 4, []),
        'GPIOIn'            : (0x0094, 4, []),
        'GPIOOut'           : (0x0098, 4, []),
        'Resv0x009C'        : (0x009c, 4, []),
        'Resv0x00A0to0x00FC': (0x00a0, 4, [(0x100-0x0A0)/4]),
        'Prescaler'         : (0x0100, 4, [MAX_PRESCALERS]),
        #'Pulse'
        'FPOutMap'          : (0x0400, 2, [MAX_FPOUT_MAP]),
        'UnivOutMap'        : (0x0440, 2, [MAX_UNIVOUT_MAP]),
        'TBOutMap'          : (0x0480, 2, [MAX_TBOUT_MAP]),
        'FPInMap'           : (0x0500, 4, [MAX_FPIN_MAP]),
        'UnivInMap'         : (0x0540, 4, [MAX_UNIVIN_MAP]),
        'FineDelay'         : (0x0580, 4, [MAX_CML_OUTPUTS]),
        'Resv0x05A0'        : (0x05a0, 4, [MAX_FPOUT_MAP]),
        #'CML'          : (0x0400, 2, [MAX_FPOUT_MAP]),
        'Resv0x0700'        : (0x0700, 4, [(0x800-0x700)/4]),
        'Databuf'           : (0x0800, 4, [MAX_BUFFER/4]),
        'DiagIn'            : (0x1000, 4, []),
        'DiagCE'            : (0x1004, 4, []),
        'DiagReset'         : (0x1008, 4, []),
        'Resv0x100C'        : (0x100c, 4, [(0x1080-0x100C)/4]),
        'DiagCounter'       : (0x1080, 4, [DIAG_MAX_COUNTERS]),
        'Resv0x1100'        : (0x1100, 4, [(0x1800-0x1100)/4]),
        'TxDatabuf'         : (0x1800, 4, [MAX_BUFFER/4]),
        #'Log'               : (0x2000, 4, []),
        #'MapRam'            : (0x4000, 4, []),
        'Resv0x6000'        : (0x1000, 4, [(0x08000-0x06000)/4]),
        'ConfigROM'         : (0x1004, 4, [64]),
        'ScratchRAM'        : (0x1008, 4, [64]),
        'SFPEEPROM'         : (0x1000, 1, [256]), #@todo 1 byt length unsupported!
        'SFPDiag'           : (0x1004, 1, [256]), #@todo 1 byt length unsupported!
        'Resv0x8400'        : (0x1008, 4, [(0x10000-0x08400)/4]),
        'Resv0x10000'       : (0x1000, 4, [(0x20000-0x10000)/4]),
        'CMLPattern'        : (0x1004, 4, [MAX_CML_OUTPUTS*4096]), # @todo Single array, should be array of arrays    
    }
    __slots__ = [x for x in FIELDS]
    
    
    def _getStruct(self, struct_class, origin, total):
        return [
            struct_class(
                self._parent,
                self.ORIGIN + origin + num*struct_class.TOTAL_BYTES)
            for num in xrange(total) ]
    
    def __init__(self, *args):
        _ExtraStruct.__init__(self, *args)
        object.__setattr__(self, 'Pulse', self._getStruct(_PulseStruct, _PulseStruct.ORIGIN, MAX_PULSES))
        object.__setattr__(self, 'CML', self._getStruct(_CMLStruct, _CMLStruct.ORIGIN, MAX_CML_OUTPUTS))
        object.__setattr__(self, 'MapRam', [self._getStruct(_MapRamItemStruct,0x4000, MAX_EVENT_CODE+1), self._getStruct(_MapRamItemStruct,0x5000, MAX_EVENT_CODE+1)])
        object.__setattr__(self, 'Log', self._getStruct(_FIFOEvent, _FIFOEvent.ORIGIN, LOG_SIZE))
