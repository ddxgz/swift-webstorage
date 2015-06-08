swift-webstorage-restapi
================

API v1:
---------------
get

> /v1/disk/

>> /v1/disk/{path2file or path}

put

> /v1/disk/

>> /v1/disk/{path2file or path}

delete

> /v1/disk/{path2file or path}


TODO
---------------
- Separate login

BUG
---------------


Functions
---------------
- Download/upload files from/to Swift
- Share files with links
- Provide API for Android client

Requirements
---------------
- Python >= 2.7 or 3.4
- python-swiftclient >= 2.4.0
- Gunicorn or uWsgi
