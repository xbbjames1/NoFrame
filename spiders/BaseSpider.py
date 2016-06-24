import threading
import time


class BaseSpider(threading.Thread):
    def __init__(self, name):
        super(BaseSpider, self).__init__()
        print "Hi it is nice to have you here Mr.", name


