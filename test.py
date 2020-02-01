#!/usr/bin/env python

from brickpi3 import BrickPi3
import time


BP = BrickPi3()

b = BrickPi3().PORT_B

BP.set_motor_limits(port=b, power=100, dps=0)
BP.set_motor_position_relative(b, -7000)
time.sleep(10)

BP.reset_all()

"""while True:
    print(BP.get_motor_encoder(a))
    time.sleep(0.5)"""