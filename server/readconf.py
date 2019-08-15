import configparser
import os

nowdir = os.path.dirname(os.path.abspath(__file__))
os.chdir(nowdir)
conf = configparser.ConfigParser()
conf.read("allconf.conf")
def readconf():
    #读取配置文件配置
    #tudo:加入后续配置
    FireOn_smtp_server = conf.get('FireOnConf','smtp_server')
    FireOn_from_who = conf.get('FireOnConf','from_who')
    FireOn_to_who = conf.get('FireOnConf','to_who')
    return FireOn_smtp_server,FireOn_from_who,FireOn_to_who
if __name__ == "__main__":
    print(conf.sections())
    FireOn_smtp_server,FireOn_from_who,FireOn_to_who = readconf()
    print(FireOn_smtp_server,FireOn_from_who,FireOn_to_who)