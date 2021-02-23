# Een verslag per dag



## Week 1

### Maandag 8 februari

**Voormiddag**: 

tutorials gekeken over nvidia jetson



**Middag**: 

gebeld met Geens en Swenny, wat duidelijkheid over het project

We moeten in afwachting van de camera's wat opzoekwerk doen en prutsen met de reverse proxy



**Namiddag**: 

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

**Ochtend**

Samen deels de Scope & Vision ingevuld (moet nog afgemaakt worden)

**Middag**

Naar ucll gegaan om de bordjes en cameras te halen

**Namiddag**

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



### Woensdag 10 februari

**Ochtend**

Sdk manager proberen te flashen, duurde heel lang

**Middag**

Martijn en robbe naar campus om proxy op te stellen

Tim & Louis geprutst aan jetson

**Namiddag**

Proxy opgesteld, bleek uiteindelijk niet nodig te zijn

We hebben heel de dag geprutst om deepstream aan de praat te krijgen, wat dan ineens lukte op te laatste 15 minuten. Het zou leuk zijn moesten we tensorflow ook geinstalleerd krijgen



### Donderdag 11 februari

**Ochtend**

camera getest, geheugen proberen verhogen

meeting met geens, heeft ons tips gegeven

**middag**

besturingssysteem opnieuw geflasht met Nvidia jetpack in de hoop dat tensorflow zou werken

**avond**

Meeting met Strypsteen, wat meer duidelijkheid gekregen

Nu proberen we tensorflow werkende te krijgen op jetson

zeer vervelend, want er is geen deftige ondersteuning voor arm

We hebben het voor vandaag opgegeven



### Vrijdag 12 februari

**Ochtend**

We kwamen met het briljante idee om om ipv de Jetson, de server die we mee hebben gekregen te gebruiken. Aangezien Tensorflow en anaconda geen goeie support hebben voor arm. We zijn begonnen met de nodige software te installeren.

**Middag**

Het is ons gelukt om [dit project](https://github.com/aqeelanwar/SocialDistancingAI) werkende te krijgen op de server. Nu kunnen we wat beginnen testen.

**Avond**

We hebben een gsm met droidcam gebruikt om video te streamen naar de server. Op de software kan je een vierkant aanduiden en moet je klikken op 2 punten die anderhalve meter uit elkaar zijn. Dan herkent de software mensen en of ze te dicht bij elkaar staan of niet.  





## Week 2

### Maandag 15 februari

**Ochtend**

Tim, Louis en Robbe maken een dockerfile voor gemakkelijkere employment

Martijn werkt aan visuele feedback in de gui



**Middag**

Nog steeds bezig aan employment op docker

Config verplaatst van command line naar config.ini



**Avond**

Docker werkt yeey



### Dinsdag 16 februari

**Ochtend & Middag**

Afgesproken op de campus met de andere groep om beeldmateriaal op te nemen. Was best gezellig. We hebben allerlei scenarios gespeeld. 

Zo te zien is een deel van de toneeltjes niet opgenomen. Spijtig...



**Avond**

We proberen onze software te laten draaien op de beelden. 



### Woensdag 17 februari

**Ochtend**

Martijn werkt aan een web interface voor het project, Tim probeert nog steeds onze image op de jetson te krijgen, Louis heeft een nieuwe methode gevonden

**Middag**

Meer van hetzelfde 

**Avond**

Louis heeft een nieuw ding werkend gekregen op de jetson





ai model training software zoeken

In text file 

Statistieken met js



### Donderdag 18 februari

We proberen om de software op de jetson te krijgen

Het is in de avond eindelijk gelukt





### Vrijdag 19 februari

**Ochtend**

Alles is weer kapot, ineens werkte het weer toen we moet de klant moesten bellen

 **Middag**

De groep splitst op, martijn en robbe werken aan een systeem om te loggen en data te dumpen

Tim en Louis proberen een manier te zoeken om het model bij te trainen en/of andere modellen uit te proberen



### Maandag 22 februari

Martijn en robbe werken verder aan een logging systeem, het is nu al uitgegroeid tot een volledige webapp met statistieken en coole grafieken



Bezig geweest met een model om te zetten naar een frozen graph zodat het efficienter is om in gebruik te nemen. 

Louis zocht op hoe je modellen moet bijtrainen, is heel moeilijk



### Dinsdag 23 februari

Louis: het is moeilijk om een model bij te trainen op windows



Geens heeft niet super veel opmerkingen

We hebben hem onze voortgang getoond 

programma misschien runnen in gpu mode



belasting van gpu enzo checken in jetson







