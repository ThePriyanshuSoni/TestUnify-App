import unittest
from UnifyNG.POM.Tests.TestProductCatalogs.addPriceBook import AddPriceBook


tc1 = unittest.TestLoader().loadTestsFromTestCase(AddPriceBook)
sanityTestSuite = unittest.TestSuite([tc1])

unittest.TextTestRunner().run(sanityTestSuite)