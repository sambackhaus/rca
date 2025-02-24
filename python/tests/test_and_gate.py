from and_gate import AndGate
from static import Static


def test_and_gate_000():
    # 0 0 -> 0
    a = [Static(0)]
    b = [Static(0)]

    and_gate = AndGate(a, b)

    assert and_gate.get_state() == 0


def test_and_gate_010():
    # 0 1 -> 0
    a = [Static(1)]
    b = [Static(0)]

    and_gate = AndGate(a, b)

    assert and_gate.get_state() == 0


def test_and_gate_100():
    # 1 0 -> 0
    a = [Static(0)]
    b = [Static(1)]

    and_gate = AndGate(a, b)

    assert and_gate.get_state() == 0


def test_and_gate_111():
    # 1 1 -> 1
    a = [Static(1)]
    b = [Static(1)]

    and_gate = AndGate(a, b)

    assert and_gate.get_state() == 1
