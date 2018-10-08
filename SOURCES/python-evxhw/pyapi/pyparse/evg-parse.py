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

#Configuration
selfthis = "volatile struct MrfEgRegs"
selftype = "evg_EvgObject"
obthis = "self->pEvg"
methodtablename = 'EvgMethods'
no_body = ['EvgEvanGetEvent', 'EvgSendDBuf']
#no_body = ['EvgEvanReadEvents','EvgSeqRamRead','EvgSeqRamWrite']

# import parse
import genc

fndeclarations, methodtable, fnbodies = genc.parseFile("egapi.h", selfthis, selftype, obthis, methodtablename, no_body)

fndeclarations += 'static PyObject * mod_EvgClose(evg_EvgObject* self);'
methodtable += '{"Close", (PyCFunction)mod_EvgClose, METH_NOARGS, "Closes the device"},'


print fndeclarations
print 'static PyMethodDef '+methodtablename+'[] = {'
print methodtable
print '{NULL, NULL, 0, NULL}  };'
print fnbodies
