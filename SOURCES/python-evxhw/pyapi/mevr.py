#!/usr/bin/python

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


import evr
import evr_map
from mevrconst import *

error = evr.error
FIFOEventStruct = evr.FIFOEventStruct


class PCIEvr(object):
    __slots__ = ['map']

    def __init__(self, real_hw):
        self.map = evr_map.EVRMap(real_hw, 0)

    def __getattr__(self, name):
        return getattr(self.map._parent, name)

    def __dir__(self):
        return dir(self.map._parent)

    def GetVal(self, *args):
        return self.map._parent.GetVal32(*args)

    def SetVal(self, *args):
        return self.map._parent.SetVal32(*args)


def new(dev_name = '/dev/era3'):
    r = PCIEvr(evr.Evr(dev_name))
    return r
