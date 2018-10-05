

ram = 0
code1 = 1
code2 = 2

n = 0
gen.SetSeqRamEvent(ram, n, 0, code1); n+=1
gen.SetSeqRamEvent(ram, n, 10000, code2); n+=1
gen.SetSeqRamEvent(ram, n, 0, code1); n+=1
gen.SetSeqRamEvent(ram, n, 10000, code2); n+=1
gen.SetSeqRamEvent(ram, n, 0, code1); n+=1
gen.SetSeqRamEvent(ram, n, 10000, code2); n+=1
gen.SetSeqRamEvent(ram, n, 0, code1); n+=1
gen.SetSeqRamEvent(ram, n, 10000, code2); n+=1
gen.SetSeqRamEvent(ram, n, 0, code1); n+=1
gen.SetSeqRamEvent(ram, n, 10000, code2); n+=1
gen.SetSeqRamEvent(ram, n, 0, code1); n+=1
gen.SetSeqRamEvent(ram, n, 10000, code2); n+=1


gen.SeqRamSWTrig(ram)



# rec.






















