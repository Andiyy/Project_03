#!/usr/bin/env python
"""Getting the current motor position."""

from brickpi3 import BrickPi3
import time

BP = BrickPi3()
a = BrickPi3().PORT_A
b = BrickPi3().PORT_B


def main():
    """Printing current motor position."""
    try:
        while True:
            print(BP.get_motor_encoder(a))
            print(BP.get_motor_encoder(b))
            time.sleep(0.5)

    except KeyboardInterrupt:
        print('Program finished!')


if __name__ == '__main__':
    main()

