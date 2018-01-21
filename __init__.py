from PIL import Image
import uuid

def gen_palette (integer):
    base_hue = (integer % 7) * 32 - 1
    compl_hue = 255 - base_hue

    return { 
        0: (0, 0, 70),
        1: (0, 0, 130),
        2: (0, 0, 190),
        3: (0, 0, 220),

        4: (base_hue, 200, 200),
        6: (base_hue, 200, 160),
        5: (base_hue, 200, 100),

        7: (base_hue, 80, 200),
        8: (base_hue, 80, 130),

        9: (compl_hue, 200, 160),
        10: (compl_hue, 80, 130),
        }

def pyvomit(myid, name):
    img = Image.new('HSV', (9, 8), "black")
    pixels = img.load()
    bigint = myid.int
    int_to_clr = gen_palette(bigint)
    for j in range(img.size[1]):
        for i in range((img.size[0] + 1) // 2):
            pixels[i,j] = int_to_clr[bigint % 11]
            pixels[img.size[0] - i - 1,j] = int_to_clr[bigint % 11]
            bigint = bigint // 11
    img = img.resize((img.size[0] * 5,img.size[1] * 5))
    img.convert('RGB').save(name)
