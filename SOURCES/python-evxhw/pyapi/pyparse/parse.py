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


#Receives a param of a C fucntion, and returns a
#structura: (is it a pointer?, type, name)
def breakParam(par):
	pointer = True
	e1 = par.rfind("*");
	if e1 < 0:
		e = par.rfind(" ");
		e1 = e
		pointer = False
	else:
		e = e1-1 
	if e < 0:
		return None
	part = par[:e+1].strip()
	parn = par[e1+1:].strip()
	return [( pointer, part , parn)]

#Receives the code betwen '()' of a C fucntion,
#and returns a list of the correspondant parameters,
#broken in elements of the structure giben by
#breakParam
def breakParams(params):
	b = 0
	ps = []
	while(1): 
		e = params.find(",",b)
		if(e < 0):
			bs = breakParam(params[b:].strip())
			if bs != None:
				ps += bs
			break
		else:
			bs = breakParam(params[b:e].strip())
			if bs != None:
				ps += bs
		b = e+1
	return ps
	

#Receives a line of C code, where we know will be
#a function declaration, and break it into a structure
#with (return type, function name, parameters struct list)
def breakFunction(fn):
	e = fn.find("(");
	if e < 0:
		return None
	b=fn[:e].strip().rfind(" ")
	fname = fn[b:e].strip()
	ftype = fn[:b].strip()
	b = e
	e = fn.find(")")
	if e < 0:
		return None
	fpars = fn[b+1:e].strip()
	ps = breakParams(fpars)
	return (ftype, fname, ps)


#Parses the text deleting the C or C+ comments it finds
def delComments(text):
	b = text.find("/");
	if text[b+1] == "/":
		e = text.find("\n", b)+1
	elif text[b+1] == "*":
		e = text.find("*/", b)+2
	else:
		return text
	return text[:b] + " " + delComments(text[e:])


#Main interface function
# filename = the name of the .h file we will read to parse
# wf = The python function we will call every time we find a C function.
def parseFile(filename, wf):
	frasebegin = "//--OLLUPAC--EXPORTABLE--FUNCTIONS--BEGIN"
	fraseend = "//--OLLUPAC--EXPORTABLE--FUNCTIONS--END"

	f = open(filename, 'r')
	f = f.read()

	b = f.find(frasebegin) + len(frasebegin);
	e = f.find(fraseend);

	f = delComments(f[b:e]).strip()

	b = 0
	while (1) :
		e = f.find(";",b)
		if e < 0:
			break
		o = f[b:e].strip()
		bf = breakFunction(o)
		b = e+1
		wf(bf)










