#!/usr/bin/env python

#
# This script demonstrates how easy is to manipulate EVR settings.
# It just loads the settings from an XML file (which can be generated
# using the GUI) and exports them to the properties (default on init values)
# of the attributes specifyed in the oDevNames array.
#
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


import IOReceiverTango
import IOReceiverXML
import ReceiverModel

def check_ok(actionName, actionObject):
	if len(actionObject._error):
		print 'WARNING: Not all setting could be ' + actionName + '. ',
		print 'Failed settings related to :'
		for i in actionObject._error: print i + ', ',
		print

		print actionObject._error
		return False
	print 'Settings ' + actionName + ': ' + str(actionObject._ok)
	return True

def run():
  #
  # Configuration
  #
	sel =  ['PULSE', 'RAM', 'UNIVIN', 'UNIVOUT', 'COUNTER' ]
	iFileName = '../timing-gui-2/parameters.xml'
	oDevNames = []

	model = ReceiverModel.MReceiver()

  #
  # Load from one XML file
  #
	importer = IOReceiverXML.MXMLIO()
	importer.load_from_file(iFileName, model, sel)

	if not check_ok('loaded', importer):
		return
	print '---------------------------\n'

  #
  # Store into multiple device properties
  #
	for devName in oDevNames:
		print 'STORING INTO', devName
		# You may write them to the Attributes of the device just by
		# uncommenting next line.
		# aio = IOReceiverTango.TangoAttributesIO(devName)
		aio = IOReceiverTango.TangoPropertiesIO(devName)
		exporter = IOReceiverTango.MTangoIO()
		exporter.save_to_tango(aio, model, sel)
		if not check_ok('saved', exporter):
			print '---------------------------\n'



if __name__ == "__main__":
	run()
