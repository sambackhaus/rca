
from ripple_carry_adder import RippleCarryAdder
from static import Static


if __name__ == "__main__":

    a = int(input("enter a number:"))
    b = int(input("enter another number:"))

    a_bin = format(a, 'b')
    b_bin = format(b, 'b')

    a_bits = [int(v) for v in list(a_bin)]
    b_bits = [int(v) for v in list(b_bin)]

    len_a = len(a_bits)
    len_b = len(b_bits)

    if len_a < len_b:
        num_zeros = len_b - len_a
        a_bits = [0] * num_zeros + a_bits
    elif len_b < len_a:
        num_zeros = len_a - len_b
        b_bits = [0] * num_zeros + b_bits

    a_bin_str = ''.join([str(s) for s in a_bits])
    b_bin_str = ''.join([str(s) for s in b_bits])

    print(f"{a} in binary is: {a_bin_str}")
    print(f"{b} in binary is: {b_bin_str}")

    n_inputs = max(len(a_bits), len(b_bits))
    a_ins = [[Static(i)] for i in a_bits]
    b_ins = [[Static(i)] for i in b_bits]

    rca = RippleCarryAdder(n_inputs=n_inputs, a_ins=a_ins, b_ins=b_ins, cin=[Static(0)])
    rca_s = rca.get_state()

    c_bin_str = ''.join([str(s) for s in rca_s])

    print(f"{a_bin_str} + {b_bin_str} = {c_bin_str}")

    c = int(c_bin_str, 2) 
    print(f"{c_bin_str} in decimal is: {c}")
