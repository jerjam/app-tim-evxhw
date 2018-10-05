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

# fac: a dictionary with the following parameters for each entry:
#         fac['option'] = [Class, (type1, 'par1'), (type2, 'par2'),...]
#     where option is the text that should appear in the args if
#     we want the factory to create an oject of this Class. Per par*
#     are the name of the parameters that will be passed to the
#     constructor, and type* its type. 'option' must be written lowercase.
def OpenDevice(fact, args = None):
	def usageMessage():
		r = 'Possible lists of parameters (in each list, some of the last may be optional):'
		for k, v in fact.iteritems():
			if k[0] is '_': #Hide '_' internal classes
				continue
			s = '\n\t' + k + ' '
			for i in range(1, len(v)):
				s += v[i][1]
			r += s
		return r
	try:
		#If not args are parsed, take them from the program call
		if args == None:
			args = sys.argv[1:]

		#if empty list arg, try to use _default
		if len(args) == 0:
			op = '_default'
		else:
			op = args[0].lower()

		#Get values comparing fact with the arguments parsed
		if op in fact:
			constructor = fact[op]
			params = args[1:]
		elif '_default' in fact:
			constructor = fact['_default']
			params = args
		else:
			print  usageMessage()
			raise 'Invalid parameters. Ensure the correct module is loaded'

		#Try to convert the params passed to the right type for each one, as defined in the fac dict
		for i in range(len(params)):
			params[i] = constructor[1+i][0](params[i])

		#Build the choosen type of object, with the provided
		#arguments to the constructor
		return apply(constructor[0], params)
	except:
		print usageMessage()
		raise


def checkSameInterface(orig, dest):
	for i in dir(orig):
		if i[0] != '_' and i not in dir(dest):
			print 'UNDEFINED: ', i
		#elif i[:3] == 'set':
		else: #TODO should be elif ismethod()
			fn = eval('orig.'+i)
			parsa =  fn.func_code.co_varnames[:fn.func_code.co_argcount]
			fnb = eval('dest.'+i)
			parsb =  fnb.func_code.co_varnames[:fnb.func_code.co_argcount]
			if parsa != parsb:
				print 'PARAMETER MISMATCH: '+i+str(parsa)+' '+str(parsb)

# checkSameInterface(EvrAccessLocal, EvrAccessTango)
# checkSameInterface(EvrAccessLocal, EvrAccessTangoConfig)

