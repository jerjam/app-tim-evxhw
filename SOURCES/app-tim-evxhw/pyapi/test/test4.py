

evcod = 10
trig = 1

rec.SetLedEvent(0, evcod, True)
rec.SetPulseMap(0, evcod, 9, -1, -1)
#rec.Params d=0, w=34464 h t
rec.MapRamEnable(0,True)

gen.Enable(True)
gen.SetTriggerEvent(trig, evcod, True)
gen.SetUnivinMap(0, trig, -1)
















rec.SetUnivOutMap(0, mevr.SIGNAL_MAP_DBUS+1) 

gen.SetUnivinMap(0, -1, 1)


evg.EvgSetDBusMap