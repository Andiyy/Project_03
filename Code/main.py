#!/usr/bin/env python
"""The programme for the 'Gipfel-Ei' project (WI-19/20).

RaspberryPi:
    - ID:       141.82.7.65
    - Name:     pi
    - Password: 000

The program controls the two motors. 
"""

from Code.brickpi3 import BrickPi3
from time import sleep, time

__author__ = "Andreas Venturini"
__license__ = "MIT"
__version__ = "0.1.5"
__email__ = "Andreas.Venturini@HS-Augsburg.DE"
__status__ = "In Work"


BP = BrickPi3()
a = BrickPi3().PORT_A
b = BrickPi3().PORT_B


def close_gripper():
    """Closes the gripper."""
    BP.set_motor_position_relative(a, -45)
    sleep(2)


def move_up():
    """ Moves the gripper to the rope drum."""
    # TODO: Change function to BP.set_motor_position_relative()
    #       Saver then the sleep()
    BP.set_motor_power(b, 80)
    BP.get_motor_status(b)
    sleep(9.5)


def move_down():
    """Moves the crab back and then down."""
    BP.set_motor_power(b, -10)
    sleep(3)
    BP.set_motor_power(b, -20)
    sleep(2)
    BP.set_motor_power(b, 0)
    sleep(2)


def open_gripper():
    """Opens the gripper."""
    BP.set_motor_position_relative(a, 45)
    sleep(1)
    BP.set_motor_power(a, 0)


def open_move_up():
    """Moves the open gripper up."""
    BP.set_motor_power(b, 80)
    sleep(1)


def main():
    try:
        start = time()
        close_gripper()
        move_up()
        move_down()
        open_gripper()
        open_move_up()
        stop = time()

        print("Time: ", stop - start)

    except KeyboardInterrupt:
        print('The program was stopped manually!')

    finally:
        BP.reset_all()
        print('Program finished!')


if __name__ == '__main__':
    main()
