# pyvomit

This semi-serious module aims to give non-numeric representation to 128 bit identifiers.

Images created so are meant to be more human friendly : they are easier remembered and compared, use less display space, and retain more accurately what an identifier is : a fingerprint.

To create images that are not complete garbage, the exporter determines a 11 color palette thanks to the first few bytes use them in a 4\*6 image and use symetry to make it 7\*6. 

Credits to gixi for the original idea.

## Example output

![example1](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/export0.png)
![example1](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/export1.png)
![example3](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/export2.png)
![example4](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/export3.png)
![example5](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/export4.png)
![example6](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/export5.png)

## Usage

    import pyvomit
    pyvomit.pyvomit(uuid.uuid4(), 'path/to/image.png')
