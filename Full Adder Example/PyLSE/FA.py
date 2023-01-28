# An attempt at implementing a Full Adder with AND and ORs (with given NOTs of inputs)

import pylse
from helpers import BaseTest, sim_and_gen, pulse_in_period

import unittest


def full_adder(x_p, x_n, y_p, y_n, cin_p, cin_n):
    # Define helpers to ensure same delay numbers
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

    # Split the inputs
    cin_p0, cin_p1 = s(cin_p)
    cin_p2, cin_p3 = s(cin_p0)
    cin_p4, cin_p5 = s(cin_p1)

    cin_n0, cin_n1 = s(cin_n)

    x_p0, x_p1 = s(x_p)
    x_p2, x_p3 = s(x_p0)
    x_n0, x_n1 = s(x_n)
    y_p0, y_p1 = s(y_p)
    y_p2, y_p3 = s(y_p0)
    y_n0, y_n1 = s(y_n)


    and_n17 = la(cin_p2, x_p1)
    and_n21 = la(cin_p3, y_p1)
    and_n19 = la(x_p2, y_p2)

    and_n19_0, and_n19_1 = s(and_n19)
    
    and_n5 = la(cin_p4, and_n19_0)
    or_n10 = fa(and_n21, and_n19_1)
    and_n11 = la(x_p3, y_n0)
    and_n13 = la(y_n1, x_n0)
    and_n12 = la(x_n1, y_p3)

    or_n7 = fa(and_n17, or_n10)
    and_n6 = la(cin_p5, and_n13)
    and_n8 = la(and_n11, cin_n0)
    and_n9 = la(cin_n1, and_n12)

    cout = or_n7

    or_n22 = fa(and_n8, and_n9)

    or_n15 = fa(and_n6, or_n22)

    or_n16 = fa(and_n5, or_n15)

    sum = or_n16

    sum_0, sum_1 = s(sum)
    cout_0, cout_1 = s(cout)
    
    s_p = sum_0
    c_p = cout_0

    # s_p = dro(jtl(sum_0), clks[0])
    # s_n = dro(jtl(sum_1), clks[1])
    # c_p = dro(jtl(cout_0), clks[2])
    # c_n = dro(jtl(cout_1), clks[3])

    # return s_p, s_n, c_p, c_n
    return s_p, c_p




if __name__ == "__main__":

    T = 80  # duration of a phase

    # Provided input: a=1, b=1, cin=0
    a_p = pylse.inp_at(0*T, name='a_p')
    a_n = pylse.inp_at(1*T,  name='a_n')
    b_p = pylse.inp_at(0*T, name='b_p')
    b_n = pylse.inp_at(1*T, name='b_n')
    cin_p = pylse.inp_at(1*T, name='cin_p')
    cin_n = pylse.inp_at(0*T, name='cin_n')

    # Call full_adder_xSFQ()
    # s_p, s_n, cout_p, cout_n = full_adder(a_p, a_n, b_p, b_n, cin_p, cin_n)
    s_p, cout_p= full_adder(a_p, a_n, b_p, b_n, cin_p, cin_n)

    # Probe outputs
    # Expected output: s=0, cout=1
    pylse.inspect(s_p, 's_p')
    # pylse.inspect(s_n, 's_n')
    pylse.inspect(cout_p, 'cout_p')
    # pylse.inspect(cout_n, 'cout_n')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()
