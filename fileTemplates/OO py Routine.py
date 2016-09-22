# encoding: ISO8859-1
from OpenOrange import *
from Routine import Routine

class ${NAME}(Routine):

    @classmethod
    def defaults(cls, routine):
        specs = routine.getRecord()

    def run(self):
        specs = self.getRecord()