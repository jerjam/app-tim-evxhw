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


#ifndef __EVG_MODULE___H____
#define __EVG_MODULE___H____

//Python includes
#include <Python.h>
#include <structmember.h>
#include <object.h>

//EVG includes
#include "egcpci.h"
#include "egapi.h"

//MACROs
void throwError(void * err, const char* mis, const char* funname);
#define RAISE_ERROR_SEL(err, s, funname,  mis) { throwError (err, mis, funname); return NULL; }

#define RAISE_ERROR(s,funname) RAISE_ERROR_SEL(EvgException, s, funname, evg_get_errmsg(s))

#define COND_RAISE_ERROR(s, funname) { if(s!=0) RAISE_ERROR(s, funname) }
#define VALIDATE_NOT_CLOSED(funname) if(!self->pEvg) RAISE_ERROR_SEL(PyExc_ValueError, 0,funname, "I/O operation on a closed device!");


static PyMethodDef EvgMethods[];
static PyObject *EvgException;

///////////////////////////////////////
// PYTHON OBJECTS
///////////////////////////////////////

///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
//// evg.Evg()

//python: evg.Evg() Object
typedef struct {
	PyObject_HEAD;
	int fd;
	volatile struct MrfEgRegs *pEvg;
} evg_EvgObject;


static void Evg_dealloc(evg_EvgObject* self);
static int Evg_init(evg_EvgObject *self, PyObject *args, PyObject *kwds);
static PyObject* Evg_repr(evg_EvgObject *self);
static int Evg_print(evg_EvgObject *self, FILE *fp, int flags);


//python: evg.Evg() type
static PyTypeObject evg_EvgType = {
	PyObject_HEAD_INIT(NULL)
	.tp_name = "evg.Evg",
	.tp_init = (initproc)Evg_init,
	.tp_dealloc = (destructor)Evg_dealloc,
// 	.tp_new = Evg_new,
	.tp_basicsize = sizeof(evg_EvgObject),
	.tp_flags = Py_TPFLAGS_DEFAULT /*| Py_TPFLAGS_BASETYPE*/,
	.tp_doc = "Evg objects",
	.tp_repr = (reprfunc)Evg_repr,
	.tp_print = (printfunc)Evg_print,
	.tp_methods = EvgMethods
};


///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
//// evg.EvanStruct()

typedef struct {
	PyObject_HEAD;
	unsigned int TimestampHigh;
	unsigned int TimestampLow;
	unsigned int EventCode;
}EvanStructObject;

static PyMemberDef EvanStruct_members[] = {
	{"TimestampHigh", T_UINT, offsetof(EvanStructObject, TimestampHigh), 0, "TimestampHigh of EvanStruct"},
	{"TimestampLow", T_UINT, offsetof(EvanStructObject, TimestampLow), 0, "TimestampLow of EvanStruct"},
	{"EventCode", T_UINT, offsetof(EvanStructObject, EventCode), 0, "EventCode of EvanStruct"},
	{NULL}
};

static PyObject* EvanStruct_repr(EvanStructObject *self);

static PyTypeObject EvanStructType = {
	PyObject_HEAD_INIT(NULL)
	.tp_name = "evg.EvanStruct",
	.tp_basicsize = sizeof(EvanStructObject),
	.tp_flags = Py_TPFLAGS_DEFAULT /*| Py_TPFLAGS_BASETYPE*/,
	.tp_doc = "EvanStruct objects",
	.tp_repr = (reprfunc)EvanStruct_repr,
	.tp_members = EvanStruct_members
};


///////////////////////////////////////
///////////////////////////////////////
///////////////////////////////////////
/////////////////////////////
//// evg.SeqStruct()


typedef struct {
	PyObject_HEAD;
	unsigned int Timestamp;
	unsigned int EventCode;
}SeqStructObject;


static PyMemberDef SeqStruct_members[] = {
	{"Timestamp", T_UINT, offsetof(SeqStructObject, Timestamp), 0, "Timestamp of SeqStruct"},
	{"EventCode", T_UINT, offsetof(SeqStructObject, EventCode), 0, "Eventcode of SeqStruct"},
	{NULL}
};


static PyObject* SeqStruct_repr(SeqStructObject *self);

static PyTypeObject SeqStructType = {
	PyObject_HEAD_INIT(NULL)
	.tp_name = "evg.SeqStruct",
	.tp_basicsize = sizeof(SeqStructObject),
	.tp_flags = Py_TPFLAGS_DEFAULT /*| Py_TPFLAGS_BASETYPE*/,
	.tp_doc = "SecStruct objects",
	.tp_repr = (reprfunc)SeqStruct_repr,
	.tp_members = SeqStruct_members
};

#endif //__EVG_MODULE___H____

