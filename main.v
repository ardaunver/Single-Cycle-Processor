module main( input clk, 
				 input reset,
				 output [31:0] result
				);

wire [3:0] cond_out;
wire [1:0] op_out;
wire [5:0] funct_out;
wire [3:0] rd_out;

wire z_out;

wire pcsrc_out;
wire regwrite_out;
wire memwrite_out;
wire memtoreg_out;
wire alusrc_out;
wire [1:0] immsrc_out;
wire [1:0] regsrc_out;
wire [3:0] alucontrol_out;

wire [3:0] RA1, RA2;
wire [31:0] RD1, RD2, ALUResult, PC, Instr;



CONTROL CTRL
    (
	  .clk(clk),
	  .Cond(cond_out),
	  .Op(op_out),
	  .Funct(funct_out),
	  .Rd(rd_out),
	  
	  .Z(z_out),
	  
	  .PCSrc(pcsrc_out),
	  .RegWrite(regwrite_out),
	  .MemWrite(memwrite_out),
	  .MemtoReg(memtoreg_out),
	  .ALUSrc(alusrc_out),
	  .ImmSrc(immsrc_out),
	  .RegSrc(regsrc_out),
	  .ALUControl(alucontrol_out)
	  
    );

DATAPATH #(.WIDTH(32)) DP
    (
	  .clk(clk), 
	  .reset(reset),
	  
	  .ALUSrc(alusrc_out), 
	  .MemtoReg(memtoreg_out), 
	  .Reg_Write(regwrite_out), 
	  .PCSrc(pcsrc_out), 
	  .Mem_Write(memwrite_out), 
	  .ImmSrc(immsrc_out),
	  .RegSrc(regsrc_out),
	  .ALUControl(alucontrol_out),
	  
	  .Cond(cond_out),
	  .Op(op_out),
	  .Funct(funct_out),
	  .Rd(rd_out),
	  
	  .Result(result),
	  .RA1(RA1), .RA2(RA2), .RD1(RD1), .RD2(RD2), .ALUResult(ALUResult), .PC(PC), .Instr(Instr),	
	  .Z(z_out)
    );	 
				
endmodule

/*

	  output [3:0] RA1, RA2,
	  output [WIDTH-1:0] RD1, RD2, ALUResult, PC, Instr,
	  
	  */