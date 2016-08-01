#!/usr/bin/env python

from time import sleep

import paho.mqtt.client as mqtt
import pifacedigitalio
import yaml

pifacedigital = pifacedigitalio.PiFaceDigital()

config = open('config.yaml', 'r')
config = yaml.load(config)


def on_connect(client, userdata, flasg, rc):
    client.subscribe(config['mqtt_topic'])


def on_message(client, userdata, msg):
    if (msg.payload == 'GARAGE_BUTTON'):
        pifacedigital.output_pins[0].toggle()
        sleep(0.5)
        pifacedigital.output_pins[0].toggle()


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(config['server']['address'], config['server']['port'], 60)
    client.loop_forever()


if __name__ == "__main__":
    main()
