# from pyrtl import *
import pyrtl
import io

# Full Adder with Dual Rail
def fa(x_p, x_n, y_p, y_n, cin_p, cin_n):
    
    s_p = (cin_p & ((x_n & y_n) | (x_p & y_p)) ) | (cin_n & ((x_n & y_p) | (x_p & y_n)))
    s_n = (cin_p & ((x_p & y_n) | (x_n & y_p)) ) | (cin_n & ((x_p & y_p) | (x_n & y_n)))

    cout_p = (x_p & y_p) | (y_p & cin_p) | (x_p & cin_p)
    cout_n = (x_n & y_n) | (y_n & cin_n) | (x_n & cin_n)

    return s_p, s_n, cout_p, cout_n

# Testbench
x_p = pyrtl.Input(1, 'x_p')
x_n = pyrtl.Input(1, 'x_n')
y_p = pyrtl.Input(1, 'y_p')
y_n = pyrtl.Input(1, 'y_n')
cin_p = pyrtl.Input(1, 'cin_p')
cin_n = pyrtl.Input(1, 'cin_n')

sum_p = pyrtl.Output(1, 'sum_p')
sum_n = pyrtl.Output(1, 'sum_n')
cout_p = pyrtl.Output(1, 'cout_p')
cout_n = pyrtl.Output(1, 'cout_n')

# Instantiate the Full Adder
output = fa(x_p, x_n, y_p, y_n, cin_p, cin_n)
sum_p <<= output[0]
sum_n <<= output[1]
cout_p <<= output[2]
cout_n <<= output[3]

# Simulation
sim = pyrtl.Simulation()
sim.step({'x_p':0, 'x_n':1, 'y_p':0, 'y_n':1, 'cin_p':0, 'cin_n':1}) #   Correct Output: cout_p = 0, sum_p = 0
sim.step({'x_p':0, 'x_n':1, 'y_p':0, 'y_n':1, 'cin_p':1, 'cin_n':0}) #   Correct Output: cout_p = 0, sum_p = 1
sim.step({'x_p':0, 'x_n':1, 'y_p':1, 'y_n':0, 'cin_p':0, 'cin_n':1}) #   Correct Output: cout_p = 0, sum_p = 1
sim.step({'x_p':0, 'x_n':1, 'y_p':1, 'y_n':0, 'cin_p':1, 'cin_n':0}) #   Correct Output: cout_p = 1, sum_p = 0
sim.step({'x_p':1, 'x_n':0, 'y_p':0, 'y_n':1, 'cin_p':0, 'cin_n':1}) #   Correct Output: cout_p = 0, sum_p = 1
sim.step({'x_p':1, 'x_n':0, 'y_p':0, 'y_n':1, 'cin_p':1, 'cin_n':0}) #   Correct Output: cout_p = 1, sum_p = 0
sim.step({'x_p':1, 'x_n':0, 'y_p':1, 'y_n':0, 'cin_p':0, 'cin_n':1}) #   Correct Output: cout_p = 1, sum_p = 0
sim.step({'x_p':1, 'x_n':0, 'y_p':1, 'y_n':0, 'cin_p':1, 'cin_n':0}) #   Correct Output: cout_p = 1, sum_p = 1
sim.tracer.render_trace()

# Synthesis
# print("Synthesis:")
pyrtl.synthesize()
pyrtl.optimize()

# Output to Verilog file "FA_AND_OR.v"
vfile = open("FA_DR.v", "w")
pyrtl.output_to_verilog(vfile)
vfile.close()

# Print Verilog to terminal
with io.StringIO() as vfile:
    pyrtl.output_to_verilog(vfile)
    print(vfile.getvalue())

# --------- VISUALIZATION ---------

# Trivial Graph Format
tgffile = open("FA_DR.tgf", "w")
pyrtl.output_to_trivialgraph(tgffile)
tgffile.close()

# Graphviz
gvfile = open("FA_DR.DOT", "w")
pyrtl.output_to_graphviz(gvfile)
gvfile.close()

# SVG
# svgfile = open("FA_AND_OR.svg", "w")
# pyrtl.output_to_svg(svgfile) #TODO: Find the problem with outputing to SVG
# svgfile.close()