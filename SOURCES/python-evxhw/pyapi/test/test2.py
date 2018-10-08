

mxc = 5
triggerg = 6
triggerr = 6
event = 15
prescr = 1
prescg = 1

rec.Enable(True)
rec.GetViolation(True)

rec.MapRamEnable(0,False)
#ram, event code, trigger, set, clear
rec.SetLedEvent(0, event, True)
rec.SetPulseMap(0, event, triggerr, 0, 0)
#trig, prescaler, delay, width
rec.SetPulseParams(triggerr, prescr, 0, 0)
#pulse, polarity, reset_ena, set_ena, trigg_ena, enable
rec.SetPulseProperties(triggerr, 0, 0, 0, 1, 1)
rec.MapRamEnable(0,True)

gen.Enable(True)
gen.SetMXCPrescaler(mxc, prescg)
gen.SetMxcTrigMap(mxc, triggerg)
gen.SetTriggerEvent(triggerg, event, True)













