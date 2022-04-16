from operator import mul
f = open('input.txt', 'r')
line = f.read().strip()
tape = bin(int('f' + line, 16))[6:]

vsum = 0
def read(packet):
    global vsum
    v = int(packet[:3], 2)
    vsum += v
    t = int(packet[3:6], 2)
    cursor = 6
    if t == 4:
        # literal value
        bits = ''
        while True:
            tip = packet[cursor]
            bits += packet[cursor+1:cursor+5]
            cursor += 5
            if tip == '0':
                break
        value = int(bits, 2)
        return (cursor, value)
    length_type = packet[cursor]
    cursor += 1
    values = []
    read_length = 0
    if length_type == '0':
        length = int(packet[cursor: cursor+15], 2)
        cursor += 15
        rl = 0
        to_read = packet[cursor: cursor+length]
        while rl < length:
            (cc, vv) = read(to_read[rl:])
            rl += cc
            values.append(vv)
        read_length = cursor + rl
    elif length_type == '1':
        num_p = int(packet[cursor: cursor+11], 2)
        cursor += 11
        for i in xrange(num_p):
            (cc, vv) = read(packet[cursor:])
            cursor += cc
            values.append(vv)
        read_length = cursor
    else:
        print 'lol error' 
        return None
    
    # Do the types
    if t == 0:
        value = sum(values)
    elif t == 1:
        value = reduce(mul, values)
    elif t == 2:
        value = min(values)
    elif t == 3:
        value = max(values)
    elif t == 5:
        value = 1 if values[0] > values[1] else 0
    elif t == 6:
        value = 1 if values[0] < values[1] else 0
    elif t == 7:
        value = 1 if values[0] == values[1] else 0
    else:
        print 'lol op error'
        return None
    return (read_length, value)

cc, vv = read(tape)
print '---------------'
print vv
