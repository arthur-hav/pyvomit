# pyvomit

This semi-serious module aims to give non-numeric representation to 128 bit identifiers.

Images created so are meant to be more human friendly : they are easier to remember and to compare, use less display space, and retain more accurately what an identifier is : a fingerprint.

To create images that are not complete garbage, the exporter determines a 11 color palette and use them in a 5\*8 image ((5\*8)^11 > 2^128). Then uses symetry to make it 9\*8. 

Credits to gixi for the original idea.

## Example output

128 bits examples
![example1](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/export0.png)
![example1](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/export1.png)
![example3](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/export2.png)
![example4](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/export3.png)
![example5](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/export4.png)
![example6](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/export5.png)

64 bits examples
![small1](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/small0.png)
![small1](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/small1.png)
![small3](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/small2.png)
![small4](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/small3.png)
![small5](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/small4.png)
![small6](https://raw.githubusercontent.com/arthur-hav/pyvomit/master/examples/small5.png)

## Usage

    import pyvomit
    import uuid
    pyvomit.pyvomit128(uuid.uuid4().int, 'path/to/image.png')
