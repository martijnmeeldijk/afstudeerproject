## Berekening accuraatheid van het systeem

Note: Dit gaat strikt over de violations, niet over het herkennen van personen.

Voor de berekening van de accuraatheid van ons systeem hebben we 2 filmpjes geanalyseerd en nagegaan waar ons systeem in de fout gaat. Nu is dit onder voorbehoud omdat wij ook fouten maken.

Om de onderstaande termen wat op te frissen:

- A **true positive** is an outcome where the model *correctly* predicts the *positive* class.
- A **true negative** is an outcome where the model *correctly* predicts the *negative* class.
- A **false positive** is an outcome where the model *incorrectly* predicts the *positive* class.
- A **false negative** is an outcome where the model *incorrectly* predicts the *negative* class.

De 'class' in ons geval is een violation. 

Het eerste filmpje dat we hebben geanalyseerd is te vinden in onze github repository, genaamd vid_short.mp4.

|          | True positives | False positives | True negatives | False negatives |
| :------- | -------------- | --------------- | -------------- | --------------- |
| **Hits** | 34             | 11              | 0              | 0               |

Het tweede filmpje dat we hebben geanalyseerd is gopro1k.mp4

|          | True positives | False positives | True negatives | False negatives |
| :------- | -------------- | --------------- | -------------- | --------------- |
| **Hits** | 112            | 46              | 0              | 0               |

Nu gaan we accuraatheid berekenen door middel van deze formule.

![](C:\Users\timva\Documents\School\afstudeerproject\afstudeerproject\docs\img\precision.png)

Filmpje 1:
$$
34/(34+11)=0.75
$$


Filmpje 2:

​			
$$
112/(112+46)=0.70
$$
Gemiddelde accuraatheid:
$$
(0.70 + 0.75)/2 = 0.72
$$
Het accuraatheid van het systeem berekend op deze filmpjes komt dus uit op 0.72 met andere woorden, 72% van de tijd correct.