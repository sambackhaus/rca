from static import Static


def test_static():
    static = Static()
    assert static.get_state() == 0

    static = Static(state=1)
    assert static.get_state() == 1

    static.state = 0
    assert static.get_state() == 0

    static.state = 1
    assert static.get_state() == 1

