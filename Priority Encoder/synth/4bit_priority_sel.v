/* Generated by Yosys 0.25+99 (git sha1 54bf15a5b, x86_64-apple-darwin20.2-clang 10.0.0-4ubuntu1 -fPIC -Os) */

(* top =  1  *)
(* src = "4bit_priority_sel.v:2.1-15.10" *)
module priority_sel1(req, en, gnt);
  (* src = "4bit_priority_sel.v:11.21-11.33" *)
  wire _00_;
  (* src = "4bit_priority_sel.v:12.21-12.33" *)
  wire _01_;
  (* src = "4bit_priority_sel.v:12.21-12.44" *)
  wire _02_;
  (* src = "4bit_priority_sel.v:13.21-13.33" *)
  wire _03_;
  (* src = "4bit_priority_sel.v:13.21-13.44" *)
  wire _04_;
  (* src = "4bit_priority_sel.v:13.21-13.55" *)
  wire _05_;
  (* src = "4bit_priority_sel.v:11.37-11.44" *)
  wire _06_;
  (* src = "4bit_priority_sel.v:12.37-12.44" *)
  wire _07_;
  (* src = "4bit_priority_sel.v:13.37-13.44" *)
  wire _08_;
  (* src = "4bit_priority_sel.v:4.25-4.27" *)
  input en;
  wire en;
  (* src = "4bit_priority_sel.v:5.24-5.27" *)
  output [3:0] gnt;
  wire [3:0] gnt;
  (* src = "4bit_priority_sel.v:3.24-3.27" *)
  input [3:0] req;
  wire [3:0] req;
  assign _00_ = en &(* src = "4bit_priority_sel.v:11.21-11.33" *)  req[2];
  assign gnt[2] = _00_ &(* src = "4bit_priority_sel.v:11.21-11.44" *)  _06_;
  assign _01_ = en &(* src = "4bit_priority_sel.v:12.21-12.33" *)  req[1];
  assign _02_ = _01_ &(* src = "4bit_priority_sel.v:12.21-12.44" *)  _07_;
  assign gnt[1] = _02_ &(* src = "4bit_priority_sel.v:12.21-12.55" *)  _06_;
  assign _03_ = en &(* src = "4bit_priority_sel.v:13.21-13.33" *)  req[0];
  assign _04_ = _03_ &(* src = "4bit_priority_sel.v:13.21-13.44" *)  _08_;
  assign _05_ = _04_ &(* src = "4bit_priority_sel.v:13.21-13.55" *)  _07_;
  assign gnt[0] = _05_ &(* src = "4bit_priority_sel.v:13.21-13.66" *)  _06_;
  assign gnt[3] = en &(* src = "4bit_priority_sel.v:10.21-10.33" *)  req[3];
  assign _08_ = ~(* src = "4bit_priority_sel.v:13.37-13.44" *) req[1];
  assign _07_ = ~(* src = "4bit_priority_sel.v:13.48-13.55" *) req[2];
  assign _06_ = ~(* src = "4bit_priority_sel.v:13.59-13.66" *) req[3];
endmodule