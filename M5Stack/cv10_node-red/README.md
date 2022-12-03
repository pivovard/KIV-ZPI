# Node-red

ZCU cloud [](https://nuada.zcu.cz/) ([navod](https://support.zcu.cz/index.php/Cloudov%C3%A9_slu%C5%BEby))


### Install on Linux
```
# Instal nodejs npm

sudo apt update
sudo apt install nodejs npm
npm install -g n
sudo n stable

# Instal node-red
sudo apt install node-red

# Set port
# Add line -A INPUT -p tcp --dport 1880 -j ACCEPT to /etc/iptables/rules.v4.local
nano /etc/iptables/rules.v4.local
sudo service iptables restart

# Instal SmartNORA
cd ~/.node-red
npm install node-red-contrib-smartnora

# Run Node-red
node-red

```

### Install on Windows

1. Install [docker ](https://docs.docker.com/desktop/install/windows-install/)
2. `docker run -it -p 1880:1880 -v node_red_data:/data --name mynodered nodered/node-red`