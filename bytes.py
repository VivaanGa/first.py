bytecode = b""

def size(a, b, c, d):
    global bytecode
    bytecode += b"BM" + bytearray([a, b, c, d]) + b"\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00"
    global w, x, y, z
    w, x, y, z = a, b, c, d

def wh(w, h):
    global bytecode
    bytecode += bytearray([w & 0xFF, (w >> 8) & 0xFF, (w >> 16) & 0xFF, (w >> 24) & 0xFF, h & 0xFF, (h >> 8) & 0xFF, (h >> 16) & 0xFF, (h >> 24) & 0xFF])

def cp(n, n2): 
    global bytecode   
    bytecode += bytearray([n, n2]) + b"\x18\x00"

def bitpx(n, n2): 
    global bytecode   
    bytecode += bytearray([n, n2])

def cmpr(a, b, c, d):
    global bytecode
    bytecode += bytearray([a & 0xFF, b & 0xFF, c & 0xFF, d & 0xFF])

def hr(a, b, c, d):
    global bytecode
    bytecode += bytearray([a & 0xFF, b & 0xFF, c & 0xFF, d & 0xFF])

def vr(a, b, c, d):
    global bytecode
    bytecode += bytearray([a & 0xFF, b & 0xFF, c & 0xFF, d & 0xFF])

def nclr(a, b, c, d):
    global bytecode
    bytecode += bytearray([a & 0xFF, b & 0xFF, c & 0xFF, d & 0xFF])

def iclr(a, b, c, d):
    global bytecode
    bytecode += bytearray([a & 0xFF, b & 0xFF, c & 0xFF, d & 0xFF])

def backgroundclr(r, g, b):
    global br, bg, bb
    br, bg, bb = b, g, r

def pxcode(h, w):
    global bytecode
    for rh in range(h):
        for rw in range(w):
            bytecode += bytearray([br, bg, bb])

def rectanglecode(x, y, h, w, **kwargs):
    global bytecode
    b, g, r = kwargs.get("bg", (255, 255, 255))
    
    for rh in range(y, y + h):
        for rw in range(x, x + w):
            if 0 <= rw < w and 0 <= rh < h:
                bytecode += bytearray([b, g, r])
    
# Example usage
size(0, 0, 0x36, 0x00)
wh(100, 100)
cp(1, 0)
cmpr(0, 0, 0, 0)
hr(0, 0, 0, 0)
vr(0, 0, 0, 0)
nclr(0, 0, 0, 0)
iclr(0, 0, 0, 0)
pxcode(100, 100)
rectanglecode(30, 30, 40, 40, bg=(255, 0, 0))
# Save to BMP file
with open("output.bmp", "wb") as f:
    f.write(bytecode)
