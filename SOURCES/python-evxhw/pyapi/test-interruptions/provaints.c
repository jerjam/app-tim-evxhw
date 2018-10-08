
#include <stdlib.h>
#include <stdio.h>
// #include "erapi.h"

#include "erapi.c"

void handler(int n)
{
	printf("ei que passa neeeng %d\n", n);
}

int main()
{
	int fd;
	int oflags;

	struct MrfErRegs *pEr;

	fd = EvrOpen(&pEr, "/dev/evs/r13");
	oflags = fcntl(fd, F_GETFL);
	printf("PREFLAGS: %x\n", oflags);

	EvrEnable(pEr, 1);
		
// 	EvrSetVal(pEr, 0xc, 0xff);
	printf("0x%x\n", EvrIrqEnable(pEr, EVR_IRQ_MASTER_ENABLE | EVR_IRQFLAG_HEARTBEAT));
	EvrIrqAssignHandler(pEr, fd, handler);
	oflags = fcntl(fd, F_GETFL);
	printf("POSTFLAGS: %x\n", oflags);
	EvrSetVal(pEr, 0x8, 0xff);
	EvrDumpStatus(pEr);
	sleep(3);
	EvrDumpStatus(pEr);

// 	EvrEnable(pEr, 0);
	EvrClose(fd);
}

