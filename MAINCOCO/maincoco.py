import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge
from cocotb.triggers import RisingEdge
from cocotb.binary import BinaryValue



def t(dut):
    print(f'PC: {dut.PC.value}')
    print(f'Instr: {dut.Instr.value}')
    
    print(f'RA1: {dut.RA1.value}')
    print(f'RA2: {dut.RA2.value}')

    print(f'RD1: {dut.RD1.value}')
    print(f'RD2: {dut.RD2.value}')

    print(f'ALUResult: {dut.ALUResult.value}')

    print(f'result: {dut.result.value}')

    print('\n')
    print(f'PCSrc: {dut.pcsrc_out.value}')
    print(f'RegWrite: {dut.regwrite_out.value}')
    print(f'MemWrite: {dut.memwrite_out.value}')
    print(f'MemtoReg: {dut.memtoreg_out.value}')
    print(f'ALUSrc: {dut.alusrc_out.value}')
    print(f'ImmSrc: {dut.immsrc_out.value}')
    print(f'RegSrc: {dut.regsrc_out.value}')
    print(f'ALUControl: {dut.alucontrol_out.value}\n')
    print(f'Flag Z: {dut.z_out.value}\n')


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

    #dut.PCSrc.value = 0
    print(" ~~~~~~~~~~~~~~~~~~ \n")

    print(" ### TESTING SUBROUTINES ###")
    print(" ### READING THE INSTRUCTIONS FROM inst_mem_sub.txt  ###")

    await clkedge
    print(f'PC: {dut.PC.value}')


    print(" ~~~~~~~~~~~~~~~~~~ \n")


    dut.reset.value = 0


    #Instr = 0b1110 01 000000 0000 0001 000000000000
    print("Testing LDR Operation... \n")

    print("LDR R1, R0; \n") #1
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    
    print("LDR R2, R0, #4; \n") # Counter
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    
    print("LDR R3, R0, #8; \n") #4
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    
    print("LDR R4, R0, #C; \n") #4 for base address
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    # 16
    print("LDR R5, R4 #4; \n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("ADD R10, R5 R10; \n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("SUB R2, R2 R1; \n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("CMP R2, R0; \n") 
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("BEQ 40; \n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    # ADDRESS 36
    print("ADD R4, R4 R3; \n") 
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("B ; 16\n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print('##################')
 
    # 16
    print("LDR R5, R4 #4; \n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("ADD R10, R5 R10; \n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("SUB R2, R2 R1; \n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("CMP R2, R0; \n") 
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("BEQ 40; \n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    # ADDRESS 36
    print("ADD R4, R4 R3; \n") 
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("B ; 16\n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print('##################')
 

   # 16
    print("LDR R5, R4 #4; \n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("ADD R10, R5 R10; \n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("SUB R2, R2 R1; \n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("CMP R2, R0; \n") 
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("BEQ 40; \n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    # ADDRESS 36
    print("ADD R4, R4 R3; \n") 
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print("B ; 16\n") # First
    print("R0 = 0, mem[8] = 4, Write 4 to R2 \n")
    await clkedge
    t(dut)
    dut.reset.value = 0

    print('##################')
 






