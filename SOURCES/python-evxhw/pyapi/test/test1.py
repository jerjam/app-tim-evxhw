





prescaler_base = 0x100
prescaler = 0


rec.Enable(True)
rec.GetViolation(True)

rec.SetVal(prescaler_base + 4*prescaler, 2)
rec.SetUnivOutMap(0, mevr.SIGNAL_MAP_PRESC + prescaler)

gen.Enable(True)

















