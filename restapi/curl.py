import commands
import sys
import os
import logging

logging.basicConfig(format='===========%(levelname)s:%(message)s=========', 
    level=logging.DEBUG)





# child = subprocess.Popen(['curl -X', method, url, data, '-v'])


def main():
    url = ' http://10.200.44.84:8080/v1/disk/fold1/fqrouter2.12.7.apk '
    head = ' -H "username:test:tester" -H "password:testing" '
    method = ' GET '
    post_data = """ -d '{"key1":"value1"}' """
    data = ''

    if len(sys.argv) > 1:
        method = sys.argv[1]
        logging.debug(sys.argv)
        if sys.argv[1] is 'POST' or 'post':
            # data = post_data
            # tfile = open('swiftconf.conf')
            # data = tfile
            data = '--data-binary "@swiftconf.conf" '
            head += '-H "Content-Type: application/json" '
            logging.debug('head:%s' % head)
            stat = commands.getoutput('curl -X ' + method + head + url + data + ' -v')
            logging.debug('stat:%s' % stat)
    stat = commands.getoutput('curl -X ' + method + head + url + data + ' -v')
    logging.debug('stat:%s' % stat)

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
    main()