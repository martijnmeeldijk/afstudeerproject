# Een verslag per dag

## Inhoud

* [Week 1](#week-1)
     * [Maandag 8 februari](#maandag-8-februari)
     * [Dinsdag 9 februari](#dinsdag-9-februari)
     * [Woensdag 10 februari](#woensdag-10-februari)
     * [Donderdag 11 februari](#donderdag-11-februari)
     * [Vrijdag 12 februari](#vrijdag-12-februari)
* [Week 2](#week-2)
     * [Maandag 15 februari](#maandag-15-februari)
     * [Dinsdag 16 februari](#dinsdag-16-februari)
     * [Woensdag 17 februari](#woensdag-17-februari)
     * [Donderdag 18 februari](#donderdag-18-februari)
     * [Vrijdag 19 februari](#vrijdag-19-februari)
* [Week 3](#week-3)
     * [Maandag 22 februari](#maandag-22-februari)
     * [Dinsdag 23 februari](#dinsdag-23-februari)
     * [Woensdag 24 februari](#woensdag-24-februari)
     * [Donderdag 25 februari](#donderdag-25-februari)
     * [Vrijdag 26 februari](#vrijdag-26-februari)





## Week 1

### Maandag 8 februari

**Voormiddag**: 

Tutorials gekeken over nvidia jetson



**Middag**: 

Gebeld met meneer Geens en Swennen, wat duidelijkheid over het project

We moeten in afwachting van de camera's wat opzoekwerk doen en leren hoe we een reverse proxy opzetten om aan de camerabeelden te kunnen.



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

Samen deels de Scope & Vision ingevuld (moet nog afgemaakt worden).

**Middag**

Naar ucll gegaan om de bordjes en cameras te halen.

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

Sdk manager proberen te flashen (met een vm), duurde heel lang

**Middag**

Martijn en Robbe naar campus om proxy op te stellen, hebben server meegekregen.

Tim & Louis geprutst aan jetson

**Namiddag**

Proxy opgesteld, bleek uiteindelijk niet nodig te zijn

We hebben heel de dag geprutst om deepstream aan de praat te krijgen, wat dan ineens lukte op te laatste 15 minuten. Het zou leuk zijn moesten we tensorflow ook geinstalleerd krijgen



### Donderdag 11 februari

**Ochtend**

camera getest, geheugen proberen verhogen

meeting met geens, heeft ons tips gegeven

**middag**

Besturingssysteem opnieuw geflasht (met NVidia SDKManager op de server, dit ging al veel beter dan op een VM), in de hoop dat tensorflow zou werken

**avond**

Meeting met Strypsteen, wat meer duidelijkheid gekregen

Nu proberen we tensorflow werkende te krijgen op jetson

zeer vervelend, want er is geen deftige ondersteuning voor ARM



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

Tim, Louis en Robbe maken een dockerfile voor gemakkelijkere deployment

Martijn werkt aan visuele feedback in de gui



**Middag**

Nog steeds bezig aan deployment op docker

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

Research naar statistieken met js, hebben veel docs gelezen van Chart JS



### Donderdag 18 februari

We proberen om de software op de jetson te krijgen

Het is in de avond eindelijk gelukt



### Vrijdag 19 februari

**Ochtend**

Alles is weer kapot, ineens werkte het weer tijdens een call met de klant.

 **Middag**

De groep splitst op, Martijn en Robbe werken aan een systeem om te loggen en data te dumpen

Tim en Louis proberen een manier te zoeken om het model bij te trainen en/of andere modellen uit te proberen



## Week 3

### Maandag 22 februari

Martijn en Robbe werken verder aan een logging systeem, het is nu al uitgegroeid tot een volledige webapp met statistieken en coole grafieken.

Tim bezig geweest met een model om te zetten naar een frozen graph zodat het efficienter is om in gebruik te nemen. 

Louis zocht op hoe je modellen moet bijtrainen, is heel moeilijk



### Dinsdag 23 februari

Louis: het is moeilijk om een model bij te trainen op windows

Tim: Verder zetten van het proberen van een model bij te trainen. Een oplossing gevonden die zeer belovend was. Werkende training van model is met tensorflow 2 maar onze applicatie werkt met tensorflow 1 wat voor problemen zorgt.

Hadden meeting met mr. Geens, we hebben hem onze voortgang getoond.

Enkele opmerkingen van mr. Geens: 

​	programma misschien runnen in gpu mode

​	belasting van gpu enzo checken in jetson



### Woensdag 24 februari


Het model bijtrainen in tensorflow 2 is veel belovend want de loss zit rond 0.35. Het omzetten van het model van tensorflow2 naar tensorflow1 gaat wel zorgen voor moeilijkheden.

We breiden de webapp uit om de configuratie in de webapp te doen, zodat er geen files moeten aangepast worden

De webapp gedebugt, daar zaten we wel even aan vast

### Donderdag 25 februari

We zijn bezig met het model bij te trainen met tensorflow 1. Toch gelukt om model bij te trainen met tensorflow 1 maar het uiteindelijke resultaat is heel slecht. Na vele uren komen we op een loss van 4.758 uit voor onze model terwijl een aangeraden loss 0.3 is (loss is een beschrijving van de nauwkeurigheid van het model in cijfers). Besloten om toch maar met het model getraint met tensorflow 2 te werken.

Gewerkt aan integratie van de webapp en het AI project



### Vrijdag 26 februari

De hele tijd bezig geweest met het proberen omzetten van het model van tensorflow2 naar tensorflow1 maar deze pogingen waren uiteindelijk onsuccesvol. We gaan het hier moeten laten en onze bevindingen moeten delen met de klant dat het wel mogelijk is, maar niet in deze gelimiteerde tijd. Teveel errors en bugs in tensorflow die door het bedrijf zelf nog niet zijn opgelost.

Verderzetten van de integratie van het project en de webapp. Creatie van startup config zodat de opstart van het gehele project met 1 command kan.  

###### Meer info over de problemen hierover in: [Problemen bijtrainen AI](ProblemenMetBijtrainenVanAI.md)

### Maandag 1 maart

Na de vergadering met de klant hadden ze gevraagd voor een verandering van informatie die gegeven wordt in de webapp. In de onderstaand images kan je ziet wat we hadden en wat ze wilden.

Before:

<img src="img/Screenshot%20from%202021-03-01%2016-18-29.png"/>

After:

<img src="img/156170343_1318109225224515_6135300971342547283_n.png"/>

Martijn en Robbe hebben zich daarmee bezighouden. Tim werkte aan documentatie en verdere uitbreidingen van handige informatie voor de klant. Louis werkte nog aan een extensions voor het project dat er bij een violation een mail gestuurd wordt.

De logs zijn nu ook event based. Elke violation wordt nu weggeschreven naar de log ipv met een log_interval parameter te werken, die om de x frames het aantal violations wegschreef, ook dit was nog een verzoek van de klant.

![image-20210305110533535](img/dagverslagen/image-20210305110533535.png)




