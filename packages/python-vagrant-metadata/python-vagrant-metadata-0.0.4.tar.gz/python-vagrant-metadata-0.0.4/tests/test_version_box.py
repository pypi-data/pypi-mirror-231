"""
Test VersionBox and VersionBoxList class
"""

from unittest import TestCase, main as unittest_main

from vagrant_metadata.provider import Provider
from vagrant_metadata.version_box import VersionBox


class TestVagrantVersionBoxClass(TestCase):

    def test_version_have_provider(self):
        version = VersionBox('1.0.0', providers=[
            Provider("libvirt", "", "", ""),
            Provider("virtualbox", "", "", "")
        ])
        self.assertTrue(version.have_provider('libvirt'))
        self.assertFalse(version.have_provider('hyperV'))

    def test_version_empty_provider(self):
        version = VersionBox('1.0.0')
        self.assertFalse(version.have_provider('libvirt'))
        self.assertEqual(version.provider('libvirt'), None)
        with self.assertRaises(AttributeError):
            version.libvirt  # pylint: disable=E1101

    def test_version_provider(self):
        p = Provider("libvirt", "", "", "")
        version = VersionBox('1.0.0', providers=[
            p,
            Provider("virtualbox", "", "", "")
        ])
        self.assertEqual(version.provider('libvirt'), p)
        self.assertEqual(version['libvirt'], p)

    def test_version_compare_attribut_version(self):
        version = VersionBox('1.0.0')
        self.assertFalse(version.version < VersionBox('0.0.1').version)
        self.assertFalse(version.version > VersionBox('1.0.1').version)
        self.assertTrue(version.version == VersionBox('1.0.0').version)

    def test_version_compare(self):
        version = VersionBox('1.0.0', [])
        self.assertFalse(version < VersionBox('0.0.1'))
        self.assertFalse(version > VersionBox('1.0.1'))
        self.assertTrue(version == VersionBox('1.0.0'))


if __name__ == '__main__':
    unittest_main()
