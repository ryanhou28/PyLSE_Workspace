// Generated automatically via PyRTL
// As one initial test of synthesis, map to FPGA with:
//   yosys -p "synth_xilinx -top toplevel" thisfile.v

module toplevel(clk, rst, cin_n, cin_p, x_n, x_p, y_n, y_p, cout_n, cout_p, sum_n, sum_p);
    input clk;
    input rst;
    input cin_n;
    input cin_p;
    input x_n;
    input x_p;
    input y_n;
    input y_p;
    output cout_n;
    output cout_p;
    output sum_n;
    output sum_p;

    wire tmp34;
    wire tmp36;
    wire tmp39;
    wire tmp41;
    wire tmp42;
    wire tmp43;
    wire tmp44;
    wire tmp45;
    wire tmp46;
    wire tmp47;
    wire tmp48;
    wire tmp50;
    wire tmp51;
    wire tmp52;
    wire tmp53;
    wire tmp56;
    wire tmp57;
    wire tmp59;
    wire tmp60;
    wire tmp61;

    // Combinational
    assign cout_n = tmp39;
    assign cout_p = tmp42;
    assign sum_n = tmp50;
    assign sum_p = tmp48;
    assign tmp34 = x_n & y_n;
    assign tmp36 = x_n & cin_n;
    assign tmp39 = tmp43 | tmp36;
    assign tmp41 = x_p & y_p;
    assign tmp42 = tmp53 | tmp61;
    assign tmp43 = tmp34 | tmp56;
    assign tmp44 = cin_p & tmp47;
    assign tmp45 = tmp34 | tmp41;
    assign tmp46 = cin_n & tmp47;
    assign tmp47 = tmp60 | tmp57;
    assign tmp48 = tmp51 | tmp46;
    assign tmp50 = tmp44 | tmp52;
    assign tmp51 = cin_p & tmp45;
    assign tmp52 = cin_n & tmp45;
    assign tmp53 = tmp41 | tmp59;
    assign tmp56 = y_n & cin_n;
    assign tmp57 = x_p & y_n;
    assign tmp59 = y_p & cin_p;
    assign tmp60 = x_n & y_p;
    assign tmp61 = x_p & cin_p;

endmodule

