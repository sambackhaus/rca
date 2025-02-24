from xor_gate import XorGate
from static import Static


def test_xor_gate_000():
    # 0 0 -> 0
    a = [Static(0)]
    b = [Static(0)]

    xor_gate = XorGate(a, b)

    assert xor_gate.get_state() == 0


def test_xor_gate_010():
    # 0 1 -> 1
    a = [Static(1)]
    b = [Static(0)]

    xor_gate = XorGate(a, b)

    assert xor_gate.get_state() == 1


def test_xor_gate_100():
    # 1 0 -> 1
    a = [Static(0)]
    b = [Static(1)]

    xor_gate = XorGate(a, b)

    assert xor_gate.get_state() == 1


def test_xor_gate_111():
    # 1 1 -> 0
    a = [Static(1)]
    b = [Static(1)]

    xor_gate = XorGate(a, b)

    assert xor_gate.get_state() == 0
