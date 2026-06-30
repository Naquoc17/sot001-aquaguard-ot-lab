PROGRAM main
  VAR
    Chlorine_PV : REAL AT %ID0;
    Chlorine_SP : REAL AT %QD0 := 2.0;
    Pump_Run : BOOL AT %QX0.0;
  END_VAR

if Chlorine_PV < Chlorine_SP then
    Pump_Run := TRUE;
else
    Pump_Run := FALSE;
end_if;

END_PROGRAM