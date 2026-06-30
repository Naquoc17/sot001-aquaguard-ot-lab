import asyncio
from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import ModbusSequntialDataBlock, ModbusSlaveContext, ModbusServerContext

# Register map (Holding Registers, FC03/FC16)
# Reg 0-1 : Chlorine_PV = 3.0 (REAL 32-bit)
# Reg 2-3 : Chlorine_SP = 2.0 (REAL 32-bit)
# Reg 4   : Pump_Run = 0 (BOOL)

store = ModbusSlaveContext(
    hr=ModbusSequntialDataBlock(0, [0] * 5