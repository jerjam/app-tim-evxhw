
prescaler_base = 0x100
prescaler = 0


frac_div = 0x80
RFDIV_4 = 0x03
frec50 = 0x009743ad

rec.Enable(True)
rec.GetViolation(True)

rec.SetVal(prescaler_base + 4*prescaler, 2)
rec.SetUnivOutMap(0, mevr.SIGNAL_MAP_PRESC + prescaler)
rec.SetVal(frac_div, frec50)

gen.Enable(True)
gen.SetRFInput(1, RFDIV_4)

rec.GetViolation(True)












