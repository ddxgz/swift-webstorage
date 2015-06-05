swift-webstorage
================

The initial content is mostly forked from cschwede/django-swiftbrowser.

TODO
---------------
- ~~Swiftbrowser works as is outside Swift server~~
- Separate login

BUG
---------------
###Swiftbrowser
- return 'unauthorized' after successfully uploaded a object

###Swiftstorage
- containerview redirect to login view when haven't login

Functions
---------------
- Download/upload files from/to Swift
- Share files with links
- Provide API for Android client

Requirements
---------------
- Python >= 2.7 or 3.4
- Django >= 1.7.2
- python-swiftclient >= 2.4.0
- Gunicorn >= 19.0.0


Test Requirements
----------------
- Mock >= 1.0.1
