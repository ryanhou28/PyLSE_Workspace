// AND Cells:

// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// 2-input and, 1x
// Q = DIN1 & DIN2
module and2s1 (Q, DIN1, DIN2);
	output Q;
	input  DIN1;
	input  DIN2;
	and _i0 (Q,DIN1,DIN2);
	specify	(DIN1 => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	(DIN2 => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// 2-input AND, 2x
// Q = DIN1 & DIN2
module and2s2 (Q, DIN1, DIN2);
	output Q;
	input  DIN1;
	input  DIN2;
	and _i0 (Q,DIN1,DIN2);
	specify	(DIN1 => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	(DIN2 => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// 2-input AND, 3x
// Q = DIN1 & DIN2
module and2s3 (Q, DIN1, DIN2);
	output Q;
	input  DIN1;
	input  DIN2;
	and _i0 (Q,DIN1,DIN2);
	specify	(DIN1 => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	(DIN2 => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine


// OR Cells:
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// 2-input or, 1x
// Q = DIN1 | DIN2
module or2s1 (Q, DIN1, DIN2);
	output Q;
	input  DIN1;
	input  DIN2;
	or _i0 (Q,DIN1,DIN2);
	specify	(DIN1 => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	(DIN2 => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// 2-input or, 2x
// Q = DIN1 | DIN2
module or2s2 (Q, DIN1, DIN2);
	output Q;
	input  DIN1;
	input  DIN2;
	or _i0 (Q,DIN1,DIN2);
	specify	(DIN1 => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	(DIN2 => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// 2-input or, 3x
// Q = DIN1 | DIN2
module or2s3 (Q, DIN1, DIN2);
	output Q;
	input  DIN1;
	input  DIN2;
	or _i0 (Q,DIN1,DIN2);
	specify	(DIN1 => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	(DIN2 => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine


// Dual Inverter Cells:
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// dual inverter, 1x
// Q1 = !DIN1;Q2 = !DIN2
module di2s1 (Q1, Q2, DIN1, DIN2);
	output Q1;
	output Q2;
	input  DIN1;
	input  DIN2;
	not _i0 (Q1,DIN1);
	not _i1 (Q2,DIN2);
	specify	(DIN1 => Q1) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	(DIN2 => Q2) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// dual inverter, 2x
// Q1 = !DIN1;Q2 = !DIN2
module di2s2 (Q1, Q2, DIN1, DIN2);
	output Q1;
	output Q2;
	input  DIN1;
	input  DIN2;
	not _i0 (Q1,DIN1);
	not _i1 (Q2,DIN2);
	specify	(DIN1 => Q1) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	(DIN2 => Q2) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// dual inverter, 3x
// Q1 = !DIN1;Q2 = !DIN2
module di2s3 (Q1, Q2, DIN1, DIN2);
	output Q1;
	output Q2;
	input  DIN1;
	input  DIN2;
	not _i0 (Q1,DIN1);
	not _i1 (Q2,DIN2);
	specify	(DIN1 => Q1) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	(DIN2 => Q2) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// dual inverter, 4x
// Q1 = !DIN1;Q2 = !DIN2
module di2s4 (Q1, Q2, DIN1, DIN2);
	output Q1;
	output Q2;
	input  DIN1;
	input  DIN2;
	not _i0 (Q1,DIN1);
	not _i1 (Q2,DIN2);
	specify	(DIN1 => Q1) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	(DIN2 => Q2) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// dual inverter, 5x
// Q1 = !DIN1;Q2 = !DIN2
module di2s5 (Q1, Q2, DIN1, DIN2);
	output Q1;
	output Q2;
	input  DIN1;
	input  DIN2;
	not _i0 (Q1,DIN1);
	not _i1 (Q2,DIN2);
	specify	(DIN1 => Q1) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	(DIN2 => Q2) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// dual inverter, 6x
// Q1 = !DIN1;Q2 = !DIN2
module di2s6 (Q1, Q2, DIN1, DIN2);
	output Q1;
	output Q2;
	input  DIN1;
	input  DIN2;
	not _i0 (Q1,DIN1);
	not _i1 (Q2,DIN2);
	specify	(DIN1 => Q1) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	(DIN2 => Q2) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine

// Inverter Cells:
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// inverter, 1x
// Q = !DIN
module i1s1 (Q, DIN);
	output Q;
	input  DIN;
	not _i0 (Q,DIN);
	specify	(DIN => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// inverter, 2x
// Q = !DIN
module i1s2 (Q, DIN);
	output Q;
	input  DIN;
	not _i0 (Q,DIN);
	specify	(DIN => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// inverter, 3x
// Q = !DIN
module i1s3 (Q, DIN);
	output Q;
	input  DIN;
	not _i0 (Q,DIN);
	specify	(DIN => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// inverter, 4x
// Q = !DIN
module i1s4 (Q, DIN);
	output Q;
	input  DIN;
	not _i0 (Q,DIN);
	specify	(DIN => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// inverter, 5x
// Q = !DIN
module i1s5 (Q, DIN);
	output Q;
	input  DIN;
	not _i0 (Q,DIN);
	specify	(DIN => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// inverter, 6x
// Q = !DIN
module i1s6 (Q, DIN);
	output Q;
	input  DIN;
	not _i0 (Q,DIN);
	specify	(DIN => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// inverter, 7x
// Q = !DIN
module i1s7 (Q, DIN);
	output Q;
	input  DIN;
	not _i0 (Q,DIN);
	specify	(DIN => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// inverting buffer, 1x
// Q = !DIN
module ib1s1 (Q, DIN);
	output Q;
	input  DIN;
	not _i0 (Q,DIN);
	specify	(DIN => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// inverting buffer, 2x
// Q = !DIN
module ib1s2 (Q, DIN);
	output Q;
	input  DIN;
	not _i0 (Q,DIN);
	specify	(DIN => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// inverting buffer, 3x
// Q = !DIN
module ib1s3 (Q, DIN);
	output Q;
	input  DIN;
	not _i0 (Q,DIN);
	specify	(DIN => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// inverting buffer, 4x
// Q = !DIN
module ib1s4 (Q, DIN);
	output Q;
	input  DIN;
	not _i0 (Q,DIN);
	specify	(DIN => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine
// Copyright 1998-1999 LEDA Systems, Inc.
`celldefine
// inverting buffer, 5x
// Q = !DIN
module ib1s5 (Q, DIN);
	output Q;
	input  DIN;
	not _i0 (Q,DIN);
	specify	(DIN => Q) = (`ifdef unit_delay 1 `else 0 `endif ,`ifdef unit_delay 1 `else 0 `endif );
	endspecify
endmodule
`endcelldefine