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


#ifndef __EVR_MODULE___H____
#define __EVR_MODULE___H____

//Python includes
#include <Python.h>
#include <structmember.h>

//EVR includes
#include "erapi.h"

//MACROs
void throwError(void * err, const char* mis, const char* funname);
#define RAISE_ERROR_SEL(err, s, funname,  mis) { throwError (err, mis, funname); return NULL; }

#define RAISE_ERROR(s,funname) RAISE_ERROR_SEL(EvrException, s, funname, evr_get_errmsg(s))

#define COND_RAISE_ERROR(s, funname) { if(s!=0) RAISE_ERROR(s, funname) }
#define VALIDATE_NOT_CLOSED(funname) if(!self->pEvr) RAISE_ERROR_SEL(PyExc_ValueError, 0,funname, "I/O operation on a closed device!");

static PyMethodDef EvrMethods[];
static PyObject *EvrException;

///////////////////////////////////////
// PYTHON OBJECTS
///////////////////////////////////////

//python: evr.Evr() object
typedef struct {
	PyObject_HEAD;
	int fd;
	struct MrfErRegs *pEvr;
} evr_EvrObject;

static void Evr_dealloc(evr_EvrObject* self);
static int Evr_init(evr_EvrObject *self, PyObject *args, PyObject *kwds);
static PyObject* Evr_repr(evr_EvrObject *self);
static int Evr_print(evr_EvrObject *self, FILE *fp, int flags);

static PyMemberDef evr_object_members[] = {
  {"__fd__", T_INT, offsetof(evr_EvrObject, fd), READONLY, "File descriptor"},
  {NULL}
};

//python: evr.Evr() type
static PyTypeObject evr_EvrType = {
	PyObject_HEAD_INIT(NULL)
	.tp_name = "evr.Evr",
	.tp_init = (initproc)Evr_init,
	.tp_dealloc = (destructor)Evr_dealloc,
	.tp_basicsize = sizeof(evr_EvrObject),
	.tp_flags = Py_TPFLAGS_DEFAULT /*| Py_TPFLAGS_BASETYPE*/,
	.tp_doc = "Evr objects",
	.tp_repr = (reprfunc)Evr_repr,
	.tp_print = (printfunc)Evr_print,

  .tp_members = evr_object_members,
	.tp_methods = EvrMethods
};

///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
//// evr.FIFOEventStruct

typedef struct {
	PyObject_HEAD;
	unsigned int TimestampHigh;
	unsigned int TimestampLow;
	unsigned int EventCode;
	unsigned int reserved;
}FIFOEventStructObject;

static PyMemberDef FIFOEventStruct_members[] = {
	{"TimestampHigh", T_UINT, offsetof(FIFOEventStructObject, TimestampHigh), 0, "TimestampHigh of FIFOEventStruct"},
	{"TimestampLow", T_UINT, offsetof(FIFOEventStructObject, TimestampLow), 0, "TimestampLow of FIFOEventStruct"},
	{"EventCode", T_UINT, offsetof(FIFOEventStructObject, EventCode), 0, "EventCode of FIFOEventStruct"},
	{"reserved", T_UINT, offsetof(FIFOEventStructObject, reserved), 0, "reserved"},
};

static PyObject* FIFOEventStruct_repr(FIFOEventStructObject *self);

static PyTypeObject FIFOEventStructType = {
	PyObject_HEAD_INIT(NULL)
	.tp_name = "evr.FIFOEventStruct",
	.tp_basicsize = sizeof(FIFOEventStructObject),
	.tp_flags = Py_TPFLAGS_DEFAULT /*| Py_TPFLAGS_BASETYPE*/,
	.tp_doc = "FIFOEventStruct objects",
	.tp_repr = (reprfunc)FIFOEventStruct_repr,
	.tp_members = FIFOEventStruct_members
};

///////////////////////////////////////////
// IMPORTED FROM LIBEVR FUNCTIONS
//int EvrInit();
//int EvrOpen(struct MrfErRegs **pEvr, char *dev);
//int EvrClose(struct MrfErRegs *pEvr, int fd);

#endif //__EVR_MODULE___H____

