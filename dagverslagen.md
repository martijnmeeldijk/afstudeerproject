# Een verslag per dag



## Week 1

### Maandag 8 februari

<u>Voormiddag</u>: 

tutorials gekeken over nvidia jetson



<u>Middag</u>: 

gebeld met Geens en Swenny, wat duidelijkheid over het project

We moeten in afwachting van de camera's wat opzoekwerk doen en prutsen met de reverse proxy



<u>Namiddag</u>: 

(Martijn & Robbe) nginx config gemaakt

https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/

https://www.scaleway.com/en/docs/how-to-configure-nginx-reverse-proxy/



onze conf:

```nginx

user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
        worker_connections 768;
        # multi_accept on;
}

http {

        ##
        # Basic Settings
        ##

        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;
        types_hash_max_size 2048;
        include /etc/nginx/mime.types;
        default_type application/octet-stream;


        ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
        ssl_prefer_server_ciphers on;


    server { 
        listen 192.168.0.100:80; 
        root   /usr/share/nginx/html; 
 
        location / { 
            satisfy all; 
 
            allow 192.168.0.0/24;
            allow 127.0.0.1;
            allow  all; #Hier kunnen we instellen dat we alleen onze ip adressen toelaten.

            auth_basic           "Administrator’s Area";
            auth_basic_user_file /etc/apache2/.htpasswd;
    }
}
```



(Tim)

geprutst met Docker; gekeken of er voorgetrainde AI's bestaan die we mogelijks zouden kunnen gebruiken voor ons project

(Louis)

Community projects dingen gekeken; Hello AI world video; Object detection guide

https://github.com/dusty-nv/jetson-inference

https://github.com/neuralet/neuralet/tree/master/applications/smart-distancing

https://developer.nvidia.com/embedded/community/jetson-projects