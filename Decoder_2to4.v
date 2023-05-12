module Decoder_2to4
    (
	  input [1:0] IN,
      output reg [3:0] OUT
    );

always @(*) begin
	case(IN)
		2'b00:OUT=4'b0001;
		2'b01:OUT=4'b0010;
		2'b10:OUT=4'b0100;
		2'b11:OUT=4'b1000;
	endcase
end

endmodule
