import paho.mqtt.client as mqtt
import subprocess
import RPi.GPIO as GPIO
import time

topic_to="esp32/aircon"
keepalive = 300

#MQTTブローカーへの接続処理
def on_connect(client, userdata, flags, rc):
 print("Connected withresult code "+str(rc))
 client.subscribe(topic_to)

def on_disconnect(client, userdata, flags, rc):
    print("Unexpected disconnection.")
    client.loop_stop()

def on_message(client, userdata, msg):
 print(msg.topic+" "+str(msg.payload))

#MQTTブローカーからメッセージを受け取った場合の処理
 if msg.payload == "airOn":
  print("airon!")
  subprocess.call(["sudo","python3", "irrp.py", "-p", "-g13", "-f", "codes", "air_con"+":"+"airon"])
 if msg.payload == "defOn":
  print("defon!")
  subprocess.call(["sudo","python3", "irrp.py", "-p", "-g13", "-f", "codes", "air_con"+":"+"defon"])
 if msg.payload == "heatOn":
  print("heaton!")
  subprocess.call(["sudo","python3", "irrp.py", "-p", "-g13", "-f", "codes", "air_con"+":"+"heaton"])
 if msg.payload == "airconOff":
  print("off!")
  subprocess.call(["sudo","python3", "irrp.py", "-p", "-g13", "-f", "codes", "air_con"+":"+"off"])

#MQTTブローカーへの接続に必要な情報
if __name__ == '__main__':
  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_message = on_message
  client.on_disconnect = on_disconnect
  client.tls_set("/etc/ssl/certs/ca-certificates.crt") #証明書のパスを指定
  client.username_pw_set("username","password") #ユーザー名、パスワードを指定
  client.connect("sarvername" , port, keepalive) #接続先のサーバー名とポート番号を指定
  client.subscribe("topicname") #トピック名を指定
  client.loop_forever()
