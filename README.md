# AquaGuard — SOT-001 OT Security Lab

A virtual water-treatment facility used as the hands-on lab for CompTIA SecOT+ (SOT-001).

## Plant overview

A small chlorination loop:
- **Sensor** → measures chlorine concentration (Process Variable, PV)
- **Dosing pump** (actuator) → adds chlorine
- **PLC** (OpenPLC) → runs the control loop: if PV < SP, run pump
- Safe target: chlorine SP = 2.0 ppm

## Folder structure

```
SOT001-AquaGuard-Lab/
├── plc/
│   └── AquaGuard/          OpenPLC project (source: pous/programs/main.st)
├── scripts/                Python scripts (pymodbus server + attack)
├── captures/               Wireshark .pcapng files (gitignored)
├── docs/                   Lab documentation
└── README.md
```

## Toolchain

| Tool | Role |
|------|------|
| OpenPLC Runtime v4 | Run the PLC — scan cycle, watchdog, Modbus TCP server |
| OpenPLC Editor v4 | Write / upload ST programs |
| pymodbus 3.x | Modbus TCP server (simulated PLC) + master + attacker scripts |
| Wireshark | Capture and analyze Modbus TCP traffic |

## Lab arc (aligned with SOT-001 curriculum)

- L01 — Toolchain setup + Purdue model
- L02 — LOTO / JSA safety procedures
- L03 — Plant device modeling (OpenPLC)
- L04 — Dosing loop in Structured Text + watchdog test
- L05 — Modbus capture (FC03/FC04 reads vs FC16 write) + FC16 injection attack
- L06-L35 — Risk, threat intel, architecture, security ops, incident response
