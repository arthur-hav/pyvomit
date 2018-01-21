from PIL import Image

def gen_8_palette (integer):
    base_hue = (integer % 16) * 16

    return { 
        1: (0, 0, 100),
        2: (0, 0, 170),
        3: (0, 0, 220),

        4: (base_hue, 200, 200),
        6: (base_hue, 200, 160),
        5: (base_hue, 200, 100),
        7: (base_hue, 80, 200),
        0: (base_hue, 80, 130),

        }

def gen_11_palette (integer):
    base_hue = (integer % 16) * 16
    integer = integer // 8
    compl_hue = 128 - base_hue + (integer % 8) * 16

    return { 
        0: (0, 0, 70),
        1: (0, 0, 130),
        2: (0, 0, 190),
        3: (0, 0, 220),

        4: (base_hue, 200, 200),
        5: (base_hue, 200, 100),

        7: (base_hue, 80, 200),
        8: (base_hue, 80, 130),

        9: (compl_hue, 200, 200),
        6: (compl_hue, 150, 160),
        10: (compl_hue, 80, 130),
        }


def _vomit(bigint, pal, img):
    pixels = img.load()
    for j in range(img.size[1]):
        for i in range((img.size[0] + 1) // 2):
            pixels[i,j] = pal[bigint % len(pal)]
            pixels[img.size[0] - i - 1,j] = pal[bigint % len(pal)]
            bigint = bigint // len(pal)
    if bigint > 0:
        raise ValueError('Integer too big')
    img = img.resize((img.size[0] * 5,img.size[1] * 5))
    return img


def pyvomit128(bigint, name):
    img = Image.new('HSV', (9, 8), "black")
    pal = gen_11_palette(bigint // 8)
    img = _vomit(bigint, pal, img)
    img.convert('RGB').save(name)

def pyvomit64(bigint, name):
    img = Image.new('HSV', (7, 5), "black")
    pal = gen_8_palette(bigint)
    img = _vomit(bigint // 16, pal, img)
    img.convert('RGB').save(name)

def _gen_examples():
    for i in range(6):
        import random
        rng = random.randint(0, 2**128)
        pyvomit128(rng, 'examples/export{i}.png'.format(i=i))
    for i in range(6):
        rng = random.randint(0, 2**64)
        pyvomit64(rng, 'examples/small{i}.png'.format(i=i))

if __name__ == '__main__':
    _gen_examples()
