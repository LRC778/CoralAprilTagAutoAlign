from commands2 import Command
from subsystems.coral_subsystem import CoralSubsystem
from constants.constants import Setpoint
from rev import SparkBase

class MoveToL2Command(Command):
    def __init__(self, coral: CoralSubsystem):
        super().__init__()
        self.coral = coral
        self.addRequirements(self.coral)

    def initialize(self):
        pass

    def execute(self):
        self.coral.arm_closed_loop_controller.setReference(Setpoint.Arm.K_LEVEL_2, SparkBase.ControlType.kPosition)
        self.coral.elevator_closed_loop_controller.setReference(Setpoint.Elevator.K_LEVEL_2, SparkBase.ControlType.kPosition)

    def isFinished(self):
        return True

    def end(self, interrupted):
        if interrupted is True:
            return True