module ps_tb;
    // Logic for 8-bit
    logic [1:0] req;
    logic en;
    logic [1:0] gnt;
    logic [1:0] correct_gnt;
    logic req_up;
    logic correct_req_up;
    logic correct;

    // Instantiate the priority selector
    ps ps2(req, en, gnt, req_up);

    // Evaluate correct output
    assign correct_gnt[1]=en&req[1];
    assign correct_gnt[0]=en&req[0]&~req[1];
    assign correct_req_up = req[1] || req[0];
    assign correct=((correct_gnt==gnt) && (correct_req_up == req_up));

    always @(correct)
    begin
        #2
        // Check correctness
        if(!correct)
        begin
            $display("@@@ Incorrect at time %4.0f", $time);
            $display("@@@ gnt=%b, en=%b, req=%b",gnt,en,req);
            $display("@@@ expected result gnt=%b, req_up=%b", correct_gnt, correct_req_up);
            $finish;
        end

    end

    task test_ps2(
        logic [1:0] test_req_in,
        logic       test_en_in
    );
        #5
        req = test_req_in;
        en = test_en_in;
    endtask

    // Counter for for loop
    integer i;

    initial 
    begin
		$dumpvars;

        $monitor("Time:%4.0f req:%b en:%b gnt:%b req_up:%b", $time, req, en, gnt, req_up);
        test_ps2(2'b00, 1);
        test_ps2(2'b01, 1);
        test_ps2(2'b10, 1);
        test_ps2(2'b11, 1);
        test_ps2(2'b00, 0);
        test_ps2(2'b01, 0);
        test_ps2(2'b10, 0);
        test_ps2(2'b11, 0);
        #5
        $finish;
     end // initial
endmodule
