import commands
import sys
import os
import logging

logging.basicConfig(format='===========%(levelname)s:%(message)s=========', 
    level=logging.DEBUG)



uploadcurl = 'curl -i https://swift-cluster.example.com/v1/my_account/container/photos/ -X POST \
       -F max_file_size=5373952000 -F max_file_count=1 -F expires=%s \
       -F signature=%s \
       -F redirect=https://example.com/done.html \
       -F file=@/home/pc/b.py'

# child = subprocess.Popen(['curl -X', method, url, data, '-v'])


def main():
    url = ' http://10.200.44.84:8080/v1/disk/fold1/fqrouter2.12.7.apk '
    head = ' -H "username:test:tester" -H "password:testing" '
    method = ' GET '
    post_data = """ -d '{"key1":"value1"}' """
    data = ''

    if len(sys.argv) > 1:
        # method = sys.argv[1]
        logging.debug(sys.argv[1])
        # if cmp(sys.argv[1], 'POST' or 'post'):
        #     # data = post_data
        #     # tfile = open('swiftconf.conf')
        #     # data = tfile
        #     method = ' PUT '
        #     data = '--data-binary "@swiftconf.conf" '
        #     head += '-H "Content-Type: application/json" '
        #     url = ' http://10.200.44.84:8080/v1/disk/swiftconf.conf '
        #     logging.debug('head:%s' % head)
        #     stat = commands.getoutput('curl -X ' + method + head + url + data + ' -v')
        #     logging.debug('stat:%s' % stat)

        # if cmp(sys.argv[1], 'PUT' or 'put'):
        #     method = ' PUT '
        #     url = ' http://10.200.44.84:8080/v1/disk/fold1/subfole1/swiftconf.conf '
        #     data = """ -d '{"file": "b.py"}' """
        #     stat = commands.getoutput('curl -X ' + method + head + url + data + ' -v')
        #     logging.debug('---stat:%s' % stat)

        # if cmp(sys.argv[1], 'DELETE' or 'delete'):
        #     method = ' DELETE '
        #     url = ' http://10.200.44.84:8080/v1/disk/a.py '
        #     data = """ -d '{"file": "b.py"}' """
        #     stat = commands.getoutput('curl -X ' + method + head + url + data + ' -v')
        #     logging.debug('---stat:%s' % stat)


    # stat = commands.getoutput('curl -X ' + method + head + url + data + ' -v')
    # logging.debug('stat:%s' % stat)

    # option = sys.argv[1]
    # filename = sys.argv[2]
    # if option == '--count':
    #   print_words(filename)
    # elif option == '--topcount':
    #   print_top(filename)
    # else:
    #   print 'unknown option: ' + option
    #   sys.exit(1)

if __name__ == '__main__':
    puturl='http://10.200.46.211:8080/v1/AUTH_test/disk/b.py?temp_url_sig=84f8a72c332bc47eb3dd0b9bedc24f8cc481e239&temp_url_expires=1433733460'
    # stat = commands.getoutput('curl -i http://10.200.46.211:8080/v1/AUTH_test/disk/swiftconf.conf -X POST \
    #    -F max_file_size=5373952000 -F max_file_count=1 -F expires=1433733751 \
    #    -F signature=9c0f7ac2d6bb5a32371e0087980d517430ef8127 \
    #    -F redirect=http://10.200.46.211:8080 \
    #    -F file=@swiftconf.conf')
    # stat = commands.getoutput('curl -X POST -T curl.py -D -\
    #     -H "X-Auth-Token: AUTH_tk237f2dde05dc419c8ee825bb9d6e2f60"\
    #     http://10.200.46.211:8080/v1/AUTH_test/disk/curl.py')

    ## this is ok to upload a file
    stat = commands.getoutput('curl -X PUT --data-binary "@curl.py" \
        -H "X-Auth-Token: AUTH_tk237f2dde05dc419c8ee825bb9d6e2f60"\
        http://10.200.46.211:8080/v1/AUTH_test/disk/curl.py')
    logging.debug('put stat:%s' % stat)
    main()