"""
Test utils functions
"""
import requests_mock

from unittest import TestCase, main as unittest_main
from vagrant_metadata import fetch, forge_metadata_url


class TestVagrantMetadataUtils(TestCase):

    def test_forge_metadata_url_error(self):
        with self.assertRaises(Exception):
            forge_metadata_url('toto')
        with self.assertRaises(Exception):
            forge_metadata_url(None)

    def test_forge_metadata_url_work(self):
        self.assertEqual(forge_metadata_url('name/box'),
                         'https://app.vagrantup.com/name/boxes/box')
        self.assertEqual(forge_metadata_url('name/box/toto'),
                         'https://app.vagrantup.com/name/boxes/box')

    @requests_mock.Mocker()
    def test_fetch(self, mock):
        mock.get('http://test.com', text='''
{
  "description":"Test",
  "short_description":"description",
  "name":"test",
  "versions":[
     {
        "version":"1.0.1",
        "status":"active",
        "description_html":"<h1></h1>",
        "description_markdown":"",
        "providers":[
           {
              "name":"libvirt",
              "url":"https://test.com/test.box",
              "checksum":null,
              "checksum_type":null
           },
           {
              "name":"virtualbox",
              "url":"https://test.com/test.box",
              "checksum":null,
              "checksum_type":null
           }
        ]
     },
     {
        "version":"1.0.0",
        "status":"active",
        "description_html":"<h1></h1>",
        "description_markdown":"",
        "providers":[
           {
              "name":"libvirt",
              "url":"https://test.com/test.box",
              "checksum":null,
              "checksum_type":null
           },
           {
              "name":"virtualbox",
              "url":"https://test.com/test.box",
              "checksum":null,
              "checksum_type":null
           }
        ]
     }
  ]
}
        ''')
        meta = fetch('http://test.com')
        self.assertEqual(meta.name, 'test')
        self.assertEqual(meta.description, 'Test')
        #self.assertEqual(meta['1.0.0'].provider('libvirt').url, "https://test.com/test.box")


if __name__ == '__main__':
    unittest_main()
