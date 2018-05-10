import thread
import time
import requests
import os, sys


def make_request(threadName,delay):
    try: 
        resp = requests.get("http://CloudApp-env.p4qatt7jd3.sa-east-1.elasticbeanstalk.com/insert/%s" % threadName, headers="")
        count = 0
        while resp.status_code == 200:
           count += 1
           if count == 5:
               thread.start_new_thread(make_request, ("%s0" % threadName, 1,))
               count = 0
           time.sleep(delay)
           resp = requests.get("http://CloudApp-env.p4qatt7jd3.sa-east-1.elasticbeanstalk.com/insert/%s" % threadName, headers="")
    except:
        print("Got error after created the %s thread!" % thread._count())
        os._exit(1)

try:
   thread.start_new_thread(make_request, ("1", 2, ))
   thread.start_new_thread(make_request, ("2", 2, ))
except:
   print "Error: unable to start thread"

while 1:
   pass
