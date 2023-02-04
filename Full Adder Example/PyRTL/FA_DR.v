// Generated automatically via PyRTL
// As one initial test of synthesis, map to FPGA with:
//   yosys -p "synth_xilinx -top toplevel" thisfile.v

module toplevel(clk, rst, cin_p, x_p, y_p, cout_n, cout_p, sum_n, sum_p);
    input clk;
    input rst;
    input cin_p;
    input x_p;
    input y_p;
    output cout_n;
    output cout_p;
    output sum_n;
    output sum_p;

    wire tmp35;
    wire tmp36;
    wire tmp37;
    wire tmp39;
    wire tmp40;
    wire tmp42;
    wire tmp43;
    wire tmp44;
    wire tmp45;
    wire tmp47;
    wire tmp49;
    wire tmp50;
    wire tmp51;
    wire tmp52;
    wire tmp55;
    wire tmp56;
    wire tmp57;
    wire tmp59;
    wire tmp60;
    wire tmp61;
    wire tmp62;
    wire tmp63;
    wire tmp64;

    // Combinational
    assign cout_n = tmp35;
    assign cout_p = tmp63;
    assign sum_n = tmp52;
    assign sum_p = tmp47;
    assign tmp35 = tmp36 | tmp40;
    assign tmp36 = tmp59 | tmp44;
    assign tmp37 = ~cin_p;
    assign tmp39 = x_p & cin_p;
    assign tmp40 = tmp43 & tmp37;
    assign tmp42 = tmp62 | tmp50;
    assign tmp43 = ~x_p;
    assign tmp44 = tmp51 & tmp37;
    assign tmp45 = tmp59 | tmp61;
    assign tmp47 = tmp49 | tmp60;
    assign tmp49 = cin_p & tmp45;
    assign tmp50 = x_p & tmp51;
    assign tmp51 = ~y_p;
    assign tmp52 = tmp57 | tmp56;
    assign tmp55 = tmp61 | tmp64;
    assign tmp56 = tmp37 & tmp45;
    assign tmp57 = cin_p & tmp42;
    assign tmp59 = tmp43 & tmp51;
    assign tmp60 = tmp37 & tmp42;
    assign tmp61 = x_p & y_p;
    assign tmp62 = tmp43 & y_p;
    assign tmp63 = tmp55 | tmp39;
    assign tmp64 = y_p & cin_p;

endmodule

