import os, unittest
from deterministic_encryption_utils.encryption.extensions.ModificationTimeFileSaltProvider import ModificationTimeFileSaltProvider
from tests.SaltProviderTestBase import SaltProviderTestBase

class TestModificationTimeFileSaltProvider(SaltProviderTestBase, unittest.TestCase):

    def constructSubject(self):
        return ModificationTimeFileSaltProvider()
    
    def getId(self):
        return 'mtime'

    def testGivenSaltForFile(self):
        tmpFile = os.path.join(self.tmpDir, 'afile')
        open(tmpFile, 'a').close()
        salt = self.subject.getSaltFor(tmpFile)
        self.assertEqual(str(os.path.getmtime(tmpFile)), salt)

    def testDirectoryPath(self):
        tmpDir = os.path.join(self.tmpDir, 'adir')
        os.mkdir(tmpDir)
        with self.assertRaises(ValueError) as _:
            self.subject.getSaltFor(tmpDir)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()