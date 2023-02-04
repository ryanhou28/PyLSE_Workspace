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

    wire tmp38;
    wire tmp39;
    wire tmp40;
    wire tmp42;
    wire tmp43;
    wire tmp44;
    wire tmp45;
    wire tmp46;
    wire tmp47;
    wire tmp48;
    wire tmp49;
    wire tmp50;
    wire tmp51;
    wire tmp52;
    wire tmp53;
    wire tmp54;
    wire tmp56;
    wire tmp57;
    wire tmp58;
    wire tmp59;
    wire tmp61;
    wire tmp62;
    wire tmp63;
    wire tmp64;
    wire tmp65;
    wire tmp67;
    wire tmp68;
    wire tmp70;
    wire tmp71;
    wire tmp72;

    // Combinational
    assign cout_n = tmp49;
    assign cout_p = tmp67;
    assign sum_n = tmp68;
    assign sum_p = tmp39;
    assign tmp38 = ~cin_p;
    assign tmp39 = tmp47 | tmp45;
    assign tmp40 = tmp61 & tmp38;
    assign tmp42 = tmp43 | tmp56;
    assign tmp43 = tmp51 | tmp54;
    assign tmp44 = ~y_p;
    assign tmp45 = tmp58 & cin_p;
    assign tmp46 = tmp72 & y_p;
    assign tmp47 = tmp71 | tmp59;
    assign tmp48 = tmp52 & tmp44;
    assign tmp49 = tmp53 | tmp64;
    assign tmp50 = tmp72 & cin_p;
    assign tmp51 = tmp65 & tmp38;
    assign tmp52 = cin_p & x_p;
    assign tmp53 = tmp65 | tmp62;
    assign tmp54 = tmp50 & y_p;
    assign tmp56 = tmp58 & tmp38;
    assign tmp57 = tmp46 & tmp38;
    assign tmp58 = y_p & x_p;
    assign tmp59 = tmp65 & cin_p;
    assign tmp61 = x_p & tmp44;
    assign tmp62 = tmp72 & tmp38;
    assign tmp63 = y_p & cin_p;
    assign tmp64 = tmp44 & tmp38;
    assign tmp65 = tmp72 & tmp44;
    assign tmp67 = tmp70 | tmp52;
    assign tmp68 = tmp42 | tmp48;
    assign tmp70 = tmp58 | tmp63;
    assign tmp71 = tmp40 | tmp57;
    assign tmp72 = ~x_p;

endmodule

