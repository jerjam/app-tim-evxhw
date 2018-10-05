
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



import mevg, mevr

if False:
  r13 = mevr.new('/dev/evs/r13')
  r14 = mevr.new('/dev/evs/r14')
  g10 = mevg.new('/dev/evs/g10')
  g12 = mevg.new('/dev/evs/g12')


def rdMapItem(dev, event):
  r = dev.GetVal(0x4000 + 16*event)
  print bin(r)
  return r


def wtMapItem(dev, event, val):
  dev.SetVal(0x4000 + 16*event, val)

def buscaSub(ob, txt):
  for el in filter(lambda(x): txt in x,  dir(ob)):
    print el

def bin(num, hexa = False):
  rbinsep = ''
  rhexsep = ''
  rhex = ''
  rbin = ''
  vx = 0;
  for i in range(0, 32):
    if num & (1 << i):
      rbinsep = "1" + rbinsep
      rbin = '1' + rbin
      vx |= 1 << (i % 4)
    else:
      rbinsep = "0" + rbinsep
      rbin = '0' + rbin
    if (i+1) % 4 == 0:
      rbinsep = " " + rbinsep
      rhexsep = "    " + ("%x" % vx) + rhexsep
      rhex = ("%x" % vx) + rhex
      vx = 0
  print "  " + rbinsep
  print "0x" + rhexsep
  print '0x' + rhex
  if hexa:
	  return '0x' + rhex
  #return rbin

def printRegisterMap(dev):
	r = ''
	p = 0
	for y in range (8):
		r += ("%02x" % y) + ': '
		for x in range(4):
			aux = bin(dev.GetVal(p), True)[2:]
			if len(aux) < 2:
				aux = '0' + aux
			r += aux
			p += 4
			r += ' '
		r += '\n'
	print r



