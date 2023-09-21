# WebDav Implementation
This drb-driver-webdav module implements the webdav protocol access with DRB data model.

## WebDav Factory and WebDav Node
The module implements the factory model defined in DRB in its node resolver. Based on the python entry point mechanism, this module can be dynamically imported into applications.

The entry point group reference is `drb.driver`.<br/>
The implementation name is `webdav`.<br/>
The factory class is encoded into `drb.driver.webdav`.<br/>
The webdav signature id is  `ee1b4fc6-8da0-11ec-b909-0242ac120002`<br/>

The Webdav can be instantiated from an uri, the `hostname` and a set of optional options. The `ParsedPath` class provided in drb core module can help to manage these inputs.

## Using this module
The project is present in https://www.pypi.org service. it can be freely 
loaded into projects with the following command line:

```commandline
pip install drb-driver-webdav
```
## Access Data
`DrbWebdavNode` manages the webdav protocol to access remote data. The construction
parameter is the host url and a set of optional argument.

```python
from drb.drivers.webdav import DrbWebdavNode

# Anonymous connection
node = DrbWebdavNode(webdav_hostname="hostname")

# Basic Auth connection
node = DrbWebdavNode(webdav_hostname="hostname",
                     webdav_login='user',
                     webdav_password='password'
                     )

# Certificate connection
node = DrbWebdavNode(webdav_hostname="hostname",
                     webdav_login='user',
                     webdav_password='password',
                     webdav_cert_path='/etc/ssl/certs/certificate.crt',
                     webdav_key_path='/etc/ssl/private/certificate.key'
                     )
```
Webdav protocol allows navigation inside the webdav server. To do so this 
implementation is able to provide children of the same DrbWebdavNode type.

## Authentication
Required key is host name or IP address of the WevDAV-server with param name `webdav_hostname`.
For authentication in WebDAV server use `webdav_login`, `webdav_password`.
For an anonymous login do not specify auth properties.
When a proxy server you need to specify settings to connect through it with `proxy_hostname`, `proxy_login` and `proxy_password`.
If you want to use the certificate path to certificate and private key use `webdav_cert_path` and `webdav_key_path`.

## Limitations

None

## Documentation

The documentation of this implementation can be found here https://drb-python.gitlab.io/impl/webdav