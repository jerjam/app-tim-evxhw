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



SEQ1 = 0
SEQ2 = 1


SEQRAMS       =  2
MXCS          =  8
UNIVINS       =  10
TRIGGERS      =  8


MAX_FPOUT_MAP          =  32
MAX_UNIVOUT_MAP        =  32
MAX_TBOUT_MAP          =  64
MAX_FPIN_MAP           =  16
MAX_UNIVIN_MAP         =  16
MAX_TBIN_MAP           =  64
MAX_BUFFER             =  2048
MAX_SEQRAMEV           =  2048
MAX_SEQRAMS            =  4
MAX_EVENT_CODE         =  255
MAX_MXCS               =  16
MAX_TRIGGERS           =  16
SEQRAM_CLKSEL_BITS     =  5
SEQRAM_MAX_TRIG_BITS   =  5
DBUS_BITS              =  8

#/* -- Status Register bit mappings */
STATUS_RXDBUS_HIGH   = 31
STATUS_RXDBUS_LOW    = 24
STATUS_TXDBUS_HIGH   = 23
STATUS_TXDBUS_LOW    = 16
#/* -- Control Register bit mappings */
CTRL_MASTER_ENABLE   = 31
CTRL_RX_DISABLE      = 30
CTRL_MXC_RESET       = 24
CTRL_SEQRAM_ALT      = 16
#/* -- Interrupt Flag/Enable Register bit mappings */
IRQ_MASTER_ENABLE = 31
IRQFLAG_DATABUF   = 5
IRQFLAG_RXFIFOFULL= 1
IRQFLAG_VIOLATION = 0
#/* -- SW Event Register bit mappings */
SWEVENT_PENDING   = 9
SWEVENT_ENABLE    = 8
SWEVENT_CODE_HIGH = 7
SWEVENT_CODE_LOW  = 0
#/* -- AC Input Control Register bit mappings */
ACCTRL_BYPASS     = 17
ACCTRL_ACSYNC     = 16
ACCTRL_DIV_HIGH   = 15
ACCTRL_DIV_LOW    = 8
ACCTRL_DELAY_HIGH = 7
ACCTRL_DELAY_LOW  = 0
#/* -- AC Input Mapping Register bit mappings */
ACMAP_TRIG_BASE   =0
#/* -- Databuffer Control Register bit mappings */
DATABUF_COMPLETE  = 20
DATABUF_RUNNING   = 19
DATABUF_TRIGGER   = 18
DATABUF_ENA       = 17
DATABUF_MODE      = 16
DATABUF_SIZEHIGH  = 11
DATABUF_SIZELOW   = 2
#/* -- Clock Control Register bit mapppings */
CLKCTRL_EXTRF        =24
CLKCTRL_DIV_HIGH     =21
CLKCTRL_DIV_LOW      =16
CLKCTRL_RECDCM_RUN   = 15
CLKCTRL_RECDCM_INITD = 14
CLKCTRL_RECDCM_PSDONE= 13
CLKCTRL_EVDCM_STOPPED= 12
CLKCTRL_EVDCM_LOCKED =11
CLKCTRL_EVDCM_PSDONE =10
CLKCTRL_CGLOCK       =9
CLKCTRL_RECDCM_PSDEC =8
CLKCTRL_RECDCM_PSINC =7
CLKCTRL_RECDCM_RESET =6
CLKCTRL_EVDCM_PSDEC  =5
CLKCTRL_EVDCM_PSINC  =4
CLKCTRL_EVDCM_SRUN   =3
CLKCTRL_EVDCM_SRES   =2
CLKCTRL_EVDCM_RES    =1
CLKCTRL_USE_RXRECCLK =0
#/* -- RF Divider Settings */
RFDIV_MASK = 0x003F
RFDIV_1   = 0x00
RFDIV_2   = 0x01
RFDIV_3   = 0x02
RFDIV_4   = 0x03
RFDIV_5   = 0x04
RFDIV_6   = 0x05
RFDIV_7   = 0x06
RFDIV_8   = 0x07
RFDIV_9   = 0x08
RFDIV_10  = 0x09
RFDIV_11  = 0x0A
RFDIV_12  = 0x0B
RFDIV_OFF = 0x0C
RFDIV_14  = 0x0D
RFDIV_15  = 0x0E
RFDIV_16  = 0x0F
RFDIV_17  = 0x10
RFDIV_18  = 0x11
RFDIV_19  = 0x12
RFDIV_20  = 0x13
#/* -- Event Analyser Control Register bit mappings */
EVANCTRL_RESET      = 3
EVANCTRL_NOTEMPTY   = 3
EVANCTRL_CLROVERFLOW= 2
EVANCTRL_OVERFLOW   = 2
EVANCTRL_ENABLE     = 1
EVANCTRL_COUNTRES   = 0
#/* -- Sequence RAM Control Register bit mappings */
SQRC_RUNNING        = 25
SQRC_ENABLED        = 24
SQRC_SWTRIGGER      = 21
SQRC_SINGLE         = 20
SQRC_RECYCLE        = 19
SQRC_RESET          = 18
SQRC_DISABLE        = 17
SQRC_ENABLE         = 16
SQRC_TRIGSEL_LOW    = 0
#/* -- Sequence RAM Triggers */
SEQTRIG_MAX         = 31
SEQTRIG_SWTRIGGER2  = 18
SEQTRIG_SWTRIGGER1  = 17
SEQTRIG_ACINPUT     = 16
SEQTRIG_MXC_BASE    = 0
#/* -- Event Trigger bit mappings */
EVENTTRIG_ENABLE    = 8
EVENTTRIG_CODE_HIGH = 7
EVENTTRIG_CODE_LOW  = 0
#/* -- Input mapping bits */
INMAP_TRIG_BASE     = 0
INMAP_DBUS_BASE     = 16
#/* -- Multiplexed Counter Mapping Bits */
MXC_READ            = 31
MXCMAP_TRIG_BASE    = 0
#/* -- Distributed Bus Mapping Bits */
DBUS_SEL_BITS       = 4
DBUS_SEL_MASK       = 3
DBUS_SEL_OFF        = 0
DBUS_SEL_EXT        = 1
DBUS_SEL_MXC        = 2
DBUS_SEL_FORWARD    = 3











