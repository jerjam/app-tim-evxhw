/*
  erapi.c -- Functions for Micro-Research Event Receiver
             Application Programming Interface

  Author: Jukka Pietarinen (MRF)
  Date:   08.12.2006

*/

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <stdio.h>
#include <endian.h>
#include <byteswap.h>
#include <errno.h>
#include <signal.h>
#include <sys/ioctl.h>
#include <string.h> // memcpy
#include <unistd.h> // close

#include "erapi.h"
#include <stddef.h>



#define DEBUG 1
#define DEBUG_PRINTF printf
// #define DEBUG_PRINTF(x...) buf += sprintf(buf, x)

/*#define GET_OFFSET(stru, val) (size_t)&(((stru*)NULL)->val)*/

#define _CHECK_RANGE(op, min, overmax, err) if ( (op) < (min) || (op) >= (overmax)) return (err);

#define _CHECK_PULSE_RANGE(pulse) _CHECK_RANGE(pulse, 0, EVR_MAX_PULSES, RERR_PULSE_RANGE)

#define _CHECK_UNIVOUT_MAP_RANGE(output) _CHECK_RANGE(output, 0, EVR_MAX_UNIVOUT_MAP, RERR_UNIVOUT_MAP_RANGE)

#define _CHECK_RAM_RANGE(ram) _CHECK_RANGE(ram, 0, EVR_MAPRAMS, RERR_RAM_RANGE)

#define _CHECK_EVENT_RANGE(code) _CHECK_RANGE(code, 1, EVR_MAX_EVENT_CODE+1, RERR_EVENT_CODE_RANGE)

#define _CHECK_PRESCALER_RANGE(prescaler) _CHECK_RANGE(prescaler, 0, EVR_MAX_PRESCALERS, RERR_PRESCALERS_RANGE)

#define _CHECK_TTLIN_RANGE(ttlin) _CHECK_RANGE(ttlin, 0, EVR_MAX_FPIN_MAP, RERR_UNIVIN_RANGE)

#define _DUMP_AUX_BEGIN(out, buf) static char __buf[2048]; if(out == 0) buf = __buf;

#define _DUMP_AUX_END(out, buf) if (out == 0) printf(__buf);



const char * evr_get_errmsg(RESULT s)
{
	static const char* errors[] = {
		"OK",
		"Parameter out of range: ram must be 0 or 1",
		"Parameter out of range: event code must be 1 to 255",
		"Parameter out of range: pulse must be 0 to EVR_MAX_PULSES",
		"Parameter out of range: univ out must be 0 to EVR_MAX_UNIVOUT_MAP",
		"Parameter out of range: prescaler must be 0 to EVR_MAX_PRESCALERS",
		"Parameter out of range: ttlin must be 0 to EVR_MAX_FPIN_MAP",
		"Parameter out of range: output must be 0 to EVR_MAX_FPOUT_MAP",

		"UNKNOWN ERROR"
	};
	const int errsz = sizeof(errors)/sizeof(errors[0]);

	if ( (s < 0) || (s >= errsz) )
		return errors[errsz-1];
	return errors[s];
}

int EvrOpen(volatile struct MrfErRegs **pEr, char *device_name)
{
  int fd;

  /* Open Event Receiver device for read/write */
  fd = open(device_name, O_RDWR);
#ifdef DEBUG
  DEBUG_PRINTF("EvrOpen: open(\"%s\", O_RDWR) returned %d\n", device_name, fd);
#endif
  if (fd != -1)
    {
      /* Memory map Event Receiver registers */
      *pEr = (struct MrfErRegs *) mmap(0, EVR_MEM_WINDOW, PROT_READ | PROT_WRITE,
					MAP_SHARED, fd, 0);
#ifdef DEBUG
  DEBUG_PRINTF("EvrOpen: mmap returned %08x, errno %d\n", (int) *pEr,
	       errno);
#endif
      if (*pEr == MAP_FAILED)
	{
	  close(fd);
	  return -1;
	}
    }

  return fd;
}

int EvrClose(int fd)
{
  int result;

  result = munmap(0, EVR_MEM_WINDOW);
  return close(fd);
}

int EvrEnable(volatile struct MrfErRegs *pEr, int state)
{
  if (state)
    pEr->Control |= be32_to_cpu(1 << C_EVR_CTRL_MASTER_ENABLE);
  else
    pEr->Control &= be32_to_cpu(~(1 << C_EVR_CTRL_MASTER_ENABLE));

  return EvrGetEnable(pEr);
}

int EvrOutputEnable(volatile struct MrfErRegs *pEr, int state)
{
  if (state)
    pEr->Control |= be32_to_cpu(1 << C_EVR_CTRL_OUTEN);
  else
    pEr->Control &= be32_to_cpu(~(1 << C_EVR_CTRL_OUTEN));

  return EvrGetEnable(pEr);
}

int EvrGetEnable(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->Control & be32_to_cpu(1 << C_EVR_CTRL_MASTER_ENABLE));
}

int EvrGetOutputEnable(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->Control & be32_to_cpu(1 << C_EVR_CTRL_OUTEN));
}

int EvrGetViolation(volatile struct MrfErRegs *pEr, int clear)
{
  int result;

  result = be32_to_cpu(pEr->IrqFlag & be32_to_cpu(1 << C_EVR_IRQFLAG_VIOLATION));
  if (clear && result)
    pEr->IrqFlag = be32_to_cpu(result);

  return result;
}

void EvrDumpStatus(volatile struct MrfErRegs *pEr, char * out)
{
  int result;
  char *buf = out;
  _DUMP_AUX_BEGIN(out, buf)

  result = be32_to_cpu(pEr->Status);
  buf += sprintf(buf, "Status %08x ", result);
  if (result & (1 << C_EVR_STATUS_LEGACY_VIO))
	  buf += sprintf(buf, "LEGVIO ");
  if (result & (1 << C_EVR_STATUS_LOG_STOPPED))
	  buf += sprintf(buf, "LOGSTOP ");
  buf += sprintf(buf, "\n");
  result = be32_to_cpu(pEr->Control);
  buf += sprintf(buf, "Control %08x: ", result);
  if (result & (1 << C_EVR_CTRL_MASTER_ENABLE))
    buf += sprintf(buf, "MSEN ");
  if (result & (1 << C_EVR_CTRL_EVENT_FWD_ENA))
    buf += sprintf(buf, "FWD ");
  if (result & (1 << C_EVR_CTRL_TXLOOPBACK))
    buf += sprintf(buf, "TXLP ");
  if (result & (1 << C_EVR_CTRL_RXLOOPBACK))
    buf += sprintf(buf, "RXLP ");
  if (result & (1 << C_EVR_CTRL_TS_CLOCK_DBUS))
    buf += sprintf(buf, "DSDBUS ");
  if (result & (1 << C_EVR_CTRL_MAP_RAM_ENABLE))
    buf += sprintf(buf, "MAPENA ");
  if (result & (1 << C_EVR_CTRL_MAP_RAM_SELECT))
    buf += sprintf(buf, "MAPSEL ");
  buf += sprintf(buf, "\n");
  result = be32_to_cpu(pEr->IrqFlag);
  buf += sprintf(buf, "IRQ Flag %08x: ", result);
  if (result & (1 << C_EVR_IRQ_MASTER_ENABLE))
    buf += sprintf(buf, "IRQEN ");
  if (result & (1 << C_EVR_IRQFLAG_DATABUF))
    buf += sprintf(buf, "DBUF ");
  if (result & (1 << C_EVR_IRQFLAG_PULSE))
    buf += sprintf(buf, "PULSE ");
  if (result & (1 << C_EVR_IRQFLAG_EVENT))
    buf += sprintf(buf, "EVENT ");
  if (result & (1 << C_EVR_IRQFLAG_HEARTBEAT))
    buf += sprintf(buf, "HB ");
  if (result & (1 << C_EVR_IRQFLAG_FIFOFULL))
    buf += sprintf(buf, "FF ");
  if (result & (1 << C_EVR_IRQFLAG_VIOLATION))
    buf += sprintf(buf, "VIO ");
  buf += sprintf(buf, "\n");
  result = be32_to_cpu(pEr->DataBufControl);
  buf += sprintf(buf, "DataBufControl %08x\n", result);

  _DUMP_AUX_END(out, buf)
//  return buf - out;
}

void EvrDumpMapRam(volatile struct MrfErRegs *pEr, int ram, char* out)
{
  int code;
  int intev;
  int ptrig, pset, pclr;
  char *buf = out;
  _DUMP_AUX_BEGIN(out, buf)

  if (ram < 0 || ram >= EVR_MAPRAMS) {
	*out = 0;
	return;
  }

  for (code = 0; code <= EVR_MAX_EVENT_CODE; code++)
    {
      intev = be32_to_cpu(pEr->MapRam[ram][code].IntEvent);
      ptrig = be32_to_cpu(pEr->MapRam[ram][code].PulseTrigger);
      pset = be32_to_cpu(pEr->MapRam[ram][code].PulseSet);
      pclr = be32_to_cpu(pEr->MapRam[ram][code].PulseClear);

      if (intev ||
	  ptrig ||
	  pset ||
	  pclr)
	{
	  buf += sprintf(buf, "Code 0x%02x (%3d): ", code, code);
	  if (intev & (1 << C_EVR_MAP_SAVE_EVENT))
	    buf += sprintf(buf, "SAVE ");
	  if (intev & (1 << C_EVR_MAP_LATCH_TIMESTAMP))
	    buf += sprintf(buf, "LTS ");
	  if (intev & (1 << C_EVR_MAP_LED_EVENT))
	    buf += sprintf(buf, "LED ");
	  if (intev & (1 << C_EVR_MAP_FORWARD_EVENT))
	    buf += sprintf(buf, "FWD ");
	  if (intev & (1 << C_EVR_MAP_STOP_LOG))
	    buf += sprintf(buf, "STOPLOG ");
	  if (intev & (1 << C_EVR_MAP_HEARTBEAT_EVENT))
	    buf += sprintf(buf, "HB ");
	  if (intev & (1 << C_EVR_MAP_RESETPRESC_EVENT))
	    buf += sprintf(buf, "RESPRSC ");
	  if (intev & (1 << C_EVR_MAP_TIMESTAMP_RESET))
	    buf += sprintf(buf, "RESTS ");
	  if (intev & (1 << C_EVR_MAP_TIMESTAMP_CLK))
	    buf += sprintf(buf, "TSCLK ");
	  if (intev & (1 << C_EVR_MAP_SECONDS_1))
	    buf += sprintf(buf, "SEC1 ");
	  if (intev & (1 << C_EVR_MAP_SECONDS_0))
	    buf += sprintf(buf, "SEC0 ");
	  if (ptrig)
	    buf += sprintf(buf, "Trig %08x", ptrig);
	  if (pset)
	    buf += sprintf(buf, "Set %08x", pset);
	  if (pclr)
	    buf += sprintf(buf, "Clear %08x", pclr);
	  buf += sprintf(buf, "\n");
	}
    }
  //return buf - out;
  _DUMP_AUX_END(out, buf)
}

RESULT EvrMapRamEnable(volatile struct MrfErRegs *pEr, int ram, int enable)
{
  int result;

  _CHECK_RAM_RANGE(ram)

  result = be32_to_cpu(pEr->Control);
  result &= ~((1 << C_EVR_CTRL_MAP_RAM_ENABLE) | (1 << C_EVR_CTRL_MAP_RAM_SELECT));
  if (ram == 1)
    result |= (1 << C_EVR_CTRL_MAP_RAM_SELECT);
  if (enable == 1)
    result |= (1 << C_EVR_CTRL_MAP_RAM_ENABLE);
  pEr->Control = be32_to_cpu(result);

  return 0;
}

RESULT EvrSetPulseMap(volatile struct MrfErRegs *pEr, int ram, int code, int trig,
		   int set, int clear)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code)

  if (trig >= 0 && trig < EVR_MAX_PULSES)
    pEr->MapRam[ram][code].PulseTrigger |= be32_to_cpu(1 << trig);
  if (set >= 0 && set < EVR_MAX_PULSES)
    pEr->MapRam[ram][code].PulseSet |= be32_to_cpu(1 << set);
  if (clear >= 0 && clear < EVR_MAX_PULSES)
    pEr->MapRam[ram][code].PulseClear |= be32_to_cpu(1 << clear);

  return 0;
}

int EvrSetForwardEvent(volatile struct MrfErRegs *pEr, int ram, int code, int enable)
{
  if (ram < 0 || ram >= EVR_MAPRAMS)
    return -1;

  if (code <= 0 || code > EVR_MAX_EVENT_CODE)
    return -1;

  if (!enable)
    pEr->MapRam[ram][code].IntEvent &= be32_to_cpu(~(1 << C_EVR_MAP_FORWARD_EVENT));
  if (enable)
    pEr->MapRam[ram][code].IntEvent |= be32_to_cpu(1 << C_EVR_MAP_FORWARD_EVENT);

  return 0;
}

int EvrEnableEventForwarding(volatile struct MrfErRegs *pEr, int enable)
{
  if (enable)
    pEr->Control |= be32_to_cpu(1 << C_EVR_CTRL_EVENT_FWD_ENA);
  else
    pEr->Control &= be32_to_cpu(~(1 << C_EVR_CTRL_EVENT_FWD_ENA));

  return EvrGetEventForwarding(pEr);
}

int EvrGetEventForwarding(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->Control & be32_to_cpu(1 << C_EVR_CTRL_EVENT_FWD_ENA));
}

RESULT EvrSetLedEvent(volatile struct MrfErRegs *pEr, int ram, int code, int enable)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code);

  if (!enable)
    pEr->MapRam[ram][code].IntEvent &= be32_to_cpu(~(1 << C_EVR_MAP_LED_EVENT));
  if (enable)
    pEr->MapRam[ram][code].IntEvent |= be32_to_cpu(1 << C_EVR_MAP_LED_EVENT);

  return 0;
}

RESULT EvrSetSeconds0Event(volatile struct MrfErRegs *pEr, int ram, int code, int enable)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code);

  if (!enable)
    pEr->MapRam[ram][code].IntEvent &= be32_to_cpu(~(1 << C_EVR_MAP_SECONDS_0));
  if (enable)
    pEr->MapRam[ram][code].IntEvent |= be32_to_cpu(1 << C_EVR_MAP_SECONDS_0);

  return 0;
}

RESULT EvrSetSeconds1Event(volatile struct MrfErRegs *pEr, int ram, int code, int enable)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code);

  if (!enable)
    pEr->MapRam[ram][code].IntEvent &= be32_to_cpu(~(1 << C_EVR_MAP_SECONDS_1));
  if (enable)
    pEr->MapRam[ram][code].IntEvent |= be32_to_cpu(1 << C_EVR_MAP_SECONDS_1);

  return 0;
}

RESULT EvrSetTimestampResetEvent(volatile struct MrfErRegs *pEr, int ram, int code, int enable)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code);

  if (!enable)
    pEr->MapRam[ram][code].IntEvent &= be32_to_cpu(~(1 << C_EVR_MAP_TIMESTAMP_RESET));
  if (enable)
    pEr->MapRam[ram][code].IntEvent |= be32_to_cpu(1 << C_EVR_MAP_TIMESTAMP_RESET);

  return 0;
}

RESULT EvrSetTimestampClockEvent(volatile struct MrfErRegs *pEr, int ram, int code, int enable)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code);

  if (!enable)
    pEr->MapRam[ram][code].IntEvent &= be32_to_cpu(~(1 << C_EVR_MAP_TIMESTAMP_CLK));
  if (enable)
    pEr->MapRam[ram][code].IntEvent |= be32_to_cpu(1 << C_EVR_MAP_TIMESTAMP_CLK);

  return 0;
}

int EvrSetFIFOEvent(volatile struct MrfErRegs *pEr, int ram, int code, int enable)
{
  if (ram < 0 || ram >= EVR_MAPRAMS)
    return -1;

  if (code <= 0 || code > EVR_MAX_EVENT_CODE)
    return -1;

  if (!enable)
    pEr->MapRam[ram][code].IntEvent &= be32_to_cpu(~(1 << C_EVR_MAP_SAVE_EVENT));
  if (enable)
    pEr->MapRam[ram][code].IntEvent |= be32_to_cpu(1 << C_EVR_MAP_SAVE_EVENT);

  return 0;
}

int EvrSetLatchEvent(volatile struct MrfErRegs *pEr, int ram, int code, int enable)
{
  if (ram < 0 || ram >= EVR_MAPRAMS)
    return -1;

  if (code <= 0 || code > EVR_MAX_EVENT_CODE)
    return -1;

  if (!enable)
    pEr->MapRam[ram][code].IntEvent &= be32_to_cpu(~(1 << C_EVR_MAP_LATCH_TIMESTAMP));
  if (enable)
    pEr->MapRam[ram][code].IntEvent |= be32_to_cpu(1 << C_EVR_MAP_LATCH_TIMESTAMP);

  return 0;
}

int EvrSetLogEvent(volatile struct MrfErRegs *pEr, int ram, int code, int enable)
{
  if (ram < 0 || ram >= EVR_MAPRAMS)
    return -1;

  if (code <= 0 || code > EVR_MAX_EVENT_CODE)
    return -1;

  if (!enable)
    pEr->MapRam[ram][code].IntEvent &= be32_to_cpu(~(1 << C_EVR_MAP_LOG_EVENT));
  if (enable)
    pEr->MapRam[ram][code].IntEvent |= be32_to_cpu(1 << C_EVR_MAP_LOG_EVENT);

  return 0;
}

int EvrSetLogStopEvent(volatile struct MrfErRegs *pEr, int ram, int code, int enable)
{
  if (ram < 0 || ram >= EVR_MAPRAMS)
    return -1;

  if (code <= 0 || code > EVR_MAX_EVENT_CODE)
    return -1;

  if (!enable)
    pEr->MapRam[ram][code].IntEvent &= be32_to_cpu(~(1 << C_EVR_MAP_STOP_LOG));
  if (enable)
    pEr->MapRam[ram][code].IntEvent |= be32_to_cpu(1 << C_EVR_MAP_STOP_LOG);

  return 0;
}

int EvrClearFIFO(volatile struct MrfErRegs *pEr)
{
  int ctrl;

  ctrl = be32_to_cpu(pEr->Control);
  ctrl |= (1 << C_EVR_CTRL_RESET_EVENTFIFO);
  pEr->Control = be32_to_cpu(ctrl);

  return be32_to_cpu(pEr->Control);
}

int EvrGetFIFOEvent(volatile struct MrfErRegs *pEr, struct FIFOEvent *fe)
{
  int stat;

  stat = be32_to_cpu(pEr->IrqFlag);
  if (stat & (1 << C_EVR_IRQFLAG_EVENT))
    {
      fe->EventCode = be32_to_cpu(pEr->FIFOEvent);
      fe->TimestampHigh = be32_to_cpu(pEr->FIFOSeconds);
      fe->TimestampLow = be32_to_cpu(pEr->FIFOTimestamp);
      return 0;
    }
  else
    return -1;
}

int EvrEnableLog(volatile struct MrfErRegs *pEr, int enable)
{
  if (enable)
    pEr->Control |= be32_to_cpu(1 << C_EVR_CTRL_LOG_ENABLE);
  else
    pEr->Control |= be32_to_cpu(1 << C_EVR_CTRL_LOG_DISABLE);

  return EvrGetLogState(pEr);
}

int EvrGetLogState(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->Status & be32_to_cpu(1 << C_EVR_STATUS_LOG_STOPPED));
}

int EvrGetLogStart(volatile struct MrfErRegs *pEr)
{
  int pos;

  pos = be32_to_cpu(pEr->LogStatus);
  if (pos >= 0)
    return 0;
  else
    return (pos & (EVR_LOG_SIZE - 1));
}

int EvrGetLogEntries(volatile struct MrfErRegs *pEr)
{
  int pos;

  pos = be32_to_cpu(pEr->LogStatus);
  if (pos >= 0)
    return pos;
  else
    return EVR_LOG_SIZE;
}

int EvrEnableLogStopEvent(volatile struct MrfErRegs *pEr, int enable)
{
  if (enable)
    pEr->Control |= be32_to_cpu(1 << C_EVR_CTRL_LOG_STOP_EV_EN);
  else
    pEr->Control &= be32_to_cpu(~(1 << C_EVR_CTRL_LOG_STOP_EV_EN));

  return EvrGetLogStopEvent(pEr);
}

int EvrGetLogStopEvent(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->Control & be32_to_cpu(1 << C_EVR_CTRL_LOG_STOP_EV_EN));
}

int EvrDumpFIFO(volatile struct MrfErRegs *pEr)
{
  struct FIFOEvent fe;
  int i;

  do
    {
      i = EvrGetFIFOEvent(pEr, &fe);
      if (!i)
	{
	  printf("FIFO Code %08x, %08x:%08x\n",
		 fe.EventCode, fe.TimestampHigh, fe.TimestampLow);
	}
    }
  while (!i);

  return 0;
}

int EvrClearLog(volatile struct MrfErRegs *pEr)
{
  int ctrl;

  ctrl = be32_to_cpu(pEr->Control);
  ctrl |= (1 << C_EVR_CTRL_LOG_RESET);
  pEr->Control = be32_to_cpu(ctrl);

  return be32_to_cpu(pEr->Control);
}

void EvrDumpLog(volatile struct MrfErRegs *pEr, char *out)
{
  int pos, i;
  char *buf = out;
  _DUMP_AUX_BEGIN(out, buf)

  pos = EvrGetLogStart(pEr);
  i = EvrGetLogEntries(pEr);
  if (i > 512) i = 512;
  for (; i; i--)
    {
      // Eventcode contains some more data than just the event code, but
      // it is not documented what it is. So we ignore it & 0xff
      buf += sprintf(buf, "Log Code %08x, %08x:%08x\n",
	     be32_to_cpu(pEr->Log[pos].EventCode) & 0xff,
	     be32_to_cpu(pEr->Log[pos].TimestampHigh),
	     be32_to_cpu(pEr->Log[pos].TimestampLow));
      pos++;
      pos &= (EVR_LOG_SIZE - 1);
    }

  _DUMP_AUX_END(out, buf)
}

RESULT EvrClearPulseMap(volatile struct MrfErRegs *pEr, int ram, int code, int trig,
		     int set, int clear)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code)

  if (trig >= 0 && trig < EVR_MAX_PULSES)
    pEr->MapRam[ram][code].PulseTrigger &= be32_to_cpu(~(1 << trig));
  if (set >= 0 && set < EVR_MAX_PULSES)
    pEr->MapRam[ram][code].PulseSet &= be32_to_cpu(~(1 << set));
  if (clear >= 0 && clear < EVR_MAX_PULSES)
    pEr->MapRam[ram][code].PulseClear &= be32_to_cpu(~(1 << clear));

  return 0;
}

RESULT EvrSetPulseParams(volatile struct MrfErRegs *pEr, int pulse, unsigned int presc,
		      unsigned int delay, unsigned int width)
{
  _CHECK_PULSE_RANGE(pulse)

  pEr->Pulse[pulse].Prescaler = be32_to_cpu(presc);
  pEr->Pulse[pulse].Delay = be32_to_cpu(delay);
  pEr->Pulse[pulse].Width = be32_to_cpu(width);

  return 0;
}

void EvrDumpPulses(volatile struct MrfErRegs *pEr, int pulses, char *out)
{
  int i, control;
  char * buf = out;
  _DUMP_AUX_BEGIN(out, buf)

  for (i = 0; i < pulses; i++)
    {
      buf += sprintf(buf, "Pulse %02x Presc %08x Delay %08x Width %08x", i,
		   be32_to_cpu(pEr->Pulse[i].Prescaler),
		   be32_to_cpu(pEr->Pulse[i].Delay),
		   be32_to_cpu(pEr->Pulse[i].Width));
      control = be32_to_cpu(pEr->Pulse[i].Control);
      buf += sprintf(buf, " Output %d", control & (1 << C_EVR_PULSE_OUT) ? 1 : 0);
      if (control & (1 << C_EVR_PULSE_POLARITY))
	buf += sprintf(buf, " NEG");
      if (control & (1 << C_EVR_PULSE_MAP_RESET_ENA))
	buf += sprintf(buf, " MAPRES");
      if (control & (1 << C_EVR_PULSE_MAP_SET_ENA))
	buf += sprintf(buf, " MAPSET");
      if (control & (1 << C_EVR_PULSE_MAP_TRIG_ENA))
	buf += sprintf(buf, " MAPTRIG");
      if (control & (1 << C_EVR_PULSE_ENA))
	buf += sprintf(buf, " ENA");
      buf += sprintf(buf, "\n");
    }

    //return buf - out;
    _DUMP_AUX_END(out, buf)
}

int EvrSetPulseProperties(volatile struct MrfErRegs *pEr, int pulse, int polarity,
			  int map_reset_ena, int map_set_ena, int map_trigger_ena,
			  int enable)
{
  int result;

  _CHECK_PULSE_RANGE(pulse)

  result = be32_to_cpu(pEr->Pulse[pulse].Control);

  /* 0 clears, 1 sets, others don't change */
  if (polarity == 0)
    result &= ~(1 << C_EVR_PULSE_POLARITY);
  if (polarity == 1)
    result |= (1 << C_EVR_PULSE_POLARITY);

  if (map_reset_ena == 0)
    result &= ~(1 << C_EVR_PULSE_MAP_RESET_ENA);
  if (map_reset_ena == 1)
    result |= (1 << C_EVR_PULSE_MAP_RESET_ENA);

  if (map_set_ena == 0)
    result &= ~(1 << C_EVR_PULSE_MAP_SET_ENA);
  if (map_set_ena == 1)
    result |= (1 << C_EVR_PULSE_MAP_SET_ENA);

  if (map_trigger_ena == 0)
    result &= ~(1 << C_EVR_PULSE_MAP_TRIG_ENA);
  if (map_trigger_ena == 1)
    result |= (1 << C_EVR_PULSE_MAP_TRIG_ENA);

  if (enable == 0)
    result &= ~(1 << C_EVR_PULSE_ENA);
  if (enable == 1)
    result |= (1 << C_EVR_PULSE_ENA);

#ifdef DEBUG
  DEBUG_PRINTF("Pulse[%d].Control %08x\n", pulse, result);
#endif

  pEr->Pulse[pulse].Control = be32_to_cpu(result);

  return 0;
}

RESULT EvrSetUnivOutMap(volatile struct MrfErRegs *pEr, int output, int map)
{

  _CHECK_UNIVOUT_MAP_RANGE(output)

  pEr->UnivOutMap[output] = be16_to_cpu(map);

  return 0;
}

void EvrDumpUnivOutMap(volatile struct MrfErRegs *pEr, int outputs, char* out)
{
  int i;
  char *buf = out;
  _DUMP_AUX_BEGIN(out, buf)

  for (i = 0; i < outputs; i++)
    buf += sprintf(buf, "UnivOut[%d] %02x\n", i, be16_to_cpu(pEr->UnivOutMap[i]));

  //return buf - out;
  _DUMP_AUX_END(out, buf)
}

int EvrSetFPOutMap(volatile struct MrfErRegs *pEr, int output, int map)
{
  if (output < 0 || output >= EVR_MAX_FPOUT_MAP)
    return RERR_FPOUT_MAP_RANGE;

  pEr->FPOutMap[output] = be16_to_cpu(map);
  return 0;
}

void EvrDumpFPOutMap(volatile struct MrfErRegs *pEr, int outputs)
{
  int i;

  for (i = 0; i < outputs; i++)
    DEBUG_PRINTF("FPOut[%d] %02x\n", i, be16_to_cpu(pEr->FPOutMap[i]));
}

int EvrSetTBOutMap(volatile struct MrfErRegs *pEr, int output, int map)
{
  if (output < 0 || output >= EVR_MAX_TBOUT_MAP)
    return -1;

  pEr->TBOutMap[output] = be16_to_cpu(map);
  return 0;
}

void EvrDumpTBOutMap(volatile struct MrfErRegs *pEr, int outputs)
{
  int i;

  for (i = 0; i < outputs; i++)
    DEBUG_PRINTF("TBOut[%d] %02x\n", i, be16_to_cpu(pEr->TBOutMap[i]));
}

void EvrIrqAssignHandler(volatile struct MrfErRegs *pEr, int fd,
			 void (*handler)(int))
{
  struct sigaction act;
  int oflags;
  int result;

  act.sa_handler = handler;
  sigemptyset(&act.sa_mask);
  act.sa_flags = 0;

  result = sigaction(SIGIO, &act, NULL);
  printf("sigaction returned %d\n", result);
  fcntl(fd, F_SETOWN, getpid());
  oflags = fcntl(fd, F_GETFL);
  fcntl(fd, F_SETFL, oflags | FASYNC);
  /* Now enable handler */
  EvrIrqHandled(fd);
}

int EvrIrqEnable(volatile struct MrfErRegs *pEr, int mask)
{
  pEr->IrqEnable = be32_to_cpu(mask);
  return be32_to_cpu(pEr->IrqEnable);
}

int EvrGetIrqFlags(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->IrqFlag);
}

int EvrClearIrqFlags(volatile struct MrfErRegs *pEr, int mask)
{
  pEr->IrqFlag = be32_to_cpu(mask);
  return be32_to_cpu(pEr->IrqFlag);
}

void EvrIrqHandled(int fd)
{
  ioctl(fd, EV_IOCIRQEN);
}

int EvrSetPulseIrqMap(volatile struct MrfErRegs *pEr, int map)
{
  pEr->PulseIrqMap = be32_to_cpu(map);
  return 0;
}

void EvrClearDiagCounters(volatile struct MrfErRegs *pEr)
{
  pEr->DiagReset = 0xffffffff;
  pEr->DiagReset = 0x0;
}

void EvrEnableDiagCounters(volatile struct MrfErRegs *pEr, int enable)
{
  if (enable)
    pEr->DiagCE = 0xffffffff;
  else
    pEr->DiagCE = 0;
}

u32 EvrGetDiagCounter(volatile struct MrfErRegs *pEr, int idx)
{
  return be32_to_cpu(pEr->DiagCounter[idx]);
}

int EvrUnivDlyEnable(volatile struct MrfErRegs *pEr, int dlymod, int enable)
{
  u32 gpio;
  int sh = 0;

  switch (dlymod)
    {
    case 0:
      sh = 0;
      break;
    case 1:
      sh = 4;
      break;
    default:
      return -1;
    }

  /* Setup outputs for both slots */
  pEr->GPIODir = be32_to_cpu(((EVR_UNIV_DLY_DIN | EVR_UNIV_DLY_SCLK |
	    EVR_UNIV_DLY_LCLK | EVR_UNIV_DLY_DIS) |
	   ((EVR_UNIV_DLY_DIN | EVR_UNIV_DLY_SCLK |
	     EVR_UNIV_DLY_LCLK | EVR_UNIV_DLY_DIS) << 4)));
  gpio = be32_to_cpu(pEr->GPIOOut) & ~(EVR_UNIV_DLY_DIS << sh);
  if (!enable)
    gpio |= (EVR_UNIV_DLY_DIS << sh);
  pEr->GPIOOut = be32_to_cpu(gpio);

  return 0;
}

int EvrUnivDlySetDelay(volatile struct MrfErRegs *pEr, int dlymod, int dly0, int dly1)
{
  u32 gpio;
  int sh = 0;
  int sd;
  int sr, i, din, sclk, lclk, dbit;

  switch (dlymod)
    {
    case 0:
      sh = 0;
      break;
    case 1:
      sh = 4;
      break;
    default:
      return -1;
    }

  din = EVR_UNIV_DLY_DIN << sh;
  sclk = EVR_UNIV_DLY_SCLK << sh;
  lclk = EVR_UNIV_DLY_LCLK << sh;

  gpio = be32_to_cpu(pEr->GPIOOut) & ~((EVR_UNIV_DLY_DIN | EVR_UNIV_DLY_SCLK |
					EVR_UNIV_DLY_LCLK) |
				       ((EVR_UNIV_DLY_DIN | EVR_UNIV_DLY_SCLK |
					 EVR_UNIV_DLY_LCLK) << 4));
  /* Limit delay values */
  dly0 &= 0x03ff;
  dly1 &= 0x03ff;

  /* We have to shift in the bits in following order:
     DA7, DA6, DA5, DA4, DA3, DA2, DA1, DA0,
     DB3, DB2, DB1, DB0, LENA, 0, DA9, DA8,
     LENB, 0, DB9, DB8, DB7, DB6, DB5, DB4 */

  sd = ((dly1 & 0x0ff) << 16) |
    ((dly0 & 0x00f) << 12) | (dly1 & 0x300) |
    (dly0 >> 4);

  sr = sd;
  for (i = 24; i; i--)
    {
      dbit = 0;
      if (sr & 0x00800000)
	dbit = din;
      pEr->GPIOOut = be32_to_cpu(gpio | dbit);
      pEr->GPIOOut = be32_to_cpu(gpio | dbit | sclk);
      pEr->GPIOOut = be32_to_cpu(gpio | dbit);
      sr <<= 1;
    }

  pEr->GPIOOut = be32_to_cpu(gpio | lclk);
  pEr->GPIOOut = be32_to_cpu(gpio);

  /* Latch enables active */
  sr = sd | 0x000880;
  for (i = 24; i; i--)
    {
      dbit = 0;
      if (sr & 0x00800000)
	dbit = din;
      pEr->GPIOOut = be32_to_cpu(gpio | dbit);
      pEr->GPIOOut = be32_to_cpu(gpio | dbit | sclk);
      pEr->GPIOOut = be32_to_cpu(gpio | dbit);
      sr <<= 1;
    }

  pEr->GPIOOut = be32_to_cpu(gpio | lclk);
  pEr->GPIOOut = be32_to_cpu(gpio);

  sr = sd;
  for (i = 24; i; i--)
    {
      dbit = 0;
      if (sr & 0x00800000)
	dbit = din;
      pEr->GPIOOut = be32_to_cpu(gpio | dbit);
      pEr->GPIOOut = be32_to_cpu(gpio | dbit | sclk);
      pEr->GPIOOut = be32_to_cpu(gpio | dbit);
      sr <<= 1;
    }

  pEr->GPIOOut = be32_to_cpu(gpio | lclk);
  pEr->GPIOOut = be32_to_cpu(gpio);

  return 0;
}

void EvrDumpHex(volatile struct MrfErRegs *pEr)
{
  u32 *p = (u32 *) pEr;
  int i,j;

  for (i = 0; i < 0x600; i += 0x20)
    {
      printf("%08x: ", i);
      for (j = 0; j < 8; j++)
	printf("%08x ", be32_to_cpu(*p++));
      printf("\n");
    }
}

int EvrSetFracDiv(volatile struct MrfErRegs *pEr, int fracdiv)
{
  return pEr->FracDiv = be32_to_cpu(fracdiv);
}

int EvrGetFracDiv(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->FracDiv);
}

int EvrSetDBufMode(volatile struct MrfErRegs *pEr, int enable)
{
  if (enable)
    pEr->DataBufControl = be32_to_cpu(1 << C_EVR_DATABUF_MODE);
  else
    pEr->DataBufControl = 0;

  return EvrGetDBufStatus(pEr);
}

int EvrGetDBufStatus(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->DataBufControl);
}

int EvrReceiveDBuf(volatile struct MrfErRegs *pEr, int enable)
{
  if (enable)
    pEr->DataBufControl |= be32_to_cpu(1 << C_EVR_DATABUF_LOAD);
  else
    pEr->DataBufControl |= be32_to_cpu(1 << C_EVR_DATABUF_STOP);

  return EvrGetDBufStatus(pEr);
}

int EvrGetDBuf(volatile struct MrfErRegs *pEr, char *dbuf, int size)
{
  int stat, rxsize;

  stat = EvrGetDBufStatus(pEr);
  /* Check that DBUF mode enabled */
  if (!(stat & (1 << C_EVR_DATABUF_MODE)))
    return -1;
  /* Check that transfer is completed */
  if (!(stat & (1 << C_EVR_DATABUF_RXREADY)))
    return -1;

  rxsize = stat & (EVR_MAX_BUFFER-1);

  if (size < rxsize)
    return -1;

  memcpy((void *) dbuf, (void *) &pEr->Databuf[0], rxsize);

  if (stat & (1 << C_EVR_DATABUF_CHECKSUM))
    return -1;

  return rxsize;
}

int EvrSetTimestampDivider(volatile struct MrfErRegs *pEr, int div)
{
  pEr->EvCntPresc = be32_to_cpu(div);

  return be32_to_cpu(pEr->EvCntPresc);
}

int EvrGetTimestampCounter(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->TimestampEventCounter);
}

int EvrGetSecondsCounter(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->SecondsCounter);
}

int EvrGetTimestampLatch(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->TimestampLatch);
}

int EvrGetSecondsLatch(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->SecondsLatch);
}

int EvrSetTimestampDBus(volatile struct MrfErRegs *pEr, int enable)
{
  int ctrl;

  ctrl = be32_to_cpu(pEr->Control);
  if (enable)
    ctrl |= (1 << C_EVR_CTRL_TS_CLOCK_DBUS);
  else
    ctrl &= ~(1 << C_EVR_CTRL_TS_CLOCK_DBUS);
  pEr->Control = be32_to_cpu(ctrl);

  return be32_to_cpu(pEr->Control);
}

// int EvrSetPrescaler(volatile struct MrfErRegs *pEr, int presc, int div)
// {
//   if (presc >= 0 && presc < EVR_MAX_PRESCALERS)
//     {
//       pEr->Prescaler[presc] = be32_to_cpu(div);
//
//       return be32_to_cpu(pEr->Prescaler[presc]);
//     }
//   return -1;
// }

int EvrSetExtEvent(volatile struct MrfErRegs *pEr, int ttlin, int code, int edge_enable, int level_enable)
{
  int fpctrl;

  if (ttlin < 0 || ttlin > EVR_MAX_FPIN_MAP)
    return -1;

  fpctrl = be32_to_cpu(pEr->FPInMap[ttlin]);
  if (code >= 0 && code <= EVR_MAX_EVENT_CODE)
    {
      fpctrl &= ~(EVR_MAX_EVENT_CODE << C_EVR_FPIN_EXTEVENT_BASE);
      fpctrl |= code << C_EVR_FPIN_EXTEVENT_BASE;
    }
  fpctrl &= ~(1 << C_EVR_FPIN_EXT_ENABLE);
  if (edge_enable)
    fpctrl |= (1 << C_EVR_FPIN_EXT_ENABLE);

  fpctrl &= ~(1 << C_EVR_FPIN_EXTLEV_ENABLE);
  if (level_enable)
    fpctrl |= (1 << C_EVR_FPIN_EXTLEV_ENABLE);

  pEr->FPInMap[ttlin] = be32_to_cpu(fpctrl);
  if (pEr->FPInMap[ttlin] == be32_to_cpu(fpctrl))
    return 0;
  return -1;
}

int EvrSetBackEvent(volatile struct MrfErRegs *pEr, int ttlin, int code, int edge_enable, int level_enable)
{
  int fpctrl;

  if (ttlin < 0 || ttlin > EVR_MAX_FPIN_MAP)
    return -1;

  fpctrl = be32_to_cpu(pEr->FPInMap[ttlin]);
  if (code >= 0 && code <= EVR_MAX_EVENT_CODE)
    {
      fpctrl &= ~(EVR_MAX_EVENT_CODE << C_EVR_FPIN_BACKEVENT_BASE);
      fpctrl |= code << C_EVR_FPIN_BACKEVENT_BASE;
    }
  fpctrl &= ~(1 << C_EVR_FPIN_BACKEV_ENABLE);
  if (edge_enable)
    fpctrl |= (1 << C_EVR_FPIN_BACKEV_ENABLE);

  fpctrl &= ~(1 << C_EVR_FPIN_BACKLEV_ENABLE);
  if (level_enable)
    fpctrl |= (1 << C_EVR_FPIN_BACKLEV_ENABLE);

  pEr->FPInMap[ttlin] = be32_to_cpu(fpctrl);
  if (pEr->FPInMap[ttlin] == be32_to_cpu(fpctrl))
    return 0;
  return -1;
}

int EvrSetExtEdgeSensitivity(volatile struct MrfErRegs *pEr, int ttlin, int edge)
{
  int fpctrl;

  _CHECK_TTLIN_RANGE(ttlin)

  fpctrl = be32_to_cpu(pEr->FPInMap[ttlin]);
  fpctrl &= ~(1 << C_EVR_FPIN_EXT_EDGE);
  if (edge)
    fpctrl |= (1 << C_EVR_FPIN_EXT_EDGE);

  pEr->FPInMap[ttlin] = be32_to_cpu(fpctrl);
  if (pEr->FPInMap[ttlin] == be32_to_cpu(fpctrl))
    return 0;
  return -1;
}

int EvrSetExtLevelSensitivity(volatile struct MrfErRegs *pEr, int ttlin, int level)
{
  int fpctrl;

  _CHECK_TTLIN_RANGE(ttlin)

  fpctrl = be32_to_cpu(pEr->FPInMap[ttlin]);
  fpctrl &= ~(1 << C_EVR_FPIN_EXTLEV_ACT);
  if (level)
    fpctrl |= (1 << C_EVR_FPIN_EXTLEV_ACT);

  pEr->FPInMap[ttlin] = be32_to_cpu(fpctrl);
  if (pEr->FPInMap[ttlin] == be32_to_cpu(fpctrl))
    return 0;
  return -1;
}

int EvrSetBackDBus(volatile struct MrfErRegs *pEr, int ttlin, int dbus)
{
  int fpctrl;

  if (ttlin < 0 || ttlin > EVR_MAX_FPIN_MAP)
    return -1;

  if (dbus < 0 || dbus > 255)
    return -1;

  fpctrl = be32_to_cpu(pEr->FPInMap[ttlin]);
  fpctrl &= ~(255 << C_EVR_FPIN_BACKDBUS_BASE);
  fpctrl |= dbus << C_EVR_FPIN_BACKDBUS_BASE;

  pEr->FPInMap[ttlin] = be32_to_cpu(fpctrl);
  if (pEr->FPInMap[ttlin] == be32_to_cpu(fpctrl))
    return 0;
  return -1;

}

int EvrSetTxDBufMode(volatile struct MrfErRegs *pEr, int enable)
{
  if (enable)
    pEr->TxDataBufControl = be32_to_cpu(1 << C_EVR_TXDATABUF_MODE);
  else
    pEr->TxDataBufControl = 0;

  return EvrGetTxDBufStatus(pEr);
}

int EvrGetTxDBufStatus(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->TxDataBufControl);
}

int EvrSendTxDBuf(volatile struct MrfErRegs *pEr, char *dbuf, int size)
{
  int stat;

  stat = EvrGetTxDBufStatus(pEr);
  //  printf("EvgSendDBuf: stat %08x\n", stat);
  /* Check that DBUF mode enabled */
  if (!(stat & (1 << C_EVR_TXDATABUF_MODE)))
    return -1;
  /* Check that previous transfer is completed */
  if (!(stat & (1 << C_EVR_TXDATABUF_COMPLETE)))
    return -1;
  /* Check that size is valid */
  if (size & 3 || size > EVR_MAX_BUFFER || size < 4)
    return -1;

  memcpy((void *) &pEr->TxDatabuf[0], (void *) dbuf, size);

  /* Enable and set size */
  stat &= ~((EVR_MAX_BUFFER-1) | (1 << C_EVR_TXDATABUF_TRIGGER));
  stat |= (1 << C_EVR_TXDATABUF_ENA) | size;
  //  printf("EvgSendDBuf: stat %08x\n", stat);
  pEr->TxDataBufControl = be32_to_cpu(stat);
  //  printf("EvgSendDBuf: stat %08x\n", be32_to_cpu(pEr->DataBufControl));

  /* Trigger */
  pEr->TxDataBufControl = be32_to_cpu(stat | (1 << C_EVR_TXDATABUF_TRIGGER));
  //  printf("EvgSendDBuf: stat %08x\n", be32_to_cpu(pEr->DataBufControl));

  return size;
}

int EvrGetFormFactor(volatile struct MrfErRegs *pEr)
{
  int stat;

  stat = be32_to_cpu(pEr->FPGAVersion);
  return ((stat >> 24) & 0x0f);
}

int EvrSetFineDelay(volatile struct MrfErRegs *pEr, int channel, int delay)
{
  if (channel < 0 || channel >= EVR_MAX_CML_OUTPUTS)
    return -1;

  pEr->FineDelay[channel] = be32_to_cpu(delay);
  return be32_to_cpu(pEr->FineDelay[channel]);
}

int EvrCMLEnable(volatile struct MrfErRegs *pEr, int channel, int state)
{
  int ctrl;

  if (channel < 0 || channel >= EVR_MAX_CML_OUTPUTS)
    return -1;

  ctrl = be16_to_cpu(pEr->CML[channel].Control);
  printf("Control %08x\n", ctrl);
  if (state)
    {
      ctrl &= ~((1 << C_EVR_CMLCTRL_RESET) | (1 << C_EVR_CMLCTRL_POWERDOWN));
      ctrl |= (1 << C_EVR_CMLCTRL_ENABLE);
    }
  else
    {
      ctrl |= (1 << C_EVR_CMLCTRL_RESET) | (1 << C_EVR_CMLCTRL_POWERDOWN);
      ctrl &= ~(1 << C_EVR_CMLCTRL_ENABLE);
    }


  printf("Control %08x\n", ctrl);
  pEr->CML[channel].Control = be16_to_cpu(ctrl);
  return be16_to_cpu(pEr->CML[channel].Control);
}























void EvrSetVal32(volatile struct MrfErRegs *pEr, unsigned int pos, unsigned int val)
{
    volatile char * p = (volatile char *)pEr;
    *((u32*)(p + pos)) = be32_to_cpu(val);
}

unsigned int EvrGetVal32(volatile struct MrfErRegs *pEr, unsigned int pos)
{
    volatile char * p = (volatile char *)pEr;
    return be32_to_cpu(*((u32*)(p + pos)));
}

void EvrSetVal16(volatile struct MrfErRegs *pEr, unsigned int pos, unsigned int val)
{
    volatile char * p = (volatile char *)pEr;
    *((u16*)(p + pos)) = be16_to_cpu((u16)(val));
}

unsigned int EvrGetVal16(volatile struct MrfErRegs *pEr, unsigned int pos)
{
    volatile char * p = (volatile char *)pEr;
    return be16_to_cpu(*((u16*)(p + pos)));
}

void EvrSetBit(volatile struct MrfErRegs *pEr, unsigned int pos, unsigned int bit, unsigned int val)
{
	volatile char * p = (volatile char *)pEr;
	u32 v;
	v = be32_to_cpu(*((u32*)(p + pos)));
	if (val)
		v |= (1 << bit);
	else
		v &= ~(1 << bit);
	*((u32*)(p + pos)) = be32_to_cpu(v);
}




RESULT EvrEnablePulseIrq(volatile struct MrfErRegs *pEr, int pulse, int enable)
{
	int pim;

	_CHECK_PULSE_RANGE(pulse)

	pEr -> IrqEnable |= be32_to_cpu(C_EVR_IRQFLAG_PULSE);
	pim = be32_to_cpu(pEr -> PulseIrqMap);
	if (enable)
		pim |= (1 << pulse);
	else
		pim &= ~(1 << pulse);
	pEr -> PulseIrqMap = be32_to_cpu(pim);

	return 0;
}


void EvrDumpClockControl(volatile struct MrfErRegs *pEr, char *out)
{
	//char out[500];
	char* buf = out;
	u32 cc;
	_DUMP_AUX_BEGIN(out, buf)

	cc = be32_to_cpu(pEr->ClockControl);
	buf += sprintf(buf, "[0x%x]ClockControl: 0x%08lx\n", offsetof(struct MrfErRegs,ClockControl), (unsigned long)cc);

	buf += sprintf(buf, "  USE_RXRECCLK(%d)\n", (cc & (1 << C_EVR_CLKCTRL_USE_RXRECCLK))?1:0 );
	buf += sprintf(buf, "  CGLOCK(%d)\n", (cc & (1 << C_EVR_CLKCTRL_CGLOCK))?1:0 );

	buf += sprintf(buf, "  RECDCM:");
	buf += sprintf(buf, " RUN(%d)", (cc & (1 << C_EVR_CLKCTRL_RECDCM_RUN))?1:0 );
	buf += sprintf(buf, " INITD(%d)", (cc & (1 << C_EVR_CLKCTRL_RECDCM_INITD))?1:0 );
	buf += sprintf(buf, " PSDONE(%d)", (cc & (1 << C_EVR_CLKCTRL_RECDCM_PSDONE))?1:0 );
	buf += sprintf(buf, " PSDEC(%d)", (cc & (1 << C_EVR_CLKCTRL_RECDCM_PSDEC))?1:0 );
	buf += sprintf(buf, " PSINC(%d)", (cc & (1 << C_EVR_CLKCTRL_RECDCM_PSINC))?1:0 );
	buf += sprintf(buf, " RESET(%d)", (cc & (1 << C_EVR_CLKCTRL_RECDCM_RESET))?1:0 );

	buf += sprintf(buf, "\n  EVDCM:");
	buf += sprintf(buf, " RUN(%d)", (cc & (1 << C_EVR_CLKCTRL_EVDCM_STOPPED))?1:0 );
	buf += sprintf(buf, " INITD(%d)", (cc & (1 << C_EVR_CLKCTRL_EVDCM_LOCKED))?1:0 );
	buf += sprintf(buf, " PSDONE(%d)", (cc & (1 << C_EVR_CLKCTRL_EVDCM_PSDONE))?1:0 );
	buf += sprintf(buf, " PSDEC(%d)", (cc & (1 << C_EVR_CLKCTRL_EVDCM_PSDEC))?1:0 );
	buf += sprintf(buf, " PSINC(%d)", (cc & (1 << C_EVR_CLKCTRL_EVDCM_PSINC))?1:0 );
	buf += sprintf(buf, " SRUN(%d)", (cc & (1 << C_EVR_CLKCTRL_EVDCM_SRUN))?1:0 );
	buf += sprintf(buf, " SRES(%d)", (cc & (1 << C_EVR_CLKCTRL_EVDCM_SRES))?1:0 );
	buf += sprintf(buf, " RES(%d)", (cc & (1 << C_EVR_CLKCTRL_EVDCM_RES))?1:0 );

	buf += sprintf(buf, "\n");

	_DUMP_AUX_END(out, buf)
	//printf(out);
	//return buf - out;
}


int EvrGetInternalFrac(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->FracDiv);
}

int EvrSetInternalFrac(volatile struct MrfErRegs *pEr, int fracdiv)
{
  pEr->FracDiv = be32_to_cpu(fracdiv);
  return 0;
}



int EvrPCIStatus(volatile struct MrfErRegs *pEr)
{
  u32 val = 0;
  return pEr->FPGAVersion != ~val;
}


RESULT EvrGetPrescaler(volatile struct MrfErRegs *pEr, int prescid, unsigned int* presc)
{
	_CHECK_PRESCALER_RANGE(prescid)

	*presc = be32_to_cpu(pEr->Prescaler[prescid]);
	return 0;
}

RESULT EvrSetPrescaler(volatile struct MrfErRegs *pEr, int prescid, unsigned int presc)
{
	_CHECK_PRESCALER_RANGE(prescid)

	pEr->Prescaler[prescid] = be32_to_cpu(presc);
	return 0;
}

RESULT EvrGetEnableLog(volatile struct MrfErRegs *pEr, int *enable)
{
   ///@todo Does it really work? Or else I should be using EvrGetLogState() ?
  if (pEr->Control |= be32_to_cpu(1 << C_EVR_CTRL_LOG_ENABLE))
    *enable = 1;
  else
    *enable = 0;

  return 0;
}

RESULT EvrGetLogEventEnabled(volatile struct MrfErRegs *pEr, int ram, int code, int* enable)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code)

  *enable = (pEr->MapRam[ram][code].IntEvent & be32_to_cpu(1 << C_EVR_MAP_LOG_EVENT)) ? 1 : 0;

  return 0;
}

RESULT EvrGetLogStopEventEnabled(volatile struct MrfErRegs *pEr, int ram, int code, int* enable)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code)

  *enable = (pEr->MapRam[ram][code].IntEvent & be32_to_cpu(1 << C_EVR_MAP_STOP_LOG)) ? 1 : 0;

  return 0;
}

RESULT EvrGetTimestampDivider(volatile struct MrfErRegs *pEr, int *div)
{
  *div = be32_to_cpu(pEr->EvCntPresc);

  return 0;
}



void EvrSetRxDBufModeEnable(volatile struct MrfErRegs *pEr, int enable)
{
	EvrSetDBufMode(pEr, enable);
}

void EvrSetTxDBufModeEnable(volatile struct MrfErRegs *pEr, int enable)
{
	EvrSetTxDBufMode(pEr, enable);
}

unsigned EvrGetFirmwareVersion(volatile struct MrfErRegs *pEr)
{
	return be32_to_cpu(pEr->FPGAVersion);
}

RESULT EvrCloneRam(volatile struct MrfErRegs *pEr, int from, int to)
{
  unsigned code;

  _CHECK_RAM_RANGE(from) ;
  _CHECK_RAM_RANGE(to) ;
  if (from == to)
    return RERR_RAM_RANGE;

  for (code = 0; code <= EVR_MAX_EVENT_CODE; code++) {
      pEr->MapRam[to][code].IntEvent         = pEr->MapRam[from][code].IntEvent;
      pEr->MapRam[to][code].PulseTrigger     = pEr->MapRam[from][code].PulseTrigger;
      pEr->MapRam[to][code].PulseSet         = pEr->MapRam[from][code].PulseSet;
      pEr->MapRam[to][code].PulseClear       = pEr->MapRam[from][code].PulseClear;
   }
  return 0;
}

int EvrGetSerialNumber(int fd, char* sn)
{
  return ioctl(fd, EV_IOCREAD_SERIAL, sn);
}

int EvrGetMapRamEnable(volatile struct MrfErRegs *pEr, int ram)
{
//   if (ram < 0 || ram > 1)
//     return -1;
	u32 c;
	u32 r;
	c = be32_to_cpu(pEr->Control);

	r = (c & (1 << C_EVR_CTRL_MAP_RAM_ENABLE)) ? 1 : 0;
	if (ram == 0)
		r = r && ((~c) & (1 << C_EVR_CTRL_MAP_RAM_SELECT));
	if (ram == 1)
		r = r && (c & (1 << C_EVR_CTRL_MAP_RAM_SELECT));

	return r;
}

RESULT EvrGetForwardEvent(volatile struct MrfErRegs *pEr, int ram, int code, int* enable)
{
  if (ram < 0 || ram >= EVR_MAPRAMS)
    return -1;

  if (code <= 0 || code > EVR_MAX_EVENT_CODE)
    return -1;

  *enable = 0;
  if (pEr->MapRam[ram][code].IntEvent & be32_to_cpu(1 << C_EVR_MAP_FORWARD_EVENT))
    *enable = 1;

  return 0;
}

RESULT EvrSetPulseMapEx(volatile struct MrfErRegs *pEr, int ram, int code, int trig,
		   int set, int clear)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code)

  pEr->MapRam[ram][code].PulseTrigger = be32_to_cpu(trig);
  pEr->MapRam[ram][code].PulseSet = be32_to_cpu(set);
  pEr->MapRam[ram][code].PulseClear = be32_to_cpu(clear);

  return 0;
}

RESULT EvrGetPulseMapEx(volatile struct MrfErRegs *pEr, int ram, int code, int *trig,
		   int *set, int *clear)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code)

  *trig = be32_to_cpu(pEr->MapRam[ram][code].PulseTrigger);
  *set = be32_to_cpu(pEr->MapRam[ram][code].PulseSet);
  *clear = be32_to_cpu(pEr->MapRam[ram][code].PulseClear);

  return 0;
}

RESULT EvrSetPulseMapTrig(volatile struct MrfErRegs *pEr, int ram, int code, int trig)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code);

  pEr->MapRam[ram][code].PulseTrigger = be32_to_cpu(trig);
  return 0;
}

RESULT EvrSetPulseMapSet(volatile struct MrfErRegs *pEr, int ram, int code, int set)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code);

  pEr->MapRam[ram][code].PulseSet = be32_to_cpu(set);
  return 0;
}

RESULT EvrSetPulseMapClear(volatile struct MrfErRegs *pEr, int ram, int code, int clear)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code);

  pEr->MapRam[ram][code].PulseClear = be32_to_cpu(clear);
  return 0;
}

//TODO: Utilitzar aquestes i eliminar GetPulseMap"Ex"(...)
RESULT EvrGetPulseMapTrig(volatile struct MrfErRegs *pEr, int ram, int code, int *trig)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code);

  *trig = be32_to_cpu(pEr->MapRam[ram][code].PulseTrigger);
  return 0;
}

RESULT EvrGetPulseMapSet(volatile struct MrfErRegs *pEr, int ram, int code, int *set)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code);

  *set = be32_to_cpu(pEr->MapRam[ram][code].PulseSet);
  return 0;
}

RESULT EvrGetPulseMapClear(volatile struct MrfErRegs *pEr, int ram, int code, int *clear)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code);

  *clear = be32_to_cpu(pEr->MapRam[ram][code].PulseClear);
  return 0;
}

RESULT EvrGetLedEvent(volatile struct MrfErRegs *pEr, int ram, int code, int* enable)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code)

  *enable = (pEr->MapRam[ram][code].IntEvent & be32_to_cpu(1 << C_EVR_MAP_LED_EVENT)) ? 1 : 0;

  return 0;
}

RESULT EvrGetSeconds0Event(volatile struct MrfErRegs *pEr, int ram, int code, int* enable)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code)

  *enable = (pEr->MapRam[ram][code].IntEvent & be32_to_cpu(1 << C_EVR_MAP_SECONDS_0)) ? 1 : 0;

  return 0;
}

RESULT EvrGetSeconds1Event(volatile struct MrfErRegs *pEr, int ram, int code, int* enable)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code)

  *enable = (pEr->MapRam[ram][code].IntEvent & be32_to_cpu(1 << C_EVR_MAP_SECONDS_1)) ? 1 : 0;

  return 0;
}

RESULT EvrGetTimestampResetEvent(volatile struct MrfErRegs *pEr, int ram, int code, int* enable)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code)

  *enable = (pEr->MapRam[ram][code].IntEvent & be32_to_cpu(1 << C_EVR_MAP_TIMESTAMP_RESET)) ? 1 : 0;

  return 0;
}

RESULT EvrGetTimestampClockEvent(volatile struct MrfErRegs *pEr, int ram, int code, int* enable)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code)

  *enable = (pEr->MapRam[ram][code].IntEvent & be32_to_cpu(1 << C_EVR_MAP_TIMESTAMP_CLK)) ? 1 : 0;

  return 0;
}

RESULT EvrGetFIFOEventEnabled(volatile struct MrfErRegs *pEr, int ram, int code, int* enable)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code)

  *enable = (pEr->MapRam[ram][code].IntEvent & be32_to_cpu(1 << C_EVR_MAP_SAVE_EVENT)) ? 1 : 0;

  return 0;
}

RESULT EvrGetLatchEvent(volatile struct MrfErRegs *pEr, int ram, int code, int* enable)
{
  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code)

  *enable = (pEr->MapRam[ram][code].IntEvent & be32_to_cpu(1 << C_EVR_MAP_LATCH_TIMESTAMP)) ? 1 : 0;

  return 0;
}

//RESULT EvrGetFIFOStopEventEnabled(volatile struct MrfErRegs *pEr, int ram, int code, int* enable)
//{
//  _CHECK_RAM_RANGE(ram) _CHECK_EVENT_RANGE(code)

//  *enable = (pEr->MapRam[ram][code].IntEvent & be32_to_cpu(1 << C_EVR_MAP_STOP_LOG)) ? 1 : 0;

//  return 0;
//}

RESULT EvrGetPulseParams(volatile struct MrfErRegs *pEr, int pulse, unsigned int *presc, unsigned int *delay, unsigned int *width)
{
  _CHECK_PULSE_RANGE(pulse)

  *presc = be32_to_cpu(pEr->Pulse[pulse].Prescaler);
  *delay = be32_to_cpu(pEr->Pulse[pulse].Delay);
  *width = be32_to_cpu(pEr->Pulse[pulse].Width);

   return 0;
}

RESULT EvrGetPulseProperties(volatile struct MrfErRegs *pEr, int pulse, int *polarity,int *map_reset_ena, int *map_set_ena, int *map_trigger_ena,int *enable)
{
  u32 c;

  _CHECK_PULSE_RANGE(pulse)

  c = be32_to_cpu(pEr->Pulse[pulse].Control);

  *polarity = (c & (1 << C_EVR_PULSE_POLARITY))?1:0;
  *map_reset_ena = (c & (1 << C_EVR_PULSE_MAP_RESET_ENA))?1:0;
  *map_set_ena = (c & (1 << C_EVR_PULSE_MAP_SET_ENA))?1:0;
  *map_trigger_ena = (c & (1 << C_EVR_PULSE_MAP_TRIG_ENA))?1:0;
  *enable = (c & (1 << C_EVR_PULSE_ENA))?1:0;

   return 0;
}

RESULT EvrGetUnivOutMap(volatile struct MrfErRegs *pEr, int output, int *map)
{
  _CHECK_UNIVOUT_MAP_RANGE(output)

  *map =  be16_to_cpu(pEr->UnivOutMap[output]);
  return 0;
}

int EvrGetIrqEnable(volatile struct MrfErRegs *pEr)
{
  return be32_to_cpu(pEr->IrqEnable);
}

int EvrGetRxDBufModeEnable(volatile struct MrfErRegs *pEr)
{
  return (pEr->DataBufControl & be32_to_cpu(1 << C_EVR_DATABUF_MODE))?1:0;
}

int EvrGetTxDBufModeEnable(volatile struct MrfErRegs *pEr)
{
  return (pEr->TxDataBufControl & be32_to_cpu(1 << C_EVR_TXDATABUF_MODE))?1:0;
}

RESULT EvrGetExtEvent(volatile struct MrfErRegs *pEr, int ttlin, int *code, int *edge_enable, int *level_enable)
{
  int fpctrl;

  fpctrl = be32_to_cpu(pEr->FPInMap[ttlin]);

  _CHECK_TTLIN_RANGE(ttlin)

  *code = fpctrl >> C_EVR_FPIN_EXTEVENT_BASE;
  *code = *code & EVR_MAX_EVENT_CODE;

  if (fpctrl & (1 << C_EVR_FPIN_EXT_ENABLE))
    *edge_enable = 1;
  else
    *edge_enable = 0;

  if (fpctrl & (1 << C_EVR_FPIN_EXTLEV_ENABLE))
    *level_enable = 1;
  else
    *level_enable = 0;

  return 0;
}

RESULT EvrGetBackEvent(volatile struct MrfErRegs *pEr, int ttlin, int *code, int *edge_enable, int *level_enable)
{
  int fpctrl, aux;

  _CHECK_TTLIN_RANGE(ttlin)

  fpctrl = be32_to_cpu(pEr->FPInMap[ttlin]);

  aux = fpctrl & (EVR_MAX_EVENT_CODE << C_EVR_FPIN_BACKEVENT_BASE);
  *code = aux >> C_EVR_FPIN_BACKEVENT_BASE;

  if( fpctrl & (1 << C_EVR_FPIN_BACKEV_ENABLE) )
    *edge_enable = 1;
  else
    *edge_enable = 0;

  if( fpctrl & (1 << C_EVR_FPIN_BACKLEV_ENABLE) )
    *level_enable = 1;
  else
    *level_enable = 0;

  return 0;
}

RESULT EvrGetExtEdgeSensitivity(volatile struct MrfErRegs *pEr, int ttlin, int *edge)
{
  int fpctrl;

  _CHECK_TTLIN_RANGE(ttlin)

  fpctrl = be32_to_cpu(pEr->FPInMap[ttlin]);

  if ( fpctrl &= (1 << C_EVR_FPIN_EXT_EDGE) )
    *edge=1;
  else
    *edge=0;

  return 0;
}

RESULT EvrGetExtLevelSensitivity(volatile struct MrfErRegs *pEr, int ttlin, int *level)
{
  int fpctrl;

  _CHECK_TTLIN_RANGE(ttlin)

  fpctrl = be32_to_cpu(pEr->FPInMap[ttlin]);

  if (fpctrl &= (1 << C_EVR_FPIN_EXTLEV_ACT))
    *level=1;
  else
    *level=0;

  return 0;
}




RESULT EvrGetFPOutMap(volatile struct MrfErRegs *pEr, int output, int* map)
{
  if (output < 0 || output >= EVR_MAX_FPOUT_MAP)
    return RERR_FPOUT_MAP_RANGE;
  *map = be16_to_cpu(pEr->FPOutMap[output]);
  return 0;
}

int EvrGetFineDelay(volatile struct MrfErRegs *pEr, int channel)
{
  if (channel < 0 || channel >= EVR_MAX_CML_OUTPUTS)
    return -1;
  return be32_to_cpu(pEr->FineDelay[channel]);
}

int EvrCMLGetEnable(volatile struct MrfErRegs *pEr, int channel)
{
  if (channel < 0 || channel >= EVR_MAX_CML_OUTPUTS)
    return -1;

  int ctrl = be16_to_cpu(pEr->CML[channel].Control);
  if (ctrl & (1 << C_EVR_CMLCTRL_ENABLE))
    return 1;
  return 0;
}


//--------------------------------------------
//JERZY: ADDED by me
int EvrTester(volatile struct MrfErRegs *pEr)
{
    printf("Evr Tester function\n");

    return 666;
}

int EvrWriteRegToFile(volatile struct MrfErRegs *pEr)
{
u32 er_reg_tmp[0x8000/sizeof(u32)];
u32 *p = (u32 *) pEr;
long int i;

for (i = 0; i < sizeof(er_reg_tmp)/sizeof(u32); i++)
    {
    er_reg_tmp[i]=*p;
    p++;
    }

FILE *f = fopen("er.reg", "wb");
fwrite(er_reg_tmp, sizeof(u32), sizeof(er_reg_tmp)/sizeof(u32), f);
fclose(f);

return 1;
}


int EvrWriteFileToReg(volatile struct MrfErRegs *pEr)
{
u32 er_reg_tmp[0x8000/sizeof(u32)];
u32 *p = (u32 *) pEr;
long int i;

FILE *f = fopen("er.reg", "rb");
if (f)
    {
    fread(er_reg_tmp, sizeof(u32), sizeof(er_reg_tmp)/sizeof(u32), f);
    fclose(f);
    }
else return -1;


for (i = 0; i < sizeof(er_reg_tmp)/sizeof(u32); i++)
    {
    *p=er_reg_tmp[i];
    p++;
    }

return 1;
}
