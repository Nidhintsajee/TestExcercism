digits=raw_input("Enter the Binary : ")
def parse_binary(digits):
    if set(digits) - set('01'):
        raise ValueError("Invalid binary literal: " + digits)
    print sum(int(digit) * 2 ** i
               for (i, digit) in enumerate(reversed(digits)))

parse_binary(digits)
