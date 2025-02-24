from half_adder import HalfAdder
from static import Static


def test_half_adder():
    # test matrix
    tm = [
        # Inputs 	Outputs
        # A 	B 	Cout 	S
        [0,	    0, 	0, 	    0],
        [0,	    1, 	0, 	    1],
        [1,	    0, 	0, 	    1],
        [1,     1, 	1, 	    0]
    ]

    for i in range(len(tm)):
        a = tm[i][0]
        b = tm[i][1]

        half_adder = HalfAdder(a=[Static(a)], b=[Static(b)])

        assert half_adder.get_state() == tm[i][3]
        assert half_adder.get_cout() == tm[i][2]
