from full_adder import FullAdder
from static import Static


def test_full_adder():
    # test matrix
    tm = [
        # Inputs 	Outputs
        # A 	B 	Cin 	Cout 	S
         [0, 	0, 	0, 	    0, 	    0],
         [0, 	0, 	1, 	    0, 	    1],
         [0,	1, 	0, 	    0, 	    1],
         [0, 	1, 	1, 	    1, 	    0],
         [1, 	0, 	0, 	    0, 	    1],
         [1, 	0, 	1, 	    1, 	    0],
         [1, 	1, 	0, 	    1, 	    0],
         [1, 	1, 	1, 	    1, 	    1]
    ]

    for i in range(len(tm)):
        a = tm[i][0]
        b = tm[i][1]

        cin = tm[i][2]
        cout = tm[i][3]

        s = tm[i][4]

        full_adder = FullAdder(a=[Static(a)], b=[Static(b)], cin=[Static(cin)])

        assert full_adder.get_state() == s
        assert full_adder.get_cout() == cout
