module CONTROL 
    (
	  input clk,
	  input [3:0] Cond,
	  input [1:0] Op,
	  input [5:0] Funct,
	  input [3:0] Rd,
	  
	  input  Z,
	  
	  output reg PCSrc,
	  output reg RegWrite,
	  output reg MemWrite,
	  output reg MemtoReg,
	  output reg ALUSrc,
	  output reg [1:0] ImmSrc,
	  output reg [1:0] RegSrc,
	  output reg [3:0] ALUControl
	  
    );
	 
reg CondEx;
reg PCS;
reg REGW;
reg MEMW;
reg FLAGW;

reg BRANCH;

//Register_simple HOLD_Z #(.WIDTH(1))(.clk(clk), .reset(0), .DATA(Z), .OUT());
	 

//Conditional Logic (clock)
always @(*) begin

	case(Cond)
	
		4'b0000: // EQ
					if(Z == 1)
						CondEx = 1;
					else
						CondEx = 0;
		
		4'b0001:	// NE
					if(Z == 0)
						CondEx = 1;
					else 
						CondEx = 0;
		
		4'b1110:  // AL
					CondEx = 1;
		
		default: CondEx = 1;
					
		
endcase		
	 
end
	 
// Decoder
always @(*) begin

	case(Op) 
	
		2'b00:	// Data Processing Instruction (OP = 00)
		
			
			case(Funct[4:1]) // Determine the instruction
			
				4'b0100:		// ADD 
					
					begin

					PCSrc			= 1'b0;
					RegWrite		= CondEx ? 1'b1 : 1'b0;
					MemWrite		= 1'b0;
					MemtoReg		= 1'b0;
					ALUSrc		= 1'b0;
					ImmSrc		= 2'b00;
					RegSrc		= 2'b00;
					ALUControl	= 4'b0100;
					
					end
				
				4'b0010:		// SUB (A-B)
					
					begin
					
					PCSrc			= 1'b0;
					RegWrite		= CondEx ? 1'b1 : 1'b0;
					MemWrite		= 1'b0;
					MemtoReg		= 1'b0;
					ALUSrc		= 1'b0;
					ImmSrc		= 2'b00;
					RegSrc		= 2'b00;
					ALUControl	= 4'b0010;
					
					end
					
				4'b0000:		// AND
					
					begin
					

					PCSrc			= 1'b0;
					RegWrite		= CondEx ? 1'b1 : 1'b0;
					MemWrite		= 1'b0;
					MemtoReg		= 1'b0;
					ALUSrc		= 1'b0;
					ImmSrc		= 2'b00;
					RegSrc		= 2'b00;
					ALUControl	= 4'b0000;
					
					end
					
				4'b1100:		// ORR
					
					begin
					
					PCSrc			= 1'b0;
					RegWrite		= CondEx ? 1'b1 : 1'b0;
					MemWrite		= 1'b0;
					MemtoReg		= 1'b0;
					ALUSrc		= 1'b0;
					ImmSrc		= 2'b00;
					RegSrc		= 2'b00;
					ALUControl	= 4'b1100;
					
					end
					
				4'b1101:		// MOV
					
					begin
					
	
					PCSrc			= 1'b0;
					RegWrite		= CondEx ? 1'b1 : 1'b0;
					MemWrite		= 1'b0;
					MemtoReg		= 1'b0;
					ALUSrc		= 1'b0;
					ImmSrc		= 2'b00;
					RegSrc		= 2'b00; // 0X
					ALUControl	= 4'b1101;
					
					end
		
				4'b1010:		// CMP
					
					begin
					

					PCSrc			= 1'b0;
					RegWrite		= 1'b0;
					MemWrite		= 1'b0;
					MemtoReg		= 1'b0;
					ALUSrc		= 1'b0;
					ImmSrc		= 2'b00; // XX
					RegSrc		= 2'b00; 
					ALUControl	= 4'b0010;
					
					end
					
			endcase
			
		2'b01:	// Memory Instruction  (OP = 01)
		
		
			case(Funct[0]) // L bit will indicate the type of instruction
			
				1'b0:		// STR
					
					begin

					
					PCSrc			= 1'b0;
					RegWrite		= 1'b0;
					MemWrite		= CondEx ? 1'b1 : 1'b0;
					MemtoReg		= 1'b0;
					ALUSrc		= 1'b1;
					ImmSrc		= 2'b01;
					RegSrc		= 2'b10;
					ALUControl	= 4'b0100;
					
					
					end
					
				1'b1:		// LDR
					
					begin
					

					
					PCSrc			= 1'b0;
					RegWrite		= CondEx ? 1'b1 : 1'b0;
					MemWrite		= 1'b0;
					MemtoReg		= 1'b1;
					ALUSrc		= 1'b1;
					ImmSrc		= 2'b01;
					RegSrc		= 2'b00; // X0
					ALUControl	= 4'b0100;
				
					
					end
					
				endcase
		
		2'b10:	// Branch Instruction (OP = 10)
		

		
			case(Funct[5:4]) // 2 bits to determine the type of branch operation
			
				2'b00: // B
					
					begin
					

					PCSrc			= CondEx ? 1'b1 : 1'b0;
					RegWrite		= 1'b0;
					MemWrite		= 1'b0;
					MemtoReg		= 1'b0;
					ALUSrc		= 1'b1;
					ImmSrc		= 2'b10;
					RegSrc		= 2'b00; // XX
					ALUControl	= 4'b1101;
					
					end
					
				
				2'b01: // BEQ
				
					begin

					PCSrc			= CondEx ? 1'b1 : 1'b0;
					RegWrite		= 1'b0;
					MemWrite		= 1'b0;
					MemtoReg		= 1'b0;
					ALUSrc		= 1'b1;
					ImmSrc		= 2'b10;
					RegSrc		= 2'b00; // XX
					ALUControl	= 4'b1101;
					
					end
				
				2'b10: // BL
				
					begin
					
					PCSrc			= CondEx ? 1'b1 : 1'b0;
					RegWrite		= 1'b0;
					MemWrite		= 1'b0;
					MemtoReg		= 1'b0;
					ALUSrc		= 1'b1;
					ImmSrc		= 2'b10;
					RegSrc		= 2'b01; // X1
					ALUControl	= 4'b1101;
					
					end
				
				2'b11: // BX
				
					begin
					
					PCSrc			= CondEx ? 1'b1 : 1'b0;
					RegWrite		= 1'b0;
					MemWrite		= 1'b0;
					MemtoReg		= 1'b0;
					ALUSrc		= 1'b1;
					ImmSrc		= 2'b10;
					RegSrc		= 2'b00; // 0X
					ALUControl	= 4'b1101;
					
					end
			
			
			endcase
		endcase
end

 
endmodule