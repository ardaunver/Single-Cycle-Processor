import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge
from cocotb.triggers import RisingEdge
from cocotb.binary import BinaryValue



@cocotb.test()
async def DP_TEST(dut):
    """Setup testbench and run a test."""
    # Generate the clock
    await cocotb.start(Clock(dut.clk, 10, 'us').start(start_high=False))

    # set clkedge as the falling edge for triggers
    clkedge = RisingEdge(dut.clk)
    # wait until the falling edge
    dut.reset.value = 1
    await clkedge

    dut.PCSrc.value = 0
    print(" ~~~~~~~~~~~~~~~~~~ \n")

    print(" ### TESTING SUBROUTINES ###")
    print(" ### READING THE INSTRUCTIONS FROM inst_mem_sub.txt  ###")

    await clkedge
    print(f'PC: {dut.PC.value}')


    print(" ~~~~~~~~~~~~~~~~~~ \n")

    dut.reset.value = 0
    
    #Instr = 0b11100100000000010010000000000000
    print("Testing LDR Operation... \n")

    print("LDR R2, R1; \n")
    print("R1 = 0, mem[0] = 1, Write 1 to R2 \n")

    PCSrc = 0
    Reg_Write = 1
    Mem_Write = 0
    MemtoReg = 1
    ALUSrc = 1
    ImmSrc = 0b01
    RegSrc = 0b00
    ALUControl = 0b0100

    #dut.Instr.value = Instr

    
    dut.ALUSrc.value = ALUSrc
    dut.MemtoReg.value = MemtoReg
    dut.Reg_Write.value = Reg_Write
    dut.PCSrc.value = PCSrc
    dut.Mem_Write.value = Mem_Write
    dut.ImmSrc.value = ImmSrc
    dut.RegSrc.value = RegSrc
    dut.ALUControl.value = ALUControl

    await clkedge
    print(f'PC: {dut.PC.value}')
    print(f'Instr: {dut.Instr.value}')

    print(f'PCSrc: {dut.PCSrc.value}')
    print(f'Reg_Write: {dut.Reg_Write.value}')
    print(f'Mem_Write: {dut.Mem_Write.value}')
    print(f'MemtoReg: {dut.MemtoReg.value}')
    print(f'ALUSrc: {dut.ALUSrc.value}')
    print(f'ImmSrc: {dut.ImmSrc.value}')
    print(f'RegSrc: {dut.RegSrc.value}')
    print(f'ALUControl: {dut.ALUControl.value}')
    
    print(f'RA1: {dut.RA1.value}')
    print(f'RA2: {dut.RA2.value}')

    print(f'ALUResult: {dut.ALUResult.value}')

    print(f'ReadData: {dut.ReadData.value}')

    print(f'MemtoRegResult: {dut.MemtoRegResult.value}')


    assert dut.MemtoRegResult.value == 1

    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

    dut.reset.value = 0
    
    #Instr = 0b11100100000000010000000000000100
    print("Testing LDR Operation... \n")

    print("LDR R0, R1, #4; \n")
    print("R1 = 0, mem[0+4] = 4, Write 4 to R0 \n")

    PCSrc = 0
    Reg_Write = 1
    Mem_Write = 0
    MemtoReg = 1
    ALUSrc = 1
    ImmSrc = 0b01
    RegSrc = 0b00
    ALUControl = 0b0100

    #dut.Instr.value = Instr

    
    dut.ALUSrc.value = ALUSrc
    dut.MemtoReg.value = MemtoReg
    dut.Reg_Write.value = Reg_Write
    dut.PCSrc.value = PCSrc
    dut.Mem_Write.value = Mem_Write
    dut.ImmSrc.value = ImmSrc
    dut.RegSrc.value = RegSrc
    dut.ALUControl.value = ALUControl

    await clkedge
    print(f'PC: {dut.PC.value}')
    print(f'Instr: {dut.Instr.value}')

    print(f'PCSrc: {dut.PCSrc.value}')
    print(f'Reg_Write: {dut.Reg_Write.value}')
    print(f'Mem_Write: {dut.Mem_Write.value}')
    print(f'MemtoReg: {dut.MemtoReg.value}')
    print(f'ALUSrc: {dut.ALUSrc.value}')
    print(f'ImmSrc: {dut.ImmSrc.value}')
    print(f'RegSrc: {dut.RegSrc.value}')
    print(f'ALUControl: {dut.ALUControl.value}')
    
    print(f'RA1: {dut.RA1.value}')
    print(f'RA2: {dut.RA2.value}')

    print(f'ALUResult: {dut.ALUResult.value}')

    print(f'ReadData: {dut.ReadData.value}')

    print(f'MemtoRegResult: {dut.MemtoRegResult.value}')
    assert dut.MemtoRegResult.value == 4

    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

    
    dut.reset.value = 0
    
    #Instr = 0b11100000100000000111000000000010
    print("Testing ADD Operation... \n")

    print("ADD R7, R0, R2; \n") 


    PCSrc = 0
    Reg_Write = 1
    Mem_Write = 0
    MemtoReg = 0
    ALUSrc = 0
    ImmSrc = 0b00
    RegSrc = 0b00
    ALUControl = 0b0100

    #dut.Instr.value = Instr

    
    dut.ALUSrc.value = ALUSrc
    dut.MemtoReg.value = MemtoReg
    dut.Reg_Write.value = Reg_Write
    dut.PCSrc.value = PCSrc
    dut.Mem_Write.value = Mem_Write
    dut.ImmSrc.value = ImmSrc
    dut.RegSrc.value = RegSrc
    dut.ALUControl.value = ALUControl

    await clkedge
    print(f'PC: {dut.PC.value}')
    print(f'Instr: {dut.Instr.value}')

    print(f'PCSrc: {dut.PCSrc.value}')
    print(f'Reg_Write: {dut.Reg_Write.value}')
    print(f'Mem_Write: {dut.Mem_Write.value}')
    print(f'MemtoReg: {dut.MemtoReg.value}')
    print(f'ALUSrc: {dut.ALUSrc.value}')
    print(f'ImmSrc: {dut.ImmSrc.value}')
    print(f'RegSrc: {dut.RegSrc.value}')
    print(f'ALUControl: {dut.ALUControl.value}')
    
    print(f'RA1: {dut.RA1.value}')
    print(f'RA2: {dut.RA2.value}')

    print(f'ALUResult: {dut.ALUResult.value}')

    print(f'ReadData: {dut.ReadData.value}')

    print(f'MemtoRegResult: {dut.MemtoRegResult.value}')
    assert dut.MemtoRegResult.value == 5

    # CHECKING IF THE RESULT IS CORRECT
    #assert dut.MemtoRegResult.value == 3
    print("2 LDR and 1 ADD operations done successfully.\n")


    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

    dut.reset.value = 0
    
    #Instr = 0b1110 00 0 0010 0 0001 0000 000000000000
    print("Testing SUB Operation... \n")

    print("SUB R0, R1, R0; \n") 
    print("NOT R0 \n") 


    PCSrc = 0
    Reg_Write = 1
    Mem_Write = 0
    MemtoReg = 0
    ALUSrc = 0
    ImmSrc = 0b00
    RegSrc = 0b00
    ALUControl = 0b0010

    #dut.Instr.value = Instr

    
    dut.ALUSrc.value = ALUSrc
    dut.MemtoReg.value = MemtoReg
    dut.Reg_Write.value = Reg_Write
    dut.PCSrc.value = PCSrc
    dut.Mem_Write.value = Mem_Write
    dut.ImmSrc.value = ImmSrc
    dut.RegSrc.value = RegSrc
    dut.ALUControl.value = ALUControl

    await clkedge
    print(f'PC: {dut.PC.value}')
    print(f'Instr: {dut.Instr.value}')

    print(f'PCSrc: {dut.PCSrc.value}')
    print(f'Reg_Write: {dut.Reg_Write.value}')
    print(f'Mem_Write: {dut.Mem_Write.value}')
    print(f'MemtoReg: {dut.MemtoReg.value}')
    print(f'ALUSrc: {dut.ALUSrc.value}')
    print(f'ImmSrc: {dut.ImmSrc.value}')
    print(f'RegSrc: {dut.RegSrc.value}')
    print(f'ALUControl: {dut.ALUControl.value}')
    
    print(f'RA1: {dut.RA1.value}')
    print(f'RA2: {dut.RA2.value}')

    print(f'RD1: {dut.RD1.value}')
    print(f'RD2: {dut.RD2.value}')

    print(f'ALUResult: {dut.ALUResult.value}')

    print(f'ReadData: {dut.ReadData.value}')

    print(f'MemtoRegResult: {dut.MemtoRegResult.value}')


    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
    
    dut.reset.value = 0
    
    #Instr = 0b11100100000100010000000000001000
    print("Testing STR Operation... \n")

    print("STR R0 , R1, #8; \n") 


    PCSrc = 0
    Reg_Write = 0
    Mem_Write = 1
    MemtoReg = 0
    ALUSrc = 1
    ImmSrc = 0b01
    RegSrc = 0b10
    ALUControl = 0b0100

    #dut.Instr.value = Instr

    
    dut.ALUSrc.value = ALUSrc
    dut.MemtoReg.value = MemtoReg
    dut.Reg_Write.value = Reg_Write
    dut.PCSrc.value = PCSrc
    dut.Mem_Write.value = Mem_Write
    dut.ImmSrc.value = ImmSrc
    dut.RegSrc.value = RegSrc
    dut.ALUControl.value = ALUControl

    await clkedge
    print(f'PC: {dut.PC.value}')
    print(f'Instr: {dut.Instr.value}')

    print(f'PCSrc: {dut.PCSrc.value}')
    print(f'Reg_Write: {dut.Reg_Write.value}')
    print(f'Mem_Write: {dut.Mem_Write.value}')
    print(f'MemtoReg: {dut.MemtoReg.value}')
    print(f'ALUSrc: {dut.ALUSrc.value}')
    print(f'ImmSrc: {dut.ImmSrc.value}')
    print(f'RegSrc: {dut.RegSrc.value}')
    print(f'ALUControl: {dut.ALUControl.value}')
    
    print(f'RA1: {dut.RA1.value}')
    print(f'RA2: {dut.RA2.value}')

    print(f'RD1: {dut.RD1.value}')
    print(f'RD2: {dut.RD2.value}')

    print(f'ALUResult: {dut.ALUResult.value}')

    print(f'ReadData: {dut.ReadData.value}')

    print(f'MemtoRegResult: {dut.MemtoRegResult.value}')
    
    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

    dut.reset.value = 0
    
    #Instr = 0b11100100000000011000000000010000
    print("Testing LDR Operation... \n")

    print("LDR R8, R1, #8; \n")
    print("mem[0+8] , Write 3 to R0 \n")


    PCSrc = 0
    Reg_Write = 1
    Mem_Write = 0
    MemtoReg = 1
    ALUSrc = 1
    ImmSrc = 0b01
    RegSrc = 0b00
    ALUControl = 0b0100

    #dut.Instr.value = Instr

    
    dut.ALUSrc.value = ALUSrc
    dut.MemtoReg.value = MemtoReg
    dut.Reg_Write.value = Reg_Write
    dut.PCSrc.value = PCSrc
    dut.Mem_Write.value = Mem_Write
    dut.ImmSrc.value = ImmSrc
    dut.RegSrc.value = RegSrc
    dut.ALUControl.value = ALUControl

    await clkedge
    print(f'PC: {dut.PC.value}')
    print(f'Instr: {dut.Instr.value}')

    print(f'PCSrc: {dut.PCSrc.value}')
    print(f'Reg_Write: {dut.Reg_Write.value}')
    print(f'Mem_Write: {dut.Mem_Write.value}')
    print(f'MemtoReg: {dut.MemtoReg.value}')
    print(f'ALUSrc: {dut.ALUSrc.value}')
    print(f'ImmSrc: {dut.ImmSrc.value}')
    print(f'RegSrc: {dut.RegSrc.value}')
    print(f'ALUControl: {dut.ALUControl.value}')
    
    print(f'RA1: {dut.RA1.value}')
    print(f'RA2: {dut.RA2.value}')

    print(f'RD1: {dut.RD1.value}')
    print(f'RD2: {dut.RD2.value}')

    print(f'ALUResult: {dut.ALUResult.value}')

    print(f'ReadData: {dut.ReadData.value}')

    print(f'MemtoRegResult: {dut.MemtoRegResult.value}')

    print("1 STR and 1 LDR operations done successfully")

    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
    
    dut.reset.value = 0
    
    #Instr = 0b11100000100010000000000000000001
    print("Testing ADD Operation... \n")

    print("ADD R0, R8, R1; \n") 


    PCSrc = 0
    Reg_Write = 1
    Mem_Write = 0
    MemtoReg = 0
    ALUSrc = 0
    ImmSrc = 0b00
    RegSrc = 0b00
    ALUControl = 0b0100

    #dut.Instr.value = Instr

    
    dut.ALUSrc.value = ALUSrc
    dut.MemtoReg.value = MemtoReg
    dut.Reg_Write.value = Reg_Write
    dut.PCSrc.value = PCSrc
    dut.Mem_Write.value = Mem_Write
    dut.ImmSrc.value = ImmSrc
    dut.RegSrc.value = RegSrc
    dut.ALUControl.value = ALUControl

    await clkedge
    print(f'PC: {dut.PC.value}')
    print(f'Instr: {dut.Instr.value}')

    print(f'PCSrc: {dut.PCSrc.value}')
    print(f'Reg_Write: {dut.Reg_Write.value}')
    print(f'Mem_Write: {dut.Mem_Write.value}')
    print(f'MemtoReg: {dut.MemtoReg.value}')
    print(f'ALUSrc: {dut.ALUSrc.value}')
    print(f'ImmSrc: {dut.ImmSrc.value}')
    print(f'RegSrc: {dut.RegSrc.value}')
    print(f'ALUControl: {dut.ALUControl.value}')
    
    print(f'RA1: {dut.RA1.value}')
    print(f'RA2: {dut.RA2.value}')

    print(f'RD1: {dut.RD1.value}')
    print(f'RD2: {dut.RD2.value}')

    print(f'ALUResult: {dut.ALUResult.value}')

    print(f'ReadData: {dut.ReadData.value}')

    print(f'MemtoRegResult: {dut.MemtoRegResult.value}')



    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

