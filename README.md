# dht22-diamond-collector
Diamond collector for DHT22 sensor on the Raspberry Pi.

## Pi setup
As there are plenty of tutorials on how to get a DHT22 sensor working with Raspberry Pi on the Internet I will skip this bit but an importnat thing to mention is that at the moment collector is hard coded to work on GPIO 4.

## Pre-requirements
* Diamond (duh!)
* [Adafruit_Python_DHT](https://github.com/adafruit/Adafruit_Python_DHT)

## Install
```
$ cd /usr/share/diamond/collectors/
$ git clone https://github.com/artkrz/dht22-diamond-collector.git
```

## Config
* Edit **/etc/diamond/diamond.conf** and add following section where all the other collectors are:
```
[[DHT22Collector]]
enabled = True
path = dht22
interval = 10
```
* Restart diamond
* Profit
