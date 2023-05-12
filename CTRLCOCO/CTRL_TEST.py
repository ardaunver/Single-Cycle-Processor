import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge
from cocotb.triggers import RisingEdge
from cocotb.binary import BinaryValue



@cocotb.test()
async def CTRL_TEST(dut):
    """Setup testbench and run a test."""
    # Generate the clock
    await cocotb.start(Clock(dut.clk, 10, 'us').start(start_high=False))

    # set clkedge as the falling edge for triggers
    clkedge = RisingEdge(dut.clk)
    # wait until the falling edge
    #dut.reset.value = 1
    await clkedge

    print(" ~~~~~~~~~~~~~~~~~~ \n")


    print("Testing ADD Operation... \n")

    Cond = 0b1110
    Op = 0b00
    Funct = 0b001000
    Rd = 0b0010
    ALUFlags = 0b0000

    dut.Cond.value = Cond
    dut.Op.value = Op
    dut.Funct.value = Funct
    dut.Rd.value = Rd
    dut.ALUFlags.value = ALUFlags

    await clkedge

    print(f'Cond: {dut.Cond.value}')
    print(f'Op: {dut.Op.value}')
    print(f'Funct: {dut.Funct.value}')
    print(f'Rd: {dut.Rd.value}')
    print(f'ALUFlags: {dut.ALUFlags.value}\n')

    print(f'PCSrc: {dut.PCSrc.value}')
    print(f'RegWrite: {dut.RegWrite.value}')
    print(f'MemWrite: {dut.MemWrite.value}')
    print(f'MemtoReg: {dut.MemtoReg.value}')
    print(f'ALUSrc: {dut.ALUSrc.value}')
    print(f'ImmSrc: {dut.ImmSrc.value}')
    print(f'RegSrc: {dut.RegSrc.value}')
    print(f'ALUControl: {dut.ALUControl.value}\n')

    print("Testing SUB Operation... \n")

    Cond = 0b1110
    Op = 0b00
    Funct = 0b000100
    Rd = 0b0001
    ALUFlags = 0b0000

    dut.Cond.value = Cond
    dut.Op.value = Op
    dut.Funct.value = Funct
    dut.Rd.value = Rd
    dut.ALUFlags.value = ALUFlags

    await clkedge

    print(f'Cond: {dut.Cond.value}')
    print(f'Op: {dut.Op.value}')
    print(f'Funct: {dut.Funct.value}')
    print(f'Rd: {dut.Rd.value}')
    print(f'ALUFlags: {dut.ALUFlags.value}\n')

    print(f'PCSrc: {dut.PCSrc.value}')
    print(f'RegWrite: {dut.RegWrite.value}')
    print(f'MemWrite: {dut.MemWrite.value}')
    print(f'MemtoReg: {dut.MemtoReg.value}')
    print(f'ALUSrc: {dut.ALUSrc.value}')
    print(f'ImmSrc: {dut.ImmSrc.value}')
    print(f'RegSrc: {dut.RegSrc.value}')
    print(f'ALUControl: {dut.ALUControl.value}\n')

    print("Testing AND Operation... \n")

    Cond = 0b1110
    Op = 0b00
    Funct = 0b000000
    Rd = 0b0101
    ALUFlags = 0b0000

    dut.Cond.value = Cond
    dut.Op.value = Op
    dut.Funct.value = Funct
    dut.Rd.value = Rd
    dut.ALUFlags.value = ALUFlags

    await clkedge

    print(f'Cond: {dut.Cond.value}')
    print(f'Op: {dut.Op.value}')
    print(f'Funct: {dut.Funct.value}')
    print(f'Rd: {dut.Rd.value}')
    print(f'ALUFlags: {dut.ALUFlags.value}\n')

    print(f'PCSrc: {dut.PCSrc.value}')
    print(f'RegWrite: {dut.RegWrite.value}')
    print(f'MemWrite: {dut.MemWrite.value}')
    print(f'MemtoReg: {dut.MemtoReg.value}')
    print(f'ALUSrc: {dut.ALUSrc.value}')
    print(f'ImmSrc: {dut.ImmSrc.value}')
    print(f'RegSrc: {dut.RegSrc.value}')
    print(f'ALUControl: {dut.ALUControl.value}\n')



    print("Testing LDR Operation... \n")

    Cond = 0b1110
    Op = 0b01
    Funct = 0b000001
    Rd = 0b0010
    ALUFlags = 0b0000

    dut.Cond.value = Cond
    dut.Op.value = Op
    dut.Funct.value = Funct
    dut.Rd.value = Rd
    dut.ALUFlags.value = ALUFlags

    await clkedge

    print(f'Cond: {dut.Cond.value}')
    print(f'Op: {dut.Op.value}')
    print(f'Funct: {dut.Funct.value}')
    print(f'Rd: {dut.Rd.value}')
    print(f'ALUFlags: {dut.ALUFlags.value}\n')

    print(f'PCSrc: {dut.PCSrc.value}')
    print(f'RegWrite: {dut.RegWrite.value}')
    print(f'MemWrite: {dut.MemWrite.value}')
    print(f'MemtoReg: {dut.MemtoReg.value}')
    print(f'ALUSrc: {dut.ALUSrc.value}')
    print(f'ImmSrc: {dut.ImmSrc.value}')
    print(f'RegSrc: {dut.RegSrc.value}')
    print(f'ALUControl: {dut.ALUControl.value}\n')







