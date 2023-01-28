# PyLSE Workspace

## Relevant Links
[PyRTL Website](http://ucsbarchlab.github.io/PyRTL/)  
[PyRTL Github](https://github.com/UCSBarchlab/PyRTL)  
[PyRTL Documentation](https://pyrtl.readthedocs.io/en/latest/index.html)  
[PyLSE Github](https://github.com/UCSBarchlab/PyLSE)  

[A helpful GraphViz visualizer](https://dreampuf.github.io/GraphvizOnline/)


## Current goals:
- Implement some simple hardware designs in PyRTL/Verilog, take their netlist and implement it in PyLSE

## Progress:
- Created Full Adder in PyRTL with only AND and OR gates (given the NOTs of each input), exported the design to structural verilog and TGF, and implemented the design in PyLSE
    - Full Adder PyRTL: PyRTL/FA_AND_OR.py
    - Full Adder Structural Verilog: PyRTL/FA_AND_OR.v
    - Full Adder TGF: PyRTL/FA_AND_OR.tgf
    - Full Adder PyLSE: PyLSE/FA.py

## TODO:
- Optimize the logic expression for the Full Adder to use less gates (currently uses 15 LA/FA cells), add inverse of outputs (sum_n, cout_n)
    - Can take a look at [examples/full_adder_xsfq.py](https://github.com/UCSBarchlab/PyLSE/blob/main/examples/full_adder_xsfq.py) in the PyLSE repo, which implements a Full Adder with less elements.