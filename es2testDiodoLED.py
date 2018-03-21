from diodoLED import LED
lucetta = LED(18, 3)
lucetta.dammiGPIOAttuale()
lucetta.dammiIntervalloAttuale()
lucetta.settaIntervallo(10)
lucetta.lampeggia()
#lucetta.lampeggiaPerSecondi(4)
