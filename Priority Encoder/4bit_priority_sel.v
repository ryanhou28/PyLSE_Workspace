// Version 1 of a 4-bit Priority Selector using assigns
module priority_sel1(
    input        [3:0] req,
    input               en,
    output logic [3:0] gnt
);
    
    // For each line, check that enable is asserted, its corresponding line is asserted,
    //  and that all the higher bits are not asserted
    assign gnt[3] = en && req[3];
    assign gnt[2] = en && req[2] && ~req[3];
    assign gnt[1] = en && req[1] && ~req[2] && ~req[3];
    assign gnt[0] = en && req[0] && ~req[1] && ~req[2] && ~req[3];

endmodule

// Version 2 of a 4-bit Priority Selector using a combinational block
module priority_sel2(
    input        [3:0] req,
    input               en,
    output logic [3:0] gnt
);
    // Check bits from MSB to LSB
    always_comb begin
        // If bit is asserted and enabled, set the grant lines correspondingly
        if (req[3] && en)
            gnt[3:0] = 4'b1000;
        else if (req[2] && en)
            gnt[3:0] = 4'b0100;
        else if (req[1] && en)
            gnt[3:0] = 4'b0010;
        else if (req[0] && en)
            gnt[3:0] = 4'b0001;
        else
            gnt[3:0] = 4'b0000;
    end
endmodule