from or_gate import OrGate
from static import Static


def test_or_gate_000():
    # 0 0 -> 0
    a = [Static(0)]
    b = [Static(0)]

    or_gate = OrGate(a, b)

    assert or_gate.get_state() == 0


def test_or_gate_010():
    # 0 1 -> 1
    a = [Static(1)]
    b = [Static(0)]

    or_gate = OrGate(a, b)

    assert or_gate.get_state() == 1


def test_or_gate_100():
    # 1 0 -> 1
    a = [Static(0)]
    b = [Static(1)]

    or_gate = OrGate(a, b)

    assert or_gate.get_state() == 1


def test_or_gate_111():
    # 1 1 -> 1
    a = [Static(1)]
    b = [Static(1)]

    or_gate = OrGate(a, b)

    assert or_gate.get_state() == 1
