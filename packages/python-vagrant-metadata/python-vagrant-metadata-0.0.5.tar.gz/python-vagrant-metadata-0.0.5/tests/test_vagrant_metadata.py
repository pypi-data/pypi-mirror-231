"""
Acceptance test
"""

from unittest import TestCase, main as unittest_main

from vagrant_metadata import fetch, forge_metadata_url


class TestVagrantMetadata(TestCase):
    def test_acceptance(self):
        metadata = fetch(forge_metadata_url('ubuntu/trusty64'))
        url = metadata.url_for('20190514.0.0', 'virtualbox')
        self.assertEqual(
            url, 'https://vagrantcloud.com/ubuntu/boxes/trusty64/versions/20190514.0.0/providers/virtualbox.box')


if __name__ == '__main__':
    unittest_main()
