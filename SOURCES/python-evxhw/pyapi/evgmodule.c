/*
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


#include "evgmodule.h"
#include "traducg.c"

void throwError(void * err, const char* mis, const char* funname)
{
	        static char mis2[1024];
		        sprintf(mis2, "%s(%s)", mis, funname);
			        PyErr_SetString(err, mis2);
}


static PyObject * mod_EvgSendDBuf(evg_EvgObject *self, PyObject *args)
{
	int retval;
	char dbuf[EVG_MAX_BUFFER] = "";
	ssize_t size, n;
	PyObject* ob;
	VALIDATE_NOT_CLOSED("EvgSendDBuf") ;
	if (!PyArg_ParseTuple(args, "O", &ob)) return NULL;
	if (!PyList_Check(ob)) return NULL;
	size = PyList_Size(ob);
	/* Check that size is valid */
	if (size & 3 || size > EVG_MAX_BUFFER || size < 4) {
		throwError(EvgException, "Size must be >=4 and =< EVG_MAX_BUFFER and size % 4 == 0", __FUNCTION__);
		return NULL;
	}
	for (n = 0; n < size; ++n) {
		dbuf[n] = PyInt_AsLong(PyList_GET_ITEM(ob, n));
		if ( (dbuf[n] == -1) && PyErr_Occurred() )
			return NULL;
	}
	retval = EvgSendDBuf( self->pEvg, dbuf, size );
	return Py_BuildValue("i",retval);
}

/////////////////////////////////////////
// PYTHON SPECIAL METHODS
// Some of the API functions can't be directly translated into python
// by the script, because they need special cases. The problem are
// pointers, which can be translated into a return value or a input
// with unknown size.

static PyObject * mod_EvgEvanGetEvent(evg_EvgObject *self)
{
  int status;
  struct EvanStruct es;
  EvanStructObject *o;
  
  VALIDATE_NOT_CLOSED("EvgEvanGetEvent") ;

  status = EvgEvanGetEvent(self->pEvg, &es);
  if (status == 0) {
    o = PyObject_New(EvanStructObject, &EvanStructType);
    o->TimestampLow = es.TimestampLow;
    o->TimestampHigh = es.TimestampHigh;
    o->EventCode = es.EventCode;

    return (PyObject*)o;
  }
//  RAISE_ERROR(status, "EvgEvanGetEvent");
  Py_INCREF(Py_None);
  return Py_None;
}

///////////////////////////////////////
// PYTHON OBJECTS
///////////////////////////////////////

///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
//// evg.Evg()

//python: evg.Evg().Close()
static PyObject * mod_EvgClose(evg_EvgObject *self)
{
	if(self->pEvg) {
		EvgClose(self->fd);
		self->pEvg = 0;
	}
	Py_INCREF(Py_None);
	return Py_None;
}

//evg.Evg() destructor
static void Evg_dealloc(evg_EvgObject* self)
{
	if(self->pEvg)
		EvgClose( self->fd);
	self->ob_type->tp_free((PyObject*)self);
}

//evg.Evg() representation
static PyObject* Evg_repr(evg_EvgObject *self)
{
	return PyString_FromFormat("<EVG(%d)>", self->fd);
}

//evg.Evg() print
static int Evg_print(evg_EvgObject *self, FILE *fp, int flags)
{
//	char buf[6000]; //TODO: alegria! posar MACRO i la mateixa tb a traduc.c
//	if(!self->pEvr)
//		fprintf(fp, "closed device");
//	else if (flags & Py_PRINT_RAW) {
//		buf[0] = 0;
//		EvrDump(self->pEvr, buf);
//		fprintf(fp, buf);
//	}
//	else {
		fprintf(fp, "<EVG(%d)>", self->fd);
//	}
	return 0;
}

//evg.Evg() constructor
static int Evg_init(evg_EvgObject *self, PyObject *args, PyObject *kwds)
{
	volatile struct MrfEgRegs * pEvg;
	int fd;
	char * devname = "./mentida.bin";

	if (!PyArg_ParseTuple(args, "|s", &devname)){
		return -1;
	}

	fd = EvgOpen(&pEvg, devname);
	
	if(fd < 0)  {
		PyErr_SetString(PyExc_ValueError, "Unable to open device");
		return -1;
	}
	
	self->fd = fd;
	self->pEvg = pEvg;

	return 0;
}


///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
//// evg.EvanStruct()

//evg.EvanStruct() representation
static PyObject* EvanStruct_repr(EvanStructObject *self)
{
	return PyString_FromFormat("<ec(%d) tsh(%d) tsl(%d)>", 
		self->EventCode,
		self->TimestampHigh,
		self->TimestampLow);
}

///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
//// evg.SeqStruct()

//evg.SeqStruct() representation
static PyObject* SeqStruct_repr(SeqStructObject *self)
{
	return PyString_FromFormat("<ec(%d) ts(%d)>", 
		self->EventCode,
		self->Timestamp);
}



///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
//// MODULE FUNCTIONS


void init_evg_exceptions(PyObject * m)
{
    PyObject *d;

    d = PyModule_GetDict(m);
    EvgException = PyErr_NewException("evg.error", NULL, NULL);
    PyDict_SetItemString(d, "error", EvgException);
}

//initialization on import evg
PyMODINIT_FUNC initevg(void)
{
	PyObject* m;
	evg_EvgType.tp_new = PyType_GenericNew;
	if (PyType_Ready(&evg_EvgType) < 0)
		return;
	
	EvanStructType.tp_new = PyType_GenericNew;
	SeqStructType.tp_new = PyType_GenericNew;

	if ((PyType_Ready(&EvanStructType) < 0) || (PyType_Ready(&SeqStructType) < 0) )
		return;

	m = Py_InitModule3("evg", 0, "MRF Evg Module");

	init_evg_exceptions(m);	

	Py_INCREF(&evg_EvgType);
	PyModule_AddObject(m, "Evg", (PyObject *)&evg_EvgType);

	Py_INCREF(&EvanStructType);
	PyModule_AddObject(m, "EvanStruct", (PyObject *)&EvanStructType);

	Py_INCREF(&SeqStructType);
	PyModule_AddObject(m, "SeqStruct", (PyObject *)&SeqStructType);
}



