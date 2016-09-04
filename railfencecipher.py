from itertools import cycle, chain

msg=raw_input("Enter the message to decode : ")
rails=int(raw_input("Enter the position to decode : "))
def fence_pattern(rails, size):
    zig_zag = cycle(chain(range(rails), range(rails - 2, 0, -1)))
    return zip(zig_zag, range(size))


def encode(msg, rails):
    fence = fence_pattern(rails, len(msg))
    print ''.join(msg[i] for _, i in sorted(fence))


def decode(msg, rails):
    fence = fence_pattern(rails, len(msg))
    fence_msg = zip(msg, sorted(fence))
    print ''.join(char for char, _ in sorted(fence_msg, key=lambda item: item[1][1]))
    
decode(msg, rails)

msg=raw_input("Enter the message to encode : ")
rails=int(raw_input("Enter the position to encode : "))
encode(msg, rails)