import os
import re
class alive():
    def __init__(self, ip):
         self.ip=ip
    def IfAlive(self):
        #输入ip返回是否在线，是T否F
        return_alive=os.system('ping  -n 1 -w 1 %s'%self.ip)
        if return_alive:
            return 'F'
        else:
            return 'T'
    def alive_pings(self):
        #输入ip，返回当前ip，当前丢失率，最短延迟，最长延迟，平均延迟
        return_ping = os.popen('ping %s' % self.ip)
        return_ping_str = return_ping.read()
        regIP = r'\d+\.\d+\.\d+\.\d+'
        regLost = r'\(\d+%'
        regMinimum = r'Minimum = \d+ms|最短 = \d+ms'
        regMaximum = r'Maximum = \d+ms|最长 = \d+ms'
        regAverage = r'Average = \d+ms|平均 = \d+ms'
        ip_now = re.search(regIP, return_ping_str)
        lost_now = re.search(regLost, return_ping_str)
        minimum_now = re.search(regMinimum, return_ping_str)
        maximum_now = re.search(regMaximum, return_ping_str)
        average_now = re.search(regAverage, return_ping_str)
        ip_now_str = ip_now.group()
        lost_now_str = re.search(r'\d', lost_now.group()).group()
        minimum_now_str = re.search(r'\d', minimum_now.group()).group()
        maximum_now_str = re.search(r'\d', maximum_now.group()).group()
        average_now_str = re.search(r'\d', average_now.group()).group()
        return ip_now_str, lost_now_str, minimum_now_str, maximum_now_str, average_now_str