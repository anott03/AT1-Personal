import sys


def change(digit):
    """This method will change the digit from 0 to 1
    @param digit: It will be 0 or 1 which needs to be changed
    @return: The negated digit is returned
    """
    if digit == 1:
        return str(0)
    else:
        return str(1)


def negate(seq):
    """This method gets the entire sequence to be negated
    @param seq: The sequence of 0s and 1s which needs to be negated
    @return strseq: The neagted sequence of seq is returned
    """
    strseq = ''
    for edigit in seq:
        strseq = strseq+change(int(edigit))
    return strseq


def gen_thmorse_seq(noofsets):
    """This method is going to generate the thue-morse sequence
    @param noofsets: The control variable making the sequence finite.
    @return: returns the sequence           
    """
    oseq = '0'
    while noofsets > 0:
        nseq = negate(oseq)
        noofsets = noofsets - 1
        lseq = oseq + nseq
        oseq = lseq
    return lseq

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        gen_thmorse_seq(int(sys.argv[1]))
    else:
        print("Input for noofsets is not given")
