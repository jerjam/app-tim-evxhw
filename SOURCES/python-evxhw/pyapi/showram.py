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

def hexa(num):
  r1 = ""
  r2 = ""
  vx = 0;
  for i in range(0, 32):
    if num & (1 << i):
      r1 = "1" + r1
      vx |= 1 << (i % 4)
    else:
      r1 = "0" + r1
    if (i+1) % 4 == 0:
      r1 = " " + r1
      r2 = ("%x" % vx) + r2
      vx = 0
  return '0x' + r2

def showRam(dev):
	r = ''
	p = 0
	for z in range (8):
		r += str(z) + '0: '
		for y in range(4):
			#for x in range(4):
				aux = hexa(dev.GetVal(p))[2:]
				if len(aux) < 2:
					aux = '0' + aux
				r += aux
				p += 4
				r += ' '
		r += '\n'
	print r
	


