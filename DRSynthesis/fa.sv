module fa(
    input x,
    input y,
    input cin,
    output sum,
    output cout
);
    assign sum = x ^ y ^ cin;
    assign cout = (x & y) | (x & cin) | (y & cin);
endmodule