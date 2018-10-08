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

selfthis = ''
selftype = ''
obthis = ''
methodtablename = ''

methodtable = ''
fnbodies = ''
fndeclarations = ''

validableReturn = 'RESULT'

import parse


def help_doc(name, inp, out, unk):
  r = 'Calls the function ' + name + '\\n'
  if len(unk) > 0:
    r += 'THIS FUNCTION IS BAD DOCUMENTED. Its parameter specification may be wrong. The following ones are not known to be inputs or outputs.\\n'
    for p in unk:
      r += '\\t'+p+'\\n'
  if len(inp) > 0:
    r += 'It receives the following parameters: \\n'
    for p in inp:
      r += '\\t'+p+'\\n'
  else:
    r += 'It receives no input parameteres\\n'
  if len(out) > 0:
    r += 'It returns the following values: \\n'
    for p in out:
      r += '\\t'+p+'\\n'
  return r

#Receives information about ONE parameter of A C fucntion
#as given by parser.py: (is pointer?, type, name)
#Returns: (ncessari C strcuture for holding it, inpyt form pyParse, output for pyParse, name, name in funcall)
def processParam (par, n):
  pt = par[0]
  tp = par[1]
  nomor = par[2]
  #nom = "par" + str(n)
  nom = nomor
  argt = tp
  if pt:
    argt += "*"
  equiv = {
    #init, entradat, sortida, nomBuild/Read, nomFunCall
    'int' : ('int '+nom, 'i', '', '&'+nom, nom),
    'int*' : ('int '+nom, '', 'i', nom, '&'+nom),
    'unsigned int' : ('unsigned int ' + nom, 'I', '', '&'+nom, nom),
    'unsigned int*' :('unsigned int ' + nom, '', 'I', nom, '&'+nom),
    'unsigned short*' : ('unsigned short '+nom, '', 'H', nom, '&'+nom),
    'char*' : ('char '+nom+'[25000] = ""','','z', nom, nom),
    'MrfEvgSeqStruct*' : ('/*//W: Realment no el se tractar ' + argt + '*/', '', '', nom, nom),
    'MrfEvgEvanStruct*' : ('/*//W: Realment no el se tractar ' + argt + '*/', '', '', nom, nom),
    'struct EvanStruct*' : ('/*//W: Realment no el se tractar ' + argt + '*/', '', '', nom, nom),
    '__error__' : False
    }
  if not argt in equiv:
  	return equiv['__error__'];
  e = equiv[argt]
  return e 

def createFunction(fn):
  global methodtable
  global fndeclarations
  global fnbodies

  #Params Validation
  if(fn == None):
    return "//W: Not a Fun"
  rettp = fn[0]
  name = fn[1]
  args = fn[2]
  if len(args) < 1:
    return "//W: missing args", fn
  ergo = args[0]
  if not (ergo[0] and ergo[1] == selfthis):
    return "//W: incorrect 1rst param type", fn
  rettps = [ "int", validableReturn, "void", "unsigned int" ]
  if not rettp in rettps:
    return "//W: incorrect fun type"

  #write function definition
  r = ''
  if rettp != 'void':
  	r += rettp + " retval;\n"

  fcall = name + '( '+obthis+' ,'
  getargs = ''
  infmt = ''
  inargs=','
  outfmt = ''
  outargs = ','

  help_inputs = []
  help_outputs = []
  help_unk = []

  for i in range(1, len(args)):
    p = processParam (args[i], i)
    if p is False:
      fnbodies += '//W: Funcio no tractada "'+name+'", parametres desconeguts' + str(args[i]) + '\n'
      return #aquesta funcio no es tracta xq hi ha parametres desconeguts
    r+= p[0]+';\n' #definicio de variables
    if len(p[1]) > 0: #parametres dentrada
    	infmt += p[1]
	inargs += p[3] + ','
	help_inputs += [p[3]]
    elif len(p[2]) > 0: #parametres de sortida
    	outfmt += p[2]
	outargs += p[3] + ','
	help_outputs += [p[3]]
    else:
	help_unk += [p[3]]
    fcall += p[4] + ','
  r += 'VALIDATE_NOT_CLOSED("'+name+'") ;\n'
  fcall = fcall[:-1] + ");\n"
  if rettp  == 'void':
  	pass
  elif rettp == validableReturn:
	fcall = 'retval = ' + fcall + 'COND_RAISE_ERROR(retval, "'+name+'");\n'
  elif rettp == 'unsigned int':
    help_outputs = ['unsignedval'] + help_outputs;
    outfmt = "I" + outfmt
    outargs = ",retval" + outargs
    fcall = 'retval = ' + fcall
  else:
    help_outputs = ['intval'] + help_outputs;
    outfmt = "i" + outfmt
    outargs = ",retval" + outargs
    fcall = 'retval = ' + fcall

  #r += 'printf("running '+name+'\\n");\n'

  inargs = inargs[:-1]
  outargs = outargs[:-1]

  if len(inargs) > 0:
    r += "if (!PyArg_ParseTuple(args, \""+infmt+"\" "+inargs+")) return NULL;\n"
  r += fcall
  if len(outargs) > 0:
    r += 'return Py_BuildValue(\"' + outfmt + '\"' + outargs + ');\n'
  else:
    r += 'Py_INCREF(Py_None);\nreturn Py_None;\n'
  r += '}\n'
  r += '/////////////////////\n'


  if name in no_body:
    help_unk = ['**unknown**'] + help_inputs + help_outputs + help_unk
    help_inputs = []
    help_outputs = []

  #write method tabe entry
  #write fucntion declaration
  if len(inargs) > 0:
  	mtb = '{"'+name[3:]+'", (PyCFunction)mod_'+name+', METH_VARARGS, "'+help_doc(name, help_inputs, help_outputs, help_unk)+'"},'
	fdec = "static PyObject * mod_" + name + "("+selftype+" *self, PyObject *args)"
  else:
  	mtb = '{"'+name[3:]+'", (PyCFunction)mod_'+name+', METH_NOARGS, "'+help_doc(name, help_inputs, help_outputs, help_unk)+'"},'
	fdec = "static PyObject * mod_" + name + "("+selftype+" *self)"

  r = fdec + "\n{\n" + r

  if not name in no_body:
    fnbodies += r
  methodtable += mtb + '\n'
  fndeclarations += fdec + ';\n'

def parseFile (fname, selthis, seltype, othis, mtname, nbody):
  global selfthis
  global selftype
  global obthis
  global methodtablename
  global methodtable
  global fnbodies
  global fndeclarations
  global no_body
  selfthis = selthis
  selftype = seltype
  obthis = othis
  methodtablename = mtname
  methodtable = ''
  fnbodies = ''
  fndeclarations = ''
  no_body = nbody
  parse.parseFile(fname, createFunction)
  return fndeclarations, methodtable, fnbodies

