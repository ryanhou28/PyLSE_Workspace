# An attempt at implementing a half adder with AND and ORs (with given NOTs of inputs)

import pylse
from helpers import BaseTest, sim_and_gen, pulse_in_period

import unittest

# Define the half adder unit
def half_adder(x_p, x_n, y_p, y_n):
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

    # Define the actual hardware
    #   FA -> OR
    #   LA -> AND

    # Currently uses 4 LA, 4 FA cells. (8 Total)

    # Split the inputs so we have enough wires
    x_ps, x_p0 = s(x_p)
    x_p1, x_p2 = s(x_ps)

    x_ns, x_n0 = s(x_n)
    x_n1, x_n2 = s(x_ns)
    
    y_ps, y_p0 = s(y_p)
    y_p1, y_p2 = s(y_ps)

    y_ns, y_n0 = s(y_n)
    y_n1, y_n2 = s(y_ns)

    # Define logic for carry bit:
    #   c_p = x_p & y_p
    #   c_n = ~(x_p & y_p) = x_n | y_n
    c_p = la(x_p0, y_p0)
    c_n = fa(x_n0, y_n0)

    # Define logic for sum bit
    and1 = la(x_n1, y_p1)
    and2 = la(x_p1, y_n1)

    s_p = fa(and1, and2)

    or1 = fa(x_p2, y_n2)
    or2 = fa(x_n2, y_p2)

    s_n = la(or1, or2)

    return s_p, s_n, c_p, c_n

def test_single(a, b):
    # Tests input a_p = a, b_p = b at t=0
    # Default times of each signal
    a_p_t = 0
    a_n_t = 1
    b_p_t = 0
    b_n_t = 1
    if (a == 0):
        a_n_t = 0
        a_p_t = 1
    
    if (b == 0):
        b_n_t = 0
        b_p_t = 1

    a_p = pylse.inp_at(a_p_t*T, name='a_p')
    a_n = pylse.inp_at(a_n_t*T,  name='a_n')
    b_p = pylse.inp_at(b_p_t*T, name='b_p')
    b_n = pylse.inp_at(b_n_t*T, name='b_n')

    return a_p, a_n, b_p, b_n

def test_multiple(T_ap, T_an, T_bp, T_bn):
    # Test Multiple Inputs
    a_p = pylse.inp_at(*T_ap, name='a_p')
    a_n = pylse.inp_at(*T_an,  name='a_n')
    b_p = pylse.inp_at(*T_bp, name='b_p')
    b_n = pylse.inp_at(*T_bn, name='b_n')

    return a_p, a_n, b_p, b_n

if __name__ == "__main__":

    T = 80  # duration of a phase

    # Define multiple pulse times for testing
    T_ap = [0*T,            3*T]
    T_an = [    1*T,    2*T]
    T_bp = [0*T,        2*T]
    T_bn = [    1*T,        3*T]

    # Test single input
    a_p, a_n, b_p, b_n = test_single(1, 1)
    # a_p, a_n, b_p, b_n = test_multiple(T_ap, T_an, T_bp, T_bn)

    # Call full_adder_xSFQ()
    s_p, s_n, cout_p, cout_n = half_adder(a_p, a_n, b_p, b_n)

    # Probe outputs
    pylse.inspect(s_p, 's_p')
    pylse.inspect(s_n, 's_n')
    pylse.inspect(cout_p, 'cout_p')
    pylse.inspect(cout_n, 'cout_n')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()
