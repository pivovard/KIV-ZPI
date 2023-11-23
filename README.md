# KIV/ZPI
[Courseware](https://courseware.zcu.cz/portal/studium/courseware/kiv/zpi)

## M5Stack dokumentace
[Dokumentace microPython official](https://docs.m5stack.com/en/quick_start/core2/mpy) \
[Dokumentace microPython Github](https://github.com/m5stack/M5Stack_MicroPython)      \
[Dokumentace C (Arduino)](https://docs.m5stack.com/en/quick_start/core2/arduino)

## MQTT
[ampy](https://github.com/scientifichackers/ampy) - utilita pro nahrani souboru na m5stack \
[simple2](https://github.com/fizista/micropython-umqtt.simple2/) - micropython knihovna pro MQTT (včetně retain flagu)

## Cloud

### ZCU cloud
https://nuada.zcu.cz/ - [navod](https://support.zcu.cz/index.php/Cloudov%C3%A9_slu%C5%BEby)
- to ssh access add line `-A INPUT -p tcp --dport 22 -j ACCEPT` to **/etc/iptables/rules.v4.local**

### Docker

[Windows install](https://docs.docker.com/desktop/install/windows-install/) \
[Linux install](https://docs.docker.com/desktop/install/linux-install/)

### Node-red

[node-red](cv08_cloud/README.md)

### Home Assistant

[Home Assistant](https://www.home-assistant.io)

```
docker run -d -p 8123:8123 --name homeassistant --privileged --restart=unless-stopped -e TZ=Europe/Prague -v "%HOMEDRIVE%%HOMEPATH%\HomeAssistant":/config ghcr.io/home-assistant/home-assistant:stable
```

## M5Stack Emulator
https://github.com/MartinUbl/M5Stack_MicroPython_Emulator/tree/master

**Prerequisites**\
- Cmake
- boost (extrahujte do C:\Boost nebo C:\Program files\Boost)
- Qt