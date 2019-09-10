#!/usr/bin/python3

import yaml,sys
default_filename = "conf.d/conf.yml"

def load_conf(conf_file=default_filename):
    try:
        conf=yaml.safe_load(open(conf_file).read())
        #print(conf)
        if not conf: raise
        else: return conf
    except:
        print("Couldn't load config file: %s ! EXITING" % conf_file)
        exit()

if __name__ == "__main__":
    if len(sys.argv)>1:
        fname=sys.argv[1]
    else:
        fname=default_filename
    print("FILE -> %s" % fname)
    print (load_conf(fname))
