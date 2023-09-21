import os
import sys
import unittest
import uuid
from unittest.mock import patch

import webdav3.client
from drb.core import DrbNode
from drb.core.factory import FactoryLoader
from drb.nodes.logical_node import DrbLogicalNode
from drb.topics.dao import ManagerDao
from drb.topics.topic import TopicCategory

from drb.drivers.webdav.webdav import DrbWebdavFactory, DrbWebdavNode


def my_info(self, path):
    return {'name': 'a name'}


class TestDrbWebdavFactory(unittest.TestCase):
    svc_url = 'http+webdav://my.domain.com/csc'
    svc_url2 = 'https+dav://my.domain.com/csc'
    wrong_url = 'http+odata://my.domain.com/csc'
    fc_loader = None
    topic_loader = None
    webdav_id = uuid.UUID('ee1b4fc6-8da0-11ec-b909-0242ac120002')

    @classmethod
    def setUpClass(cls) -> None:
        cls.fc_loader = FactoryLoader()
        cls.topic_loader = ManagerDao()

    def test_impl_loading(self):
        topic = self.topic_loader.get_drb_topic(self.webdav_id)
        self.assertEqual(self.webdav_id, topic.id)
        self.assertEqual(
            'Web Distributed Authoring and Versioning',
            topic.label
        )
        self.assertIsNone(topic.description)
        self.assertEqual(TopicCategory.PROTOCOL, topic.category)

    def test_impl_signatures(self):
        topic = self.topic_loader.get_drb_topic(self.webdav_id)

        node = DrbLogicalNode(self.svc_url)
        self.assertTrue(topic.matches(node))
        node = DrbLogicalNode(self.svc_url2)
        self.assertTrue(topic.matches(node))
        node = DrbLogicalNode(self.wrong_url)
        self.assertFalse(topic.matches(node))

    @patch(target='webdav3.client.Client.info', new=my_info)
    def test_factory(self):
        node = DrbLogicalNode(self.svc_url)
        res = DrbWebdavFactory().create(node)
        self.assertIsInstance(node, (DrbWebdavNode, DrbNode))
