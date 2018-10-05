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


import mevgconst


evgAccessFactoryDict = {}

class EvgAccess:

	TOTAL_INPUT_PORTS = 10
	TOTAL_DBUS_BITS = mevgconst.DBUS_BITS
	TOTAL_TRIGGERS = mevgconst.TRIGGERS
	TOTAL_MXCS = mevgconst.MXCS

	SEQTRIG_MXC_BASE = mevgconst.SEQTRIG_MXC_BASE
	SEQTRIG_ACINPUT = mevgconst.SEQTRIG_ACINPUT
	SEQTRIG_SWTRIGGER1 = mevgconst.SEQTRIG_SWTRIGGER1
	SEQTRIG_SWTRIGGER2 = mevgconst.SEQTRIG_SWTRIGGER2

	SEQ1 = mevgconst.SEQ1
	SEQ2 = mevgconst.SEQ2

	DBUS_SEL_OFF = mevgconst.DBUS_SEL_OFF

	MAX_SEQRAMEV = mevgconst.MAX_SEQRAMEV

	MAX_MXCS = mevgconst.MAX_MXCS

	def deviceName(self):
		pass
	
	def deviceString(self):
		pass

	def canSetDefault(self):
		return False










