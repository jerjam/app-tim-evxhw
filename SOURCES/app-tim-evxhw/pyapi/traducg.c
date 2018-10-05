static PyObject * mod_EvgEnable(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgGetEnable(evg_EvgObject *self);
static PyObject * mod_EvgRxEnable(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgRxGetEnable(evg_EvgObject *self);
static PyObject * mod_EvgGetViolation(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgSWEventEnable(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgGetSWEventEnable(evg_EvgObject *self);
static PyObject * mod_EvgSendSWEvent(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgEvanEnable(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgEvanGetEnable(evg_EvgObject *self);
static PyObject * mod_EvgEvanReset(evg_EvgObject *self);
static PyObject * mod_EvgEvanResetCount(evg_EvgObject *self);
static PyObject * mod_EvgEvanGetEvent(evg_EvgObject *self);
static PyObject * mod_EvgSetMXCPrescaler(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgSetMxcTrigMap(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgSyncMxc(evg_EvgObject *self);
static PyObject * mod_EvgMXCDump(evg_EvgObject *self);
static PyObject * mod_EvgSetDBusMap(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgDBusDump(evg_EvgObject *self);
static PyObject * mod_EvgSetACInput(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgSetACMap(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgACDump(evg_EvgObject *self);
static PyObject * mod_EvgSetRFInput(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgSetFracDiv(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgSetSeqRamEvent(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgSeqRamDump(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgSeqRamControl(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgSeqRamSWTrig(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgSeqRamStatus(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgSetUnivinMap(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgUnivinDump(evg_EvgObject *self);
static PyObject * mod_EvgSetTriggerEvent(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgTriggerEventDump(evg_EvgObject *self);
static PyObject * mod_EvgSetUnivOutMap(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgSetDBufMode(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgGetDBufStatus(evg_EvgObject *self);
static PyObject * mod_EvgSendDBuf(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgSetVal(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgGetVal(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgGetMxcTrigMap(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgResetMxcTrigMap(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgGetMXCPrescaler(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgGetDBusMap(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgGetACInput(evg_EvgObject *self);
static PyObject * mod_EvgGetACMap(evg_EvgObject *self);
static PyObject * mod_EvgResetACMap(evg_EvgObject *self);
static PyObject * mod_EvgGetRFInput(evg_EvgObject *self);
static PyObject * mod_EvgGetInternalFrac(evg_EvgObject *self);
static PyObject * mod_EvgSetInternalFrac(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgDataBufferRead(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgDataBufferWrite(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgGetTriggerEvent(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgSeqRamGetControl(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgGetSeqRamEvent(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgClockIsCGLocked(evg_EvgObject *self);
static PyObject * mod_EvgPCIStatus(evg_EvgObject *self);
static PyObject * mod_EvgGetUnivinMap(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgGetTxDBufModeEnable(evg_EvgObject *self);
static PyObject * mod_EvgSetTxDBufModeEnable(evg_EvgObject *self, PyObject *args);
static PyObject * mod_EvgTester(evg_EvgObject *self);
static PyObject * mod_EvgWriteRegToFile(evg_EvgObject *self);
static PyObject * mod_EvgWriteFileToReg(evg_EvgObject *self);
static PyObject * mod_EvgClose(evg_EvgObject* self);
static PyMethodDef EvgMethods[] = {
{"Enable", (PyCFunction)mod_EvgEnable, METH_VARARGS, "Calls the function EvgEnable\nIt receives the following parameters: \n\t&state\nIt returns the following values: \n\tintval\n"},
{"GetEnable", (PyCFunction)mod_EvgGetEnable, METH_NOARGS, "Calls the function EvgGetEnable\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"RxEnable", (PyCFunction)mod_EvgRxEnable, METH_VARARGS, "Calls the function EvgRxEnable\nIt receives the following parameters: \n\t&state\nIt returns the following values: \n\tintval\n"},
{"RxGetEnable", (PyCFunction)mod_EvgRxGetEnable, METH_NOARGS, "Calls the function EvgRxGetEnable\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"GetViolation", (PyCFunction)mod_EvgGetViolation, METH_VARARGS, "Calls the function EvgGetViolation\nIt receives the following parameters: \n\t&clear\nIt returns the following values: \n\tintval\n"},
{"SWEventEnable", (PyCFunction)mod_EvgSWEventEnable, METH_VARARGS, "Calls the function EvgSWEventEnable\nIt receives the following parameters: \n\t&state\nIt returns the following values: \n\tintval\n"},
{"GetSWEventEnable", (PyCFunction)mod_EvgGetSWEventEnable, METH_NOARGS, "Calls the function EvgGetSWEventEnable\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"SendSWEvent", (PyCFunction)mod_EvgSendSWEvent, METH_VARARGS, "Calls the function EvgSendSWEvent\nIt receives the following parameters: \n\t&code\nIt returns the following values: \n\tintval\n"},
{"EvanEnable", (PyCFunction)mod_EvgEvanEnable, METH_VARARGS, "Calls the function EvgEvanEnable\nIt receives the following parameters: \n\t&state\nIt returns the following values: \n\tintval\n"},
{"EvanGetEnable", (PyCFunction)mod_EvgEvanGetEnable, METH_NOARGS, "Calls the function EvgEvanGetEnable\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"EvanReset", (PyCFunction)mod_EvgEvanReset, METH_NOARGS, "Calls the function EvgEvanReset\nIt receives no input parameteres\n"},
{"EvanResetCount", (PyCFunction)mod_EvgEvanResetCount, METH_NOARGS, "Calls the function EvgEvanResetCount\nIt receives no input parameteres\n"},
{"EvanGetEvent", (PyCFunction)mod_EvgEvanGetEvent, METH_NOARGS, "Calls the function EvgEvanGetEvent\nTHIS FUNCTION IS BAD DOCUMENTED. Its parameter specification may be wrong. The following ones are not known to be inputs or outputs.\n\t**unknown**\n\tintval\n\tevan\nIt receives no input parameteres\n"},
{"SetMXCPrescaler", (PyCFunction)mod_EvgSetMXCPrescaler, METH_VARARGS, "Calls the function EvgSetMXCPrescaler\nIt receives the following parameters: \n\t&mxc\n\t&presc\n"},
{"SetMxcTrigMap", (PyCFunction)mod_EvgSetMxcTrigMap, METH_VARARGS, "Calls the function EvgSetMxcTrigMap\nIt receives the following parameters: \n\t&mxc\n\t&map\n"},
{"SyncMxc", (PyCFunction)mod_EvgSyncMxc, METH_NOARGS, "Calls the function EvgSyncMxc\nIt receives no input parameteres\n"},
{"MXCDump", (PyCFunction)mod_EvgMXCDump, METH_NOARGS, "Calls the function EvgMXCDump\nIt receives no input parameteres\nIt returns the following values: \n\tout\n"},
{"SetDBusMap", (PyCFunction)mod_EvgSetDBusMap, METH_VARARGS, "Calls the function EvgSetDBusMap\nIt receives the following parameters: \n\t&dbus\n\t&map\n"},
{"DBusDump", (PyCFunction)mod_EvgDBusDump, METH_NOARGS, "Calls the function EvgDBusDump\nIt receives no input parameteres\nIt returns the following values: \n\tout\n"},
{"SetACInput", (PyCFunction)mod_EvgSetACInput, METH_VARARGS, "Calls the function EvgSetACInput\nIt receives the following parameters: \n\t&bypass\n\t&sync\n\t&div\n\t&delay\n"},
{"SetACMap", (PyCFunction)mod_EvgSetACMap, METH_VARARGS, "Calls the function EvgSetACMap\nIt receives the following parameters: \n\t&map\n"},
{"ACDump", (PyCFunction)mod_EvgACDump, METH_NOARGS, "Calls the function EvgACDump\nIt receives no input parameteres\nIt returns the following values: \n\tout\n"},
{"SetRFInput", (PyCFunction)mod_EvgSetRFInput, METH_VARARGS, "Calls the function EvgSetRFInput\nIt receives the following parameters: \n\t&useRF\n\t&div\n"},
{"SetFracDiv", (PyCFunction)mod_EvgSetFracDiv, METH_VARARGS, "Calls the function EvgSetFracDiv\nIt receives the following parameters: \n\t&fracdiv\nIt returns the following values: \n\tintval\n"},
{"SetSeqRamEvent", (PyCFunction)mod_EvgSetSeqRamEvent, METH_VARARGS, "Calls the function EvgSetSeqRamEvent\nIt receives the following parameters: \n\t&ram\n\t&pos\n\t&timestamp\n\t&code\n"},
{"SeqRamDump", (PyCFunction)mod_EvgSeqRamDump, METH_VARARGS, "Calls the function EvgSeqRamDump\nIt receives the following parameters: \n\t&ram\nIt returns the following values: \n\tout\n"},
{"SeqRamControl", (PyCFunction)mod_EvgSeqRamControl, METH_VARARGS, "Calls the function EvgSeqRamControl\nIt receives the following parameters: \n\t&ram\n\t&enable\n\t&single\n\t&recycle\n\t&reset\n\t&trigsel\n"},
{"SeqRamSWTrig", (PyCFunction)mod_EvgSeqRamSWTrig, METH_VARARGS, "Calls the function EvgSeqRamSWTrig\nIt receives the following parameters: \n\t&ram\n"},
{"SeqRamStatus", (PyCFunction)mod_EvgSeqRamStatus, METH_VARARGS, "Calls the function EvgSeqRamStatus\nIt receives the following parameters: \n\t&ram\nIt returns the following values: \n\tout\n"},
{"SetUnivinMap", (PyCFunction)mod_EvgSetUnivinMap, METH_VARARGS, "Calls the function EvgSetUnivinMap\nIt receives the following parameters: \n\t&univ\n\t&trig\n\t&dbus\n"},
{"UnivinDump", (PyCFunction)mod_EvgUnivinDump, METH_NOARGS, "Calls the function EvgUnivinDump\nIt receives no input parameteres\nIt returns the following values: \n\tout\n"},
{"SetTriggerEvent", (PyCFunction)mod_EvgSetTriggerEvent, METH_VARARGS, "Calls the function EvgSetTriggerEvent\nIt receives the following parameters: \n\t&trigger\n\t&code\n\t&enable\n"},
{"TriggerEventDump", (PyCFunction)mod_EvgTriggerEventDump, METH_NOARGS, "Calls the function EvgTriggerEventDump\nIt receives no input parameteres\nIt returns the following values: \n\tout\n"},
{"SetUnivOutMap", (PyCFunction)mod_EvgSetUnivOutMap, METH_VARARGS, "Calls the function EvgSetUnivOutMap\nIt receives the following parameters: \n\t&output\n\t&map\nIt returns the following values: \n\tintval\n"},
{"SetDBufMode", (PyCFunction)mod_EvgSetDBufMode, METH_VARARGS, "Calls the function EvgSetDBufMode\nIt receives the following parameters: \n\t&enable\nIt returns the following values: \n\tintval\n"},
{"GetDBufStatus", (PyCFunction)mod_EvgGetDBufStatus, METH_NOARGS, "Calls the function EvgGetDBufStatus\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"SendDBuf", (PyCFunction)mod_EvgSendDBuf, METH_VARARGS, "Calls the function EvgSendDBuf\nTHIS FUNCTION IS BAD DOCUMENTED. Its parameter specification may be wrong. The following ones are not known to be inputs or outputs.\n\t**unknown**\n\t&size\n\tintval\n\tdbuf\nIt receives no input parameteres\n"},
{"SetVal", (PyCFunction)mod_EvgSetVal, METH_VARARGS, "Calls the function EvgSetVal\nIt receives the following parameters: \n\t&pos\n\t&val\n"},
{"GetVal", (PyCFunction)mod_EvgGetVal, METH_VARARGS, "Calls the function EvgGetVal\nIt receives the following parameters: \n\t&pos\nIt returns the following values: \n\tintval\n"},
{"GetMxcTrigMap", (PyCFunction)mod_EvgGetMxcTrigMap, METH_VARARGS, "Calls the function EvgGetMxcTrigMap\nIt receives the following parameters: \n\t&mxc\nIt returns the following values: \n\tmap\n"},
{"ResetMxcTrigMap", (PyCFunction)mod_EvgResetMxcTrigMap, METH_VARARGS, "Calls the function EvgResetMxcTrigMap\nIt receives the following parameters: \n\t&mxc\n"},
{"GetMXCPrescaler", (PyCFunction)mod_EvgGetMXCPrescaler, METH_VARARGS, "Calls the function EvgGetMXCPrescaler\nIt receives the following parameters: \n\t&mxc\nIt returns the following values: \n\tunsignedval\n"},
{"GetDBusMap", (PyCFunction)mod_EvgGetDBusMap, METH_VARARGS, "Calls the function EvgGetDBusMap\nIt receives the following parameters: \n\t&dbus\nIt returns the following values: \n\tmap\n"},
{"GetACInput", (PyCFunction)mod_EvgGetACInput, METH_NOARGS, "Calls the function EvgGetACInput\nIt receives no input parameteres\nIt returns the following values: \n\tbypass\n\tsync\n\tdiv\n\tdelay\n"},
{"GetACMap", (PyCFunction)mod_EvgGetACMap, METH_NOARGS, "Calls the function EvgGetACMap\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"ResetACMap", (PyCFunction)mod_EvgResetACMap, METH_NOARGS, "Calls the function EvgResetACMap\nIt receives no input parameteres\n"},
{"GetRFInput", (PyCFunction)mod_EvgGetRFInput, METH_NOARGS, "Calls the function EvgGetRFInput\nIt receives no input parameteres\nIt returns the following values: \n\tuseRF\n\tdiv\n"},
{"GetInternalFrac", (PyCFunction)mod_EvgGetInternalFrac, METH_NOARGS, "Calls the function EvgGetInternalFrac\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"SetInternalFrac", (PyCFunction)mod_EvgSetInternalFrac, METH_VARARGS, "Calls the function EvgSetInternalFrac\nIt receives the following parameters: \n\t&fracdiv\n"},
{"DataBufferRead", (PyCFunction)mod_EvgDataBufferRead, METH_VARARGS, "Calls the function EvgDataBufferRead\nIt receives the following parameters: \n\t&offset\nIt returns the following values: \n\tvalue\n"},
{"DataBufferWrite", (PyCFunction)mod_EvgDataBufferWrite, METH_VARARGS, "Calls the function EvgDataBufferWrite\nIt receives the following parameters: \n\t&offset\n\t&value\n"},
{"GetTriggerEvent", (PyCFunction)mod_EvgGetTriggerEvent, METH_VARARGS, "Calls the function EvgGetTriggerEvent\nIt receives the following parameters: \n\t&trigger\nIt returns the following values: \n\tcode\n\tenable\n"},
{"SeqRamGetControl", (PyCFunction)mod_EvgSeqRamGetControl, METH_VARARGS, "Calls the function EvgSeqRamGetControl\nIt receives the following parameters: \n\t&ram\nIt returns the following values: \n\tenable\n\tsingle\n\trecycle\n\ttrigsel\n"},
{"GetSeqRamEvent", (PyCFunction)mod_EvgGetSeqRamEvent, METH_VARARGS, "Calls the function EvgGetSeqRamEvent\nIt receives the following parameters: \n\t&ram\n\t&pos\nIt returns the following values: \n\ttimestamp\n\tcode\n"},
{"ClockIsCGLocked", (PyCFunction)mod_EvgClockIsCGLocked, METH_NOARGS, "Calls the function EvgClockIsCGLocked\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"PCIStatus", (PyCFunction)mod_EvgPCIStatus, METH_NOARGS, "Calls the function EvgPCIStatus\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"GetUnivinMap", (PyCFunction)mod_EvgGetUnivinMap, METH_VARARGS, "Calls the function EvgGetUnivinMap\nIt receives the following parameters: \n\t&univ\nIt returns the following values: \n\ttrig\n\tdbus\n"},
{"GetTxDBufModeEnable", (PyCFunction)mod_EvgGetTxDBufModeEnable, METH_NOARGS, "Calls the function EvgGetTxDBufModeEnable\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"SetTxDBufModeEnable", (PyCFunction)mod_EvgSetTxDBufModeEnable, METH_VARARGS, "Calls the function EvgSetTxDBufModeEnable\nIt receives the following parameters: \n\t&enable\n"},
{"Tester", (PyCFunction)mod_EvgTester, METH_NOARGS, "Calls the function EvgTester\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"WriteRegToFile", (PyCFunction)mod_EvgWriteRegToFile, METH_NOARGS, "Calls the function EvgWriteRegToFile\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"WriteFileToReg", (PyCFunction)mod_EvgWriteFileToReg, METH_NOARGS, "Calls the function EvgWriteFileToReg\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"Close", (PyCFunction)mod_EvgClose, METH_NOARGS, "Closes the device"},
{NULL, NULL, 0, NULL}  };
static PyObject * mod_EvgEnable(evg_EvgObject *self, PyObject *args)
{
int retval;
int state;
VALIDATE_NOT_CLOSED("EvgEnable") ;
if (!PyArg_ParseTuple(args, "i" ,&state)) return NULL;
retval = EvgEnable( self->pEvg ,state);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgGetEnable(evg_EvgObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvgGetEnable") ;
retval = EvgGetEnable( self->pEvg );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgRxEnable(evg_EvgObject *self, PyObject *args)
{
int retval;
int state;
VALIDATE_NOT_CLOSED("EvgRxEnable") ;
if (!PyArg_ParseTuple(args, "i" ,&state)) return NULL;
retval = EvgRxEnable( self->pEvg ,state);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgRxGetEnable(evg_EvgObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvgRxGetEnable") ;
retval = EvgRxGetEnable( self->pEvg );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgGetViolation(evg_EvgObject *self, PyObject *args)
{
int retval;
int clear;
VALIDATE_NOT_CLOSED("EvgGetViolation") ;
if (!PyArg_ParseTuple(args, "i" ,&clear)) return NULL;
retval = EvgGetViolation( self->pEvg ,clear);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgSWEventEnable(evg_EvgObject *self, PyObject *args)
{
int retval;
int state;
VALIDATE_NOT_CLOSED("EvgSWEventEnable") ;
if (!PyArg_ParseTuple(args, "i" ,&state)) return NULL;
retval = EvgSWEventEnable( self->pEvg ,state);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgGetSWEventEnable(evg_EvgObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvgGetSWEventEnable") ;
retval = EvgGetSWEventEnable( self->pEvg );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgSendSWEvent(evg_EvgObject *self, PyObject *args)
{
int retval;
int code;
VALIDATE_NOT_CLOSED("EvgSendSWEvent") ;
if (!PyArg_ParseTuple(args, "i" ,&code)) return NULL;
retval = EvgSendSWEvent( self->pEvg ,code);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgEvanEnable(evg_EvgObject *self, PyObject *args)
{
int retval;
int state;
VALIDATE_NOT_CLOSED("EvgEvanEnable") ;
if (!PyArg_ParseTuple(args, "i" ,&state)) return NULL;
retval = EvgEvanEnable( self->pEvg ,state);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgEvanGetEnable(evg_EvgObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvgEvanGetEnable") ;
retval = EvgEvanGetEnable( self->pEvg );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgEvanReset(evg_EvgObject *self)
{
VALIDATE_NOT_CLOSED("EvgEvanReset") ;
EvgEvanReset( self->pEvg );
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgEvanResetCount(evg_EvgObject *self)
{
VALIDATE_NOT_CLOSED("EvgEvanResetCount") ;
EvgEvanResetCount( self->pEvg );
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgSetMXCPrescaler(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int mxc;
unsigned int presc;
VALIDATE_NOT_CLOSED("EvgSetMXCPrescaler") ;
if (!PyArg_ParseTuple(args, "iI" ,&mxc,&presc)) return NULL;
retval = EvgSetMXCPrescaler( self->pEvg ,mxc,presc);
COND_RAISE_ERROR(retval, "EvgSetMXCPrescaler");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgSetMxcTrigMap(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int mxc;
int map;
VALIDATE_NOT_CLOSED("EvgSetMxcTrigMap") ;
if (!PyArg_ParseTuple(args, "ii" ,&mxc,&map)) return NULL;
retval = EvgSetMxcTrigMap( self->pEvg ,mxc,map);
COND_RAISE_ERROR(retval, "EvgSetMxcTrigMap");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgSyncMxc(evg_EvgObject *self)
{
VALIDATE_NOT_CLOSED("EvgSyncMxc") ;
EvgSyncMxc( self->pEvg );
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgMXCDump(evg_EvgObject *self)
{
char out[25000] = "";
VALIDATE_NOT_CLOSED("EvgMXCDump") ;
EvgMXCDump( self->pEvg ,out);
return Py_BuildValue("z",out);
}
/////////////////////
static PyObject * mod_EvgSetDBusMap(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int dbus;
int map;
VALIDATE_NOT_CLOSED("EvgSetDBusMap") ;
if (!PyArg_ParseTuple(args, "ii" ,&dbus,&map)) return NULL;
retval = EvgSetDBusMap( self->pEvg ,dbus,map);
COND_RAISE_ERROR(retval, "EvgSetDBusMap");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgDBusDump(evg_EvgObject *self)
{
char out[25000] = "";
VALIDATE_NOT_CLOSED("EvgDBusDump") ;
EvgDBusDump( self->pEvg ,out);
return Py_BuildValue("z",out);
}
/////////////////////
static PyObject * mod_EvgSetACInput(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int bypass;
int sync;
int div;
int delay;
VALIDATE_NOT_CLOSED("EvgSetACInput") ;
if (!PyArg_ParseTuple(args, "iiii" ,&bypass,&sync,&div,&delay)) return NULL;
retval = EvgSetACInput( self->pEvg ,bypass,sync,div,delay);
COND_RAISE_ERROR(retval, "EvgSetACInput");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgSetACMap(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int map;
VALIDATE_NOT_CLOSED("EvgSetACMap") ;
if (!PyArg_ParseTuple(args, "i" ,&map)) return NULL;
retval = EvgSetACMap( self->pEvg ,map);
COND_RAISE_ERROR(retval, "EvgSetACMap");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgACDump(evg_EvgObject *self)
{
char out[25000] = "";
VALIDATE_NOT_CLOSED("EvgACDump") ;
EvgACDump( self->pEvg ,out);
return Py_BuildValue("z",out);
}
/////////////////////
static PyObject * mod_EvgSetRFInput(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int useRF;
int div;
VALIDATE_NOT_CLOSED("EvgSetRFInput") ;
if (!PyArg_ParseTuple(args, "ii" ,&useRF,&div)) return NULL;
retval = EvgSetRFInput( self->pEvg ,useRF,div);
COND_RAISE_ERROR(retval, "EvgSetRFInput");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgSetFracDiv(evg_EvgObject *self, PyObject *args)
{
int retval;
int fracdiv;
VALIDATE_NOT_CLOSED("EvgSetFracDiv") ;
if (!PyArg_ParseTuple(args, "i" ,&fracdiv)) return NULL;
retval = EvgSetFracDiv( self->pEvg ,fracdiv);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgSetSeqRamEvent(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int ram;
int pos;
unsigned int timestamp;
int code;
VALIDATE_NOT_CLOSED("EvgSetSeqRamEvent") ;
if (!PyArg_ParseTuple(args, "iiIi" ,&ram,&pos,&timestamp,&code)) return NULL;
retval = EvgSetSeqRamEvent( self->pEvg ,ram,pos,timestamp,code);
COND_RAISE_ERROR(retval, "EvgSetSeqRamEvent");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgSeqRamDump(evg_EvgObject *self, PyObject *args)
{
int ram;
char out[25000] = "";
VALIDATE_NOT_CLOSED("EvgSeqRamDump") ;
if (!PyArg_ParseTuple(args, "i" ,&ram)) return NULL;
EvgSeqRamDump( self->pEvg ,ram,out);
return Py_BuildValue("z",out);
}
/////////////////////
static PyObject * mod_EvgSeqRamControl(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int ram;
int enable;
int single;
int recycle;
int reset;
int trigsel;
VALIDATE_NOT_CLOSED("EvgSeqRamControl") ;
if (!PyArg_ParseTuple(args, "iiiiii" ,&ram,&enable,&single,&recycle,&reset,&trigsel)) return NULL;
retval = EvgSeqRamControl( self->pEvg ,ram,enable,single,recycle,reset,trigsel);
COND_RAISE_ERROR(retval, "EvgSeqRamControl");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgSeqRamSWTrig(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int ram;
VALIDATE_NOT_CLOSED("EvgSeqRamSWTrig") ;
if (!PyArg_ParseTuple(args, "i" ,&ram)) return NULL;
retval = EvgSeqRamSWTrig( self->pEvg ,ram);
COND_RAISE_ERROR(retval, "EvgSeqRamSWTrig");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgSeqRamStatus(evg_EvgObject *self, PyObject *args)
{
int ram;
char out[25000] = "";
VALIDATE_NOT_CLOSED("EvgSeqRamStatus") ;
if (!PyArg_ParseTuple(args, "i" ,&ram)) return NULL;
EvgSeqRamStatus( self->pEvg ,ram,out);
return Py_BuildValue("z",out);
}
/////////////////////
static PyObject * mod_EvgSetUnivinMap(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int univ;
int trig;
int dbus;
VALIDATE_NOT_CLOSED("EvgSetUnivinMap") ;
if (!PyArg_ParseTuple(args, "iii" ,&univ,&trig,&dbus)) return NULL;
retval = EvgSetUnivinMap( self->pEvg ,univ,trig,dbus);
COND_RAISE_ERROR(retval, "EvgSetUnivinMap");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgUnivinDump(evg_EvgObject *self)
{
char out[25000] = "";
VALIDATE_NOT_CLOSED("EvgUnivinDump") ;
EvgUnivinDump( self->pEvg ,out);
return Py_BuildValue("z",out);
}
/////////////////////
static PyObject * mod_EvgSetTriggerEvent(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int trigger;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvgSetTriggerEvent") ;
if (!PyArg_ParseTuple(args, "iii" ,&trigger,&code,&enable)) return NULL;
retval = EvgSetTriggerEvent( self->pEvg ,trigger,code,enable);
COND_RAISE_ERROR(retval, "EvgSetTriggerEvent");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgTriggerEventDump(evg_EvgObject *self)
{
char out[25000] = "";
VALIDATE_NOT_CLOSED("EvgTriggerEventDump") ;
EvgTriggerEventDump( self->pEvg ,out);
return Py_BuildValue("z",out);
}
/////////////////////
static PyObject * mod_EvgSetUnivOutMap(evg_EvgObject *self, PyObject *args)
{
int retval;
int output;
int map;
VALIDATE_NOT_CLOSED("EvgSetUnivOutMap") ;
if (!PyArg_ParseTuple(args, "ii" ,&output,&map)) return NULL;
retval = EvgSetUnivOutMap( self->pEvg ,output,map);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgSetDBufMode(evg_EvgObject *self, PyObject *args)
{
int retval;
int enable;
VALIDATE_NOT_CLOSED("EvgSetDBufMode") ;
if (!PyArg_ParseTuple(args, "i" ,&enable)) return NULL;
retval = EvgSetDBufMode( self->pEvg ,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgGetDBufStatus(evg_EvgObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvgGetDBufStatus") ;
retval = EvgGetDBufStatus( self->pEvg );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgSetVal(evg_EvgObject *self, PyObject *args)
{
unsigned int pos;
unsigned int val;
VALIDATE_NOT_CLOSED("EvgSetVal") ;
if (!PyArg_ParseTuple(args, "II" ,&pos,&val)) return NULL;
EvgSetVal( self->pEvg ,pos,val);
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgGetVal(evg_EvgObject *self, PyObject *args)
{
int retval;
unsigned int pos;
VALIDATE_NOT_CLOSED("EvgGetVal") ;
if (!PyArg_ParseTuple(args, "I" ,&pos)) return NULL;
retval = EvgGetVal( self->pEvg ,pos);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgGetMxcTrigMap(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int mxc;
int map;
VALIDATE_NOT_CLOSED("EvgGetMxcTrigMap") ;
if (!PyArg_ParseTuple(args, "i" ,&mxc)) return NULL;
retval = EvgGetMxcTrigMap( self->pEvg ,mxc,&map);
COND_RAISE_ERROR(retval, "EvgGetMxcTrigMap");
return Py_BuildValue("i",map);
}
/////////////////////
static PyObject * mod_EvgResetMxcTrigMap(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int mxc;
VALIDATE_NOT_CLOSED("EvgResetMxcTrigMap") ;
if (!PyArg_ParseTuple(args, "i" ,&mxc)) return NULL;
retval = EvgResetMxcTrigMap( self->pEvg ,mxc);
COND_RAISE_ERROR(retval, "EvgResetMxcTrigMap");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgGetMXCPrescaler(evg_EvgObject *self, PyObject *args)
{
unsigned int retval;
int mxc;
VALIDATE_NOT_CLOSED("EvgGetMXCPrescaler") ;
if (!PyArg_ParseTuple(args, "i" ,&mxc)) return NULL;
retval = EvgGetMXCPrescaler( self->pEvg ,mxc);
return Py_BuildValue("I",retval);
}
/////////////////////
static PyObject * mod_EvgGetDBusMap(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int dbus;
int map;
VALIDATE_NOT_CLOSED("EvgGetDBusMap") ;
if (!PyArg_ParseTuple(args, "i" ,&dbus)) return NULL;
retval = EvgGetDBusMap( self->pEvg ,dbus,&map);
COND_RAISE_ERROR(retval, "EvgGetDBusMap");
return Py_BuildValue("i",map);
}
/////////////////////
static PyObject * mod_EvgGetACInput(evg_EvgObject *self)
{
int bypass;
int sync;
int div;
int delay;
VALIDATE_NOT_CLOSED("EvgGetACInput") ;
EvgGetACInput( self->pEvg ,&bypass,&sync,&div,&delay);
return Py_BuildValue("iiii",bypass,sync,div,delay);
}
/////////////////////
static PyObject * mod_EvgGetACMap(evg_EvgObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvgGetACMap") ;
retval = EvgGetACMap( self->pEvg );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgResetACMap(evg_EvgObject *self)
{
VALIDATE_NOT_CLOSED("EvgResetACMap") ;
EvgResetACMap( self->pEvg );
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgGetRFInput(evg_EvgObject *self)
{
int useRF;
int div;
VALIDATE_NOT_CLOSED("EvgGetRFInput") ;
EvgGetRFInput( self->pEvg ,&useRF,&div);
return Py_BuildValue("ii",useRF,div);
}
/////////////////////
static PyObject * mod_EvgGetInternalFrac(evg_EvgObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvgGetInternalFrac") ;
retval = EvgGetInternalFrac( self->pEvg );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgSetInternalFrac(evg_EvgObject *self, PyObject *args)
{
int fracdiv;
VALIDATE_NOT_CLOSED("EvgSetInternalFrac") ;
if (!PyArg_ParseTuple(args, "i" ,&fracdiv)) return NULL;
EvgSetInternalFrac( self->pEvg ,fracdiv);
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgDataBufferRead(evg_EvgObject *self, PyObject *args)
{
unsigned int offset;
unsigned int value;
VALIDATE_NOT_CLOSED("EvgDataBufferRead") ;
if (!PyArg_ParseTuple(args, "I" ,&offset)) return NULL;
EvgDataBufferRead( self->pEvg ,offset,&value);
return Py_BuildValue("I",value);
}
/////////////////////
static PyObject * mod_EvgDataBufferWrite(evg_EvgObject *self, PyObject *args)
{
unsigned int offset;
unsigned int value;
VALIDATE_NOT_CLOSED("EvgDataBufferWrite") ;
if (!PyArg_ParseTuple(args, "II" ,&offset,&value)) return NULL;
EvgDataBufferWrite( self->pEvg ,offset,value);
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgGetTriggerEvent(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int trigger;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvgGetTriggerEvent") ;
if (!PyArg_ParseTuple(args, "i" ,&trigger)) return NULL;
retval = EvgGetTriggerEvent( self->pEvg ,trigger,&code,&enable);
COND_RAISE_ERROR(retval, "EvgGetTriggerEvent");
return Py_BuildValue("ii",code,enable);
}
/////////////////////
static PyObject * mod_EvgSeqRamGetControl(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int ram;
int enable;
int single;
int recycle;
int trigsel;
VALIDATE_NOT_CLOSED("EvgSeqRamGetControl") ;
if (!PyArg_ParseTuple(args, "i" ,&ram)) return NULL;
retval = EvgSeqRamGetControl( self->pEvg ,ram,&enable,&single,&recycle,&trigsel);
COND_RAISE_ERROR(retval, "EvgSeqRamGetControl");
return Py_BuildValue("iiii",enable,single,recycle,trigsel);
}
/////////////////////
static PyObject * mod_EvgGetSeqRamEvent(evg_EvgObject *self, PyObject *args)
{
RESULT retval;
int ram;
int pos;
unsigned int timestamp;
int code;
VALIDATE_NOT_CLOSED("EvgGetSeqRamEvent") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&pos)) return NULL;
retval = EvgGetSeqRamEvent( self->pEvg ,ram,pos,&timestamp,&code);
COND_RAISE_ERROR(retval, "EvgGetSeqRamEvent");
return Py_BuildValue("Ii",timestamp,code);
}
/////////////////////
static PyObject * mod_EvgClockIsCGLocked(evg_EvgObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvgClockIsCGLocked") ;
retval = EvgClockIsCGLocked( self->pEvg );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgPCIStatus(evg_EvgObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvgPCIStatus") ;
retval = EvgPCIStatus( self->pEvg );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgGetUnivinMap(evg_EvgObject *self, PyObject *args)
{
int univ;
int trig;
int dbus;
VALIDATE_NOT_CLOSED("EvgGetUnivinMap") ;
if (!PyArg_ParseTuple(args, "i" ,&univ)) return NULL;
EvgGetUnivinMap( self->pEvg ,univ,&trig,&dbus);
return Py_BuildValue("ii",trig,dbus);
}
/////////////////////
static PyObject * mod_EvgGetTxDBufModeEnable(evg_EvgObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvgGetTxDBufModeEnable") ;
retval = EvgGetTxDBufModeEnable( self->pEvg );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgSetTxDBufModeEnable(evg_EvgObject *self, PyObject *args)
{
int enable;
VALIDATE_NOT_CLOSED("EvgSetTxDBufModeEnable") ;
if (!PyArg_ParseTuple(args, "i" ,&enable)) return NULL;
EvgSetTxDBufModeEnable( self->pEvg ,enable);
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvgTester(evg_EvgObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvgTester") ;
retval = EvgTester( self->pEvg );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgWriteRegToFile(evg_EvgObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvgWriteRegToFile") ;
retval = EvgWriteRegToFile( self->pEvg );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvgWriteFileToReg(evg_EvgObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvgWriteFileToReg") ;
retval = EvgWriteFileToReg( self->pEvg );
return Py_BuildValue("i",retval);
}
/////////////////////

