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

#import sys
#sys.path.insert(0, '../../pyapi/')

import mevrconst


evrAccessFactoryDict = {}



class EvrAccess:
	# The following constants are public, and very likely to
	# be accessed from the caller class (usually a pseudo-control,
	# so it can adapt to different capable devices with no trouble)
	TOTAL_EVENT_CODE = mevrconst.TOTAL_EVENT_CODE
	TOTAL_PULSES = mevrconst.TOTAL_PULSES
	TOTAL_OUTPUT_PORTS = mevrconst.TOTAL_OUTPUT_PORTS
	TOTAL_PRESCALERS = mevrconst.TOTAL_PRESCALERS

	SIGNAL_MAP_PULSE = mevrconst.SIGNAL_MAP_PULSE
	SIGNAL_MAP_DBUS = mevrconst.SIGNAL_MAP_DBUS
	SIGNAL_MAP_PRESC = mevrconst.SIGNAL_MAP_PRESC
	
	def deviceName(self):
		pass
	
	def deviceString(self):
		pass

	def clearViolation(self):
		pass

	def canSetDefault(self):
		return False



