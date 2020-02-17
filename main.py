#!/usr/bin/env python
"""The program for the 'Gipfel-Ei'-project (WI-19/20).

RaspberryPi:
    - ID:       141.82.7.65
    - Name:     pi
    - Password: 000

The program controls the two motors. 
"""

from brickpi3 import BrickPi3
import time

__author__ = 'Andreas Venturini'
__license__ = 'MIT'
__version__ = '1.0'
__email__ = 'Andreas.Venturini@HS-Augsburg.DE'
__status__ = 'Done'


BP = BrickPi3()
a = BrickPi3().PORT_A
b = BrickPi3().PORT_B


def close_gripper():
    """Closes the gripper."""
    BP.set_motor_position_relative(a, -45)
    time.sleep(2)


def move_up():
    """ Moves the gripper to the rope drum."""
    BP.reset_motor_encoder(b)
    BP.set_motor_limits(b, power=80)

    BP.set_motor_position_kd(b, kd=70)
    BP.set_motor_position_kp(b, kp=70)
    BP.set_motor_position(b, 6710)
    time.sleep(17)


def move_down():
    """Moves the crab back and then down."""
    BP.reset_motor_encoder(b)
    BP.set_motor_limits(b, power=15)
    BP.set_motor_position(b, -200)
    time.sleep(2)


def open_gripper():
    """Opens the gripper."""
    BP.set_motor_power(a, 30)
    time.sleep(1)


def open_move_up():
    """Moves the open gripper up."""
    BP.reset_motor_encoder(b)
    BP.set_motor_limits(b, power=100)
    BP.set_motor_position(b, 200)
    time.sleep(2)


def main():
    try:
        start = time.time()
        close_gripper()
        move_up()
        move_down()
        open_gripper()
        open_move_up()
        print("Time: ", time.time() - start)

    except KeyboardInterrupt:
        print('The program was stopped manually!')

    finally:
        BP.reset_all()
        print('Program finished!')


if __name__ == '__main__':
    main()
