import urllib.request
from PIL import Image


num_bytes_left = 3 * 128 ** 2
all_bytes = b''

while num_bytes_left > 0: 
    all_bytes += urllib.request.urlopen("https://www.random.org/integers/?num=10000&min=0&max=255&col=1&base=10&format=plain&rnd=new").read()
    num_bytes_left -= 10000

random_bytes = [int(x) for x in all_bytes[:-1].decode().split('\n')]

img = Image.new('RGB', (128,128))
pixels = img.load()

for i in range(img.size[0]):    
    for j in range(img.size[1]):
        x = random_bytes.pop()
        y = random_bytes.pop()
        z = random_bytes.pop()
        pixels[i,j] = (x, y, z)

img.show()
img.save("bm.bmp")
