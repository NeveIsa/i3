"""
test_sub.py is an example of a subscriber to a topic
"""
	
import paho.mqtt.client as mqtt
import time

logfile = None

def on_connect(client, userdata, flags, rc):
    m = "Connected flags " + str(flags) + " Result code "\
    + str(rc) + " Client_id  " + str(client)
    print(m)

def on_message(client, userdata, msg):
    global logfile
    
    print "Message received  " + msg.payload
    
    # if not logfile is None:
    #     logfile.write(str(time.time()) + ',' + msg.payload + ',' + msg.topic + '\n')
    #     logfile.flush()

def test_sub(logfilename=None):   
    global logfile
    # INSERT INTO users (username, pw) VALUES ('u1$hub1$dev1','PBKDF2$sha256$901$EaCwVL9LPas4l6Lv$kh5PQOk2+ss5ie5fRWXKdb+e457A8RFa')
        #account = 'zxc'
    account = "sampad_buyer" 
    #pw = 'zxc'
    pw = 'ywqk7po0zk9q'
    topic = 'sampad/isac/random'
    sub_client = mqtt.Client(account)
    sub_client.on_connect = on_connect
    sub_client.on_message = on_message
    sub_client.username_pw_set(account, pw)
    sub_client.connect('18.219.4.146', 1883) #connect to broker

    sub_client.subscribe(topic)
    
    if not logfilename is None:
        logfile = open(logfilename, 'w')
        
    rc = 0
    while rc == 0:
        rc = sub_client.loop()
        time.sleep(1)
        
if __name__ == '__main__':
    test_sub('sub.log')
