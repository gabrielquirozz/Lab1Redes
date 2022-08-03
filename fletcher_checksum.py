def fletcher32(data, length):
    w_len = length
    c0 = 0
    c1 = 0
    x = 0

    while w_len >= 360:
        for i in range (360):
            c0 = c0 + ord(data[x])
            c1 = c1 + c0
            x = x + 1
        c0 = c0 % 65535
        c1 = c1 % 65535
        w_len = w_len - 360
    
    for i in range (w_len):
       c0 = c0 + ord(data[x])
       c1 = c1 + c0
       x = x + 1
    c0 = c0 % 65535
    c1 = c1 % 65535
    return (c1 << 16 | c0)