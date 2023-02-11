# An attempt at implementing a Full Adder with AND and ORs (with given NOTs of inputs)

import pylse
from helpers import BaseTest, sim_and_gen, pulse_in_period

import unittest

# Define the full adder unit
def full_adder(x_p, x_n, y_p, y_n, cin_p, cin_n):
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

    # Currently uses 10 LA, 8 FA cells. (18 Total)
    # TODO: Optimize it to match optimal solution with 14 total cells
    # Split input to get enough wires

    # Split x_p
    x_ps0, x_p0 = s(x_p)
    x_p1 , x_p2 = s(x_ps0)
    # Split x_n
    x_ns0, x_n0 = s(x_n)
    x_n1 , x_n2 = s(x_ns0)
    # Split y_p
    y_ps0, y_p0 = s(y_p)
    y_p1 , y_p2 = s(y_ps0)
    # Split y_n
    y_ns0, y_n0 = s(y_n)
    y_n1 , y_n2 = s(y_ns0)
    # Split cin_p
    cin_ps0, cin_p0 = s(cin_p)
    cin_p1 , cin_p2 = s(cin_ps0)
    # Split cin_n
    cin_ns0, cin_n0 = s(cin_n)
    cin_n1 , cin_n2 = s(cin_ns0)

    # Define logic gates
    and1 = la(x_p0, y_p0)
    and2 = la(x_n0, y_p1)
    and3 = la(x_p1, y_n0)
    and4 = la(x_n1, y_n1)

    # Split our results
    and1_0, and1_1 = s(and1)
    and4_0, and4_1 = s(and4)

    OR1 = fa(and1_0, and4_0)
    OR2 = fa(and2, and3)

    # Split results
    OR1_0, OR1_1 = s(OR1)
    OR2_0, OR2_1 = s(OR2)

    xy   = fa(x_p2, y_p2)
    xnyn = fa(x_n2, y_n2)

    cxy     = la(cin_p0, xy)
    cnxnyn  = la(cin_n0, xnyn)

    c_p = fa(and1_1, cxy)
    c_n = fa(and4_1, cnxnyn)

    cOR1   = la(cin_p1, OR1_0)
    cnOR2  = la(cin_n1, OR2_0)

    cOR2   = la(cin_p2, OR2_1)
    cnOR1  = la(cin_n2, OR1_1)

    s_p = fa(cOR1, cnOR2)
    s_n = fa(cOR2, cnOR1)

    return s_p, s_n, c_p, c_n

def test_single(a, b, c):
    # Tests input a_p = a, b_p = b at t=0
    # Default times of each signal
    a_p_t, b_p_t, c_p_t = 0, 0, 0
    a_n_t, b_n_t, c_n_t = 1, 1, 1
    if (a == 0):
        a_n_t = 0
        a_p_t = 1
    
    if (b == 0):
        b_n_t = 0
        b_p_t = 1

    if (c == 0):
        c_n_t = 0
        c_p_t = 1
    
    a_p = pylse.inp_at(a_p_t*T, name='a_p')
    a_n = pylse.inp_at(a_n_t*T,  name='a_n')
    b_p = pylse.inp_at(b_p_t*T, name='b_p')
    b_n = pylse.inp_at(b_n_t*T, name='b_n')
    cin_p = pylse.inp_at(c_p_t*T, name='cin_p')
    cin_n = pylse.inp_at(c_n_t*T, name='cin_n')

    return a_p, a_n, b_p, b_n, cin_p, cin_n

def test_multiple(T_ap, T_an, T_bp, T_bn):
    # Provide multiple inputs
    a_p = pylse.inp_at(*T_ap, name='a_p')
    a_n = pylse.inp_at(*T_an,  name='a_n')
    b_p = pylse.inp_at(*T_bp, name='b_p')
    b_n = pylse.inp_at(*T_bn, name='b_n')
    cin_p = pylse.inp_at(*T_cp, name='cin_p')
    cin_n = pylse.inp_at(*T_cn, name='cin_n')
    return a_p, a_n, b_p, b_n, cin_p, cin_n


if __name__ == "__main__":

    T = 80  # duration of a phase

    # Define multiple pulses for testing
    T_ap = [0*T, 2*T, 4*T]
    T_an = [1*T, 3*T, 5*T, 6*T]
    T_bp = [0*T, 2*T, 5*T]
    T_bn = [1*T, 3*T, 4*T, 6*T]
    T_cp = [1*T, 2*T, 6*T]
    T_cn = [0*T, 3*T, 4*T, 5*T]

    # Test input
    a_p, a_n, b_p, b_n, cin_p, cin_n = test_single(1, 1, 1)
    # a_p, a_n, b_p, b_n, cin_p, cin_n = test_multiple(T_ap, T_an, T_bp, T_bn, T_cp, T_cn)

    # Instantiate the output
    s_p, s_n, cout_p, cout_n = full_adder(a_p, a_n, b_p, b_n, cin_p, cin_n)

    # Probe outputs
    pylse.inspect(s_p, 's_p')
    pylse.inspect(s_n, 's_n')
    pylse.inspect(cout_p, 'cout_p')
    pylse.inspect(cout_n, 'cout_n')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()
