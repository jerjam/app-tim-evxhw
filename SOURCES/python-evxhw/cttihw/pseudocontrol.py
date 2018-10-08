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


import xml.dom.minidom
from xml.dom.minidom import Node




#Described in ./doc/README-pyui.TXT
#All the pseudoControls derive from here
#They must implement getFromDev, getFromForm, set2Dev and set2Form and have a controlName string variable
#The get* fucntions should return the same. They should return a (list) of values, even if there is only one to
#return.
#This way, PseudoControl can provide an interface which allows:
# restore() to sycronize the Control contents with the real device ones
# applyConf() to set up the device as specifyed by the form interface
# io() Saving the device contents to a file or loading from a file to the form
class PseudoControl:
	def restore(self):
		r = self.getFromDev()
		apply(self.set2Form, r)
	def applyConf(self):
		r = self.getFromForm()
		apply(self.set2Dev, r)

# 	def ioXML(self, doc, par, saving):
# 		#http://www.oreilly.com/catalog/pythonxml/chapter/ch01.html
# 		if saving:
# 			#f.func_code.co_argcount
# 			#f.func_code.co_names
# 			pars = self.getFromDev()
# 			r = {}
# 			el = doc.createElement('control')
# 			el.setAttribute('name', self.controlName)
# 			for i in range(1, self.set2Dev.func_code.co_argcount):
# 				nom = self.set2Dev.func_code.co_varnames[i]
# 				val = pars[i-1]
# 				elf = doc.createElement('field')
# 				elf.setAttribute('name', nom)
# 				#TODO: No gestiono be tuples ni dictionaris, i dins de llistes nom'es llistes, lo anterior tp!
# 				print type(val)
# 				if type(val) not in (dict, tuple, list):
# 					elf.setAttribute('value', str(val))
# 				if type(val) is list:
# 					for i in range(len(val)):
# 						elf2 = doc.createElement('value')
# 						elf2.setAttribute('id', str(i))
# 						elf2.setAttribute('val', str(val[i]))
# 						elf.appendChild(elf2)
# 				elif type(val) is dict:
# 					for k, v in val.iteritems():
# 						if type(v) is dict:
# 							elf2 = doc.createElement('value')
# 							elf2.setAttribute('id', str(k))
# 							elf.appendChild(elf2)
# 							for k2, v2 in v.iteritems():
# 								elf3 = doc.createElement('value')
# 								elf3.setAttribute('id', str(k2))
# 								elf3.setAttribute('val', str(v2))
# 								elf2.appendChild(elf3)
# 						else:
# 							print 'CACA'
# 
# 				el.appendChild(elf)
# 				print self.controlName + '.' + nom + ' =', val
# 				r[nom] = val
# 			#print doc.toxml()
# 			par.appendChild(el)
# # 			print r
# 			#TODO: aprofitar aixo daqui dalt per fer fitxers amb mes sentit, ja que tinc els noms de les coses que guardo i tot i tal
# # 			dict[self.controlName] = pars
# 		else:
# 			#TODO: llegir no en sap pas!
# 			pars = dict[self.controlName]
# 			apply(self.set2Form, pars)
#TODO: aprofitar aixo daqui dalt per fer fitxers amb mes sentit, ja que tinc els noms de les coses que guardo i tot i tal


	def io(self, dict, saving):
		""" Input/Output Method. Reads the pseudo-control settings into a dictionary or vice-versa.

		Parameters:
		  - dict: The dictionary where to store or read. The relevant contents are on dict[self.controlName]
		  - saving: If True we are saving the pseudo-control contents into the dict, so it is written. Else the settings from the dictionary flow to the pseudo-control.
		  """
		if saving:
			pars = self.getFromDev()
			r = {}
			for i in range(1, self.set2Dev.func_code.co_argcount):
				nom = self.set2Dev.func_code.co_varnames[i]
				val = pars[i-1]
				print self.controlName + '.' + nom + ' =', val
				r[nom] = val
			
			dict[self.controlName] = pars
		else:
			pars = dict[self.controlName]
			apply(self.set2Form, pars)



