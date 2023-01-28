import pyrtl
import io
def fa(x, y, cin):
    sum = x ^ y ^ cin
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

# Output to Verilog
print("Output to verilog")
with io.StringIO() as vfile:
    pyrtl.output_to_verilog(vfile)
    print(vfile.getvalue())