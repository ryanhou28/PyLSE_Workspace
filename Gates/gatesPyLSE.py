# An attempt at implementing a Full Adder with AND and ORs (with given NOTs of inputs)

import pylse
from helpers import BaseTest, sim_and_gen, pulse_in_period

import unittest

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


# DEFINITION OF THE LOGIC GATES:
def OR(x_p, x_n, y_p, y_n):

    or_p = fa(x_p, y_p)
    or_n = la(x_n, y_n)

    return or_p, or_n

def AND(x_p, x_n, y_p, y_n):

    and_p = la(x_p, y_p)
    and_n = fa(x_n, y_n)

    return and_p, and_n

def NAND(x_p, x_n, y_p, y_n):

    nand = fa(x_n, y_n)
    nand_n = la(x_p, y_p)

    return nand, nand_n

def NOR(x_p, x_n, y_p, y_n):

    nor      = la(x_n, y_n)
    nor_n = fa(x_p, y_p)

    return nor, nor_n


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
    # Test Multiple Signals at once
    a_p = pylse.inp_at(*T_ap, name='a_p')
    a_n = pylse.inp_at(*T_an,  name='a_n')
    b_p = pylse.inp_at(*T_bp, name='b_p')
    b_n = pylse.inp_at(*T_bn, name='b_n')

    return a_p, a_n, b_p, b_n

if __name__ == "__main__":

    T = 80  # duration of a phase

    # Define times for multiple pulse testing
    T_ap = [    1*T,2*T,    4*T]
    T_an = [0*T,        3*T,    5*T]
    T_bp = [    1*T,    3*T,4*T]
    T_bn = [0*T,    2*T,        5*T]


    a_p, a_n, b_p, b_n = test_single(1, 1)

    # a_p, a_n, b_p, b_n = test_multiple(T_ap, T_an, T_bp, T_bn)

    # Instantiate the logic module
    out_p, out_n = OR(a_p, a_n, b_p, b_n)

    # Probe outputs
    pylse.inspect(out_p, 'out')
    pylse.inspect(out_n, 'out_n')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()
