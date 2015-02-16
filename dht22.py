#!/usr/bin/pythoni

import sys
import Adafruit_DHT
import diamond.collector

class DHT22Collector(diamond.collector.Collector):
    def collect(self):
        humidity, temperature = Adafruit_DHT.read_retry(22, 4)
        if humidity is not None and temperature is not None:
            self.publish('temperature', temperature, precision=2)
            self.publish('humidity', humidity, precision=2)
