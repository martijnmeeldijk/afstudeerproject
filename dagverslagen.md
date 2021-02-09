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



### Dinsdag 9 februari

<u>Ochtend</u>

Samen deels de Scope & Vision ingevuld (moet nog afgemaakt worden)

<u>Middag</u>

Naar ucll gegaan om de bordjes en cameras te halen

<u>Namiddag</u>

Extra research

Kennis gemaakt met het Xavier bordje

Al wat software geïnstalleerd en geprobeerd tensoflow aan de praat te krijgen (nog niet gelukt, voor morgen)

deze tutorial verder doen: https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html (stap 3)



Bronnen:

[Real time object detection](https://www.mygreatlearning.com/blog/object-detection-using-tensorflow/)

[Covid Social distancing detector](https://github.com/basileroth75/covid-social-distancing-detection)

https://towardsdatascience.com/analyse-a-soccer-game-using-tensorflow-object-detection-and-opencv-e321c230e8f2

[NVidia Peoplenet](https://ngc.nvidia.com/catalog/models/nvidia:tlt_peoplenet)

[Jupyterlab](https://jupyterlab.readthedocs.io/en/stable/) soort van ide/interface om te prutsen met python en data

[Jetson AI courses](https://developer.nvidia.com/embedded/learn/jetson-ai-certification-programs)

