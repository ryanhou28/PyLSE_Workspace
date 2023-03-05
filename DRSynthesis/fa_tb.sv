module ps_tb;
    logic x_in;
    logic y_in;
    logic c_in;
    logic sum_out;
    logic cout_out;
    logic correct_sum;
    logic correct_cout;
    logic correct;

    // Instantiate the full adder
    fa fa2(x_in, y_in, c_in, sum_out, cout_out);

    // Evaluate correct output
    logic [1:0] correct_2bit;
    assign correct_2bit = x_in + y_in + c_in;
    assign correct_sum = correct_2bit[0];
    assign correct_cout = correct_2bit[1];

    always @(correct)
    begin
        #2
        // Check correctness
        if(!correct)
        begin
            $display("@@@ Incorrect at time %4.0f", $time);
            $display("@@@ sum = %b, cout = %b", sum_out, cout_out);
            $display("@@@ expected result sum = %b, cout = %b", correct_sum, correct_cout);
            $finish;
        end

    end

    task test_fa(
        logic test_x,
        logic test_y,
        logic test_cin
    );
        #5
        x_in = test_x;
        y_in = test_y;
        c_in = test_cin;
    endtask

    // Counter for for loop
    integer i;

    initial 
    begin
		$dumpvars;

        $monitor("Time:%4.0f x:%b y:%b cin:%b sum:%b cout:%b", $time, x_in, y_in, c_in, sum_out, cout_out);
        test_fa(0, 0, 0);
        test_fa(0, 0, 1);
        test_fa(0, 1, 0);
        test_fa(0, 1, 1);
        test_fa(1, 0, 0);
        test_fa(1, 0, 1);
        test_fa(1, 1, 0);
        test_fa(1, 1, 1);
        #5
        $finish;
     end // initial
endmodule
