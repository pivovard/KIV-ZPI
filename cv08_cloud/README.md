# Node-red

https://nodered.org/

### Smart nora

https://smart-nora.eu/ - [docs](https://github.com/andrei-tatar/node-red-contrib-smartnora/tree/master/doc)

### ZCU cloud

https://nuada.zcu.cz/ - [navod](https://support.zcu.cz/index.php/Cloudov%C3%A9_slu%C5%BEby)
- to ssh access add line `-A INPUT -p tcp --dport 22 -j ACCEPT` to **/etc/iptables/rules.v4.local**

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
4. Instal SmartNORA (optional)
```
cd ~/.node-red
npm install node-red-contrib-smartnora
```
5. Run Node-red
```
node-red
```

### Set https

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
- when certbot asks for a domain name enter your server host name (**sulisXX.zcu.cz**)
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

### Install node-red on Windows

1. Install [docker ](https://docs.docker.com/desktop/install/windows-install/)
2. `docker run -it -p 1880:1880 -v node_red_data:/data --name mynodered nodered/node-red`
