
import mevr
import signal
import time
import os
import fcntl



class TestIRQ :
	irqNum = 0

	def handler(self, a, b):
		global p, er
		print '**** que passa neng\n'
		self.irqNum = self.irqNum + 1
		self._device.SetVal(0x8, 0xff);
		self._device.IrqHandled()
		
	def __init__(self, devname = '/dev/evs/r13'):
		self._device = mevr.new(devname)
		self._device.Enable(True)

		me = (-1 << mevr.IRQ_MASTER_ENABLE)
		hb = (1 << mevr.IRQFLAG_HEARTBEAT)
		self._device.IrqEnable(me | hb)

		signal.signal(signal.SIGIO, self.handler)
		self._device.IrqAssignHandler()


	def run(self):
		for i in range(5):
			print '-----------------------'
			self._device.DumpStatus()
			time.sleep(3)
			self._device.DumpStatus()

	def Close(self):
		print '\nTOTAL IRQs: ', self.irqNum, '\n'
		self._device.Enable(False)
		self._device.Close()


a = TestIRQ()
a.run()
a.Close()