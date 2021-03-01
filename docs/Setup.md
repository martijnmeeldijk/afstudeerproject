# Setup om het project op te zetten

## Steps
- Clone de repo
- Cd naar SocialDistancingAI
- Python 3.7 is aangeraden
- Pip install -r xrequirements.txt (als je met specifieke python versie wilt "python3.x -m pip install -r xrequirements.txt"). Zou je problemen hebben met tensorflow of andere dependencies kan het helpen om [deze guide](https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html) van nvdia te volgen.
- Normaal is alles nu mooi geïnstalleerd
- Run het project met deze command "sudo flask run"(Als je problemen hebt met flask probeer dit dan is opnieuw handmatig te installeren door "sudo pip install Flask" of "sudo -H python3.7 -m pip install Flask
"te runnen)

## Veranderen van email adres en custom message voor het sturen van violation mail
- mailer.py heeft de klasse Mailer met functie send() deze oproepen zal een mail sturen
- in de configs (settings) kan je veranderen naar wie de mail gestuurd wordt
- je kan ook een custom message maken in html of plain text in de settings
