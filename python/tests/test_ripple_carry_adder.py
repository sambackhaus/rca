from full_adder import FullAdder
from ripple_carry_adder import RippleCarryAdder
from static import Static


def test_ripple_carry_adder():
    n_inputs = 4

    # test matrix
    tm = [
        #           A            B            S
        # Cin  A3 A2 A1 A0  B3 B2 B1 B0  S3 S2 S1 S0  Cout
        # [ 0,   0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0],
        [ 0,   0, 0, 0, 1,  0, 0, 0, 1,  0, 0, 1, 0,  0],
        [ 0,   0, 0, 1, 0,  0, 0, 1, 0,  0, 1, 0, 0,  0],
        [ 0,   0, 0, 1, 1,  0, 0, 1, 1,  0, 1, 1, 0,  0],
        [ 0,   0, 1, 0, 0,  0, 1, 0, 0,  1, 0, 0, 0,  0],
        [ 0,   0, 1, 0, 1,  0, 1, 0, 1,  1, 0, 1, 0,  0],
        [ 0,   0, 1, 1, 0,  0, 1, 1, 0,  1, 1, 0, 0,  0],
        [ 0,   0, 1, 1, 1,  0, 1, 1, 1,  1, 1, 1, 0,  0],
        [ 0,   1, 0, 0, 0,  1, 0, 0, 0,  0, 0, 0, 0,  1],
        [ 0,   1, 0, 0, 1,  1, 0, 0, 1,  0, 0, 1, 0,  1],
        [ 0,   1, 0, 1, 0,  1, 0, 1, 0,  0, 1, 0, 0,  1],
        [ 0,   1, 0, 1, 1,  1, 0, 1, 1,  0, 1, 1, 0,  1],
        [ 0,   1, 1, 0, 0,  1, 1, 0, 0,  1, 0, 0, 0,  1],
        [ 0,   1, 1, 0, 1,  1, 1, 0, 1,  1, 0, 1, 0,  1],
        [ 0,   1, 1, 1, 0,  1, 1, 1, 0,  1, 1, 0, 0,  1],
        [ 0,   1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 0,  1],
        [ 1,   1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1]
    ]

    for i in range(len(tm)):
        cin = tm[i][0]
        
        a3 = tm[i][1]
        a2 = tm[i][2]
        a1 = tm[i][3]
        a0 = tm[i][4]
        
        b3 = tm[i][5]
        b2 = tm[i][6]
        b1 = tm[i][7]
        b0 = tm[i][8]
        
        s3 = tm[i][9]
        s2 = tm[i][10]
        s1 = tm[i][11]
        s0 = tm[i][12]

        cout = tm[i][13]

        rca = RippleCarryAdder(n_inputs=4,
                               a_ins = [
                                 [Static(a0)],
                                 [Static(a1)],
                                 [Static(a2)],
                                 [Static(a3)]
                               ],
                               b_ins = [
                                 [Static(b0)],
                                 [Static(b1)],
                                 [Static(b2)],
                                 [Static(b3)]
                               ],
                               cin=[Static(cin)])
        
        assert [s0, s1, s2, s3] == rca.get_state()
        assert cout == rca.get_cout()