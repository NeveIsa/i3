#!/usr/bin/python3

import helper_conf
import time,datetime,sys

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


if __name__=="__main__":
    if len(sys.argv) > 1:
        conf=helper_conf.load_conf(sys.argv[1])
    else:
        conf=helper_conf.load_conf()

    conf_msg="| CONFIG: %s |\n" % conf
    print("{0}\n{1}\n{0}".format ("-"*len(conf_msg),conf_msg))

    # set auth if username and passwords are present in the config.
    auth = {'username':conf["user"],'password':conf["pass"]} if conf['user'] and conf['pass'] else None

    while True:
        try:
            time.sleep(1)
            publish.single(topic=conf['pub_topic'], payload="hello", qos=0, retain=False, hostname=conf['host'],port=conf['port'], client_id="", keepalive=60, will=None, auth=auth,tls=None, protocol=mqtt.MQTTv31)
            print("%s -> published" % datetime.datetime.now().isoformat())
        except KeyboardInterrupt:
            print("Exiting...")
            exit()
