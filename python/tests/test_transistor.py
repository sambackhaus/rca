from transistor import Transistor
from static import Static


def test_transistor():
    t1 = Transistor()
    assert t1.get_state() == 0

    static_state_1 = Static(state=1)

    t1.a.append(static_state_1)
    assert t1.get_state() == 0

    t1.b.append(static_state_1)
    assert t1.get_state() == 1
