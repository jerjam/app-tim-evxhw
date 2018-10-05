/*
  egapi.c -- Functions for Micro-Research Event Generator
             Application Programming Interface

  Author: Jukka Pietarinen (MRF)
  Date:   05.12.2006

*/

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <stdio.h>
#include <endian.h>
#include <byteswap.h>
#include <errno.h>
#include <string.h> // memcpy
#include <unistd.h> // close
#include "egcpci.h"
#include "egapi.h"


#define DEBUG 1
#define DEBUG_PRINTF printf

#define _CHECK_RANGE(op, min, overmax, err) if ( (op) < (min) || (op) >= (overmax)) return (err);

#define _CHECK_MXC_RANGE(mxc) _CHECK_RANGE(mxc, 0, EVG_MAX_MXCS, GERR_MXC_RANGE)

#define _CHECK_TRIGGER_RANGE(map) _CHECK_RANGE(map, 0, EVG_MAX_TRIGGERS, GERR_TRIGGER_RANGE)

#define _CHECK_DBUS_BITS_RANGE(x) _CHECK_RANGE(x, 0, EVG_DBUS_BITS, GERR_DBUS_BITS_RANGE)

#define _CHECK_DBUS_SEL_MASK(map) if (map < 0 || map > C_EVG_DBUS_SEL_MASK) return GERR_DBUS_SEL_MASK;

#define _CHECK_SEQRAMS_RANGE(x) _CHECK_RANGE(x, 0, EVG_SEQRAMS, GERR_SEQRAMS_RANGE)

#define _CHECK_SEQRAMEV_RANGE(x) _CHECK_RANGE(x, 0, EVG_MAX_SEQRAMEV, GERR_SEQRAMEV_RANGE)

#define _CHECK_EVENT_CODE_RANGE(x) _CHECK_RANGE(x, 0, EVG_MAX_EVENT_CODE, GERR_EVENT_CODE_RANGE)

#define _CHECK_RAMSWTRIG_RANGE(x) _CHECK_RANGE(x, 0, 2, GERR_RAMSWTRIG_RANGE)

#define _CHECK_UNIVIN_RANGE(x) _CHECK_RANGE(x, 0, EVG_MAX_UNIVIN_MAP, GERR_UNIVIN_RANGE)



#define _DUMP_AUX_BEGIN(out, buf) static char __buf[2048]; char *buf = out; if(buf == 0) buf = __buf;

#define _DUMP_AUX_END(out, buf) if (out == 0) printf(__buf);

int __bit2int(u32 bits);

const char * evg_get_errmsg(RESULT s)
{
	static const char* errors[] = {
		"OK",
		"Parameter out of range: mxc",
		"Parameter out of range: trigger",
		"Parameter out of range: dbus bits",
		"Parameter out of range: dbus sel mask",
		"Parameter out of range: seqrams",
		"Parameter out of range: seqramev",
		"Parameter out of range: event_code",
		"Parameter out of range: ramswtrig",
		"Parameter out of range: univin",

		"UNKNOWN ERROR"
	};
	const int errsz = sizeof(errors)/sizeof(errors[0]);

	if ( (s < 0) || (s >= errsz) )
		return errors[errsz-1];
	return errors[s];
}


int EvgOpen(volatile struct MrfEgRegs **pEg, char *device_name)
{
  int fd;

  /* Open Event Generator device for read/write */
  fd = open(device_name, O_RDWR);
#ifdef DEBUG
  DEBUG_PRINTF("EvgOpen: open(\"%s\", O_RDWR) returned %d\n", device_name, fd);
#endif
  if (fd != -1)
    {
      /* Memory map Event Generator registers */
      *pEg = (struct MrfEgRegs *) mmap(0, EVG_MEM_WINDOW, PROT_READ | PROT_WRITE,
					MAP_SHARED, fd, 0);
#ifdef DEBUG
  DEBUG_PRINTF("EvgOpen: mmap returned %08x, errno %d\n", (int) *pEg,
	       errno);
#endif
      if (*pEg == MAP_FAILED)
	{
	  close(fd);
	  return -1;
	}
    }

  return fd;
}

int EvgClose(int fd)
{
  int result;

  result = munmap(0, EVG_MEM_WINDOW);
  return close(fd);
}

int EvgEnable(volatile struct MrfEgRegs *pEg, int state)
{
  if (state)
    pEg->Control |= be32_to_cpu(1 << C_EVG_CTRL_MASTER_ENABLE);
  else
    pEg->Control &= be32_to_cpu(~(1 << C_EVG_CTRL_MASTER_ENABLE));

  return EvgGetEnable(pEg);
}

int EvgGetEnable(volatile struct MrfEgRegs *pEg)
{
  return be32_to_cpu(pEg->Control & be32_to_cpu(1 << C_EVG_CTRL_MASTER_ENABLE));
}

int EvgRxEnable(volatile struct MrfEgRegs *pEg, int state)
{
  if (!state)
    pEg->Control |= be32_to_cpu((1 << C_EVG_CTRL_RX_DISABLE) |
				(1 << C_EVG_CTRL_RX_PWRDOWN));
  else
    pEg->Control &= be32_to_cpu(~((1 << C_EVG_CTRL_RX_DISABLE) |
				  (1 << C_EVG_CTRL_RX_PWRDOWN)));

  return EvgRxGetEnable(pEg);
}

int EvgRxGetEnable(volatile struct MrfEgRegs *pEg)
{
  return be32_to_cpu(~(pEg->Control) &
		     be32_to_cpu((1 << C_EVG_CTRL_RX_DISABLE) |
				 (1 << C_EVG_CTRL_RX_PWRDOWN)));
}

int EvgGetViolation(volatile struct MrfEgRegs *pEg, int clear)
{
  int result;

  result = be32_to_cpu(pEg->IrqFlag & be32_to_cpu(1 << C_EVG_IRQFLAG_VIOLATION));
  if (clear && result)
    pEg->IrqFlag = be32_to_cpu(result);

  return result;
}

int EvgSWEventEnable(volatile struct MrfEgRegs *pEg, int state)
{
  unsigned int mask = ~((1 << (C_EVG_SWEVENT_CODE_HIGH + 1)) -
    (1 << C_EVG_SWEVENT_CODE_LOW));
  int swe;

  swe = be32_to_cpu(pEg->SWEvent);
  if (state)
    pEg->SWEvent = be32_to_cpu(1 << C_EVG_SWEVENT_ENABLE | (swe & mask));
  else
    pEg->SWEvent = be32_to_cpu(~(1 << C_EVG_SWEVENT_ENABLE) & swe & mask);
  return EvgGetSWEventEnable(pEg);
}

int EvgGetSWEventEnable(volatile struct MrfEgRegs *pEg)
{
  return be32_to_cpu(pEg->SWEvent & be32_to_cpu(1 << C_EVG_SWEVENT_ENABLE));
}

int EvgSendSWEvent(volatile struct MrfEgRegs *pEg, int code)
{
  unsigned int mask = ~((1 << (C_EVG_SWEVENT_CODE_HIGH + 1)) -
    (1 << C_EVG_SWEVENT_CODE_LOW));
  int swcode;

  swcode = be32_to_cpu(pEg->SWEvent);
  swcode &= mask;
  swcode |= (code & EVG_MAX_EVENT_CODE);

  pEg->SWEvent = be32_to_cpu(swcode);

  return be32_to_cpu(pEg->SWEvent);
}

int EvgEvanEnable(volatile struct MrfEgRegs *pEg, int state)
{
  if (state)
    pEg->EvanControl |= be32_to_cpu(1 << C_EVG_EVANCTRL_ENABLE);
  else
    pEg->EvanControl &= be32_to_cpu(~(1 << C_EVG_EVANCTRL_ENABLE));

  return EvgEvanGetEnable(pEg);
}

int EvgEvanGetEnable(volatile struct MrfEgRegs *pEg)
{
  return be32_to_cpu(pEg->EvanControl & be32_to_cpu(1 << C_EVG_EVANCTRL_ENABLE));
}

void EvgEvanReset(volatile struct MrfEgRegs *pEg)
{
  struct EvanStruct evan;

  pEg->EvanControl |= be32_to_cpu(1 << C_EVG_EVANCTRL_RESET);
  /* Dummy read to clear FIFO */
  EvgEvanGetEvent(pEg, &evan);
}

void EvgEvanResetCount(volatile struct MrfEgRegs *pEg)
{
  pEg->EvanControl |= be32_to_cpu(1 << C_EVG_EVANCTRL_COUNTRES);
}

int EvgEvanGetEvent(volatile struct MrfEgRegs *pEg, struct EvanStruct *evan)
{
  if (pEg->EvanControl & be32_to_cpu(1 << C_EVG_EVANCTRL_NOTEMPTY))
    {
      /* Reading the event code & dbus data, pops the next item first from the event
	 analyzer fifo */
      evan->EventCode = be32_to_cpu(pEg->EvanCode);
      evan->TimestampHigh = be32_to_cpu(pEg->EvanTimeH);
      evan->TimestampLow = be32_to_cpu(pEg->EvanTimeL);
      return 0;
    }
  return -1;
}

RESULT EvgSetMXCPrescaler(volatile struct MrfEgRegs *pEg, int mxc, unsigned int presc)
{
  _CHECK_MXC_RANGE(mxc)

  pEg->MXC[mxc].Prescaler = be32_to_cpu(presc);

  return 0;
}

RESULT EvgSetMxcTrigMap(volatile struct MrfEgRegs *pEg, int mxc, int map)
{
   _CHECK_MXC_RANGE(mxc)
//   _CHECK_TRIGGER_RANGE(map)

  if (map < -1 || map >= EVG_MAX_TRIGGERS)
    return -1;

  if (map >= 0)
    pEg->MXC[mxc].Control = be32_to_cpu(1 << (map + C_EVG_MXCMAP_TRIG_BASE));
  else
    pEg->MXC[mxc].Control = be32_to_cpu(0);

  return 0;
}

void EvgSyncMxc(volatile struct MrfEgRegs *pEg)
{
  pEg->Control |= be32_to_cpu(1 << C_EVG_CTRL_MXC_RESET);
}

void EvgMXCDump(volatile struct MrfEgRegs *pEg, char* out)
{
  int mxc;
  _DUMP_AUX_BEGIN(out, buf)

  for (mxc = 0; mxc < EVG_MXCS; mxc++)
    {
      buf += sprintf(buf, "MXC%d Prescaler %08x (%d) Trig %08x State %d\n",
		   mxc,
		   be32_to_cpu(pEg->MXC[mxc].Prescaler),
		   be32_to_cpu(pEg->MXC[mxc].Prescaler),
		   be32_to_cpu(pEg->MXC[mxc].Control) &
		   ((1 << EVG_MAX_TRIGGERS) - 1),
		   (be32_to_cpu(pEg->MXC[mxc].Control) & (1 << C_EVG_MXC_READ))
		   ? 1 : 0);
    }
  _DUMP_AUX_END(out, buf)
}

RESULT EvgSetDBusMap(volatile struct MrfEgRegs *pEg, int dbus, int map)
{
  int mask;

  _CHECK_DBUS_BITS_RANGE(dbus)
  _CHECK_DBUS_SEL_MASK(map)

  mask = ~(C_EVG_DBUS_SEL_MASK << (dbus*C_EVG_DBUS_SEL_BITS));
  pEg->DBusMap &= be32_to_cpu(mask);
  pEg->DBusMap |= be32_to_cpu(map << (dbus*C_EVG_DBUS_SEL_BITS));

  return 0;
}

void EvgDBusDump(volatile struct MrfEgRegs *pEg, char* out)
{
  int dbus;
  _DUMP_AUX_BEGIN(out, buf)

  for (dbus = 0; dbus < EVG_DBUS_BITS; dbus++)
    {
      buf += sprintf(buf, "DBUS%d ", dbus);
      switch ((be32_to_cpu(pEg->DBusMap) >> (dbus*C_EVG_DBUS_SEL_BITS)) &
	      ((1 << C_EVG_DBUS_SEL_BITS) - 1))
	{
	case C_EVG_DBUS_SEL_OFF:
	  buf += sprintf(buf, "OFF\n");
	  break;
	case C_EVG_DBUS_SEL_EXT:
	  buf += sprintf(buf, "EXT\n");
	  break;
	case C_EVG_DBUS_SEL_MXC:
	  buf += sprintf(buf, "MXC\n");
	  break;
	case C_EVG_DBUS_SEL_FORWARD:
	  buf += sprintf(buf, "FWD\n");
	  break;
	default:
	  buf += sprintf(buf, "Unknown\n");
	  break;
	}
    }
    _DUMP_AUX_END(out, buf)
}

RESULT EvgSetACInput(volatile struct MrfEgRegs *pEg, int bypass, int sync, int div, int delay)
{
  unsigned int result;

  result = be32_to_cpu(pEg->ACControl);

  if (bypass == 0)
    result &= ~(1 << C_EVG_ACCTRL_BYPASS);
  if (bypass == 1)
    result |= (1 << C_EVG_ACCTRL_BYPASS);

  if (sync == 0)
    result &= ~(1 << C_EVG_ACCTRL_ACSYNC);
  if (sync == 1)
    result |= (1 << C_EVG_ACCTRL_ACSYNC);

  if (div > 0 && div < (2 << (C_EVG_ACCTRL_DIV_HIGH - C_EVG_ACCTRL_DIV_LOW)))
    {
      result &= ~((2 << C_EVG_ACCTRL_DIV_HIGH) - (1 << C_EVG_ACCTRL_DIV_LOW));
      result |= div << C_EVG_ACCTRL_DIV_LOW;
    }

  if (delay > 0 && delay < (2 << (C_EVG_ACCTRL_DELAY_HIGH - C_EVG_ACCTRL_DELAY_LOW)))
    {
      result &= ~((2 << C_EVG_ACCTRL_DELAY_HIGH) - (1 << C_EVG_ACCTRL_DELAY_LOW));
      result |= delay << C_EVG_ACCTRL_DELAY_LOW;
    }

  pEg->ACControl = be32_to_cpu(result);

  return 0;
}

RESULT EvgSetACMap(volatile struct MrfEgRegs *pEg, int map)
{
//  _CHECK_TRIGGER_RANGE(map)
  if (map > EVG_MAX_TRIGGERS)
    return -1;

  if (map >= 0)
    pEg->ACMap = be32_to_cpu(1 << map);
  else
    pEg->ACMap = 0;

  return 0;
}

void EvgACDump(volatile struct MrfEgRegs *pEg, char* out)
{
  unsigned int result;
  _DUMP_AUX_BEGIN(out, buf)

  result = be32_to_cpu(pEg->ACControl);
  buf += sprintf(buf, "AC Input div %d delay %d", (result &
					    ( (2 << C_EVG_ACCTRL_DIV_HIGH)
					    - (1 << C_EVG_ACCTRL_DIV_LOW)) )
	       >> C_EVG_ACCTRL_DIV_LOW,
	       (result &
		((2 << C_EVG_ACCTRL_DELAY_HIGH) - (1 << C_EVG_ACCTRL_DELAY_LOW)))
	       >> C_EVG_ACCTRL_DELAY_LOW);
  if (result & (1 << C_EVG_ACCTRL_BYPASS))
    buf += sprintf(buf, " BYPASS");
  if (result & (1 << C_EVG_ACCTRL_ACSYNC))
    buf += sprintf(buf, " SYNCMXC7");
  buf += sprintf(buf, "\n");

  _DUMP_AUX_END(out, buf)
}

RESULT EvgSetRFInput(volatile struct MrfEgRegs *pEg, int useRF, int div)
{
  int rfdiv;

  rfdiv = be32_to_cpu(pEg->ClockControl);

  if (useRF == 0)
    rfdiv &= ~(1 << C_EVG_CLKCTRL_EXTRF);
  if (useRF == 1)
    rfdiv |= (1 << C_EVG_CLKCTRL_EXTRF);

  if (div >= 0 && div <= C_EVG_RFDIV_MASK)
    {
      rfdiv &= ~(C_EVG_RFDIV_MASK << C_EVG_CLKCTRL_DIV_LOW);
      rfdiv |= div << C_EVG_CLKCTRL_DIV_LOW;
    }

  pEg->ClockControl = be32_to_cpu(rfdiv);

  return 0;
}

int EvgSetFracDiv(volatile struct MrfEgRegs *pEg, int fracdiv)
{
  return pEg->FracDiv = be32_to_cpu(fracdiv);
}

RESULT EvgSetSeqRamEvent(volatile struct MrfEgRegs *pEg, int ram, int pos, unsigned int timestamp, int code)
{
  _CHECK_SEQRAMS_RANGE(ram)
  _CHECK_SEQRAMEV_RANGE(pos)
  _CHECK_EVENT_CODE_RANGE(code)

  pEg->SeqRam[ram][pos].Timestamp = be32_to_cpu(timestamp);
  pEg->SeqRam[ram][pos].EventCode = be32_to_cpu(code);

  return 0;
}

void EvgSeqRamDump(volatile struct MrfEgRegs *pEg, int ram, char* out)
{
  int pos;
  _DUMP_AUX_BEGIN(out, buf)

  if (ram < 0 || ram >= EVG_SEQRAMS)
    return;

  for (pos = 0; pos < EVG_MAX_SEQRAMEV; pos++)
    if (pEg->SeqRam[ram][pos].EventCode)
      buf += sprintf(buf, "Ram%d: Timestamp %08lx Code %02lx\n",
		   ram,
		   (unsigned long)be32_to_cpu(pEg->SeqRam[ram][pos].Timestamp),
		   (unsigned long)be32_to_cpu(pEg->SeqRam[ram][pos].EventCode));
  _DUMP_AUX_END(out, buf)
}

RESULT EvgSeqRamControl(volatile struct MrfEgRegs *pEg, int ram, int enable, int single, int recycle, int reset, int trigsel)
{
  int control;

  _CHECK_SEQRAMS_RANGE(ram)

  control = be32_to_cpu(pEg->SeqRamControl[ram]);

  if (enable == 0)
    control |= (1 << C_EVG_SQRC_DISABLE);
  if (enable == 1)
    control |= (1 << C_EVG_SQRC_ENABLE);

  if (single == 0)
    control &= ~(1 << C_EVG_SQRC_SINGLE);
  if (single == 1)
    control |= (1 << C_EVG_SQRC_SINGLE);

  if (recycle == 0)
    control &= ~(1 << C_EVG_SQRC_RECYCLE);
  if (recycle == 1)
    control |= (1 << C_EVG_SQRC_RECYCLE);

  if (reset == 1)
    control |= (1 << C_EVG_SQRC_RESET);

  if (trigsel >= 0 && trigsel <= C_EVG_SEQTRIG_MAX)
    {
      control &= ~(C_EVG_SEQTRIG_MAX << C_EVG_SQRC_TRIGSEL_LOW);
      control |= (trigsel << C_EVG_SQRC_TRIGSEL_LOW);
    }

  pEg->SeqRamControl[ram] = be32_to_cpu(control);

  return 0;
}

RESULT EvgSeqRamSWTrig(volatile struct MrfEgRegs *pEg, int trig)
{
  _CHECK_RAMSWTRIG_RANGE(trig)

  pEg->SeqRamControl[trig] |= be32_to_cpu(1 << C_EVG_SQRC_SWTRIGGER);

  return 0;
}

void EvgSeqRamStatus(volatile struct MrfEgRegs *pEg, int ram, char* out)
{
  int control;
  _DUMP_AUX_BEGIN(out, buf)

  if (ram < 0 || ram >= EVG_SEQRAMS)
    return;

  control = be32_to_cpu(pEg->SeqRamControl[ram]);

  buf += sprintf(buf, "RAM%d:", ram);
  if (control & (1 << C_EVG_SQRC_RUNNING))
    buf += sprintf(buf, " RUN");
  if (control & (1 << C_EVG_SQRC_ENABLED))
    buf += sprintf(buf, " ENA");
  if (control & (1 << C_EVG_SQRC_SINGLE))
    buf += sprintf(buf, " SINGLE");
  if (control & (1 << C_EVG_SQRC_RECYCLE))
    buf += sprintf(buf, " RECYCLE");
  buf += sprintf(buf, " Trigsel %02x\n", (control >> C_EVG_SQRC_TRIGSEL_LOW) & C_EVG_SEQTRIG_MAX);

  _DUMP_AUX_END(out, buf)
}

RESULT EvgSetUnivinMap(volatile struct MrfEgRegs *pEg, int univ, int trig, int dbus)
{
  int map = 0;

  _CHECK_UNIVIN_RANGE(univ)

  if (trig >= EVG_MAX_TRIGGERS)
    return GERR_TRIGGER_RANGE; //TODO: no ben be, q aqui -1 es valid

  if (dbus >= EVG_DBUS_BITS)
    return GERR_DBUS_BITS_RANGE;

  if (trig >= 0)
    map |= (1 << (C_EVG_INMAP_TRIG_BASE + trig));

  if (dbus >= 0)
    map |= (1 << (C_EVG_INMAP_DBUS_BASE + dbus));

  pEg->UnivInMap[univ] = be32_to_cpu(map);

  return 0;
}

void EvgUnivinDump(volatile struct MrfEgRegs *pEg, char* out)
{
  int univ;
  _DUMP_AUX_BEGIN(out, buf)

  for (univ = 0; univ < EVG_UNIVINS; univ++)
    {
      buf += sprintf(buf, "UnivIn%d Mapped to Trig %08x, DBus %02x\n",
		   univ,
		   (be32_to_cpu(pEg->UnivInMap[univ]) >> C_EVG_INMAP_TRIG_BASE)
		   & ((1 << EVG_MAX_TRIGGERS) - 1),
		   (be32_to_cpu(pEg->UnivInMap[univ]) >> C_EVG_INMAP_DBUS_BASE)
		   & ((1 << EVG_DBUS_BITS) - 1));
    }
  _DUMP_AUX_END(out, buf)
}

RESULT EvgSetTriggerEvent(volatile struct MrfEgRegs *pEg, int trigger, int code, int enable)
{
  int result;

  _CHECK_TRIGGER_RANGE(trigger)

  result = be32_to_cpu(pEg->EventTrigger[trigger]);

  //TODO: piltrafilla, tas segur que aixo esta be? ho he canviat, he afegit el ~ davant
  if (code >= 0 && code <= EVG_MAX_EVENT_CODE)
    {
      result &= ~((1 << (C_EVG_EVENTTRIG_CODE_HIGH + 1)) -
	(1 << C_EVG_EVENTTRIG_CODE_LOW));
      result |= (code << C_EVG_EVENTTRIG_CODE_LOW);
    }

  if (enable == 0)
    result &= ~(1 << C_EVG_EVENTTRIG_ENABLE);
  if (enable == 1)
    result |= (1 << C_EVG_EVENTTRIG_ENABLE);

  pEg->EventTrigger[trigger] = be32_to_cpu(result);

  return 0;
}

void EvgTriggerEventDump(volatile struct MrfEgRegs *pEg, char* out)
{
  int trigger, result;
  _DUMP_AUX_BEGIN(out, buf)

  for (trigger = 0; trigger < EVG_TRIGGERS; trigger++)
    {
      result = be32_to_cpu(pEg->EventTrigger[trigger]);
      buf += sprintf(buf, "Trigger%d code %02x %s\n",
	     trigger, (result & ((1 << (C_EVG_EVENTTRIG_CODE_HIGH + 1)) -
				 (1 << C_EVG_EVENTTRIG_CODE_LOW))) >>
	     C_EVG_EVENTTRIG_CODE_LOW, result & (1 << C_EVG_EVENTTRIG_ENABLE) ?
	     "ENABLED" : "DISABLED");
    }
  _DUMP_AUX_END(out, buf)
}

int EvgSetUnivOutMap(volatile struct MrfEgRegs *pEg, int output, int map)
{
  pEg->UnivOutMap[output] = be16_to_cpu(map);
  return 0;
}

int EvgSetDBufMode(volatile struct MrfEgRegs *pEg, int enable)
{
  if (enable)
    pEg->DataBufControl = be32_to_cpu(1 << C_EVG_DATABUF_MODE);
  else
    pEg->DataBufControl = 0;

  return EvgGetDBufStatus(pEg);
}

int EvgGetDBufStatus(volatile struct MrfEgRegs *pEg)
{
  return be32_to_cpu(pEg->DataBufControl);
}

int EvgSendDBuf(volatile struct MrfEgRegs *pEg, char *dbuf, int size)
{
  int stat;

  stat = EvgGetDBufStatus(pEg);
  //  printf("EvgSendDBuf: stat %08x\n", stat);
  /* Check that DBUF mode enabled */
  if (!(stat & (1 << C_EVG_DATABUF_MODE)))
    return -1;
  /* Check that previous transfer is completed */
  if (!(stat & (1 << C_EVG_DATABUF_COMPLETE)))
    return -1;
  /* Check that size is valid */
  if (size & 3 || size > EVG_MAX_BUFFER || size < 4)
    return -1;

  memcpy((void *) &pEg->Databuf[0], (void *) dbuf, size);

  /* Enable and set size */
  stat &= ~((EVG_MAX_BUFFER-1) | (1 << C_EVG_DATABUF_TRIGGER));
  stat |= (1 << C_EVG_DATABUF_ENA) | size;
  //  printf("EvgSendDBuf: stat %08x\n", stat);
  pEg->DataBufControl = be32_to_cpu(stat);
  //  printf("EvgSendDBuf: stat %08x\n", be32_to_cpu(pEg->DataBufControl));

  /* Trigger */
  pEg->DataBufControl = be32_to_cpu(stat | (1 << C_EVG_DATABUF_TRIGGER));
  //  printf("EvgSendDBuf: stat %08x\n", be32_to_cpu(pEg->DataBufControl));

  return size;
}

void EvgSetVal(volatile struct MrfEgRegs *pEg, unsigned int pos, unsigned int val)
{
	volatile char * p = (char*)pEg;
	*((u32*)(p + pos)) = be32_to_cpu(val);
}

int EvgGetVal(volatile struct MrfEgRegs *pEg, unsigned int pos)
{
        volatile char * p = (char*)pEg;
        return be32_to_cpu(*((u32*)(p + pos)));

}


void EvgDataBufferRead(volatile struct MrfEgRegs *pEg, unsigned int offset, unsigned int * value)
{
// 	unsigned int size = devtoh16(pEvg->DataBufSize);
//
// 	if ( offset >= size )
// 		return EVG_SIZE_ERR;

	*value = be32_to_cpu(pEg->Databuf[offset]);
}

void EvgDataBufferWrite(volatile struct MrfEgRegs *pEg, unsigned int offset, unsigned int value)
{
// 	unsigned int size = devtoh16(pEvg->DataBufSize);
//
// 	if ( offset >= size )
// 		return EVG_SIZE_ERR;

	pEg->Databuf[offset] = be32_to_cpu(value);
}



/** After changing the RF of the device some values wont be modified until the C_EVG_CLKCTRL_CGLOCK bit is set, including
SequenceRam enables.
*/
int EvgClockIsCGLocked(volatile struct MrfEgRegs *pEg)
{
  u32 ck = be32_to_cpu(pEg->ClockControl);
  return (ck & ( 1 << C_EVG_CLKCTRL_CGLOCK ))?1:0;
}


int EvgPCIStatus(volatile struct MrfEgRegs *pEg)
{
  u32 val = 0;
  return pEg->FPGAVersion != ~val;
}

int EvgGetTxDBufModeEnable(volatile struct MrfEgRegs *pEg)
{
  return (pEg->DataBufControl & be32_to_cpu(1 << C_EVG_DATABUF_MODE))? 1 : 0;
}

void EvgSetTxDBufModeEnable(volatile struct MrfEgRegs *pEg, int enable)
{
	EvgSetDBufMode(pEg, enable);
}

unsigned int EvgGetMXCPrescaler(volatile struct MrfEgRegs *pEg, int mxc)
{
  //TODO: RESULT
  if (mxc < 0 || mxc >= EVG_MAX_MXCS)
    return -1;

  return be32_to_cpu(pEg->MXC[mxc].Prescaler);
}

RESULT EvgResetMxcTrigMap(volatile struct MrfEgRegs *pEg, int mxc)
{
  _CHECK_MXC_RANGE(mxc)

  pEg->MXC[mxc].Control = be32_to_cpu(0);

  return 0;
}

RESULT EvgGetMxcTrigMap(volatile struct MrfEgRegs *pEg, int mxc, int* map)
{
  u32 aux;
  int i;
   _CHECK_MXC_RANGE(mxc)

  *map = -1;
  aux = be32_to_cpu(pEg->MXC[mxc].Control);
  for(i = 0; i < EVG_MAX_TRIGGERS; ++i) {
    if(aux & (1 << (i + C_EVG_MXCMAP_TRIG_BASE))) {
      *map = i;
      break;
    }
  }

  return 0;
}

RESULT EvgGetDBusMap(volatile struct MrfEgRegs *pEg, int dbus, int* map)
{
//  int mask;

  _CHECK_DBUS_BITS_RANGE(dbus)

  *map = ((be32_to_cpu(pEg->DBusMap) >> (dbus*C_EVG_DBUS_SEL_BITS)) &
	      ((1 << C_EVG_DBUS_SEL_BITS) - 1));
  return 0;
}

void EvgGetACInput(volatile struct MrfEgRegs *pEg, int *bypass, int *sync, int *div, int *delay)
{
  u32 result = be32_to_cpu(pEg->ACControl);
  *div = (result &
              ( (2 << C_EVG_ACCTRL_DIV_HIGH)
              - (1 << C_EVG_ACCTRL_DIV_LOW)) )
         >> C_EVG_ACCTRL_DIV_LOW;
  *delay = (result &
    ((2 << C_EVG_ACCTRL_DELAY_HIGH) - (1 << C_EVG_ACCTRL_DELAY_LOW)))
         >> C_EVG_ACCTRL_DELAY_LOW;
  *bypass = (result & (1 << C_EVG_ACCTRL_BYPASS)) ? 1 : 0;
  *sync = (result & (1 << C_EVG_ACCTRL_ACSYNC)) ? 1 : 0;
}

int EvgGetACMap(volatile struct MrfEgRegs *pEg)
{
  u32 aux = be32_to_cpu(pEg->ACMap);
  int i;

  if (!aux)
    return -1;
  for(i = 0; i < EVG_MAX_TRIGGERS; ++i){
    if (aux & (1 << i) )
      return i;
  }

  return -1;
}

void EvgResetACMap(volatile struct MrfEgRegs *pEg)
{
  pEg->ACMap = 0;
}

int EvgGetInternalFrac(volatile struct MrfEgRegs *pEg)
{
  return be32_to_cpu(pEg->FracDiv);
}

void EvgSetInternalFrac(volatile struct MrfEgRegs *pEg, int fracdiv)
{
  pEg->FracDiv = be32_to_cpu(fracdiv);
}

void EvgGetRFInput(volatile struct MrfEgRegs *pEg, int *useRF, int *div)
{
  int rfdiv;

  rfdiv = be32_to_cpu(pEg->ClockControl);
  *useRF = (rfdiv & (1 << C_EVG_CLKCTRL_EXTRF)) ? 1 : 0;

  rfdiv = rfdiv >> C_EVG_CLKCTRL_DIV_LOW;
  rfdiv &= C_EVG_RFDIV_MASK;
  *div = rfdiv;
}

RESULT EvgGetSeqRamEvent(volatile struct MrfEgRegs *pEg, int ram, int pos, unsigned int *timestamp, int *code)
{
  _CHECK_SEQRAMS_RANGE(ram)
  _CHECK_SEQRAMEV_RANGE(pos)

  *timestamp = be32_to_cpu(pEg->SeqRam[ram][pos].Timestamp);
  *code = be32_to_cpu(pEg->SeqRam[ram][pos].EventCode);

   return 0;
}

RESULT EvgSeqRamGetControl(volatile struct MrfEgRegs *pEg, int ram, int *enable, int *single, int *recycle, int *trigsel)
{
  int control;

  _CHECK_SEQRAMS_RANGE(ram)


  control = be32_to_cpu(pEg->SeqRamControl[ram]);
  *enable = (control & (1 << C_EVG_SQRC_ENABLED))?1:0;
  *single = (control & (1 << C_EVG_SQRC_SINGLE))?1:0;
  *recycle = (control & (1 << C_EVG_SQRC_RECYCLE))?1:0;
//    printf("CACA: %x\n", control);
  *trigsel = (control & (C_EVG_SEQTRIG_MAX << C_EVG_SQRC_TRIGSEL_LOW)) >> C_EVG_SQRC_TRIGSEL_LOW;

   return 0;
}

void EvgGetUnivinMap(volatile struct MrfEgRegs *pEg, int univ, int *trig, int *dbus)
{
  u32 v = be32_to_cpu(pEg->UnivInMap[univ]);
  u32 tr, db;

  tr = (v >> C_EVG_INMAP_TRIG_BASE) & ((1 << EVG_MAX_TRIGGERS) - 1);
  db = (v >> C_EVG_INMAP_DBUS_BASE) & ((1 << EVG_DBUS_BITS) - 1);

  *trig = __bit2int(tr);
  *dbus = __bit2int(db);
}

RESULT EvgGetTriggerEvent(volatile struct MrfEgRegs *pEg, int trigger, int *code, int *enable)
{
  int result;

  _CHECK_TRIGGER_RANGE(trigger)

  result = be32_to_cpu(pEg->EventTrigger[trigger]);

  *enable = (result & (1 << C_EVG_EVENTTRIG_ENABLE))?1:0;

  result &= (1 << (C_EVG_EVENTTRIG_CODE_HIGH + 1)) -
    (1 << C_EVG_EVENTTRIG_CODE_LOW);
  *code = result >> C_EVG_EVENTTRIG_CODE_LOW;



   return 0;
}

int __bit2int(u32 bits)
{
  int n;

  for(n=0; n< 32; ++n) {
    if (bits & (1<<n))
      return n;
  }
  return -1;
}


//--------------------------------------------
//JERZY: ADDED by me
int EvgTester(volatile struct MrfEgRegs *pEg)
{
    printf("Evg Tester function\n");

    return 666;
}


int EvgWriteRegToFile(volatile struct MrfEgRegs *pEg)
{
u32 eg_reg_tmp[sizeof(struct MrfEgRegs)/sizeof(u32)];
u32 *p = (u32 *) pEg;
long int i;

for (i = 0; i < (sizeof(struct MrfEgRegs)/sizeof(u32)); i++)
    {
    eg_reg_tmp[i]=*p;
    p++;
    }


FILE *f = fopen("eg.reg", "wb");
fwrite(eg_reg_tmp, sizeof(u32), sizeof(eg_reg_tmp)/sizeof(u32), f);
fclose(f);

return 1;
}

int EvgWriteFileToReg(volatile struct MrfEgRegs *pEg)
{

u32 eg_reg_tmp[sizeof(struct MrfEgRegs)/sizeof(u32)];
u32 *p = (u32 *) pEg;
long int i;

FILE *f = fopen("eg.reg", "rb");

if (f)
{
    fread(eg_reg_tmp, sizeof(u32), sizeof(eg_reg_tmp)/sizeof(u32), f);
    fclose(f);
}
else return -1;

for (i = 0; i < (sizeof(struct MrfEgRegs)/sizeof(u32)); i++)
{
    *p=eg_reg_tmp[i];
    p++;
}

return 1;
}
