limit=int(raw_input("Enter the limit: "))
def sum_of_multiples(limit, multiples=None):
    if multiples[0] == 0:
        # multiples of 0 don't change the sum
        multiples = multiples[1:]
    print sum(value for value in range(limit)
               if any(value % multiple == 0
                      for multiple in multiples))
                      
sum_of_multiples(limit)