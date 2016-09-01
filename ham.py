s1=raw_input("Enter the First strands : ")
s2=raw_input("Enter the second strands : ")
def distance(s1, s2):
    print sum(a != b for a, b in zip(s1, s2))

distance(s1, s2)