import os, unittest
from encviewfuse.encryption.extensions.ModificationTimeFilenameSaltProvider import ModificationTimeFilenameSaltProvider
from tests.SaltProviderTestBase import SaltProviderTestBase

class TestModificationTimeFilenameSaltProvider(SaltProviderTestBase, unittest.TestCase):

    def constructSubject(self):
        return ModificationTimeFilenameSaltProvider()
    
    def getId(self):
        return 'mtime'

    def testGivenSaltForFile(self):
        tmpFile = os.path.join(self.tmpDir, 'afile')
        open(tmpFile, 'a').close()
        salt = self.subject.getSaltFor(tmpFile)
        self.assertEqual(str(os.path.getmtime(tmpFile)), salt)
        
    def testGivenSaltForDirectory(self):
        tmpDir = os.path.join(self.tmpDir, 'adir')
        os.mkdir(tmpDir)
        salt = self.subject.getSaltFor(tmpDir)
        self.assertEqual('adir', salt)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()