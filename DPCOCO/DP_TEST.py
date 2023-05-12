import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge
from cocotb.triggers import RisingEdge
from cocotb.binary import BinaryValue


'''

This is theinputs and outputs of the Datapath module 

module DATAPATH #(parameter WIDTH=32)
    (
	  input clk, 
	  // Control Signals
	  input ALUSrc, MemtoReg, Reg_Write, PCSrc, Mem_Write,
	  input [1:0] ImmSrc,
	  input [1:0] RegSrc,
	  input [3:0] ALUControl,
	  
	  // Output signals
	  output [3:0] Cond,
	  output [1:0] Op,
	  output [5:0] Funct,
	  output [3:0] Rd,
	  
	  output [WIDTH-1:0] Result,

	  output  CO,
	  output OVF,
	  output N, Z
    );
	
'''

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

    print(" ### TESTING THE DATAPATH ###")
    print(" ### READING THE INSTRUCTIONS FROM inst_mem.txt  ###")

    await clkedge
    print(f'PC: {dut.PC.value}')


    print(" ~~~~~~~~~~~~~~~~~~ \n")

    dut.reset.value = 0
    
    #Instr = 0b11100100000000100101000000000000
    print("Testing LDR Operation... \n")

    print("LDR R5, R2; \n")
    print("R2 = 0, mem[0] = 4, Write 4 to R5 \n")

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

    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

    dut.reset.value = 0
    
    #Instr = 0b11100100000000100110000000000100
    print("Testing LDR Operation... \n")

    print("LDR R6, R2, #4; \n")
    print("R2 = 0, mem[4] = 7, Write 7 to R6 \n")


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

    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

    dut.reset.value = 0
    
    #Instr = 0b11100000100001100111000000000101
    print("Testing ADD Operation... \n")

    print("ADD R7, R6, R5; \n") 
    print("Write R5 + R6 (4+7) to R7 (11).\n") 


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

    # CHECKING IF THE RESULT IS CORRECT
    assert dut.MemtoRegResult.value == 11
    print("2 LDR and 1 ADD operations done successfully.\n")


    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")


    dut.reset.value = 0
    
    #Instr = 0b1110 00 0 0010 0 0110 1000 000000000101
    print("Testing SUB Operation... \n")

    print("SUB R8, R6, R5; \n") 
    print("Write R6 - R5 (7-4) to R8 (3).\n") 


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

    print(f'ALUResult: {dut.ALUResult.value}')

    print(f'ReadData: {dut.ReadData.value}')

    print(f'MemtoRegResult: {dut.MemtoRegResult.value}')

    assert dut.MemtoRegResult.value == 3
    print("SUB operation done successfully.\n")


    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")


    dut.reset.value = 0
    
    #Instr = 0b1110 01 000001 0000 1000 000000001100
    print("Testing STR Operation... \n")

    print("STR R8 (3), R2, #12; \n") 
    print("Store value of R8 in the memory address [R2] (which is zero) added 12 (mem[12]).\n") 


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
    
    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")


    dut.reset.value = 0
    
    #Instr = 0b11100100000000100000000000001100
    print("Testing LDR Operation... \n")

    print("LDR R0, R2, #12; \n")
    print("R2 = 0, mem[0+12] = 3, Write 3 to R0 \n")


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

    assert dut.MemtoRegResult.value == 3
    print("1 STR and 1 LDR operations done successfully")

    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")


    assert dut.PC.value == 20
    print("PC must be 20 after 5 instructions")




    dut.reset.value = 0
    
    #Instr = 0b11100001100000000011000000000101
    print("Testing ORR Operation... \n")

    print("ORR R3, R0, R5; \n")
    print("Write (0011) or (0100) = (0111) to R3. \n")


    PCSrc = 0
    Reg_Write = 1
    Mem_Write = 0
    MemtoReg = 0
    ALUSrc = 0
    ImmSrc = 0b00
    RegSrc = 0b00
    ALUControl = 0b1100

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

    assert dut.MemtoRegResult.value == 7
    print("7 is written to R3.")

    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

    
    dut.reset.value = 0
    
    #Instr = 0b11100000000000110100000100000000
    print("Testing AND Operation... \n")

    print("AND R4, R3, R0, #3; \n")
    print("Write (0111) and (1100) = (0100) to R4. \n")


    PCSrc = 0
    Reg_Write = 1
    Mem_Write = 0
    MemtoReg = 0
    ALUSrc = 0
    ImmSrc = 0b00
    RegSrc = 0b00
    ALUControl = 0b0000

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
    print("4 is written to R4.")

    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

    dut.reset.value = 0
    
    #Instr = 0b11100000000001000001000100000100
    print("Testing MOV Operation... \n")

    print("MOV R1, R4, #2; \n")
    print("Write (10000) to R1. \n")


    PCSrc = 0
    Reg_Write = 1
    Mem_Write = 0
    MemtoReg = 0
    ALUSrc = 0
    ImmSrc = 0b00
    RegSrc = 0b00
    ALUControl = 0b1101

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

    assert dut.MemtoRegResult.value == 16
    print("16 is written to R1.")

    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")


    dut.reset.value = 0
    
    #Instr = 0b11101000000000000000000000010000
    print("Testing B Operation... \n")

    print("B #64; \n")
    print("Branch to address: 64 \n")
    print("PC gets 64  \n")


    PCSrc = 1
    Reg_Write = 0
    Mem_Write = 0
    MemtoReg = 0
    ALUSrc = 1
    ImmSrc = 0b10
    RegSrc = 0b00
    ALUControl = 0b1101

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
    # 0x0A0B0C0D is written at 64-67
    print(f'Instr: {dut.Instr.value}\n')

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

    print(" ### End of Instruction ###\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")


    await clkedge

    print('At the next clock cycle, PC is updated')
    print(f'PC: {dut.PC.value}')
    print('PC: 40 -> 64')


