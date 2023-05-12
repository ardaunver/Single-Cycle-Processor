module DATAPATH #(parameter WIDTH=32)
    (
	  input clk, reset,
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
	  output [3:0] RA1, RA2,
	  output [WIDTH-1:0] RD1, RD2, ALUResult, PC, Instr,
	  output Z
    );
	 
wire zero;

wire ZRegInput;

// You need to turn the outputs off and leave only the wires for below

wire [WIDTH-1:0]  PCdot, PCPlus4, PCPlus8, 
						ShiftOut, SrcB, ExtImm, ReadData, MemtoRegResult;


	 
Instruction_memory InstMem (.ADDR(PC), .RD(Instr));

Adder #(.WIDTH(WIDTH)) ADDER1(.DATA_A(PC), .DATA_B(32'h0004), .OUT(PCPlus4));
Adder #(.WIDTH(WIDTH)) ADDER2(.DATA_A(32'h0004), .DATA_B(PCPlus4), .OUT(PCPlus8));

Register_simple #(.WIDTH(WIDTH)) PCReg (.clk(clk), .reset(reset), .DATA(PCdot), .OUT(PC));

Register_simple #(.WIDTH(WIDTH)) RegZ (.clk(clk), .reset(reset), .DATA(ZRegInput), .OUT(Z));

Mux_2to1 #(.WIDTH(WIDTH)) M0 (.select(PCSrc), .input_0(PCPlus4), .input_1(MemtoRegResult), .output_value(PCdot));
	 
Mux_2to1 M1 (.select(RegSrc[0]), .input_0(Instr[19:16]), .input_1(PCPlus8), 			.output_value(RA1));
Mux_2to1 M2 (.select(RegSrc[1]), .input_0(Instr[3:0]), 	.input_1(Instr[15:12]), 	.output_value(RA2));


Register_file #(.WIDTH(WIDTH)) RegF (.clk(clk), .write_enable(Reg_Write), .reset(reset), 
										.Source_select_0(RA1), .Source_select_1(RA2), .Destination_select(Instr[15:12]), 
										.DATA(MemtoRegResult), .Reg_15(PCPlus8), 
									   .out_0(RD1), .out_1(RD2));
												
Mux_2to1 #(.WIDTH(WIDTH)) M3 (.select(ALUSrc), 		.input_0(ShiftOut), 			.input_1(ExtImm), 			.output_value(SrcB));
		
Extender Ext (.A(Instr[23:0]), .select(ImmSrc), .Q(ExtImm));

shifter #(.WIDTH(WIDTH)) SHIFT (.control(Instr[6:5]), .shamt(Instr[11:7]), .DATA(RD2), .OUT(ShiftOut));

ALU #(.WIDTH(WIDTH)) ALU (.control(ALUControl), .CI(0), .DATA_A(RD1), .DATA_B(SrcB), .OUT(ALUResult), .CO(zero), .OVF(zero), .N(zero), .Z(ZRegInput));




Mux_2to1 #(.WIDTH(WIDTH)) M4 (.select(MemtoReg), 	.input_0(ALUResult), 		.input_1(ReadData), 		.output_value(MemtoRegResult));

//Data_memory #(.BYTE_SIZE(4), .ADDR_WIDTH(WIDTH)) DM (.clk(clk), .WE(Mem_Write), .ADDR(ALUResult), .WD(RD2), .RD(ReadData));
Data_memory DM (.clk(clk), .WE(Mem_Write), .ADDR(ALUResult), .WD(RD2), .RD(ReadData));


assign Result = MemtoRegResult;

// Inputs for the Controller
assign Cond = Instr[31:28];
assign Op = Instr[27:26];
assign Funct = Instr[25:20];
assign Rd = Instr[15:12];

	 
endmodule	 