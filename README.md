# Offline blockchain SmartGrid transactions using LP-WAN technology.

This project aims to evaluate the effectiveness of running blockchain operation using distributed LP-WAN devices, particularly with LoRa.

## Comparison of LP-WAN technologies and why we choose LoRa
https://medium.com/@mehmetmertzgn/comparison-of-lp-wan-technologies-lora-vs-sigfox-vs-nb-iot-7dc20914272b

## LoRa
-	Good for: LoRa is good for sensors that send data with long time intervals. 
-	Shortcomings: Because of the frequency band that is used, there will be a high latency between devices in a crowded city. This would make LoRa not a suitable solution for products that needs fast communication such as health monitoring systems. Also, there is a need to create your own gateway or join a network if you want to connect your system to the internet.

## Project Setup
4x Heltec WiFi LoRa 32 (V2):We bought 4 pieces of this module to serve as our LoRa modules. They also have ESP32 chips in it, this means that we can also connect these devices to the internet if possible to act as gateways to communicate with blockchain servers.

1x Raspberry Pi 3 Module B: We used Raspberry Pi Module B as our main gateway. This serves as a blockchain communicator between edge nodes and the blockchain 
servers.


## Use Case
Smart Grid: Being able to have an offline blockchain in local smartgrids have great benefits.With the rise of solar panels and batteries, there will be neighborhoods which can be self-sufficient for most of the time. In these environments, there will be prosumers that will both produce and consume energy. These users should be negotiating with consumers. Our vision is that with the help of blockchains and smart-contracts, we can create local microgrids without any need for central authority. Users can pay for tokens in this environment and their smart meters will automatically communicate with each other in producers near their home. We are planning to develop a working protype in this domain.
