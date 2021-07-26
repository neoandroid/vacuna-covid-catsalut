vacunaCovid-catsalut
====================
Aquesta aplicació permet extreure el llistat de centres disponibles per vacunar de forma automàtica utilitzant la pàgina https://vacunacovid.catsalut.gencat.cat


Requisits
---------
- Python 3.5 o superior
- Python bindings for Selenium: pip install selenium
- Google Chrome WebDriver: https://chromedriver.chromium.org/downloads
- Automate de LlamaLab (o qualsevol altre aplicació que et permeti enviar els SMS al correu elctrònic)

Configuració
------------
1. Editem el fitxer vacuna.py i omplim els valors de les variables globals que es troben a l'inici
2. Si utilitzem un compte de Gmail hem de tenir activat l'accés IMAP. Trobareu instruccions per activar-ho a l'enllaç: https://support.google.com/mail/answer/7126229?hl=ca
3. Sovint l'accés IMAP de Gmail ens demanarà una contrasenya d'aplicació enlloc de la que utilitzem habitualment. Per crear-la seguim les instruccions de: https://support.google.com/mail/answer/185833?hl=ca
4. Configurar al mòbil l'aplicació Automate o un altre per enviar els SMS al compte de correu.

Execució
--------
Des d'un terminal executem:
```
$ python vacuna.py
```
