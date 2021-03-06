## Problemen met het bijtrainen van AI

In dit document beschrijven we de problemen die we hebben ondervonden bij het trainen van het model dat instaat voor de persoonsherkenning in ons project. Hopelijk kan het nuttig zijn in de eventuele verdere ontwikkeling.


### Maandag 22 feb en Dinsdag 23 feb 
Het bijtrainen van ai is al een moeilijke opgave omdat er vrij weinig duidelijke documentatie te vinden is. De weinige documentatie die te vinden is, is vaak ook te wiskundig of complex voor ons, omdat we nog maar net kennis hebben gemaakt met AI. 
Code snippets hiervoor zijn overal te vinden maar weinig zijn goed gedocumenteerd, waardoor vaak niet duidelijk is wat de code exact doet. Tensorflow is een framework dat je helpt bij het trainen en bijtrainen van modellen en dit is ook wat we willen gebruiken voor ons model. Dus blijven we ook zoeken.

### Woensdag 24 feb
Na vele uren rond te zoeken op het internet naar een goede guide zodat we het wiel niet zelf moesten heruitvinden hebben we die eindelijk [hier](https://gilberttanner.com/blog/tensorflow-object-detection-with-tensorflow-2-creating-a-custom-model) gevonden. Deze werkt met een docker container zodat de vele dependencies die nodig zijn en vaak vele errors geven, nu helemaal in orde zijn. Nu blijkt dat deze fantastische guide gemaakt is voor tensorflow 2, maar we hebben hoop dat het bijgetrainde model omzetbaar is naar tensorflow 1, want ons project werkt met tensorflow 1. Na enkele uren voorbereidingen te maken zoals: op afbeeldingen handmatig mensen aanduiden, omzetten naar een csv en dan nog wat errors oplossen, hebben we eindelijk het trainen kunnen opzetten. Het was veelbelovend want bij elke stap die er getoond werd, verbeterde onze loss heel goed. (loss is een uitdrukking voor de nauwkeurigheid van het model, hoe lager hoe beter.) We waren begonnen met een loss van 7 en geëindigd met een loss van 0.35. Exact wat we wilden. Het omzetten van het model voor tensorflow 1 is een hele uitdaging die maar niet lijkt te willen lukken dus besloten we om toch maar te trainen in tensorflow 1 met een gelijkaardige guide.

### Donderdag 25 feb
Het bijtrainen van het model in tensorflow 1 zorgt voor wat problemen. We moeten een ouder model gebruiken, dat even accuraat zou moeten zijn. Maar uit ervaring weten we dat we zo'n uitspraken met een korreltje zout moeten nemen. 
Het bijtrainen van het model is gelukt, maar wanneer we deze willen gebruiken herkent ons model geen mensen meer. Er is waarschijnlijk iets misgelopen tijdens het trainen zonder een error te geven. We besloten om dit achterwege te laten want opnieuw beginnen trainen ging te veel tijd innemen dat we niet hadden. We besloten ons te focussen op het model dat getraind is in tensorflow 2 om te zetten naar tensorflow 1.

### Vrijdag 26 feb
Het omzetten van het model van tensorflow 2 naar tensorflow 1 is niet gelukt. De documentatie hiervoor is weer heel verwarrend met veel bronnen die iets anders zeggen. Uiteindelijk toch een script gevonden om dit te doen maar dit was natuurlijk niet zonder error. Na vele uren van debugging hebben we het moeten opgeven. We zaten vast op een error waarvan een issue was geopend op github bij de developers van tensorflow zelf, maar hier was nog geen concrete oplossing voor. We zijn er van overtuigd dat we dit met genoeg tijd kunnen oplossen, maar tot onze grote spijt loopt het project binnenkort op zijn einde.

### Conclusie
Nu we zo goed als op het einde komen van de ontwikkeling van ons project zijn we van mening dat indien we wat meer tijd hadden gehad we ook dit deel, het bijtrainen/trainen van het model, tot een goed eind had kunnnen brengen. Hopelijk krijgen we ooit nog eens de kans om dit verder uit te werken, want het is wel heel interessant en een mooie skill om toe te voegen aan onze cv's.
