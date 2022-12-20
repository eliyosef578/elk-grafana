import logging
import logstash
import sys
import random

host = 'logstash'

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 12000, version=1))
# test_logger.addHandler(logstash.TCPLogstashHandler(host, 5959, version=1))


#test_logger.error('python-logstash: test logstash error message.')
#test_logger.info('python-logstash: test logstash info message.')
#test_logger.warning('python-logstash: test logstash warning message.')

# add extra field to logstash message

number_list = [111, 222, 333, 444, 555]
name_list = ["eli", "moshe", "david", "dave", "may"]
#print('python-logstash: test extra fields', extra=extra)
b=0
a=0
count = 0
from time import sleep
while True:
    sleep(5)
    a = a + 2
    b = b + 3
    strt = bool(random.getrandbits(1))
    DeviceID = random.choice(number_list)
    name1 = random.choice(name_list)
    count = count + 1
    extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': strt,
    #'test_dict': {'a': 1, 'b': 'c'},
    'test_float': a,
    'test_integer': b,
    'device_id': DeviceID,
    'first_name': name1,
    #'test_list': [1, 2, '3'],
}
    t = {"a":a, "b":b, "count":count}

    if count % 2 == 0:
        test_logger.info('python-logstash: test extra fields', extra=extra)
        #logger.error('error count: %s, number of message: %s, test: %s',count,a,b)
    else:
        #logger.info('python-logstash: test logstash info message:{} '.format(count))
        #logger.info('error count: %s, number of message: %s, test: %s',count,a,b)
        print(t)
