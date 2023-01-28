# from pyrtl import *
import pyrtl
import io
# Full Adder using only AND and ORs
# To convert this to only using AND and ORs
# XOR = A&(~B) | (~A)&B
def fa(x, y, cin):
    # sum = x ^ y ^ cin
    # sum = (temp&(~cin)) | ((~temp)&cin) # This wouldn't work since we use an extra NOT for ~temp
    sum = (x & ~y & ~cin) | (~x & y & ~cin) | (~x & ~y & cin) | (x & y & cin)
    cout = x&y | y&cin | x&cin
    return sum, cout

# Testbench
x = pyrtl.Input(1, 'x')
y = pyrtl.Input(1, 'y')
cin = pyrtl.Input(1, 'cin')

sum = pyrtl.Output(1, 'sum')
cout = pyrtl.Output(1, 'cout')

output = fa(x, y, cin)
sum <<= output[0]
cout <<= output[1]

sim = pyrtl.Simulation()
sim.step({'x':0, 'y':0, 'cin':0})
sim.step({'x':0, 'y':0, 'cin':1})
sim.step({'x':0, 'y':1, 'cin':0})
sim.step({'x':0, 'y':1, 'cin':1})
sim.step({'x':1, 'y':0, 'cin':0})
sim.step({'x':1, 'y':0, 'cin':1})
sim.step({'x':1, 'y':1, 'cin':0})
sim.step({'x':1, 'y':1, 'cin':1})
sim.tracer.render_trace()

# Synthesis
# print("Synthesis:")
pyrtl.synthesize()
pyrtl.optimize()

# Output to Verilog file
vfile = open("FA_AND_OR.v", "w")
pyrtl.output_to_verilog(vfile)
vfile.close()

# Print Verilog to terminal
with io.StringIO() as vfile:
    pyrtl.output_to_verilog(vfile)
    print(vfile.getvalue())

# --------- VISUALIZATION ---------

# Trivial Graph Format
tgffile = open("FA_AND_OR.tgf", "w")
pyrtl.output_to_trivialgraph(tgffile)
tgffile.close()

# Graphviz
gvfile = open("FA_AND_OR.DOT", "w")
pyrtl.output_to_graphviz(gvfile)
gvfile.close()

# SVG
# svgfile = open("FA_AND_OR.svg", "w")
# pyrtl.output_to_svg(svgfile)
# svgfile.close()