# De Lag op de Camera verminderen

## Waarom was er grote latency?

Het programma wilt elke frame dat binnenkomt tonen en dan verwerken, het probleem hiermee is dat de verwerking te lang duurt op het bordje.
Hierdoor was de volgende frame steeds later en later zijn doordat het programma de frames die in de buffer zaten nam.

## Wat was de oplossing hiervoor?

Ik heb een paar uur gezocht naar hoe ik de buffer weg kreeg maar dit kon ik nergens vinden waarbij het dan ook werkte.
Uiteindelijk een Klasse VideoCapture gemaakt, deze maakt gebruik van de cv2.VideoCapture
maar gaat als de volgende frame opgevraagd wordt zal hij de frame die net is aangekomen geven.
Op deze manier maakt hij niet gebruik van de Buffer en is de lag met zeer grote maten verminderd.
Het enige waar de lag van de camera nu van afhangt is hoe snel het bordje 1 frame kan verwerken.
