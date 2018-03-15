# -*- coding: UTF-8 -*-

import time

# 将格式字符串转换为时间戳
a = "2018-02-02 10:45"
print time.mktime(time.strptime(a,"%Y-%m-%d %H:%M"))