import pyrtl
import io

# A half adder
def halfAdder(x, y):
    sum = x ^ y
    carry = x & y
    return sum, carry

# Testbench
x = pyrtl.Input(1, 'x')
y = pyrtl.Input(1, 'y')
sum_out = pyrtl.Output(1, 'sum')
carry_out = pyrtl.Output(1, 'carry')

# Instantiate module
sum, carry = halfAdder(x, y)
sum_out <<= sum
carry_out <<= carry

# Simulate
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)
sim.step({'x': 0, 'y': 0})
sim.step({'x': 0, 'y': 1})
sim.step({'x': 1, 'y': 0})
sim.step({'x': 1, 'y': 1})
sim_trace.render_trace()

# Synthesis
pyrtl.synthesize()
pyrtl.optimize()

# Output Verilog to Terminal
with io.StringIO() as vfile:
    pyrtl.output_to_verilog(vfile)
    print(vfile.getvalue())
