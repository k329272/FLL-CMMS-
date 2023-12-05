from pybricks.pupdevices import UltrasonicSensor
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.parameters import Button
from pybricks.parameters import Color
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
system.name("Rooster")
def Setup():
    if (system.reset_reason() == 2):
        print("Rebooting from error")
    print("Booting")
    print("Battery voltage: " + str(battery.voltage()) + " mV")
    print("Battery current: " + str(battery.current()) + " mA")
    if charger.connected():
        if (charger.status() == 1):
            print("Charging")
        else if (charger.status() == 2):
            print("Battery full")
        else:
            print("Error!")
    Dist = UltrasonicSensor(Port.E)
    lights.on(1, 1, 0, 0)
    ArmA = Motor(Port.D)
    ArmB = Motor(Port.F)
    ColorSense = ColorSensor(Port.C)
    ColorSense.lights.off()
    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.B)
    drive_base = DriveBase(left_motor, right_motor, wheel_diameter=89.231, axle_track=100)
    drive_base.use_gyro(True)
    light.blink(color.red, 0.5)
def turnArm(Arm1, Arm2, Mode=1, Speed=500):
    if (Mode = 1):
        ArmA.run_target(Speed, Arm1, then = Stop.HOLD)
        ArmB.run_target(Speed, Arm2, then = Stop.HOLD)
    else :
        ArmB.run_target(Speed, Arm2, then = Stop.HOLD)
        ArmA.run_target(Speed, Arm1, then = Stop.HOLD)
def TrackLine(Distance):
    NewDirection=0
    NewDistance=0
    while (Distance > NewDistance):
        if (ColorSense.color() == "White"):
            if (NewDirection = 1):
                NewDirection = 0
                while (ColorSense.color() != "White"):
                    
