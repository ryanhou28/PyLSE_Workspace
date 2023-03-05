`celldefine
module andDR (out_p, out_n, in1_p, in1_n, in2_p, in2_n);
    output out_p;
    output out_n;
    input in1_p;
    input in1_n;
    input in2_p;
    input in2_n;

    and _and1 (out_p, in1_p, in2_p);
    or _or1 (out_n, in1_n, in2_n);
    // assign out_p = in1_p & in2_p;
    // assign out_n = in1_n | in2_n;

endmodule
`endcelldefine

`celldefine
module orDR (out_p, out_n, in1_p, in1_n, in2_p, in2_n);
    output out_p;
    output out_n;
    input in1_p;
    input in1_n;
    input in2_p;
    input in2_n;

    or _or1 (out_p, in1_p, in2_p);
    and _and1 (out_n, in1_n, in2_n);
    // assign out_p = in1_p | in2_p;
    // assign out_n = in1_n & in2_n;

endmodule
`endcelldefine

`celldefine
module notDR (out_p, out_n, in_p, in_n);
    output out_p;
    output out_n;
    input in_p;
    input in_n;

    not (out_p, in_p);
    not (out_n, in_n);

endmodule
`endcelldefine