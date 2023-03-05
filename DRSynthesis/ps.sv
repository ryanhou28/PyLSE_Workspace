// 2-bit Priority Selector
module ps(
    input           [1:0] req,
    input                  en,
    output logic    [1:0] gnt,
    output logic          req_up
);
    // Set grant lines
    assign gnt[1] = en && req[1];
    assign gnt[0] = en && ~req[1] && req[0];
    
    assign req_up = req[1] || req[0];

endmodule