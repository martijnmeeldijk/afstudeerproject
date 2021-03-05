# De lag op de Camera verminderen

## Waarom was er grote latency?

Het programma wilt elke frame die binnenkomt tonen en dan verwerken, het probleem hiermee is dat de verwerking te lang duurt op het bordje.
Hierdoor komen er steeds meer frames binnen dan er verwerkt kunnen worden, en loopt het bordje steeds meer achter. Alle te verwerken frames komen in een buffer terecht, en het bordje wilt ook elke frame in die buffer analyseren.

## Wat was de oplossing hiervoor?

Ik heb een paar uur gezocht naar hoe ik de buffer weg kreeg maar dit kon ik nergens vinden waarbij het dan ook werkte.
Uiteindelijk een Klasse VideoCapture gemaakt, deze maakt gebruik van de cv2.VideoCapture
maar gaat als de volgende frame opgevraagd wordt zal hij de frame die net is aangekomen geven.

Op deze manier maakt hij geen gebruik van de Buffer en is er veel minder lag.
Het enige waar de lag van de camera nu van afhangt is hoe snel het bordje 1 frame kan verwerken.
Deze gebruikt ook multithreading voor nog iets meer efficiëntie. Het versturen van mails gebeurt op een andere thread, zodat de main thread zich enkel bezig hoeft te houden met het verwerken van frames.