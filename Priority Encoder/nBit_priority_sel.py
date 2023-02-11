from pyrtl import *

#Implementing an n-bit fixed priority seletor
def sel(req, en):
    # Grant request to the most significant line if enabled

    # Get width of the input
    reqWidth = len(req)

    # Declare gnt
    gnt = {}

    # MSB
    gnt[reqWidth - 1] = en & req[reqWidth - 1]

    # Iterate over each bit from MSB to LSB
    for i in reversed(range(reqWidth - 1)):
        # Check if any more significant bits are set
        prev = ~req[i + 1]
        for j in range(i + 1, reqWidth):
            prev = prev & ~req[j]

        # Check for setting conditions
        gnt[i] = en & req[i] & prev

    # Concatenate the grant for each line into a wire of the same length
    gnt_ret = concat_list([gnt[i] for i in range(reqWidth)])

    return gnt_ret

# Testbench
x = Input(4, 'x')
y = Output(4, 'y')

y <<= sel(x, 1)

sim = Simulation()
sim.step_multiple({'x':[*range(16)]})
print("Hexadecimal Trace:")
sim.tracer.render_trace()
print("Binary Trace:")
sim.tracer.render_trace(repr_func=bin, symbol_len=10)

