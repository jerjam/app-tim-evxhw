
# Original File:
#   evan_monitor.c -- Micro-Research Event Generator
#                Application Programming Interface Test Application
#
#   Author: Jukka Pietarinen (MRF)
#   Date:   05.12.2006
#
# Ported to Python:
#   Author: Ramon Sune (CELLS)
#   Date:   2008/03/08


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


import sys
import mevg
import time

EVG_RF_FREQ = 499.654E6
EVG_RF_DIVIDER = 8.0

_default_dev = '/dev/evs/g12'

def main(devfile):
	eg = mevg.new(devfile)

	eg.EvanReset()
	eg.EvanResetCount()
	eg.EvanEnable(True)

	while True:
		event = eg.EvanGetEvent()
		while not event is None:
			print repr(long(event.TimestampLow))
			ts = (long(event.TimestampHigh) << 32) + event.TimestampLow
			sec = ts / (EVG_RF_FREQ/EVG_RF_DIVIDER)
			print (
				"Timestamp %08x%08x, %16.9Lf, event %02x, dbus %02x" %
				(event.TimestampHigh, event.TimestampLow, sec, event.EventCode & 0x00ff, event.EventCode >> 8))
			event = eg.EvanGetEvent()
		time.sleep(1)

	eg.EvanEnable(False)
	eg.Close()

if len(sys.argv) < 2:
	print ("Usage: %s /dev/evs/g12" % sys.argv[0] )
	print "Defaulting to ", _default_dev
else:
	_default_dev = sys.argv[1]

main(_default_dev)
