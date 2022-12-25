import logging
import logstash
import sys
import random
import uuid
from time import sleep

host = 'logstash'

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 12000, version=1))
# test_logger.addHandler(logstash.TCPLogstashHandler(host, 5959, version=1))


# add extra field to logstash message

device_list = ["10010", "23412", "15674", "12202", "12345"]
version_list = ["0.1.2", "0.7.8", "1.0.0", "1.2.0", "2.0.1"]
mission_list = ["ex-112", "ol-120", "ta-086", "ma-108"]
name_list = ["lionel", "eric", "david", "dave", "Emma", "Mia", "Evelyn"]
noise_list = ["49.8", "38.5", "98.7", "45.7", "48.8", "13.7"]
componnent_list = ["parser", "sender", "db", "viewer", "handler", "crisper"]



b=0
a=0
count = 0

while True:
    sleep(5)
    a = a + 2
    b = b + 3
    count = count + 1
    status = bool(random.getrandbits(1))
    DeviceID = random.choice(device_list)
    Version = random.choice(version_list)
    name = random.choice(name_list)
    noise_level = random.choice(noise_list)
    service = random.choice(componnent_list)
    extra = {
    # 'test_string': 'python version: ' + repr(sys.version_info),
    'status': status,
    #'test_dict': {'a': 1, 'b': 'c'},
    # 'test_float': a,
    # 'test_integer': b,
    'device_id': DeviceID,
    'version': Version,
    'first_name': name,
    'noise': noise_level,
    'service': service,
    'mission': mission_list, 
    'cid': str(uuid.uuid4()),

}
    t = {"a":a, "b":b, "count":count}

    if count % 2 == 0:
        test_logger.info('get message: '+ str(count), extra=extra)
    else:
        print(t)
        test_logger.error('error: ' + str(count), extra=extra)
