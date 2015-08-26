#!/usr/bin/python2.7
import ConfigParser

tuple()
def config_read(fn):
    config = ConfigParser.ConfigParser()
    config.read(fn);
    for section in config.sections():
        for pair in config.items(section):
#            print pair , type(pair)
            for item in pair:
                print item
    print config.get('M1', 'ip_port');



if __name__ == "__main__":
    config_read("myconfigure.cfg")
