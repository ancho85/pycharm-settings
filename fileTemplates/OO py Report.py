# encoding: ISO8859-1
from OpenOrange import *
from Report import Report

class ${NAME}(Report):

    def defaults(self):
        Report.defaults(self)
        specs = self.getRecord()

    def run(self):
        specs = self.getRecord()