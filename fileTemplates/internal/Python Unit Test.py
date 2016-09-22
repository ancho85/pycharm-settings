# encoding: ISO8859-1
from OpenOrange import *
import unittest2 as unittest
from PlayeroTestCase import PlayeroTestCase
import mock
from MonkeyPatch import MonkeyPatch
from mocked_records import TestErrorResponse

class TestClass(PlayeroTestCase):
    @classmethod
    def setUpClass(cls):
        cls.emptyRecords()

    @classmethod
    def tearDownClass(cls):
        cls.emptyRecords()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_something(self):
        pass

    @staticmethod
    def emptyRecords():
        from DeleteRecordRoutine import DeleteRecordRoutine
        rut = DeleteRecordRoutine()
        specs = rut.getRecord()
        specs.Table = "RecName"
        rut.run()
        commit()

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestClass))
    return suite