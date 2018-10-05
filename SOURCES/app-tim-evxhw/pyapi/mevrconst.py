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



MAX_FPOUT_MAP    =  32
MAX_UNIVOUT_MAP  =  32
MAX_TBOUT_MAP    =  64
MAX_FPIN_MAP     =  16
MAX_UNIVIN_MAP   =  16
MAX_TBIN_MAP     =  64
MAX_BUFFER       =  2048
MAPRAMS          =  2
MAX_PRESCALERS   =  64
MAX_PULSES       =  32
MAX_CML_OUTPUTS  =  8
MAX_EVENT_CODE   =  255

DIAG_MAX_COUNTERS = 32
LOG_SIZE = 512

#Real: @todo add to Evr based on the form factor
TOTAL_EVENT_CODE = MAX_EVENT_CODE
TOTAL_PULSES = 10
#Real: @todo JJ to implement a fine delay for UNIV 8,9,10,11
#EVR max outputs are 12
TOTAL_OUTPUT_PORTS = 12
TOTAL_PRESCALERS = 3





#/* -- Interrupt Flag/Enable Register bit mappings */
C_IRQ_MASTER_ENABLE    =  31
C_IRQFLAG_DATABUF      =  5
C_IRQFLAG_PULSE        =  4
C_IRQFLAG_EVENT        =  3
C_IRQFLAG_HEARTBEAT    =  2
C_IRQFLAG_FIFOFULL     =  1
C_IRQFLAG_VIOLATION    =  0
IRQ_MASTER_ENABLE      = (-1 << C_IRQ_MASTER_ENABLE)
IRQFLAG_DATABUF        = (1 << C_IRQFLAG_DATABUF)
IRQFLAG_PULSE          = (1 << C_IRQFLAG_PULSE)
IRQFLAG_EVENT          = (1 << C_IRQFLAG_EVENT)
IRQFLAG_HEARTBEAT      = (1 << C_IRQFLAG_HEARTBEAT)
IRQFLAG_FIFOFULL       = (1 << C_IRQFLAG_FIFOFULL)
IRQFLAG_VIOLATION      = (1 << C_IRQFLAG_VIOLATION)



SIGNAL_MAP_BITS   =    6
SIGNAL_MAP_PULSE  =    0
SIGNAL_MAP_DBUS   =    32
SIGNAL_MAP_PRESC  =    40
SIGNAL_MAP_HIGH   =    62
SIGNAL_MAP_LOW    =    63



#/* -- Clock Control Register bit mapppings */
CLKCTRL_RECDCM_RUN     =  15
CLKCTRL_RECDCM_INITD   =  14
CLKCTRL_RECDCM_PSDONE  =  13
CLKCTRL_EVDCM_STOPPED  =  12
CLKCTRL_EVDCM_LOCKED   =  11
CLKCTRL_EVDCM_PSDONE   =  10
CLKCTRL_CGLOCK         =  9
CLKCTRL_RECDCM_PSDEC   =  8
CLKCTRL_RECDCM_PSINC   =  7
CLKCTRL_RECDCM_RESET   =  6
CLKCTRL_EVDCM_PSDEC    =  5
CLKCTRL_EVDCM_PSINC    =  4
CLKCTRL_EVDCM_SRUN     =  3
CLKCTRL_EVDCM_SRES     =  2
CLKCTRL_EVDCM_RES      =  1
CLKCTRL_USE_RXRECCLK   =  0




