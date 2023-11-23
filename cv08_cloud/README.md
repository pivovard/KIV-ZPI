# Node-red

https://nodered.org/

### Run node-red in docker container

```
docker run -it -p 1880:1880 -v node_red_data:/data --name mynodered nodered/node-red
```
Restart a stopped container: `docker start mynodered`

### Install node-red on Linux

1. Instal nodejs npm
```
sudo apt update
sudo apt install nodejs npm
npm install -g n
sudo n stable
```
2. Instal node-red
```
sudo npm install -g node-red
```
3. Set port
- add line `-A INPUT -p tcp --dport 1880 -j ACCEPT` to **/etc/iptables/rules.v4.local**
```
nano /etc/iptables/rules.v4.local
sudo service iptables restart
```
4. Run Node-red
```
node-red
```

### Install additional nodes (optional)
#### Dashboard
[dashboard](https://flows.nodered.org/node/node-red-dashboard)
```
cd ~/.node-red
npm install node-red-dashboard
```
#### Smart nora

https://smart-nora.eu/ - [docs](https://github.com/andrei-tatar/node-red-contrib-smartnora/tree/master/doc)
```
cd ~/.node-red
npm install node-red-contrib-smartnora
```

### Set https (optional)

To access https page (properly) we need SSL certificate. In this case we'll require a certificate from [CA Let's encrypt](https://letsencrypt.org/) via sw [Certbot](https://certbot.eff.org/).

1. Instal snapd
```
sudo apt install snapd
sudo snap install core
sudo snap refresh core
```

2. Install certbot
```
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

3. Add line `-A INPUT -p tcp --dport 80 -j ACCEPT` to **/etc/iptables/rules.v4.local**

4. Run certbot
- when certbot asks for a domain name enter your server host name **sulis##.zcu.cz** (use your own domain instead of ##)
```
sudo certbot certonly --standalone
```

5. In **~/.node-red/settings.js** uncomment following code and enter generated key and certificate.
```
https: {
    key: require("fs").readFileSync('/etc/letsencrypt/live/sulisXX.zcu.cz/privkey.pem'),
    cert: require("fs").readFileSync('/etc/letsencrypt/live/sulisXX.zcu.cz/fullchain.pem')
},
```
