# 2-1 MUX design with xSFQ

import pylse

import unittest

import os, sys
# Add path of parent directory to import helpers.py
parent_dir = os.path.abspath('..')
sys.path.insert(1, parent_dir)
from helpers import BaseTest, sim_and_gen, pulse_in_period

# Define the mux unit
def mux(x_p, x_n, y_p, y_n, s_p, s_n):
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

    # Currently uses 4 LA, 2 FA cells. (6 Total)

    # Define the actual hardware
    #   FA -> OR
    #   LA -> AND

    # Split wires
    s_p0, s_p1 = s(s_p)
    s_n0, s_n1 = s(s_n)

    # Define logic for o_p
    and1 = la(x_p, s_n0)
    and2 = la(y_p, s_p0)

    o_p = fa(and1, and2)

    # Define logic for o_n. Apply DeMorgan's
    and3 = la(x_n, s_n1)
    and4 = la(y_n, s_p1)

    o_n = fa(and3, and4)

    return o_p, o_n

def test_single(a, b, s):
    # Tests input x_p = a, y_p = b, s_p = s at t=0
    # Default times of each signal
    a_p_t = 0
    a_n_t = 1
    b_p_t = 0
    b_n_t = 1
    s_p_t = 0
    s_n_t = 1
    if (a == 0):
        a_n_t = 0
        a_p_t = 1
    
    if (b == 0):
        b_n_t = 0
        b_p_t = 1
    
    if (s == 0):
        s_n_t = 0
        s_p_t = 1

    a_p = pylse.inp_at(a_p_t*T, name='a_p')
    a_n = pylse.inp_at(a_n_t*T, name='a_n')
    b_p = pylse.inp_at(b_p_t*T, name='b_p')
    b_n = pylse.inp_at(b_n_t*T, name='b_n')
    s_p = pylse.inp_at(s_p_t*T, name = 's_p')
    s_n = pylse.inp_at(s_n_t*T, name = 's_n')

    return a_p, a_n, b_p, b_n, s_p, s_n

def test_multiple(T_ap, T_an, T_bp, T_bn, T_sp, T_sn):
    # Test Multiple Inputs
    a_p = pylse.inp_at(*T_ap, name='a_p')
    a_n = pylse.inp_at(*T_an, name='a_n')
    b_p = pylse.inp_at(*T_bp, name='b_p')
    b_n = pylse.inp_at(*T_bn, name='b_n')
    s_p = pylse.inp_at(*T_sp, name='s_p')
    s_n = pylse.inp_at(*T_sn, name='s_n')

    return a_p, a_n, b_p, b_n, s_p, s_n

if __name__ == "__main__":

    T = 80  # duration of a phase

    # Define multiple pulse times for testing
    T_ap = [0*T,        3*T]
    T_an = [    1*T,2*T]
    T_bp = [0*T,    2*T]
    T_bn = [    1*T,    3*T]
    T_sp = [    1*T,2*T]
    T_sn = [0*T,        3*T]

    # Test single input
    a_p, a_n, b_p, b_n, s_p, s_n = test_single(1, 1, 0)
    # a_p, a_n, b_p, b_n = test_multiple(T_ap, T_an, T_bp, T_bn, T_sp, T_sn)

    # Instantiate the mux module
    o_p, o_n = mux(a_p, a_n, b_p, b_n, s_p, s_n)

    # Probe outputs
    pylse.inspect(o_p, 'o_p')
    pylse.inspect(o_n, 'o_n')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()
