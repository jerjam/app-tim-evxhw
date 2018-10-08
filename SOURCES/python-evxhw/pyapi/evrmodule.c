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


#include "evrmodule.h"
#include "traducr.c"
#include <unistd.h>
#include <fcntl.h>

void throwError(void * err, const char* mis, const char* funname)
{
	        static char mis2[1024];
		        sprintf(mis2, "%s(%s)", mis, funname);
			        PyErr_SetString(err, mis2);
}

///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
//// evg.FIFOEventStruct()

//evg.FIFOEventStruct() representation
static PyObject* FIFOEventStruct_repr(FIFOEventStructObject *self)
{
	return PyString_FromFormat("FIFOEventStruct<ec(%d) tsh(%d) tsl(%d) rsv(%d)>",
		self->EventCode,
		self->TimestampHigh,
		self->TimestampLow,
		self->reserved);
}

/////////////////////////////////////////
// PYTHON SPECIAL METHODS
// Some of the API functions can't be directly translated into python
// by the script, because they need special cases. The problem are
// pointers, which can be translated into a return value or a input
// with unknown size.

static PyObject * mod_EvrGetFIFOEvent(evr_EvrObject *self)
{
  int status;
  struct FIFOEvent es;
  FIFOEventStructObject *o;
  
  VALIDATE_NOT_CLOSED("EvrGetFIFOEvent") ;

  status = EvrGetFIFOEvent(self->pEvr, &es);
  if (status == 0) {
    o = PyObject_New(FIFOEventStructObject, &FIFOEventStructType);
    o->TimestampLow = es.TimestampLow;
    o->TimestampHigh = es.TimestampHigh;
    o->EventCode = es.EventCode;
    o->reserved = es.reserved;

    return (PyObject*)o;
  }

  Py_INCREF(Py_None);
  return Py_None;
}

static PyObject * mod_EvrSendTxDBuf(evr_EvrObject *self, PyObject *args)
{
	int retval;
	char dbuf[EVR_MAX_BUFFER] = "";
	ssize_t size, n;
	PyObject* ob;
	VALIDATE_NOT_CLOSED("EvrSendTxDBuf") ;
	if (!PyArg_ParseTuple(args, "O", &ob)) return NULL;
	if (!PyList_Check(ob)) return NULL;
	size = PyList_Size(ob);
	/* Check that size is valid */
	if (size & 3 || size > EVR_MAX_BUFFER || size < 4) {
		throwError(EvrException, "Size must be >=4 and =< EVR_MAX_BUFFER and size % 4 == 0", __FUNCTION__);
		return NULL;
	}
	for (n = 0; n < size; ++n) {
		dbuf[n] = PyInt_AsLong(PyList_GET_ITEM(ob, n));
		if ( (dbuf[n] == -1) && PyErr_Occurred() )
			return NULL;
	}
	retval = EvrSendTxDBuf( self->pEvr ,dbuf, size );
	return Py_BuildValue("i",retval);
}

static PyObject * mod_EvrGetDBuf(evr_EvrObject *self, PyObject *args)
{
	int retval;
	char dbuf[EVR_MAX_BUFFER] = "";
	int size;
	int n;
	VALIDATE_NOT_CLOSED("EvrGetDBuf") ;
	if (!PyArg_ParseTuple(args, "i" ,&size)) return NULL;
	retval = EvrGetDBuf( self->pEvr ,dbuf,size);
	if (retval < 0) {
		throwError(EvrException, "Bad return", "EvrGetDBuf");
		return NULL;
	}

	PyObject* ob = PyList_New(size);
	if (!ob) return NULL;
	for(n =0; n < size; ++n) {
		PyList_SET_ITEM(ob, n, PyInt_FromLong((long)dbuf[n]));
	}
	
	return Py_BuildValue("O",ob);
}


////////////////////////////////
// EVR PYTHON OBJECT BASIC METHODS

static PyObject * mod_EvrGetSerialNumber(evr_EvrObject *self)
{
	int r;
	char serial[32];

	if (!self->pEvr) {
		Py_INCREF(Py_None);
		return Py_None;
	}
	
	r = EvrGetSerialNumber(self->fd, serial);
	if (r != 0) {
		snprintf(serial, 32, "Bad return value %d", r);
		throwError(EvrException, "Bad return", "EvrGetSerialNumber");
		return 0;
	}

	return PyString_FromString(serial);
}

static PyObject * mod_EvrIrqHandled(evr_EvrObject *self)
{
	//VALIDATE_NOT_CLOSED("EvrIrqHandled");
	if(self->pEvr)
		EvrIrqHandled(self->fd);

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject * mod_EvrIrqAssignHandler(evr_EvrObject *self)
{
	int fd, oflags;
	VALIDATE_NOT_CLOSED("EvrIrqHandled");

	fd = self->fd;
	fcntl(fd, F_SETOWN, getpid());
	oflags = fcntl(fd, F_GETFL);
	fcntl(fd, F_SETFL, oflags | FASYNC);
	/* Now enable handler */
	EvrIrqHandled(fd);

	Py_INCREF(Py_None);
	return Py_None;
}

//python: evr.Evr().Close()
static PyObject * mod_EvrClose(evr_EvrObject *self)
{
	if(self->pEvr) {
		EvrClose(self->fd);
		self->pEvr = 0;
	}

	Py_INCREF(Py_None);
	return Py_None;
}

//evr.Evr() destructor
static void Evr_dealloc(evr_EvrObject* self)
{
	if(self->pEvr)
		EvrClose(self->fd);
	self->ob_type->tp_free((PyObject*)self);
}

//evr.Evr() representation
static PyObject* Evr_repr(evr_EvrObject *self)
{
	return PyString_FromFormat("<EVR(%d)>", self->fd);
}

//evr.Evr() print
static int Evr_print(evr_EvrObject *self, FILE *fp, int flags)
{
	static char buf[5000]; //TODO: alegria! posar MACRO i la mateixa tb a traduc.c
	//TODO: mes avall tb hi ha '10' i '4', un altre invent!! calen macros!
	size_t tam = 0;
	if(!self->pEvr)
		fprintf(fp, "closed device");
	else if (flags & Py_PRINT_RAW) {
		buf[0] = 0;
		EvrDumpStatus(self->pEvr, buf+tam);
		tam = strlen(buf);
		tam += sprintf(buf+tam, "Ram 0:\n");
		EvrDumpMapRam(self->pEvr, 0, buf+tam);
		tam += sprintf(buf+tam, "Ram 1:\n");
		EvrDumpMapRam(self->pEvr, 1, buf+tam);
		tam = strlen(buf);
		EvrDumpPulses(self->pEvr, 10, buf+tam);
		tam = strlen(buf);
		EvrDumpUnivOutMap(self->pEvr, 4, buf+tam);
		tam = strlen(buf);
		fprintf(fp, buf);
	}
	else {
		fprintf(fp, "<EVR(%d)>", self->fd);
	}
	return 0;
}

//evr.Evr() constructor
//ob = evr.Evr(filename), whith default filename value
static int Evr_init(evr_EvrObject *self, PyObject *args, PyObject *kwds)
{
	volatile struct MrfErRegs * pEvr;
	int fd;
	char * devname = "./mentida.bin";
	
	if (!PyArg_ParseTuple(args, "|s", &devname)){
		return -1;
	}
	
	fd = EvrOpen(&pEvr, devname);
	if(fd < 0)  {
		PyErr_SetString(PyExc_ValueError, "Unable to open device");
		return -1;
	}

// 	 fcntl( fd, F_SETOWN, getpid() );
// 	 fcntl( fd, F_SETFL, fcntl( fd, F_GETFL, 0) | FASYNC );

	self->fd = fd;
	self->pEvr = pEvr;

	return 0;
}


////////////////////////////////
////////////////////////////////
////////////////////////////////
// PYTHON MODULE FUNCTIONS

void init_evr_exceptions(PyObject * m)
{
    PyObject *d;

    d = PyModule_GetDict(m);
    EvrException = PyErr_NewException("evr.error", NULL, NULL);
    PyDict_SetItemString(d, "error", EvrException);
}

//init module, load on 'import evr'
PyMODINIT_FUNC initevr(void)
{
	PyObject* m;
	evr_EvrType.tp_new = PyType_GenericNew;
	if (PyType_Ready(&evr_EvrType) < 0)
		return;

	FIFOEventStructType.tp_new = PyType_GenericNew;

	if (PyType_Ready(&FIFOEventStructType) < 0)
		return;

	m = Py_InitModule3("evr", 0, "MRF Evr Module");

	init_evr_exceptions(m);
//	EvrInit();
	
	Py_INCREF(&FIFOEventStructType);
	PyModule_AddObject(m, "FIFOEventStruct", (PyObject *)&FIFOEventStructType);
	
	Py_INCREF(&evr_EvrType);
	PyModule_AddObject(m, "Evr", (PyObject *)&evr_EvrType);
}



