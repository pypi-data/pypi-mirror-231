# -*- coding: utf-8 -*-
import sys
import unittest

sys.path.append("../laonlp")

loader = unittest.TestLoader()
testSuite = loader.discover("tests")
testRunner = unittest.TextTestRunner(verbosity=1)
testRunner.run(testSuite)
