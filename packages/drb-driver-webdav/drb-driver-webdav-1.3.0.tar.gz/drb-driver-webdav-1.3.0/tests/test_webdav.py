import io
import unittest
from multiprocessing import Process
from unittest.mock import patch

import webdav3.exceptions
from drb.core import DrbNode
from drb.exceptions.core import DrbNotImplementationException
from keyring.credentials import SimpleCredential
from requests.auth import HTTPBasicAuth

from drb.drivers.webdav import DrbWebdavNode
from tests.utility import run_wsgidav_server, WsgiDavTestServer

process = Process(target=run_wsgidav_server)

_test_server = None


def my_credential(service_name, username):
    return SimpleCredential('tester', 'secret')


class TestWebdavNode(unittest.TestCase):
    process = Process(target=run_wsgidav_server)
    _test_server = None
    storage = "http://127.0.0.1:8080/"
    url_false = "https://www.bad_url.com/"
    node = None

    @classmethod
    def setUpClass(cls) -> None:
        cls._test_server = WsgiDavTestServer(with_auth=True, with_ssl=False)
        cls._test_server.start()
        cls.node = DrbWebdavNode(
            webdav_hostname=cls.storage,
            auth=HTTPBasicAuth('tester', 'secret')
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls._test_server.stop()

    def test_name(self):
        self.assertEqual('tests', self.node.name)
        self.assertEqual(
            'test_webdav.py',
            self.node['test_webdav.py'].name
        )

    def test_check_class(self):
        self.assertTrue(issubclass(DrbWebdavNode, DrbNode))

    def test_not_found(self):
        with self.assertRaises(webdav3.exceptions.NoConnection):
            DrbWebdavNode(webdav_hostname=self.url_false)

    def test_namespace_uri(self):
        self.assertIsNone(self.node.namespace_uri)

    def test_value(self):
        self.assertIsNone(self.node.value)

    def test_parent(self):
        self.assertIsNone(self.node.parent)
        child = self.node.children[0]
        self.assertEqual(self.node, child.parent)

    def test_children(self):
        self.assertEqual(6, len(self.node))
        self.assertEqual(2, len(self.node['resources']))

    def test_download(self):
        children = self.node['resources']['test_file.txt']
        with children.get_impl(io.BytesIO) as stream:
            self.assertEqual('This is my awesome test.',
                             stream.read().decode())
        with children.get_impl(io.BytesIO) as stream:
            self.assertEqual('T',
                             stream.read(1).decode())
        with self.assertRaises(DrbNotImplementationException):
            with self.node['resources'].get_impl(io.BytesIO) as stream:
                stream.read().decode()

    def test_attributes(self):
        self.assertIsNotNone(self.node.attributes)
        self.assertIsInstance(self.node.attributes, dict)

    @patch(target="keyring.get_credential", new=my_credential)
    def test_keyring_auth(self):
        node = DrbWebdavNode(
            webdav_hostname=self.storage
        )
        children = node['resources']['test_file.txt']

        with children.get_impl(io.BytesIO) as stream:
            self.assertEqual('This is my awesome test.',
                             stream.read().decode())

        self.assertEqual('tester', node.auth.username)
        self.assertEqual('secret', node.auth.password)
