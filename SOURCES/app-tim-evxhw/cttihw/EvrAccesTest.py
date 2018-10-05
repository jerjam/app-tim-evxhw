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

import evrtango
import random
import unittest
import pickle


class tl(unittest.TestCase):
	
	def setUp(self):
# 		self.eva = evrtango.EvrAccesLocal('/dev/evs/r13')
		self.eva = evrtango.EvrAccesTango('timing/EventR/rec1')
		pass
	
	
	def testopsRam(self):
		eva = self.eva
		
		def ramev(trig, set, clear, ledev):
			return {'trigger' : trig, 'set' : set, 'clear' : clear, 'ledEvent' : ledev}
		ram = {}
		
		print eva.TOTAL_EVENT_CODE
		#TODO: xq no tira de 0 a TOTAL,, q he de posar 1?
		for i in range(1, eva.TOTAL_EVENT_CODE):
			ram[i] = ramev(random.randint(0,1023),
					random.randint(0,1023),
					random.randint(0,1023),
					#random.randint(0,1)
					0 #TODO led no prob a tango
					 )
		
		eva.setOpsRam( (ram, True), (ram, False))
		
		re1, re2 = eva.getOpsRam()
		ram0 = re1[0]
		ram1 = re2[0]
		
		self.assertEqual(1,1)
		self.assertTrue(True)
		self.assertEqual(ram0, ram1); print '20'
# 		f = open('/tmp/rsune/ram', 'w')
# 		f.write(str(ram))
# 		pickle.dump(ram, f)
# 		f.close()
# 		
# 		f = open('/tmp/rsune/ram0', 'w')
# 		f.write(str(ram0))
# 		pickle.dump(ram0, f)
# 		f.close()
		self.assertEqual(ram, ram0); print '30'
		ram[3]['trigger'] += 1; print '40'
		self.assertNotEqual(ram0, ram); print '50'
		


if __name__ == '__main__':
	unittest.main()











