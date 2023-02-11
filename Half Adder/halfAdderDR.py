import pyrtl
import io

# A half adder using Dual Rail approach
def halfAdder(x_p, x_n, y_p, y_n):
    # sum = x ^ y
    sum_p = (x_n & y_p) | (x_p & y_n)
    sum_n = (x_p & y_p) | (x_n & y_n)
    carry_p = x_p & y_p
    carry_n = x_n | y_n

    return sum_p, sum_n, carry_p, carry_n

# Testbench
x_p = pyrtl.Input(1, 'x_p')
x_n = ~x_p
# x_n = pyrtl.Input(1, 'x_n')
y_p = pyrtl.Input(1, 'y_p')
# y_n = pyrtl.Input(1, 'y_n')
y_n = ~y_p
sum_p_out = pyrtl.Output(1, 'sum_p')
sum_n_out = pyrtl.Output(1, 'sum_n')
carry_p_out = pyrtl.Output(1, 'carry_p')
carry_n_out = pyrtl.Output(1, 'carry_n')

# Instantiate module
sum_p, sum_n, carry_p, carry_n = halfAdder(x_p, x_n, y_p, y_n)
sum_p_out <<= sum_p
sum_n_out <<= sum_n
carry_p_out <<= carry_p
carry_n_out <<= carry_n

# Simulate
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)
sim.step({'x_p': 0, 'y_p': 0})  # Correct Output: sum_p = 0, sum_n = 1, carry_p = 0, carry_n = 1
sim.step({'x_p': 0, 'y_p': 1})  # Correct Output: sum_p = 1, sum_n = 0, carry_p = 0, carry_n = 1
sim.step({'x_p': 1, 'y_p': 0})  # Correct Output: sum_p = 1, sum_n = 0, carry_p = 0, carry_n = 1
sim.step({'x_p': 1, 'y_p': 1})  # Correct Output: sum_p = 0, sum_n = 1, carry_p = 1, carry_n = 0
sim_trace.render_trace()

# Synthesis
pyrtl.synthesize()
pyrtl.optimize()

# Output Verilog to Terminal
with io.StringIO() as vfile:
    pyrtl.output_to_verilog(vfile)
    print(vfile.getvalue())

# Visualization
# Graphviz Export
gvfile = open("halfAdderDR.DOT", "w")
pyrtl.output_to_graphviz(gvfile)
gvfile.close()