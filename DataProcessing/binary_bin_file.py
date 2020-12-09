filename = 'binary01.bin'
data = 1

with open(filename, "wb") as f:
    f.write(bytearray([data]))