static PyObject * mod_EvrEnable(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrOutputEnable(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetEnable(evr_EvrObject *self);
static PyObject * mod_EvrGetOutputEnable(evr_EvrObject *self);
static PyObject * mod_EvrDumpStatus(evr_EvrObject *self);
static PyObject * mod_EvrGetViolation(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrDumpMapRam(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrMapRamEnable(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetForwardEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrEnableEventForwarding(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetEventForwarding(evr_EvrObject *self);
static PyObject * mod_EvrSetLedEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetSeconds0Event(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetSeconds1Event(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetTimestampResetEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetTimestampClockEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetFIFOEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetLatchEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetLogEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetLogStopEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrClearFIFO(evr_EvrObject *self);
static PyObject * mod_EvrEnableLogStopEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetLogStopEvent(evr_EvrObject *self);
static PyObject * mod_EvrEnableLog(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetLogState(evr_EvrObject *self);
static PyObject * mod_EvrGetLogStart(evr_EvrObject *self);
static PyObject * mod_EvrGetLogEntries(evr_EvrObject *self);
static PyObject * mod_EvrDumpFIFO(evr_EvrObject *self);
static PyObject * mod_EvrClearLog(evr_EvrObject *self);
static PyObject * mod_EvrDumpLog(evr_EvrObject *self);
static PyObject * mod_EvrSetPulseMap(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrClearPulseMap(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetPulseParams(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrDumpPulses(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetPulseProperties(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetUnivOutMap(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrDumpUnivOutMap(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetFPOutMap(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrDumpFPOutMap(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetTBOutMap(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrDumpTBOutMap(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrIrqEnable(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetIrqFlags(evr_EvrObject *self);
static PyObject * mod_EvrClearIrqFlags(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetPulseIrqMap(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrClearDiagCounters(evr_EvrObject *self);
static PyObject * mod_EvrEnableDiagCounters(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrUnivDlyEnable(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrUnivDlySetDelay(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrDumpHex(evr_EvrObject *self);
static PyObject * mod_EvrSetFracDiv(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetFracDiv(evr_EvrObject *self);
static PyObject * mod_EvrSetDBufMode(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetDBufStatus(evr_EvrObject *self);
static PyObject * mod_EvrReceiveDBuf(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetDBuf(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetTimestampDivider(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetTimestampCounter(evr_EvrObject *self);
static PyObject * mod_EvrGetSecondsCounter(evr_EvrObject *self);
static PyObject * mod_EvrGetTimestampLatch(evr_EvrObject *self);
static PyObject * mod_EvrGetSecondsLatch(evr_EvrObject *self);
static PyObject * mod_EvrSetTimestampDBus(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetPrescaler(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetExtEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetBackEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetExtEdgeSensitivity(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetExtLevelSensitivity(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetBackDBus(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetTxDBufMode(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetTxDBufStatus(evr_EvrObject *self);
static PyObject * mod_EvrSendTxDBuf(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetFormFactor(evr_EvrObject *self);
static PyObject * mod_EvrSetFineDelay(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrCMLEnable(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetVal32(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetVal32(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetVal16(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetVal16(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetBit(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrEnablePulseIrq(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrDumpClockControl(evr_EvrObject *self);
static PyObject * mod_EvrGetUnivOutMap(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetInternalFrac(evr_EvrObject *self);
static PyObject * mod_EvrSetInternalFrac(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetMapRamEnable(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetLedEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetSeconds0Event(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetSeconds1Event(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetTimestampResetEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetTimestampClockEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetFIFOEventEnabled(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetLatchEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetForwardEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetPulseMapEx(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetPulseMapEx(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetPulseParams(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetPulseProperties(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrPCIStatus(evr_EvrObject *self);
static PyObject * mod_EvrGetIrqEnable(evr_EvrObject *self);
static PyObject * mod_EvrSetPulseMapTrig(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetPulseMapSet(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetPulseMapClear(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetPulseMapTrig(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetPulseMapSet(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetPulseMapClear(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetPrescaler(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetExtEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetBackEvent(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetExtEdgeSensitivity(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetExtLevelSensitivity(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetEnableLog(evr_EvrObject *self);
static PyObject * mod_EvrGetLogEventEnabled(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetLogStopEventEnabled(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetTimestampDivider(evr_EvrObject *self);
static PyObject * mod_EvrGetTxDBufModeEnable(evr_EvrObject *self);
static PyObject * mod_EvrGetRxDBufModeEnable(evr_EvrObject *self);
static PyObject * mod_EvrSetRxDBufModeEnable(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrSetTxDBufModeEnable(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetFirmwareVersion(evr_EvrObject *self);
static PyObject * mod_EvrCloneRam(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetFPOutMap(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrGetFineDelay(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrCMLGetEnable(evr_EvrObject *self, PyObject *args);
static PyObject * mod_EvrTester(evr_EvrObject *self);
static PyObject * mod_EvrWriteRegToFile(evr_EvrObject *self);
static PyObject * mod_EvrWriteFileToReg(evr_EvrObject *self);
static PyObject *mod_EvrClose(evr_EvrObject* self);
static PyObject *mod_EvrIrqHandled(evr_EvrObject* self);
static PyObject *mod_EvrIrqAssignHandler(evr_EvrObject* self);
static PyObject *mod_EvrGetSerialNumber(evr_EvrObject* self);
static PyObject *mod_EvrGetFIFOEvent(evr_EvrObject* self);

static PyMethodDef EvrMethods[] = {
{"Enable", (PyCFunction)mod_EvrEnable, METH_VARARGS, "Calls the function EvrEnable\nIt receives the following parameters: \n\t&state\nIt returns the following values: \n\tintval\n"},
{"OutputEnable", (PyCFunction)mod_EvrOutputEnable, METH_VARARGS, "Calls the function EvrOutputEnable\nIt receives the following parameters: \n\t&state\nIt returns the following values: \n\tintval\n"},
{"GetEnable", (PyCFunction)mod_EvrGetEnable, METH_NOARGS, "Calls the function EvrGetEnable\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"GetOutputEnable", (PyCFunction)mod_EvrGetOutputEnable, METH_NOARGS, "Calls the function EvrGetOutputEnable\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"DumpStatus", (PyCFunction)mod_EvrDumpStatus, METH_NOARGS, "Calls the function EvrDumpStatus\nIt receives no input parameteres\nIt returns the following values: \n\tbuf\n"},
{"GetViolation", (PyCFunction)mod_EvrGetViolation, METH_VARARGS, "Calls the function EvrGetViolation\nIt receives the following parameters: \n\t&clear\nIt returns the following values: \n\tintval\n"},
{"DumpMapRam", (PyCFunction)mod_EvrDumpMapRam, METH_VARARGS, "Calls the function EvrDumpMapRam\nIt receives the following parameters: \n\t&ram\nIt returns the following values: \n\tbuf\n"},
{"MapRamEnable", (PyCFunction)mod_EvrMapRamEnable, METH_VARARGS, "Calls the function EvrMapRamEnable\nIt receives the following parameters: \n\t&ram\n\t&enable\n"},
{"SetForwardEvent", (PyCFunction)mod_EvrSetForwardEvent, METH_VARARGS, "Calls the function EvrSetForwardEvent\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&enable\nIt returns the following values: \n\tintval\n"},
{"EnableEventForwarding", (PyCFunction)mod_EvrEnableEventForwarding, METH_VARARGS, "Calls the function EvrEnableEventForwarding\nIt receives the following parameters: \n\t&enable\nIt returns the following values: \n\tintval\n"},
{"GetEventForwarding", (PyCFunction)mod_EvrGetEventForwarding, METH_NOARGS, "Calls the function EvrGetEventForwarding\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"SetLedEvent", (PyCFunction)mod_EvrSetLedEvent, METH_VARARGS, "Calls the function EvrSetLedEvent\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&enable\nIt returns the following values: \n\tintval\n"},
{"SetSeconds0Event", (PyCFunction)mod_EvrSetSeconds0Event, METH_VARARGS, "Calls the function EvrSetSeconds0Event\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&enable\nIt returns the following values: \n\tintval\n"},
{"SetSeconds1Event", (PyCFunction)mod_EvrSetSeconds1Event, METH_VARARGS, "Calls the function EvrSetSeconds1Event\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&enable\nIt returns the following values: \n\tintval\n"},
{"SetTimestampResetEvent", (PyCFunction)mod_EvrSetTimestampResetEvent, METH_VARARGS, "Calls the function EvrSetTimestampResetEvent\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&enable\nIt returns the following values: \n\tintval\n"},
{"SetTimestampClockEvent", (PyCFunction)mod_EvrSetTimestampClockEvent, METH_VARARGS, "Calls the function EvrSetTimestampClockEvent\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&enable\nIt returns the following values: \n\tintval\n"},
{"SetFIFOEvent", (PyCFunction)mod_EvrSetFIFOEvent, METH_VARARGS, "Calls the function EvrSetFIFOEvent\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&enable\nIt returns the following values: \n\tintval\n"},
{"SetLatchEvent", (PyCFunction)mod_EvrSetLatchEvent, METH_VARARGS, "Calls the function EvrSetLatchEvent\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&enable\nIt returns the following values: \n\tintval\n"},
{"SetLogEvent", (PyCFunction)mod_EvrSetLogEvent, METH_VARARGS, "Calls the function EvrSetLogEvent\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&enable\nIt returns the following values: \n\tintval\n"},
{"SetLogStopEvent", (PyCFunction)mod_EvrSetLogStopEvent, METH_VARARGS, "Calls the function EvrSetLogStopEvent\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&enable\nIt returns the following values: \n\tintval\n"},
{"ClearFIFO", (PyCFunction)mod_EvrClearFIFO, METH_NOARGS, "Calls the function EvrClearFIFO\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"EnableLogStopEvent", (PyCFunction)mod_EvrEnableLogStopEvent, METH_VARARGS, "Calls the function EvrEnableLogStopEvent\nIt receives the following parameters: \n\t&enable\nIt returns the following values: \n\tintval\n"},
{"GetLogStopEvent", (PyCFunction)mod_EvrGetLogStopEvent, METH_NOARGS, "Calls the function EvrGetLogStopEvent\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"EnableLog", (PyCFunction)mod_EvrEnableLog, METH_VARARGS, "Calls the function EvrEnableLog\nIt receives the following parameters: \n\t&enable\nIt returns the following values: \n\tintval\n"},
{"GetLogState", (PyCFunction)mod_EvrGetLogState, METH_NOARGS, "Calls the function EvrGetLogState\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"GetLogStart", (PyCFunction)mod_EvrGetLogStart, METH_NOARGS, "Calls the function EvrGetLogStart\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"GetLogEntries", (PyCFunction)mod_EvrGetLogEntries, METH_NOARGS, "Calls the function EvrGetLogEntries\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"DumpFIFO", (PyCFunction)mod_EvrDumpFIFO, METH_NOARGS, "Calls the function EvrDumpFIFO\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"ClearLog", (PyCFunction)mod_EvrClearLog, METH_NOARGS, "Calls the function EvrClearLog\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"DumpLog", (PyCFunction)mod_EvrDumpLog, METH_NOARGS, "Calls the function EvrDumpLog\nIt receives no input parameteres\nIt returns the following values: \n\tout\n"},
{"SetPulseMap", (PyCFunction)mod_EvrSetPulseMap, METH_VARARGS, "Calls the function EvrSetPulseMap\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&trig\n\t&set\n\t&clear\n"},
{"ClearPulseMap", (PyCFunction)mod_EvrClearPulseMap, METH_VARARGS, "Calls the function EvrClearPulseMap\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&trig\n\t&set\n\t&clear\n"},
{"SetPulseParams", (PyCFunction)mod_EvrSetPulseParams, METH_VARARGS, "Calls the function EvrSetPulseParams\nIt receives the following parameters: \n\t&pulse\n\t&presc\n\t&delay\n\t&width\nIt returns the following values: \n\tintval\n"},
{"DumpPulses", (PyCFunction)mod_EvrDumpPulses, METH_VARARGS, "Calls the function EvrDumpPulses\nIt receives the following parameters: \n\t&pulses\nIt returns the following values: \n\tbuf\n"},
{"SetPulseProperties", (PyCFunction)mod_EvrSetPulseProperties, METH_VARARGS, "Calls the function EvrSetPulseProperties\nIt receives the following parameters: \n\t&pulse\n\t&polarity\n\t&map_reset_ena\n\t&map_set_ena\n\t&map_trigger_ena\n\t&enable\nIt returns the following values: \n\tintval\n"},
{"SetUnivOutMap", (PyCFunction)mod_EvrSetUnivOutMap, METH_VARARGS, "Calls the function EvrSetUnivOutMap\nIt receives the following parameters: \n\t&output\n\t&map\n"},
{"DumpUnivOutMap", (PyCFunction)mod_EvrDumpUnivOutMap, METH_VARARGS, "Calls the function EvrDumpUnivOutMap\nIt receives the following parameters: \n\t&outputs\nIt returns the following values: \n\tbuf\n"},
{"SetFPOutMap", (PyCFunction)mod_EvrSetFPOutMap, METH_VARARGS, "Calls the function EvrSetFPOutMap\nIt receives the following parameters: \n\t&output\n\t&map\n"},
{"DumpFPOutMap", (PyCFunction)mod_EvrDumpFPOutMap, METH_VARARGS, "Calls the function EvrDumpFPOutMap\nIt receives the following parameters: \n\t&outputs\n"},
{"SetTBOutMap", (PyCFunction)mod_EvrSetTBOutMap, METH_VARARGS, "Calls the function EvrSetTBOutMap\nIt receives the following parameters: \n\t&output\n\t&map\nIt returns the following values: \n\tintval\n"},
{"DumpTBOutMap", (PyCFunction)mod_EvrDumpTBOutMap, METH_VARARGS, "Calls the function EvrDumpTBOutMap\nIt receives the following parameters: \n\t&outputs\n"},
{"IrqEnable", (PyCFunction)mod_EvrIrqEnable, METH_VARARGS, "Calls the function EvrIrqEnable\nIt receives the following parameters: \n\t&mask\nIt returns the following values: \n\tintval\n"},
{"GetIrqFlags", (PyCFunction)mod_EvrGetIrqFlags, METH_NOARGS, "Calls the function EvrGetIrqFlags\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"ClearIrqFlags", (PyCFunction)mod_EvrClearIrqFlags, METH_VARARGS, "Calls the function EvrClearIrqFlags\nIt receives the following parameters: \n\t&mask\nIt returns the following values: \n\tintval\n"},
{"SetPulseIrqMap", (PyCFunction)mod_EvrSetPulseIrqMap, METH_VARARGS, "Calls the function EvrSetPulseIrqMap\nIt receives the following parameters: \n\t&map\nIt returns the following values: \n\tintval\n"},
{"ClearDiagCounters", (PyCFunction)mod_EvrClearDiagCounters, METH_NOARGS, "Calls the function EvrClearDiagCounters\nIt receives no input parameteres\n"},
{"EnableDiagCounters", (PyCFunction)mod_EvrEnableDiagCounters, METH_VARARGS, "Calls the function EvrEnableDiagCounters\nIt receives the following parameters: \n\t&enable\n"},
{"UnivDlyEnable", (PyCFunction)mod_EvrUnivDlyEnable, METH_VARARGS, "Calls the function EvrUnivDlyEnable\nIt receives the following parameters: \n\t&dlymod\n\t&enable\nIt returns the following values: \n\tintval\n"},
{"UnivDlySetDelay", (PyCFunction)mod_EvrUnivDlySetDelay, METH_VARARGS, "Calls the function EvrUnivDlySetDelay\nIt receives the following parameters: \n\t&dlymod\n\t&dly0\n\t&dly1\nIt returns the following values: \n\tintval\n"},
{"DumpHex", (PyCFunction)mod_EvrDumpHex, METH_NOARGS, "Calls the function EvrDumpHex\nIt receives no input parameteres\n"},
{"SetFracDiv", (PyCFunction)mod_EvrSetFracDiv, METH_VARARGS, "Calls the function EvrSetFracDiv\nIt receives the following parameters: \n\t&fracdiv\nIt returns the following values: \n\tintval\n"},
{"GetFracDiv", (PyCFunction)mod_EvrGetFracDiv, METH_NOARGS, "Calls the function EvrGetFracDiv\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"SetDBufMode", (PyCFunction)mod_EvrSetDBufMode, METH_VARARGS, "Calls the function EvrSetDBufMode\nIt receives the following parameters: \n\t&enable\nIt returns the following values: \n\tintval\n"},
{"GetDBufStatus", (PyCFunction)mod_EvrGetDBufStatus, METH_NOARGS, "Calls the function EvrGetDBufStatus\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"ReceiveDBuf", (PyCFunction)mod_EvrReceiveDBuf, METH_VARARGS, "Calls the function EvrReceiveDBuf\nIt receives the following parameters: \n\t&enable\nIt returns the following values: \n\tintval\n"},
{"GetDBuf", (PyCFunction)mod_EvrGetDBuf, METH_VARARGS, "Calls the function EvrGetDBuf\nTHIS FUNCTION IS BAD DOCUMENTED. Its parameter specification may be wrong. The following ones are not known to be inputs or outputs.\n\t**unknown**\n\t&size\n\tintval\n\tdbuf\nIt receives no input parameteres\n"},
{"SetTimestampDivider", (PyCFunction)mod_EvrSetTimestampDivider, METH_VARARGS, "Calls the function EvrSetTimestampDivider\nIt receives the following parameters: \n\t&div\nIt returns the following values: \n\tintval\n"},
{"GetTimestampCounter", (PyCFunction)mod_EvrGetTimestampCounter, METH_NOARGS, "Calls the function EvrGetTimestampCounter\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"GetSecondsCounter", (PyCFunction)mod_EvrGetSecondsCounter, METH_NOARGS, "Calls the function EvrGetSecondsCounter\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"GetTimestampLatch", (PyCFunction)mod_EvrGetTimestampLatch, METH_NOARGS, "Calls the function EvrGetTimestampLatch\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"GetSecondsLatch", (PyCFunction)mod_EvrGetSecondsLatch, METH_NOARGS, "Calls the function EvrGetSecondsLatch\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"SetTimestampDBus", (PyCFunction)mod_EvrSetTimestampDBus, METH_VARARGS, "Calls the function EvrSetTimestampDBus\nIt receives the following parameters: \n\t&enable\nIt returns the following values: \n\tintval\n"},
{"SetPrescaler", (PyCFunction)mod_EvrSetPrescaler, METH_VARARGS, "Calls the function EvrSetPrescaler\nIt receives the following parameters: \n\t&presc\n\t&div\n"},
{"SetExtEvent", (PyCFunction)mod_EvrSetExtEvent, METH_VARARGS, "Calls the function EvrSetExtEvent\nIt receives the following parameters: \n\t&ttlin\n\t&code\n\t&edge_enable\n\t&level_enable\nIt returns the following values: \n\tintval\n"},
{"SetBackEvent", (PyCFunction)mod_EvrSetBackEvent, METH_VARARGS, "Calls the function EvrSetBackEvent\nIt receives the following parameters: \n\t&ttlin\n\t&code\n\t&edge_enable\n\t&level_enable\nIt returns the following values: \n\tintval\n"},
{"SetExtEdgeSensitivity", (PyCFunction)mod_EvrSetExtEdgeSensitivity, METH_VARARGS, "Calls the function EvrSetExtEdgeSensitivity\nIt receives the following parameters: \n\t&ttlin\n\t&edge\n"},
{"SetExtLevelSensitivity", (PyCFunction)mod_EvrSetExtLevelSensitivity, METH_VARARGS, "Calls the function EvrSetExtLevelSensitivity\nIt receives the following parameters: \n\t&ttlin\n\t&level\n"},
{"SetBackDBus", (PyCFunction)mod_EvrSetBackDBus, METH_VARARGS, "Calls the function EvrSetBackDBus\nIt receives the following parameters: \n\t&ttlin\n\t&dbus\nIt returns the following values: \n\tintval\n"},
{"SetTxDBufMode", (PyCFunction)mod_EvrSetTxDBufMode, METH_VARARGS, "Calls the function EvrSetTxDBufMode\nIt receives the following parameters: \n\t&enable\nIt returns the following values: \n\tintval\n"},
{"GetTxDBufStatus", (PyCFunction)mod_EvrGetTxDBufStatus, METH_NOARGS, "Calls the function EvrGetTxDBufStatus\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"SendTxDBuf", (PyCFunction)mod_EvrSendTxDBuf, METH_VARARGS, "Calls the function EvrSendTxDBuf\nTHIS FUNCTION IS BAD DOCUMENTED. Its parameter specification may be wrong. The following ones are not known to be inputs or outputs.\n\t**unknown**\n\t&size\n\tintval\n\tdbuf\nIt receives no input parameteres\n"},
{"GetFormFactor", (PyCFunction)mod_EvrGetFormFactor, METH_NOARGS, "Calls the function EvrGetFormFactor\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"SetFineDelay", (PyCFunction)mod_EvrSetFineDelay, METH_VARARGS, "Calls the function EvrSetFineDelay\nIt receives the following parameters: \n\t&channel\n\t&delay\nIt returns the following values: \n\tintval\n"},
{"CMLEnable", (PyCFunction)mod_EvrCMLEnable, METH_VARARGS, "Calls the function EvrCMLEnable\nIt receives the following parameters: \n\t&channel\n\t&state\nIt returns the following values: \n\tintval\n"},
{"SetVal32", (PyCFunction)mod_EvrSetVal32, METH_VARARGS, "Calls the function EvrSetVal32\nIt receives the following parameters: \n\t&pos\n\t&val\n"},
{"GetVal32", (PyCFunction)mod_EvrGetVal32, METH_VARARGS, "Calls the function EvrGetVal32\nIt receives the following parameters: \n\t&pos\nIt returns the following values: \n\tunsignedval\n"},
{"SetVal16", (PyCFunction)mod_EvrSetVal16, METH_VARARGS, "Calls the function EvrSetVal16\nIt receives the following parameters: \n\t&pos\n\t&val\n"},
{"GetVal16", (PyCFunction)mod_EvrGetVal16, METH_VARARGS, "Calls the function EvrGetVal16\nIt receives the following parameters: \n\t&pos\nIt returns the following values: \n\tunsignedval\n"},
{"SetBit", (PyCFunction)mod_EvrSetBit, METH_VARARGS, "Calls the function EvrSetBit\nIt receives the following parameters: \n\t&pos\n\t&bit\n\t&val\n"},
{"EnablePulseIrq", (PyCFunction)mod_EvrEnablePulseIrq, METH_VARARGS, "Calls the function EvrEnablePulseIrq\nIt receives the following parameters: \n\t&pulse\n\t&enable\n"},
{"DumpClockControl", (PyCFunction)mod_EvrDumpClockControl, METH_NOARGS, "Calls the function EvrDumpClockControl\nIt receives no input parameteres\nIt returns the following values: \n\tout\n"},
{"GetUnivOutMap", (PyCFunction)mod_EvrGetUnivOutMap, METH_VARARGS, "Calls the function EvrGetUnivOutMap\nIt receives the following parameters: \n\t&output\nIt returns the following values: \n\tmap\n"},
{"GetInternalFrac", (PyCFunction)mod_EvrGetInternalFrac, METH_NOARGS, "Calls the function EvrGetInternalFrac\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"SetInternalFrac", (PyCFunction)mod_EvrSetInternalFrac, METH_VARARGS, "Calls the function EvrSetInternalFrac\nIt receives the following parameters: \n\t&fracdiv\nIt returns the following values: \n\tintval\n"},
{"GetMapRamEnable", (PyCFunction)mod_EvrGetMapRamEnable, METH_VARARGS, "Calls the function EvrGetMapRamEnable\nIt receives the following parameters: \n\t&ram\nIt returns the following values: \n\tintval\n"},
{"GetLedEvent", (PyCFunction)mod_EvrGetLedEvent, METH_VARARGS, "Calls the function EvrGetLedEvent\nIt receives the following parameters: \n\t&ram\n\t&code\nIt returns the following values: \n\tenable\n"},
{"GetSeconds0Event", (PyCFunction)mod_EvrGetSeconds0Event, METH_VARARGS, "Calls the function EvrGetSeconds0Event\nIt receives the following parameters: \n\t&ram\n\t&code\nIt returns the following values: \n\tenable\n"},
{"GetSeconds1Event", (PyCFunction)mod_EvrGetSeconds1Event, METH_VARARGS, "Calls the function EvrGetSeconds1Event\nIt receives the following parameters: \n\t&ram\n\t&code\nIt returns the following values: \n\tenable\n"},
{"GetTimestampResetEvent", (PyCFunction)mod_EvrGetTimestampResetEvent, METH_VARARGS, "Calls the function EvrGetTimestampResetEvent\nIt receives the following parameters: \n\t&ram\n\t&code\nIt returns the following values: \n\tenable\n"},
{"GetTimestampClockEvent", (PyCFunction)mod_EvrGetTimestampClockEvent, METH_VARARGS, "Calls the function EvrGetTimestampClockEvent\nIt receives the following parameters: \n\t&ram\n\t&code\nIt returns the following values: \n\tenable\n"},
{"GetFIFOEventEnabled", (PyCFunction)mod_EvrGetFIFOEventEnabled, METH_VARARGS, "Calls the function EvrGetFIFOEventEnabled\nIt receives the following parameters: \n\t&ram\n\t&code\nIt returns the following values: \n\tenable\n"},
{"GetLatchEvent", (PyCFunction)mod_EvrGetLatchEvent, METH_VARARGS, "Calls the function EvrGetLatchEvent\nIt receives the following parameters: \n\t&ram\n\t&code\nIt returns the following values: \n\tenable\n"},
{"GetForwardEvent", (PyCFunction)mod_EvrGetForwardEvent, METH_VARARGS, "Calls the function EvrGetForwardEvent\nIt receives the following parameters: \n\t&ram\n\t&code\nIt returns the following values: \n\tenable\n"},
{"SetPulseMapEx", (PyCFunction)mod_EvrSetPulseMapEx, METH_VARARGS, "Calls the function EvrSetPulseMapEx\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&trig\n\t&set\n\t&clear\n"},
{"GetPulseMapEx", (PyCFunction)mod_EvrGetPulseMapEx, METH_VARARGS, "Calls the function EvrGetPulseMapEx\nIt receives the following parameters: \n\t&ram\n\t&code\nIt returns the following values: \n\ttrig\n\tset\n\tclear\n"},
{"GetPulseParams", (PyCFunction)mod_EvrGetPulseParams, METH_VARARGS, "Calls the function EvrGetPulseParams\nIt receives the following parameters: \n\t&pulse\nIt returns the following values: \n\tpresc\n\tdelay\n\twidth\n"},
{"GetPulseProperties", (PyCFunction)mod_EvrGetPulseProperties, METH_VARARGS, "Calls the function EvrGetPulseProperties\nIt receives the following parameters: \n\t&pulse\nIt returns the following values: \n\tpolarity\n\tmap_reset_ena\n\tmap_set_ena\n\tmap_trigger_ena\n\tenable\n"},
{"PCIStatus", (PyCFunction)mod_EvrPCIStatus, METH_NOARGS, "Calls the function EvrPCIStatus\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"GetIrqEnable", (PyCFunction)mod_EvrGetIrqEnable, METH_NOARGS, "Calls the function EvrGetIrqEnable\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"SetPulseMapTrig", (PyCFunction)mod_EvrSetPulseMapTrig, METH_VARARGS, "Calls the function EvrSetPulseMapTrig\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&trig\n"},
{"SetPulseMapSet", (PyCFunction)mod_EvrSetPulseMapSet, METH_VARARGS, "Calls the function EvrSetPulseMapSet\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&set\n"},
{"SetPulseMapClear", (PyCFunction)mod_EvrSetPulseMapClear, METH_VARARGS, "Calls the function EvrSetPulseMapClear\nIt receives the following parameters: \n\t&ram\n\t&code\n\t&clear\n"},
{"GetPulseMapTrig", (PyCFunction)mod_EvrGetPulseMapTrig, METH_VARARGS, "Calls the function EvrGetPulseMapTrig\nIt receives the following parameters: \n\t&ram\n\t&code\nIt returns the following values: \n\ttrig\n"},
{"GetPulseMapSet", (PyCFunction)mod_EvrGetPulseMapSet, METH_VARARGS, "Calls the function EvrGetPulseMapSet\nIt receives the following parameters: \n\t&ram\n\t&code\nIt returns the following values: \n\tset\n"},
{"GetPulseMapClear", (PyCFunction)mod_EvrGetPulseMapClear, METH_VARARGS, "Calls the function EvrGetPulseMapClear\nIt receives the following parameters: \n\t&ram\n\t&code\nIt returns the following values: \n\tclear\n"},
{"GetPrescaler", (PyCFunction)mod_EvrGetPrescaler, METH_VARARGS, "Calls the function EvrGetPrescaler\nIt receives the following parameters: \n\t&prescid\nIt returns the following values: \n\tpresc\n"},
{"GetExtEvent", (PyCFunction)mod_EvrGetExtEvent, METH_VARARGS, "Calls the function EvrGetExtEvent\nIt receives the following parameters: \n\t&ttlin\nIt returns the following values: \n\tcode\n\tedge_enable\n\tlevel_enable\n"},
{"GetBackEvent", (PyCFunction)mod_EvrGetBackEvent, METH_VARARGS, "Calls the function EvrGetBackEvent\nIt receives the following parameters: \n\t&ttlin\nIt returns the following values: \n\tcode\n\tedge_enable\n\tlevel_enable\n"},
{"GetExtEdgeSensitivity", (PyCFunction)mod_EvrGetExtEdgeSensitivity, METH_VARARGS, "Calls the function EvrGetExtEdgeSensitivity\nIt receives the following parameters: \n\t&ttlin\nIt returns the following values: \n\tedge\n"},
{"GetExtLevelSensitivity", (PyCFunction)mod_EvrGetExtLevelSensitivity, METH_VARARGS, "Calls the function EvrGetExtLevelSensitivity\nIt receives the following parameters: \n\t&ttlin\nIt returns the following values: \n\tlevel\n"},
{"GetEnableLog", (PyCFunction)mod_EvrGetEnableLog, METH_NOARGS, "Calls the function EvrGetEnableLog\nIt receives no input parameteres\nIt returns the following values: \n\tenable\n"},
{"GetLogEventEnabled", (PyCFunction)mod_EvrGetLogEventEnabled, METH_VARARGS, "Calls the function EvrGetLogEventEnabled\nIt receives the following parameters: \n\t&ram\n\t&code\nIt returns the following values: \n\tenable\n"},
{"GetLogStopEventEnabled", (PyCFunction)mod_EvrGetLogStopEventEnabled, METH_VARARGS, "Calls the function EvrGetLogStopEventEnabled\nIt receives the following parameters: \n\t&ram\n\t&code\nIt returns the following values: \n\tenable\n"},
{"GetTimestampDivider", (PyCFunction)mod_EvrGetTimestampDivider, METH_NOARGS, "Calls the function EvrGetTimestampDivider\nIt receives no input parameteres\nIt returns the following values: \n\tdiv\n"},
{"GetTxDBufModeEnable", (PyCFunction)mod_EvrGetTxDBufModeEnable, METH_NOARGS, "Calls the function EvrGetTxDBufModeEnable\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"GetRxDBufModeEnable", (PyCFunction)mod_EvrGetRxDBufModeEnable, METH_NOARGS, "Calls the function EvrGetRxDBufModeEnable\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"SetRxDBufModeEnable", (PyCFunction)mod_EvrSetRxDBufModeEnable, METH_VARARGS, "Calls the function EvrSetRxDBufModeEnable\nIt receives the following parameters: \n\t&enable\n"},
{"SetTxDBufModeEnable", (PyCFunction)mod_EvrSetTxDBufModeEnable, METH_VARARGS, "Calls the function EvrSetTxDBufModeEnable\nIt receives the following parameters: \n\t&enable\n"},
{"GetFirmwareVersion", (PyCFunction)mod_EvrGetFirmwareVersion, METH_NOARGS, "Calls the function EvrGetFirmwareVersion\nIt receives no input parameteres\nIt returns the following values: \n\tunsignedval\n"},
{"CloneRam", (PyCFunction)mod_EvrCloneRam, METH_VARARGS, "Calls the function EvrCloneRam\nIt receives the following parameters: \n\t&from\n\t&to\n"},
{"GetFPOutMap", (PyCFunction)mod_EvrGetFPOutMap, METH_VARARGS, "Calls the function EvrGetFPOutMap\nIt receives the following parameters: \n\t&output\nIt returns the following values: \n\tmap\n"},
{"GetFineDelay", (PyCFunction)mod_EvrGetFineDelay, METH_VARARGS, "Calls the function EvrGetFineDelay\nIt receives the following parameters: \n\t&channel\nIt returns the following values: \n\tintval\n"},
{"CMLGetEnable", (PyCFunction)mod_EvrCMLGetEnable, METH_VARARGS, "Calls the function EvrCMLGetEnable\nIt receives the following parameters: \n\t&channel\nIt returns the following values: \n\tintval\n"},
{"Tester", (PyCFunction)mod_EvrTester, METH_NOARGS, "Calls the function EvrTester\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"WriteRegToFile", (PyCFunction)mod_EvrWriteRegToFile, METH_NOARGS, "Calls the function EvrWriteRegToFile\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"WriteFileToReg", (PyCFunction)mod_EvrWriteFileToReg, METH_NOARGS, "Calls the function EvrWriteFileToReg\nIt receives no input parameteres\nIt returns the following values: \n\tintval\n"},
{"Close", (PyCFunction)mod_EvrClose, METH_NOARGS, "Closes the device"},
{"IrqHandled", (PyCFunction)mod_EvrIrqHandled, METH_NOARGS, "Should be called to inform the device the last interrupt has been managed so it knowns tha next one can be generated."},
{"IrqAssignHandler", (PyCFunction)mod_EvrIrqAssignHandler, METH_NOARGS, "Should be called once if the process wants to manage interrupts generated by the current device"},
{"GetSerialNumber", (PyCFunction)mod_EvrGetSerialNumber, METH_NOARGS, "Returns the serial number of the device"},
{"GetFIFOEvent", (PyCFunction)mod_EvrGetFIFOEvent, METH_NOARGS, "Pops an element from the FIFO"},

{NULL, NULL, 0, NULL}  };
static PyObject * mod_EvrEnable(evr_EvrObject *self, PyObject *args)
{
int retval;
int state;
VALIDATE_NOT_CLOSED("EvrEnable") ;
if (!PyArg_ParseTuple(args, "i" ,&state)) return NULL;
retval = EvrEnable( self->pEvr ,state);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrOutputEnable(evr_EvrObject *self, PyObject *args)
{
int retval;
int state;
VALIDATE_NOT_CLOSED("EvrOutputEnable") ;
if (!PyArg_ParseTuple(args, "i" ,&state)) return NULL;
retval = EvrOutputEnable( self->pEvr ,state);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetEnable(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetEnable") ;
retval = EvrGetEnable( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetOutputEnable(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetOutputEnable") ;
retval = EvrGetOutputEnable( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrDumpStatus(evr_EvrObject *self)
{
char buf[25000] = "";
VALIDATE_NOT_CLOSED("EvrDumpStatus") ;
EvrDumpStatus( self->pEvr ,buf);
return Py_BuildValue("z",buf);
}
/////////////////////
static PyObject * mod_EvrGetViolation(evr_EvrObject *self, PyObject *args)
{
int retval;
int clear;
VALIDATE_NOT_CLOSED("EvrGetViolation") ;
if (!PyArg_ParseTuple(args, "i" ,&clear)) return NULL;
retval = EvrGetViolation( self->pEvr ,clear);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrDumpMapRam(evr_EvrObject *self, PyObject *args)
{
int ram;
char buf[25000] = "";
VALIDATE_NOT_CLOSED("EvrDumpMapRam") ;
if (!PyArg_ParseTuple(args, "i" ,&ram)) return NULL;
EvrDumpMapRam( self->pEvr ,ram,buf);
return Py_BuildValue("z",buf);
}
/////////////////////
static PyObject * mod_EvrMapRamEnable(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int enable;
VALIDATE_NOT_CLOSED("EvrMapRamEnable") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&enable)) return NULL;
retval = EvrMapRamEnable( self->pEvr ,ram,enable);
COND_RAISE_ERROR(retval, "EvrMapRamEnable");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrSetForwardEvent(evr_EvrObject *self, PyObject *args)
{
int retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrSetForwardEvent") ;
if (!PyArg_ParseTuple(args, "iii" ,&ram,&code,&enable)) return NULL;
retval = EvrSetForwardEvent( self->pEvr ,ram,code,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrEnableEventForwarding(evr_EvrObject *self, PyObject *args)
{
int retval;
int enable;
VALIDATE_NOT_CLOSED("EvrEnableEventForwarding") ;
if (!PyArg_ParseTuple(args, "i" ,&enable)) return NULL;
retval = EvrEnableEventForwarding( self->pEvr ,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetEventForwarding(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetEventForwarding") ;
retval = EvrGetEventForwarding( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetLedEvent(evr_EvrObject *self, PyObject *args)
{
int retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrSetLedEvent") ;
if (!PyArg_ParseTuple(args, "iii" ,&ram,&code,&enable)) return NULL;
retval = EvrSetLedEvent( self->pEvr ,ram,code,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetSeconds0Event(evr_EvrObject *self, PyObject *args)
{
int retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrSetSeconds0Event") ;
if (!PyArg_ParseTuple(args, "iii" ,&ram,&code,&enable)) return NULL;
retval = EvrSetSeconds0Event( self->pEvr ,ram,code,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetSeconds1Event(evr_EvrObject *self, PyObject *args)
{
int retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrSetSeconds1Event") ;
if (!PyArg_ParseTuple(args, "iii" ,&ram,&code,&enable)) return NULL;
retval = EvrSetSeconds1Event( self->pEvr ,ram,code,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetTimestampResetEvent(evr_EvrObject *self, PyObject *args)
{
int retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrSetTimestampResetEvent") ;
if (!PyArg_ParseTuple(args, "iii" ,&ram,&code,&enable)) return NULL;
retval = EvrSetTimestampResetEvent( self->pEvr ,ram,code,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetTimestampClockEvent(evr_EvrObject *self, PyObject *args)
{
int retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrSetTimestampClockEvent") ;
if (!PyArg_ParseTuple(args, "iii" ,&ram,&code,&enable)) return NULL;
retval = EvrSetTimestampClockEvent( self->pEvr ,ram,code,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetFIFOEvent(evr_EvrObject *self, PyObject *args)
{
int retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrSetFIFOEvent") ;
if (!PyArg_ParseTuple(args, "iii" ,&ram,&code,&enable)) return NULL;
retval = EvrSetFIFOEvent( self->pEvr ,ram,code,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetLatchEvent(evr_EvrObject *self, PyObject *args)
{
int retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrSetLatchEvent") ;
if (!PyArg_ParseTuple(args, "iii" ,&ram,&code,&enable)) return NULL;
retval = EvrSetLatchEvent( self->pEvr ,ram,code,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetLogEvent(evr_EvrObject *self, PyObject *args)
{
int retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrSetLogEvent") ;
if (!PyArg_ParseTuple(args, "iii" ,&ram,&code,&enable)) return NULL;
retval = EvrSetLogEvent( self->pEvr ,ram,code,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetLogStopEvent(evr_EvrObject *self, PyObject *args)
{
int retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrSetLogStopEvent") ;
if (!PyArg_ParseTuple(args, "iii" ,&ram,&code,&enable)) return NULL;
retval = EvrSetLogStopEvent( self->pEvr ,ram,code,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrClearFIFO(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrClearFIFO") ;
retval = EvrClearFIFO( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
//W: Funcio no tractada "EvrGetFIFOEvent", parametres desconeguts(True, 'struct FIFOEvent', 'fe')
static PyObject * mod_EvrEnableLogStopEvent(evr_EvrObject *self, PyObject *args)
{
int retval;
int enable;
VALIDATE_NOT_CLOSED("EvrEnableLogStopEvent") ;
if (!PyArg_ParseTuple(args, "i" ,&enable)) return NULL;
retval = EvrEnableLogStopEvent( self->pEvr ,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetLogStopEvent(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetLogStopEvent") ;
retval = EvrGetLogStopEvent( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrEnableLog(evr_EvrObject *self, PyObject *args)
{
int retval;
int enable;
VALIDATE_NOT_CLOSED("EvrEnableLog") ;
if (!PyArg_ParseTuple(args, "i" ,&enable)) return NULL;
retval = EvrEnableLog( self->pEvr ,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetLogState(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetLogState") ;
retval = EvrGetLogState( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetLogStart(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetLogStart") ;
retval = EvrGetLogStart( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetLogEntries(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetLogEntries") ;
retval = EvrGetLogEntries( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrDumpFIFO(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrDumpFIFO") ;
retval = EvrDumpFIFO( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrClearLog(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrClearLog") ;
retval = EvrClearLog( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrDumpLog(evr_EvrObject *self)
{
char out[25000] = "";
VALIDATE_NOT_CLOSED("EvrDumpLog") ;
EvrDumpLog( self->pEvr ,out);
return Py_BuildValue("z",out);
}
/////////////////////
static PyObject * mod_EvrSetPulseMap(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int trig;
int set;
int clear;
VALIDATE_NOT_CLOSED("EvrSetPulseMap") ;
if (!PyArg_ParseTuple(args, "iiiii" ,&ram,&code,&trig,&set,&clear)) return NULL;
retval = EvrSetPulseMap( self->pEvr ,ram,code,trig,set,clear);
COND_RAISE_ERROR(retval, "EvrSetPulseMap");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrClearPulseMap(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int trig;
int set;
int clear;
VALIDATE_NOT_CLOSED("EvrClearPulseMap") ;
if (!PyArg_ParseTuple(args, "iiiii" ,&ram,&code,&trig,&set,&clear)) return NULL;
retval = EvrClearPulseMap( self->pEvr ,ram,code,trig,set,clear);
COND_RAISE_ERROR(retval, "EvrClearPulseMap");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrSetPulseParams(evr_EvrObject *self, PyObject *args)
{
int retval;
int pulse;
unsigned int presc;
unsigned int delay;
unsigned int width;
VALIDATE_NOT_CLOSED("EvrSetPulseParams") ;
if (!PyArg_ParseTuple(args, "iIII" ,&pulse,&presc,&delay,&width)) return NULL;
retval = EvrSetPulseParams( self->pEvr ,pulse,presc,delay,width);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrDumpPulses(evr_EvrObject *self, PyObject *args)
{
int pulses;
char buf[25000] = "";
VALIDATE_NOT_CLOSED("EvrDumpPulses") ;
if (!PyArg_ParseTuple(args, "i" ,&pulses)) return NULL;
EvrDumpPulses( self->pEvr ,pulses,buf);
return Py_BuildValue("z",buf);
}
/////////////////////
static PyObject * mod_EvrSetPulseProperties(evr_EvrObject *self, PyObject *args)
{
int retval;
int pulse;
int polarity;
int map_reset_ena;
int map_set_ena;
int map_trigger_ena;
int enable;
VALIDATE_NOT_CLOSED("EvrSetPulseProperties") ;
if (!PyArg_ParseTuple(args, "iiiiii" ,&pulse,&polarity,&map_reset_ena,&map_set_ena,&map_trigger_ena,&enable)) return NULL;
retval = EvrSetPulseProperties( self->pEvr ,pulse,polarity,map_reset_ena,map_set_ena,map_trigger_ena,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetUnivOutMap(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int output;
int map;
VALIDATE_NOT_CLOSED("EvrSetUnivOutMap") ;
if (!PyArg_ParseTuple(args, "ii" ,&output,&map)) return NULL;
retval = EvrSetUnivOutMap( self->pEvr ,output,map);
COND_RAISE_ERROR(retval, "EvrSetUnivOutMap");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrDumpUnivOutMap(evr_EvrObject *self, PyObject *args)
{
int outputs;
char buf[25000] = "";
VALIDATE_NOT_CLOSED("EvrDumpUnivOutMap") ;
if (!PyArg_ParseTuple(args, "i" ,&outputs)) return NULL;
EvrDumpUnivOutMap( self->pEvr ,outputs,buf);
return Py_BuildValue("z",buf);
}
/////////////////////
static PyObject * mod_EvrSetFPOutMap(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int output;
int map;
VALIDATE_NOT_CLOSED("EvrSetFPOutMap") ;
if (!PyArg_ParseTuple(args, "ii" ,&output,&map)) return NULL;
retval = EvrSetFPOutMap( self->pEvr ,output,map);
COND_RAISE_ERROR(retval, "EvrSetFPOutMap");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrDumpFPOutMap(evr_EvrObject *self, PyObject *args)
{
int outputs;
VALIDATE_NOT_CLOSED("EvrDumpFPOutMap") ;
if (!PyArg_ParseTuple(args, "i" ,&outputs)) return NULL;
EvrDumpFPOutMap( self->pEvr ,outputs);
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrSetTBOutMap(evr_EvrObject *self, PyObject *args)
{
int retval;
int output;
int map;
VALIDATE_NOT_CLOSED("EvrSetTBOutMap") ;
if (!PyArg_ParseTuple(args, "ii" ,&output,&map)) return NULL;
retval = EvrSetTBOutMap( self->pEvr ,output,map);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrDumpTBOutMap(evr_EvrObject *self, PyObject *args)
{
int outputs;
VALIDATE_NOT_CLOSED("EvrDumpTBOutMap") ;
if (!PyArg_ParseTuple(args, "i" ,&outputs)) return NULL;
EvrDumpTBOutMap( self->pEvr ,outputs);
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrIrqEnable(evr_EvrObject *self, PyObject *args)
{
int retval;
int mask;
VALIDATE_NOT_CLOSED("EvrIrqEnable") ;
if (!PyArg_ParseTuple(args, "i" ,&mask)) return NULL;
retval = EvrIrqEnable( self->pEvr ,mask);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetIrqFlags(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetIrqFlags") ;
retval = EvrGetIrqFlags( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrClearIrqFlags(evr_EvrObject *self, PyObject *args)
{
int retval;
int mask;
VALIDATE_NOT_CLOSED("EvrClearIrqFlags") ;
if (!PyArg_ParseTuple(args, "i" ,&mask)) return NULL;
retval = EvrClearIrqFlags( self->pEvr ,mask);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetPulseIrqMap(evr_EvrObject *self, PyObject *args)
{
int retval;
int map;
VALIDATE_NOT_CLOSED("EvrSetPulseIrqMap") ;
if (!PyArg_ParseTuple(args, "i" ,&map)) return NULL;
retval = EvrSetPulseIrqMap( self->pEvr ,map);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrClearDiagCounters(evr_EvrObject *self)
{
VALIDATE_NOT_CLOSED("EvrClearDiagCounters") ;
EvrClearDiagCounters( self->pEvr );
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrEnableDiagCounters(evr_EvrObject *self, PyObject *args)
{
int enable;
VALIDATE_NOT_CLOSED("EvrEnableDiagCounters") ;
if (!PyArg_ParseTuple(args, "i" ,&enable)) return NULL;
EvrEnableDiagCounters( self->pEvr ,enable);
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrUnivDlyEnable(evr_EvrObject *self, PyObject *args)
{
int retval;
int dlymod;
int enable;
VALIDATE_NOT_CLOSED("EvrUnivDlyEnable") ;
if (!PyArg_ParseTuple(args, "ii" ,&dlymod,&enable)) return NULL;
retval = EvrUnivDlyEnable( self->pEvr ,dlymod,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrUnivDlySetDelay(evr_EvrObject *self, PyObject *args)
{
int retval;
int dlymod;
int dly0;
int dly1;
VALIDATE_NOT_CLOSED("EvrUnivDlySetDelay") ;
if (!PyArg_ParseTuple(args, "iii" ,&dlymod,&dly0,&dly1)) return NULL;
retval = EvrUnivDlySetDelay( self->pEvr ,dlymod,dly0,dly1);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrDumpHex(evr_EvrObject *self)
{
VALIDATE_NOT_CLOSED("EvrDumpHex") ;
EvrDumpHex( self->pEvr );
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrSetFracDiv(evr_EvrObject *self, PyObject *args)
{
int retval;
int fracdiv;
VALIDATE_NOT_CLOSED("EvrSetFracDiv") ;
if (!PyArg_ParseTuple(args, "i" ,&fracdiv)) return NULL;
retval = EvrSetFracDiv( self->pEvr ,fracdiv);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetFracDiv(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetFracDiv") ;
retval = EvrGetFracDiv( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetDBufMode(evr_EvrObject *self, PyObject *args)
{
int retval;
int enable;
VALIDATE_NOT_CLOSED("EvrSetDBufMode") ;
if (!PyArg_ParseTuple(args, "i" ,&enable)) return NULL;
retval = EvrSetDBufMode( self->pEvr ,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetDBufStatus(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetDBufStatus") ;
retval = EvrGetDBufStatus( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrReceiveDBuf(evr_EvrObject *self, PyObject *args)
{
int retval;
int enable;
VALIDATE_NOT_CLOSED("EvrReceiveDBuf") ;
if (!PyArg_ParseTuple(args, "i" ,&enable)) return NULL;
retval = EvrReceiveDBuf( self->pEvr ,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetTimestampDivider(evr_EvrObject *self, PyObject *args)
{
int retval;
int div;
VALIDATE_NOT_CLOSED("EvrSetTimestampDivider") ;
if (!PyArg_ParseTuple(args, "i" ,&div)) return NULL;
retval = EvrSetTimestampDivider( self->pEvr ,div);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetTimestampCounter(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetTimestampCounter") ;
retval = EvrGetTimestampCounter( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetSecondsCounter(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetSecondsCounter") ;
retval = EvrGetSecondsCounter( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetTimestampLatch(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetTimestampLatch") ;
retval = EvrGetTimestampLatch( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetSecondsLatch(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetSecondsLatch") ;
retval = EvrGetSecondsLatch( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetTimestampDBus(evr_EvrObject *self, PyObject *args)
{
int retval;
int enable;
VALIDATE_NOT_CLOSED("EvrSetTimestampDBus") ;
if (!PyArg_ParseTuple(args, "i" ,&enable)) return NULL;
retval = EvrSetTimestampDBus( self->pEvr ,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetPrescaler(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int presc;
unsigned int div;
VALIDATE_NOT_CLOSED("EvrSetPrescaler") ;
if (!PyArg_ParseTuple(args, "iI" ,&presc,&div)) return NULL;
retval = EvrSetPrescaler( self->pEvr ,presc,div);
COND_RAISE_ERROR(retval, "EvrSetPrescaler");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrSetExtEvent(evr_EvrObject *self, PyObject *args)
{
int retval;
int ttlin;
int code;
int edge_enable;
int level_enable;
VALIDATE_NOT_CLOSED("EvrSetExtEvent") ;
if (!PyArg_ParseTuple(args, "iiii" ,&ttlin,&code,&edge_enable,&level_enable)) return NULL;
retval = EvrSetExtEvent( self->pEvr ,ttlin,code,edge_enable,level_enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetBackEvent(evr_EvrObject *self, PyObject *args)
{
int retval;
int ttlin;
int code;
int edge_enable;
int level_enable;
VALIDATE_NOT_CLOSED("EvrSetBackEvent") ;
if (!PyArg_ParseTuple(args, "iiii" ,&ttlin,&code,&edge_enable,&level_enable)) return NULL;
retval = EvrSetBackEvent( self->pEvr ,ttlin,code,edge_enable,level_enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetExtEdgeSensitivity(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ttlin;
int edge;
VALIDATE_NOT_CLOSED("EvrSetExtEdgeSensitivity") ;
if (!PyArg_ParseTuple(args, "ii" ,&ttlin,&edge)) return NULL;
retval = EvrSetExtEdgeSensitivity( self->pEvr ,ttlin,edge);
COND_RAISE_ERROR(retval, "EvrSetExtEdgeSensitivity");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrSetExtLevelSensitivity(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ttlin;
int level;
VALIDATE_NOT_CLOSED("EvrSetExtLevelSensitivity") ;
if (!PyArg_ParseTuple(args, "ii" ,&ttlin,&level)) return NULL;
retval = EvrSetExtLevelSensitivity( self->pEvr ,ttlin,level);
COND_RAISE_ERROR(retval, "EvrSetExtLevelSensitivity");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrSetBackDBus(evr_EvrObject *self, PyObject *args)
{
int retval;
int ttlin;
int dbus;
VALIDATE_NOT_CLOSED("EvrSetBackDBus") ;
if (!PyArg_ParseTuple(args, "ii" ,&ttlin,&dbus)) return NULL;
retval = EvrSetBackDBus( self->pEvr ,ttlin,dbus);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetTxDBufMode(evr_EvrObject *self, PyObject *args)
{
int retval;
int enable;
VALIDATE_NOT_CLOSED("EvrSetTxDBufMode") ;
if (!PyArg_ParseTuple(args, "i" ,&enable)) return NULL;
retval = EvrSetTxDBufMode( self->pEvr ,enable);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetTxDBufStatus(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetTxDBufStatus") ;
retval = EvrGetTxDBufStatus( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetFormFactor(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetFormFactor") ;
retval = EvrGetFormFactor( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetFineDelay(evr_EvrObject *self, PyObject *args)
{
int retval;
int channel;
int delay;
VALIDATE_NOT_CLOSED("EvrSetFineDelay") ;
if (!PyArg_ParseTuple(args, "ii" ,&channel,&delay)) return NULL;
retval = EvrSetFineDelay( self->pEvr ,channel,delay);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrCMLEnable(evr_EvrObject *self, PyObject *args)
{
int retval;
int channel;
int state;
VALIDATE_NOT_CLOSED("EvrCMLEnable") ;
if (!PyArg_ParseTuple(args, "ii" ,&channel,&state)) return NULL;
retval = EvrCMLEnable( self->pEvr ,channel,state);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetVal32(evr_EvrObject *self, PyObject *args)
{
unsigned int pos;
unsigned int val;
VALIDATE_NOT_CLOSED("EvrSetVal32") ;
if (!PyArg_ParseTuple(args, "II" ,&pos,&val)) return NULL;
EvrSetVal32( self->pEvr ,pos,val);
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrGetVal32(evr_EvrObject *self, PyObject *args)
{
unsigned int retval;
unsigned int pos;
VALIDATE_NOT_CLOSED("EvrGetVal32") ;
if (!PyArg_ParseTuple(args, "I" ,&pos)) return NULL;
retval = EvrGetVal32( self->pEvr ,pos);
return Py_BuildValue("I",retval);
}
/////////////////////
static PyObject * mod_EvrSetVal16(evr_EvrObject *self, PyObject *args)
{
unsigned int pos;
unsigned int val;
VALIDATE_NOT_CLOSED("EvrSetVal16") ;
if (!PyArg_ParseTuple(args, "II" ,&pos,&val)) return NULL;
EvrSetVal16( self->pEvr ,pos,val);
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrGetVal16(evr_EvrObject *self, PyObject *args)
{
unsigned int retval;
unsigned int pos;
VALIDATE_NOT_CLOSED("EvrGetVal16") ;
if (!PyArg_ParseTuple(args, "I" ,&pos)) return NULL;
retval = EvrGetVal16( self->pEvr ,pos);
return Py_BuildValue("I",retval);
}
/////////////////////
static PyObject * mod_EvrSetBit(evr_EvrObject *self, PyObject *args)
{
unsigned int pos;
unsigned int bit;
unsigned int val;
VALIDATE_NOT_CLOSED("EvrSetBit") ;
if (!PyArg_ParseTuple(args, "III" ,&pos,&bit,&val)) return NULL;
EvrSetBit( self->pEvr ,pos,bit,val);
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrEnablePulseIrq(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int pulse;
int enable;
VALIDATE_NOT_CLOSED("EvrEnablePulseIrq") ;
if (!PyArg_ParseTuple(args, "ii" ,&pulse,&enable)) return NULL;
retval = EvrEnablePulseIrq( self->pEvr ,pulse,enable);
COND_RAISE_ERROR(retval, "EvrEnablePulseIrq");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrDumpClockControl(evr_EvrObject *self)
{
char out[25000] = "";
VALIDATE_NOT_CLOSED("EvrDumpClockControl") ;
EvrDumpClockControl( self->pEvr ,out);
return Py_BuildValue("z",out);
}
/////////////////////
static PyObject * mod_EvrGetUnivOutMap(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int output;
int map;
VALIDATE_NOT_CLOSED("EvrGetUnivOutMap") ;
if (!PyArg_ParseTuple(args, "i" ,&output)) return NULL;
retval = EvrGetUnivOutMap( self->pEvr ,output,&map);
COND_RAISE_ERROR(retval, "EvrGetUnivOutMap");
return Py_BuildValue("i",map);
}
/////////////////////
static PyObject * mod_EvrGetInternalFrac(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetInternalFrac") ;
retval = EvrGetInternalFrac( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetInternalFrac(evr_EvrObject *self, PyObject *args)
{
int retval;
int fracdiv;
VALIDATE_NOT_CLOSED("EvrSetInternalFrac") ;
if (!PyArg_ParseTuple(args, "i" ,&fracdiv)) return NULL;
retval = EvrSetInternalFrac( self->pEvr ,fracdiv);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetMapRamEnable(evr_EvrObject *self, PyObject *args)
{
int retval;
int ram;
VALIDATE_NOT_CLOSED("EvrGetMapRamEnable") ;
if (!PyArg_ParseTuple(args, "i" ,&ram)) return NULL;
retval = EvrGetMapRamEnable( self->pEvr ,ram);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetLedEvent(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrGetLedEvent") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&code)) return NULL;
retval = EvrGetLedEvent( self->pEvr ,ram,code,&enable);
COND_RAISE_ERROR(retval, "EvrGetLedEvent");
return Py_BuildValue("i",enable);
}
/////////////////////
static PyObject * mod_EvrGetSeconds0Event(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrGetSeconds0Event") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&code)) return NULL;
retval = EvrGetSeconds0Event( self->pEvr ,ram,code,&enable);
COND_RAISE_ERROR(retval, "EvrGetSeconds0Event");
return Py_BuildValue("i",enable);
}
/////////////////////
static PyObject * mod_EvrGetSeconds1Event(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrGetSeconds1Event") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&code)) return NULL;
retval = EvrGetSeconds1Event( self->pEvr ,ram,code,&enable);
COND_RAISE_ERROR(retval, "EvrGetSeconds1Event");
return Py_BuildValue("i",enable);
}
/////////////////////
static PyObject * mod_EvrGetTimestampResetEvent(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrGetTimestampResetEvent") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&code)) return NULL;
retval = EvrGetTimestampResetEvent( self->pEvr ,ram,code,&enable);
COND_RAISE_ERROR(retval, "EvrGetTimestampResetEvent");
return Py_BuildValue("i",enable);
}
/////////////////////
static PyObject * mod_EvrGetTimestampClockEvent(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrGetTimestampClockEvent") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&code)) return NULL;
retval = EvrGetTimestampClockEvent( self->pEvr ,ram,code,&enable);
COND_RAISE_ERROR(retval, "EvrGetTimestampClockEvent");
return Py_BuildValue("i",enable);
}
/////////////////////
static PyObject * mod_EvrGetFIFOEventEnabled(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrGetFIFOEventEnabled") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&code)) return NULL;
retval = EvrGetFIFOEventEnabled( self->pEvr ,ram,code,&enable);
COND_RAISE_ERROR(retval, "EvrGetFIFOEventEnabled");
return Py_BuildValue("i",enable);
}
/////////////////////
static PyObject * mod_EvrGetLatchEvent(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrGetLatchEvent") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&code)) return NULL;
retval = EvrGetLatchEvent( self->pEvr ,ram,code,&enable);
COND_RAISE_ERROR(retval, "EvrGetLatchEvent");
return Py_BuildValue("i",enable);
}
/////////////////////
static PyObject * mod_EvrGetForwardEvent(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrGetForwardEvent") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&code)) return NULL;
retval = EvrGetForwardEvent( self->pEvr ,ram,code,&enable);
COND_RAISE_ERROR(retval, "EvrGetForwardEvent");
return Py_BuildValue("i",enable);
}
/////////////////////
static PyObject * mod_EvrSetPulseMapEx(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int trig;
int set;
int clear;
VALIDATE_NOT_CLOSED("EvrSetPulseMapEx") ;
if (!PyArg_ParseTuple(args, "iiiii" ,&ram,&code,&trig,&set,&clear)) return NULL;
retval = EvrSetPulseMapEx( self->pEvr ,ram,code,trig,set,clear);
COND_RAISE_ERROR(retval, "EvrSetPulseMapEx");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrGetPulseMapEx(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int trig;
int set;
int clear;
VALIDATE_NOT_CLOSED("EvrGetPulseMapEx") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&code)) return NULL;
retval = EvrGetPulseMapEx( self->pEvr ,ram,code,&trig,&set,&clear);
COND_RAISE_ERROR(retval, "EvrGetPulseMapEx");
return Py_BuildValue("iii",trig,set,clear);
}
/////////////////////
static PyObject * mod_EvrGetPulseParams(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int pulse;
unsigned int presc;
unsigned int delay;
unsigned int width;
VALIDATE_NOT_CLOSED("EvrGetPulseParams") ;
if (!PyArg_ParseTuple(args, "i" ,&pulse)) return NULL;
retval = EvrGetPulseParams( self->pEvr ,pulse,&presc,&delay,&width);
COND_RAISE_ERROR(retval, "EvrGetPulseParams");
return Py_BuildValue("III",presc,delay,width);
}
/////////////////////
static PyObject * mod_EvrGetPulseProperties(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int pulse;
int polarity;
int map_reset_ena;
int map_set_ena;
int map_trigger_ena;
int enable;
VALIDATE_NOT_CLOSED("EvrGetPulseProperties") ;
if (!PyArg_ParseTuple(args, "i" ,&pulse)) return NULL;
retval = EvrGetPulseProperties( self->pEvr ,pulse,&polarity,&map_reset_ena,&map_set_ena,&map_trigger_ena,&enable);
COND_RAISE_ERROR(retval, "EvrGetPulseProperties");
return Py_BuildValue("iiiii",polarity,map_reset_ena,map_set_ena,map_trigger_ena,enable);
}
/////////////////////
static PyObject * mod_EvrPCIStatus(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrPCIStatus") ;
retval = EvrPCIStatus( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetIrqEnable(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetIrqEnable") ;
retval = EvrGetIrqEnable( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetPulseMapTrig(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int trig;
VALIDATE_NOT_CLOSED("EvrSetPulseMapTrig") ;
if (!PyArg_ParseTuple(args, "iii" ,&ram,&code,&trig)) return NULL;
retval = EvrSetPulseMapTrig( self->pEvr ,ram,code,trig);
COND_RAISE_ERROR(retval, "EvrSetPulseMapTrig");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrSetPulseMapSet(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int set;
VALIDATE_NOT_CLOSED("EvrSetPulseMapSet") ;
if (!PyArg_ParseTuple(args, "iii" ,&ram,&code,&set)) return NULL;
retval = EvrSetPulseMapSet( self->pEvr ,ram,code,set);
COND_RAISE_ERROR(retval, "EvrSetPulseMapSet");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrSetPulseMapClear(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int clear;
VALIDATE_NOT_CLOSED("EvrSetPulseMapClear") ;
if (!PyArg_ParseTuple(args, "iii" ,&ram,&code,&clear)) return NULL;
retval = EvrSetPulseMapClear( self->pEvr ,ram,code,clear);
COND_RAISE_ERROR(retval, "EvrSetPulseMapClear");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrGetPulseMapTrig(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int trig;
VALIDATE_NOT_CLOSED("EvrGetPulseMapTrig") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&code)) return NULL;
retval = EvrGetPulseMapTrig( self->pEvr ,ram,code,&trig);
COND_RAISE_ERROR(retval, "EvrGetPulseMapTrig");
return Py_BuildValue("i",trig);
}
/////////////////////
static PyObject * mod_EvrGetPulseMapSet(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int set;
VALIDATE_NOT_CLOSED("EvrGetPulseMapSet") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&code)) return NULL;
retval = EvrGetPulseMapSet( self->pEvr ,ram,code,&set);
COND_RAISE_ERROR(retval, "EvrGetPulseMapSet");
return Py_BuildValue("i",set);
}
/////////////////////
static PyObject * mod_EvrGetPulseMapClear(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int clear;
VALIDATE_NOT_CLOSED("EvrGetPulseMapClear") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&code)) return NULL;
retval = EvrGetPulseMapClear( self->pEvr ,ram,code,&clear);
COND_RAISE_ERROR(retval, "EvrGetPulseMapClear");
return Py_BuildValue("i",clear);
}
/////////////////////
static PyObject * mod_EvrGetPrescaler(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int prescid;
unsigned int presc;
VALIDATE_NOT_CLOSED("EvrGetPrescaler") ;
if (!PyArg_ParseTuple(args, "i" ,&prescid)) return NULL;
retval = EvrGetPrescaler( self->pEvr ,prescid,&presc);
COND_RAISE_ERROR(retval, "EvrGetPrescaler");
return Py_BuildValue("I",presc);
}
/////////////////////
static PyObject * mod_EvrGetExtEvent(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ttlin;
int code;
int edge_enable;
int level_enable;
VALIDATE_NOT_CLOSED("EvrGetExtEvent") ;
if (!PyArg_ParseTuple(args, "i" ,&ttlin)) return NULL;
retval = EvrGetExtEvent( self->pEvr ,ttlin,&code,&edge_enable,&level_enable);
COND_RAISE_ERROR(retval, "EvrGetExtEvent");
return Py_BuildValue("iii",code,edge_enable,level_enable);
}
/////////////////////
static PyObject * mod_EvrGetBackEvent(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ttlin;
int code;
int edge_enable;
int level_enable;
VALIDATE_NOT_CLOSED("EvrGetBackEvent") ;
if (!PyArg_ParseTuple(args, "i" ,&ttlin)) return NULL;
retval = EvrGetBackEvent( self->pEvr ,ttlin,&code,&edge_enable,&level_enable);
COND_RAISE_ERROR(retval, "EvrGetBackEvent");
return Py_BuildValue("iii",code,edge_enable,level_enable);
}
/////////////////////
static PyObject * mod_EvrGetExtEdgeSensitivity(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ttlin;
int edge;
VALIDATE_NOT_CLOSED("EvrGetExtEdgeSensitivity") ;
if (!PyArg_ParseTuple(args, "i" ,&ttlin)) return NULL;
retval = EvrGetExtEdgeSensitivity( self->pEvr ,ttlin,&edge);
COND_RAISE_ERROR(retval, "EvrGetExtEdgeSensitivity");
return Py_BuildValue("i",edge);
}
/////////////////////
static PyObject * mod_EvrGetExtLevelSensitivity(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ttlin;
int level;
VALIDATE_NOT_CLOSED("EvrGetExtLevelSensitivity") ;
if (!PyArg_ParseTuple(args, "i" ,&ttlin)) return NULL;
retval = EvrGetExtLevelSensitivity( self->pEvr ,ttlin,&level);
COND_RAISE_ERROR(retval, "EvrGetExtLevelSensitivity");
return Py_BuildValue("i",level);
}
/////////////////////
static PyObject * mod_EvrGetEnableLog(evr_EvrObject *self)
{
RESULT retval;
int enable;
VALIDATE_NOT_CLOSED("EvrGetEnableLog") ;
retval = EvrGetEnableLog( self->pEvr ,&enable);
COND_RAISE_ERROR(retval, "EvrGetEnableLog");
return Py_BuildValue("i",enable);
}
/////////////////////
static PyObject * mod_EvrGetLogEventEnabled(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrGetLogEventEnabled") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&code)) return NULL;
retval = EvrGetLogEventEnabled( self->pEvr ,ram,code,&enable);
COND_RAISE_ERROR(retval, "EvrGetLogEventEnabled");
return Py_BuildValue("i",enable);
}
/////////////////////
static PyObject * mod_EvrGetLogStopEventEnabled(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int ram;
int code;
int enable;
VALIDATE_NOT_CLOSED("EvrGetLogStopEventEnabled") ;
if (!PyArg_ParseTuple(args, "ii" ,&ram,&code)) return NULL;
retval = EvrGetLogStopEventEnabled( self->pEvr ,ram,code,&enable);
COND_RAISE_ERROR(retval, "EvrGetLogStopEventEnabled");
return Py_BuildValue("i",enable);
}
/////////////////////
static PyObject * mod_EvrGetTimestampDivider(evr_EvrObject *self)
{
RESULT retval;
int div;
VALIDATE_NOT_CLOSED("EvrGetTimestampDivider") ;
retval = EvrGetTimestampDivider( self->pEvr ,&div);
COND_RAISE_ERROR(retval, "EvrGetTimestampDivider");
return Py_BuildValue("i",div);
}
/////////////////////
static PyObject * mod_EvrGetTxDBufModeEnable(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetTxDBufModeEnable") ;
retval = EvrGetTxDBufModeEnable( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrGetRxDBufModeEnable(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrGetRxDBufModeEnable") ;
retval = EvrGetRxDBufModeEnable( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrSetRxDBufModeEnable(evr_EvrObject *self, PyObject *args)
{
int enable;
VALIDATE_NOT_CLOSED("EvrSetRxDBufModeEnable") ;
if (!PyArg_ParseTuple(args, "i" ,&enable)) return NULL;
EvrSetRxDBufModeEnable( self->pEvr ,enable);
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrSetTxDBufModeEnable(evr_EvrObject *self, PyObject *args)
{
int enable;
VALIDATE_NOT_CLOSED("EvrSetTxDBufModeEnable") ;
if (!PyArg_ParseTuple(args, "i" ,&enable)) return NULL;
EvrSetTxDBufModeEnable( self->pEvr ,enable);
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrGetFirmwareVersion(evr_EvrObject *self)
{
unsigned int retval;
VALIDATE_NOT_CLOSED("EvrGetFirmwareVersion") ;
retval = EvrGetFirmwareVersion( self->pEvr );
return Py_BuildValue("I",retval);
}
/////////////////////
static PyObject * mod_EvrCloneRam(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int from;
int to;
VALIDATE_NOT_CLOSED("EvrCloneRam") ;
if (!PyArg_ParseTuple(args, "ii" ,&from,&to)) return NULL;
retval = EvrCloneRam( self->pEvr ,from,to);
COND_RAISE_ERROR(retval, "EvrCloneRam");
Py_INCREF(Py_None);
return Py_None;
}
/////////////////////
static PyObject * mod_EvrGetFPOutMap(evr_EvrObject *self, PyObject *args)
{
RESULT retval;
int output;
int map;
VALIDATE_NOT_CLOSED("EvrGetFPOutMap") ;
if (!PyArg_ParseTuple(args, "i" ,&output)) return NULL;
retval = EvrGetFPOutMap( self->pEvr ,output,&map);
COND_RAISE_ERROR(retval, "EvrGetFPOutMap");
return Py_BuildValue("i",map);
}
/////////////////////
static PyObject * mod_EvrGetFineDelay(evr_EvrObject *self, PyObject *args)
{
int retval;
int channel;
VALIDATE_NOT_CLOSED("EvrGetFineDelay") ;
if (!PyArg_ParseTuple(args, "i" ,&channel)) return NULL;
retval = EvrGetFineDelay( self->pEvr ,channel);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrCMLGetEnable(evr_EvrObject *self, PyObject *args)
{
int retval;
int channel;
VALIDATE_NOT_CLOSED("EvrCMLGetEnable") ;
if (!PyArg_ParseTuple(args, "i" ,&channel)) return NULL;
retval = EvrCMLGetEnable( self->pEvr ,channel);
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrTester(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrTester") ;
retval = EvrTester( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrWriteRegToFile(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrWriteRegToFile") ;
retval = EvrWriteRegToFile( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////
static PyObject * mod_EvrWriteFileToReg(evr_EvrObject *self)
{
int retval;
VALIDATE_NOT_CLOSED("EvrWriteFileToReg") ;
retval = EvrWriteFileToReg( self->pEvr );
return Py_BuildValue("i",retval);
}
/////////////////////

