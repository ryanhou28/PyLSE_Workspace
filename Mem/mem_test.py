import random

import pyrtl
from pyrtl import *
import pylse

class Mem:
    def __init__(self) -> None:
        memvals, mem_block = Mem.init_mem_block()
        self.block = mem_block
        self.memvals = memvals

        sim_trace, sim = self.init_mem_sim()
        self.sim_trace = sim_trace
        self.sim = sim

    def init_mem_block():
        mem = MemBlock(bitwidth=2, addrwidth=2, name='mem')

        waddr = Input(2, 'waddr')
        raddr = Input(2, 'raddr')
        wdata = Input(2, 'wdata')
        we = Input(1, 'we')
        
        rdata = Output(2, 'rdata')

        # Ports
        rdata <<= mem[raddr]

        WE = MemBlock.EnabledWrite
        mem[waddr] <<= WE(wdata, we)
        
        mem_init = {addr: 1 for addr in range(4)}
        memvals = {mem: mem_init}
        
        mem_block = pyrtl.working_block()
        return memvals, mem_block
    
    def init_mem_sim(self):
        sim_trace = pyrtl.SimulationTrace(block = self.block)
        sim = pyrtl.Simulation(tracer=sim_trace, memory_value_map=self.memvals, block=self.block)
        return sim_trace, sim

    # def sim_step(self, simvals: dict[str, str]):
    # Above line gives Error: TypeError: 'type' object is not subscriptable
    def sim_step(self, simvals):
        self.sim.step(simvals)
        self.sim_trace.render_trace()

    def inspect(self):
        return self.sim.inspect('rdata')
        
mem = Mem()

w, r, d = 0, 0, 0

@pylse.hole(delay=5.0, inputs=['w1', 'w0', 'r1', 'r0', 'd1', 'd0', 'we', 'clk'], outputs=['o2', 'o1', 'o0'])
def multiply(w1, w0, r1, r0, d1, d0, we, clk, time):
    global w, r, d

    w |= w1 * 2 + w0
    r |= r1 * 2 + r0
    d |= d1 * 2 + d0

    simvals = {
        'we': we,
        'waddr': w,
        'wdata': d,
        'raddr': r
    }

    mem.sim_step(simvals)
    value = mem.inspect()

    if clk:
        assert w <= 3
        assert r <= 3
        assert d <= 3
        w, r, d = 0, 0, 0
        value *= 2
    else:
        value = 0

    return ((value >> 2) & 1), ((value >> 1) & 1), value & 1


w1 = pylse.inp_at(   75,125,                    425,    525, name='w1')
w0 = pylse.inp_at(25,   125,                    425, name='w0')
r1 = pylse.inp_at(                      325,375,    475,525, name='r1')
r0 = pylse.inp_at(                  275,    375,    475, name='r0')
d1 = pylse.inp_at(                          375,425,    525, name='d1')
d0 = pylse.inp_at(                  275        ,425, name='d0')
we = pylse.inp_at(25,75,125,175,                425,    525, name='we')
clk = pylse.inp(start=50, period=50, n=16, name='clk')

q2, q1, q0 = multiply(w1, w0, r1, r0, d1, d0, we, clk)

pylse.inspect(q2, 'q2')
pylse.inspect(q1, 'q1')
pylse.inspect(q0, 'q0')


sim = pylse.Simulation()
events = sim.simulate()

sim.plot(wires_to_display=['clk', 'w1', 'w0', 'r1', 'r0', 'd1', 'd0', 'we', 'clk', 'q2', 'q1', 'q0'])