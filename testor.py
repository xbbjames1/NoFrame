# -*- coding: utf-8 -*-
#!/Users/StormX/Documents/PythonCode/TrialProject/EnvironmentSetting/bin/python

import spiders
import sys, inspect
from threading import Thread
from spiders import BaseSpider
from os import listdir
from os.path import isfile, join
from os import walk

def spiderfilter(v_m):
    list_em = []
    for _, i in v_m: 
        if issubclass(i, Thread):
            print i
            list_em.append(i)
    return list_em


if __name__ == "__main__":
    print issubclass(BaseSpider.BaseSpider, BaseSpider.BaseSpider)
    module_list = []

    for _, m in inspect.getmembers(spiders, inspect.ismodule):
        valid_m = inspect.getmembers(m, inspect.isclass)
        module_list += spiderfilter(valid_m)

    for _, obj in inspect.getmembers(sys.modules[BaseSpider.__name__], inspect.isclass):
        # print obj, obj("Hello")
        pass



