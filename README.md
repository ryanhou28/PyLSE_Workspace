# PyLSE Workspace

## Task Breakdown:
- [X] __Project 1: Logic synthesis of xSFQ circuits__
    - [x] Step 0: Implement and simulate a simple design (e.g., an adder) in Verilog or PyRTL. This design will serve as a running example throughout the project.
    - [x] Step 1:
        - [x] (a) analyze the generated gate netlist--use Design Compiler, Yosys, or any other tool of your preference for this task);
        - [x] (b) use your preferred tool to create a netlist of your example design that contains only AND and OR gates. To achieve this the design needs dual-rail inputs and outputs--read my ISCA 2021 paper (https://ieeexplore.ieee.org/abstract/document/9499888) for more information on this.
    - [x] Step 2: Implement the basic xSFQ gates (https://ieeexplore.ieee.org/abstract/document/9499888) in PyLSE
    - [x] Step 3: Use steps 1b and 2 to simulate your example in PyLSE

- [ ] __Project 2: System simulation in PyLSE__
    - [ ] Step 0: Find and analyze a toy system/architecture design that contains multiple distinct blocks--SuperNPU (https://ieeexplore.ieee.org/document/9251979) is an excellent but maybe a little hard design to start with.
    - [ ] Step 1: Implement and simulate in PyLSE one of the design's basic blocks; feel free to use xSFQ (https://ieeexplore.ieee.org/abstract/document/9499888) or conventional SFQ cells for this. Without the tool extension described in Project 1, you may have to do part of the gate stitching and logic optimization by hand (closely related to what you did in EECS 270).
    - [ ] Step 2: Emulate the remaining blocks using regular Python.
    - [ ] Step 3: Use the PyLSE holes feature to integrate Steps 1&2, and simulate the entire system.
## TODO:
- Optimize the logic expression for the Full Adder PyLSE design to use less gates (currently uses 18 LA/FA cells)
    - Can take a look at [examples/full_adder_xsfq.py](https://github.com/UCSBarchlab/PyLSE/blob/main/examples/full_adder_xsfq.py) in the PyLSE repo, which implements the same module with less elements (14 cells).
    - Figure out how to optimize the current design with Yosys or other synthesis tools. How can we use Yosys's abc command to optimize our dual rail approach?
- We can also implement some other designs (eg MUX, DEMUX, decoder, encoder, priority encoder, etc) using the same process for Project 1
- Start on Project 2:
    - Familiarize ourselves with the designs from SuperNPU (or pick another design with multiple distinct blocks)
    - Decide on a block from the design that we can implement



## Relevant Links
[PyRTL Website](http://ucsbarchlab.github.io/PyRTL/)  
[PyRTL Github](https://github.com/UCSBarchlab/PyRTL)  
[PyRTL Documentation](https://pyrtl.readthedocs.io/en/latest/index.html)  
[PyLSE Github](https://github.com/UCSBarchlab/PyLSE)  

[A helpful GraphViz visualizer](https://dreampuf.github.io/GraphvizOnline/)
