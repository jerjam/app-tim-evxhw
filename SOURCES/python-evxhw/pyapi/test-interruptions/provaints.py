


import mevr
import signal
import time
import os
import fcntl

p = 0
er = mevr.new('/dev/evs/r13')


def handler(a, b):
	global p, er
	print '**** que passa neng\n'
	p = p+1
	er.SetVal(0x8, 0xff);
	er.IrqHandled()

signal.signal(signal.SIGIO, handler)

er = mevr.new('/dev/evs/r13')
#er = mevr.new('/tmp/mentida.bin')
# er.SetVal(0xc,0xff)

er.Enable(True)

me = (-1 << mevr.IRQ_MASTER_ENABLE)
hb = (1 << mevr.IRQFLAG_HEARTBEAT)
print int(me | hb)
er.IrqEnable(me | hb)


signal.signal(signal.SIGIO, handler)

er.IrqAssignHandler()


for i in range(0,5):
	print '-----------------------'
	er.DumpStatus()
	time.sleep(3)
	er.DumpStatus()

er.Enable(False)
er.Close()

print p
