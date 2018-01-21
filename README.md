# pyvomit

This semi-serious module aims to give non-numeric representation to 128 bit identifiers.

Images created so are meant to be more human friendly : easier remembered and compared, uising less display spaced, and retaining a "fingerprint" sense of what an identifier is.

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
