# SocialDistancingAI


# Hoe installeer ik het?
Je kan best een [virtual environment](https://towardsdatascience.com/setting-up-python-platform-for-machine-learning-projects-cfd85682c54b) maken voor dit project en de dependencies installeren. 

## Clone de repo
```
git clone https://github.com/aqeelanwar/SocialDistancingAI.git
```

## Install required packages
Python 3.7 is aangeraden voor dit project, andere python versies kunnen voor problemen zorgen met de dependencies
De gegeven xrequirements.txt file kan gebruikt worden om alles te installeren met deze command. LET OP, het is xrequirements niet requirements
```
cd SocialDistancingAI
pip install -r xrequirements.txt
```
Met specifieke python versie:
```
python3.x -m pip install -r xrequirements.txt
```
Zou je problemen hebben met tensorflow of andere dependencies kan het helpen om [deze guide](https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html) van nvdia te volgen.

Normaal is alles nu mooi geïnstalleerd. Je kan het project runnen met deze command
```
sudo flask run
```
Als je problemen hebt met flask probeer dit dan is opnieuw handmatig te installeren door 
```
sudo pip install Flask
```
of 
```
sudo -H python3.7 -m pip install Flask
```

## Veranderen van email adres en custom message voor het sturen van violation mail
- mailer.py heeft de klasse Mailer met functie send() deze oproepen zal een mail sturen
- in de configs (settings) kan je veranderen naar wie de mail gestuurd wordt
- je kan ook een custom message maken in html of plain text in de settings


Idea Credits: LandingAI



