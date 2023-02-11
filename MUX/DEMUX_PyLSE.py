# 1-2 DEMUX design with xSFQ

import pylse

import unittest

import os, sys
# Add path of parent directory to import helpers.py
parent_dir = os.path.abspath('..')
sys.path.insert(1, parent_dir)
from helpers import BaseTest, sim_and_gen, pulse_in_period

# Define the demux unit
def demux(d_p, d_n, s_p, s_n):
    # Inputs:
        # Data: d_p, d_n
        # Select: s_p, s_n
    # Outputs:
        # A: a_p, a_n
        # B: b_p, b_n

    # Define helpers to ensure same delay numbers (currently the same as PyLSE example)
    def jtl(*args):
        return pylse.jtl(*args, firing_delay=5.7)

    def fa(x, y):
        """ First-arrival cell based on an inverted C-element.
            Inputs buffered with JTL for better flux transmission.
        """
        return pylse.c_inv(jtl(x), jtl(y), firing_delay=9.0)

    def la(x, y):
        """ Last-arrival cell based on a C-element.
            Inputs buffered with JTL for better flux transmission.
        """
        return pylse.c(jtl(x), jtl(y), firing_delay=8.0)

    def s(x):
        return pylse.s(x, firing_delay=4.3)

    def dro(*args):
        return pylse.dro(*args, firing_delay=5.1)

    # Currently uses 2 LA, 2 FA cells. (4 Total)

    # Define the actual hardware
    #   FA -> OR
    #   LA -> AND

    # Split wires
    d_p0, d_p1 = s(d_p)
    d_n0, d_n1 = s(d_n)
    s_p0, s_p1 = s(s_p)
    s_n0, s_n1 = s(s_n)

    # Define logic for A
    a_p = la(d_p0, s_n0)
    a_n = fa(d_n0, s_p0)

    # Define logic for B
    b_p = la(d_p1, s_p1)
    b_n = fa(d_n1, s_n1)

    return a_p, a_n, b_p, b_n

def test_single(d, s):
    # Tests input d_p = d, s_p = s
    # Default times of each signal
    d_p_t = 0
    d_n_t = 1
    s_p_t = 0
    s_n_t = 1
    if (d == 0):
        d_n_t = 0
        d_p_t = 1
    
    if (s == 0):
        s_n_t = 0
        s_p_t = 1

    d_p = pylse.inp_at(d_p_t*T, name='d_p')
    d_n = pylse.inp_at(d_n_t*T, name='d_n')
    s_p = pylse.inp_at(s_p_t*T, name = 's_p')
    s_n = pylse.inp_at(s_n_t*T, name = 's_n')

    return d_p, d_n, s_p, s_n

if __name__ == "__main__":

    T = 80  # duration of a phase

    # Test single input
    d_p, d_n, s_p, s_n = test_single(1, 1)

    # Instantiate DEMUX block
    a_p, a_n, b_p, b_n = demux(d_p, d_n, s_p, s_n)

    # Probe outputs
    pylse.inspect(a_p, 'a_p')
    pylse.inspect(a_n, 'a_n')
    pylse.inspect(b_p, 'b_p')
    pylse.inspect(b_n, 'b_n')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()
