import io
from typing import Any, List

import keyring
from deprecated.classic import deprecated
from drb.core import DrbFactory, DrbNode, ParsedPath
from drb.exceptions.core import DrbNotImplementationException
from drb.nodes.abstract_node import AbstractNode

from requests.auth import AuthBase, HTTPBasicAuth
from webdav3.client import Client
from webdav3.urn import Urn

from drb.drivers.webdav import CertAuth, TokenAuth


class Download(io.BytesIO):

    def __init__(self, path: str, webdav: Client):
        self._buff = bytearray(0)
        self._webdav = webdav
        self.__res = self._webdav.execute_request(
            'download',
            Urn(path).quote()
        )
        self._iter = None
        super().__init__(self.__res.content)

    def __init_generator(self):
        self._iter = self.__res.iter_content(self._webdav.chunk_size)

    def read(self, *args, **kwargs):
        if not (len(args) > 0 and isinstance(
                args[0],
                int
        ) and args[0] > 0):
            with self.__res as resp:
                return resp.content
        if self._iter is None:
            self.__init_generator()
        try:
            self._buff.extend(bytearray(next(self._iter)))
            res = self._buff[0:args[0]]
            del (self._buff[0:args[0]])
            return res
        except StopIteration:
            if len(self._buff) > 0:
                if args[0] < len(self._buff):
                    res = self._buff[0:args[0]]
                    del (self._buff[0:args[0]])
                    return res
                else:
                    return self._buff
            else:
                return bytes(0)

    def close(self) -> None:
        super().close()
        self.__res.close()


class WebdavConnection:
    # TODO: Check If you cannot do with another methods !
    webdav = None

    def __new__(cls, options: dict, auth: AuthBase):
        if cls.webdav is None or cls.webdav.get_url(
                cls.webdav.root
        ) != options.get('webdav_hostname'):
            if isinstance(auth, HTTPBasicAuth):
                options['webdav_login'] = auth.username
                options['webdav_password'] = auth.password
            elif isinstance(auth, CertAuth):
                options['webdav_login'] = auth.username
                options['webdav_password'] = auth.password
                options['cert_path'] = auth.cert_path
                options['key_path'] = auth.key_path
            elif isinstance(auth, TokenAuth):
                options['webdav_token'] = auth.token

            cls.webdav = Client(options)

        return cls.webdav

    def quit(self):
        self.webdav = None


class DrbWebdavNode(AbstractNode):
    """
    Drb node to access webdav server

    Parameters:
         webdav_hostname: url for WebDAV server should contain protocol
                          and ip address or domain name.
         webdav_login: (optional) Login name for WebDAV server.
                       Can be empty when using token auth.
         webdav_password: (optional) Password for WebDAV server.
                          Can be empty when using token auth.
         webdav_token: (optional) Authentication token for WebDAV server.
                       Can be empty when using login/password auth.
         webdav_root: (optional) Root directory of WebDAV server.
                      Default is `/`.
         webdav_cert_path: (optional) Path to client certificate.
         webdav_key_path: (optional) Path to private key of the client
                          certificate.
         webdav_recv_speed: (optional) Rate limit of data download speed in
                            Bytes per second, defaults to unlimited speed.
         webdav_send_speed: (optional) Rate limit of data upload speed
                            in Bytes per second. Defaults to unlimited speed.
         webdav_timeout: (optional) Timeout in seconds used in HTTP connection
                         managed by requests, defaults to 30 seconds.
         webdav_verbose: (optional) Set verbose mode on/off. By default
                         verbose mode is off.

    """

    @staticmethod
    def __to_stream(node: DrbNode, **kwargs) -> io.BytesIO:
        node.webdav = WebdavConnection(node.options, node.auth)
        if int(node @ 'size') >= 0:
            return Download(
                node.path.path,
                node.webdav,
            )
        raise DrbNotImplementationException(
            f'no implementation found')

    def __init__(self, webdav_hostname: str, auth: AuthBase = None, **kwargs):
        super().__init__()
        if '+webdav' in webdav_hostname:
            self.webdav_hostname = webdav_hostname.replace('+webdav', '')
        elif '+dav' in webdav_hostname:
            self.webdav_hostname = webdav_hostname.replace('+dav', '')
        else:
            self.webdav_hostname = webdav_hostname
        if 'options' in kwargs.keys():
            self.options = kwargs.get('options')
        else:
            self.options = {
                'webdav_hostname': webdav_hostname,
                'webdav_root': kwargs.get('webdav_root', None),
                'webdav_recv_speed': kwargs.get('webdav_recv_speed', None),
                'webdav_send_speed': kwargs.get('webdav_send_speed', None),
                'webdav_timeout': kwargs.get('webdav_timeout', 30),
                'webdav_verbose': kwargs.get('webdav_verbose', False),
            }
        self._children: List[DrbNode] = None
        self.parent = kwargs.get('parent', None)
        self._path: DrbNode = kwargs.get('path', None)
        if self.parent:
            self.webdav = self.parent.webdav
        else:
            self.webdav = None
        self._auth = auth
        self.add_impl(io.BytesIO, self.__to_stream)
        self.__init_attr(
            kwargs.get(
                'attributes',
                None
            )
        )
        self.name = self @ 'name'

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        raise NotImplementedError

    def __init_attr(self, attrs: dict = None):
        if attrs is not None:
            for e in attrs.keys():
                if attrs[e] is None:
                    self @= (e, -1)
                else:
                    self @= (e, attrs[e])
        else:
            self.webdav = WebdavConnection(self.options, self.auth)
            self.__init_attr(self.webdav.info(self.path.path))

    @property
    def path(self) -> ParsedPath:
        self.webdav = WebdavConnection(self.options, self._auth)
        if self._path is None:
            self._path = self.webdav.root
        return ParsedPath(self._path)

    @property
    def auth(self) -> AuthBase:
        if self._auth is None:
            credential = keyring.get_credential(
                service_name=self.webdav_hostname,
                username=None
            )
            if credential is not None:
                self._auth = HTTPBasicAuth(
                    credential.username,
                    credential.password
                )
        return self._auth

    @property
    @deprecated(version='1.2.0',
                reason='Only bracket browse should be use')
    def children(self) -> List[DrbNode]:
        self.webdav = WebdavConnection(self.options, self.auth)
        if self._children is None:
            self._children = []
            children_attributes = self.webdav.list(
                self.path.path,
                get_info=True
            )
            for attribute in children_attributes:
                child = DrbWebdavNode(
                    webdav_hostname=self.options.get('webdav_hostname'),
                    options=self.options,
                    parent=self,
                    path=attribute.get('path')
                )
                self._children.append(child)
        return self._children


class DrbWebdavFactory(DrbFactory):

    def _create(self, node: DrbNode) -> DrbNode:
        if isinstance(node, DrbWebdavNode):
            return node
        uri = node.path.name
        return DrbWebdavNode(uri)
