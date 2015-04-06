import importlib, os, unittest
from encviewfuse.encryption.extensions.NameFileSaltProvider import NameFileSaltProvider
baseTestModule = importlib.import_module('SaltProviderTestBase')
SaltProviderBaseTest = getattr(baseTestModule, 'SaltProviderBaseTest')

class NameFilenameSaltProviderTest(SaltProviderBaseTest, unittest.TestCase):

    def constructSubject(self):
        return NameFileSaltProvider()
    
    def getId(self):
        return 'filename'

    def testGivenSaltForFile(self):
        tmpFile = os.path.join(self.tmpDir, 'afile')
        open(tmpFile, 'a').close()
        salt = self.subject.getSaltFor(tmpFile)
        self.assertEqual('afile', salt)

    def testDirectoryPath(self):
        tmpDir = os.path.join(self.tmpDir, 'adir')
        os.mkdir(tmpDir)
        with self.assertRaises(ValueError) as _:
            self.subject.getSaltFor(tmpDir)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()