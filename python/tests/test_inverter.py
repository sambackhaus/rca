from inverter import Inverter
from static import Static


def test_inverter_0():
    zero = Static(0)
    inverter = Inverter(a=[zero])

    assert inverter.get_state() == 1


def test_inverter_1():
    one = Static(1)
    inverter = Inverter(a=[one])

    assert inverter.get_state() == 0


def test_inverter_two_ones():
    two_ones = [Static(1), Static(1)]
    inverter = Inverter(a=two_ones)

    assert inverter.get_state() == 0


def test_inverter_one_and_zero():
    one_and_zero = [Static(1), Static(0)]
    inverter = Inverter(a=one_and_zero)

    assert inverter.get_state() == 0


def test_inverter_two_zeros():
    two_zeros = [Static(0), Static(0)]
    inverter = Inverter(a=two_zeros)

    assert inverter.get_state() == 1
