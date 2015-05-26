sudo apt-get update
sudo apt-get install curl gcc memcached rsync sqlite3 xfsprogs \
                     git-core libffi-dev python-setuptools
sudo apt-get install python-coverage python-dev python-nose \
                     python-simplejson python-xattr python-eventlet \
                     python-greenlet python-pastedeploy \
                     python-netifaces python-pip python-dnspython \
                     python-mock

# loopback device
sudo mkdir /srv
sudo truncate -s 8GB /srv/swift-disk
sudo mkfs.xfs /srv/swift-disk

sudo echo '/srv/swift-disk /mnt/sdb1 xfs loop,noatime,nodiratime,nobarrier,logbufs=8 0 0' >> /etc/fstab