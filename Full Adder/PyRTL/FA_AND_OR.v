// Generated automatically via PyRTL
// As one initial test of synthesis, map to FPGA with:
//   yosys -p "synth_xilinx -top toplevel" thisfile.v

module toplevel(clk, rst, cin, x, y, cout, sum);
    input clk;
    input rst;
    input cin;
    input x;
    input y;
    output cout;
    output sum;

    wire tmp25;
    wire tmp26;
    wire tmp29;
    wire tmp30;
    wire tmp31;
    wire tmp32;
    wire tmp33;
    wire tmp34;
    wire tmp35;
    wire tmp36;
    wire tmp39;
    wire tmp40;
    wire tmp41;
    wire tmp42;
    wire tmp43;
    wire tmp44;
    wire tmp45;
    wire tmp46;

    // Combinational
    assign cout = tmp29;
    assign sum = tmp40;
    assign tmp25 = tmp43 & cin;
    assign tmp26 = tmp35 & cin;
    assign tmp29 = tmp32 | tmp41;
    assign tmp30 = tmp33 & tmp36;
    assign tmp31 = tmp34 & tmp36;
    assign tmp32 = tmp43 | tmp45;
    assign tmp33 = x & tmp44;
    assign tmp34 = tmp42 & y;
    assign tmp35 = tmp42 & tmp44;
    assign tmp36 = ~cin;
    assign tmp39 = tmp46 | tmp26;
    assign tmp40 = tmp39 | tmp25;
    assign tmp41 = x & cin;
    assign tmp42 = ~x;
    assign tmp43 = x & y;
    assign tmp44 = ~y;
    assign tmp45 = y & cin;
    assign tmp46 = tmp30 | tmp31;

endmodule

