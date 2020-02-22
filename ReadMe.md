
# GPS pour l'Adrasec 90/70
  
Ce projet permet de proposer une solution alternative aux GPS commerciaux, qui peuvent être onéreux ; il offre un affichage de multiples informations liées à un signal GPS, mais également la conversion automatique des coordonnées _GPS_ en format _MGRS_.  
  
* Informations de disponibles via l'afficheur :  
-- Date et heure (en format local).  
-- L'altitude de l'appareil (en format métrique).  
-- Coordonnées GPS (en format degrés décimaux).  
-- Coordonnées MGRS.  
-- Géolocalisation sous le format d'un QTH.

* Remarque :  
Vous remarquez dans le code qu'il est fait mention du réseau **Cospas-Sarsat**, réseau satellitaire utilisé pour la localisation de radiobalises liées aux sinistres (``printMessage_1()`` à ``printMessage_13()``); cette partie est purement facultative dans le programme et peut-être totalement supprimée, je l'ai surtout laissée pour la blague et par pur plaisir de geek.  **--** [Wiki](https://fr.wikipedia.org/wiki/Cospas-Sarsat) du réseau. **--**

### Pré-requis

Ce qui est requis pour commencer avec votre projet :
- GPSd
- MGRS
- Adafruit_DHT

### Installation

Pour bien débuter, commencez par installer les modules dont vous aurez besoin pour faire fonctionner correctement votre appareil.

_Pour faire fonctionner le module GPS :_  
``sudo apt-get install -y gpsd gpsd-clients python-gps``  
_Pour faire fonctionner le convertiseur des coordonnées GPS :_  
``sudo pip install mgrs``  
_Pour faire fonctionner le module DHT 22 :_ (**facultatif**)  
``sudo pip install Adafruit_DHT``  

Vous aurez ensuite le loisir de pouvoir obtenir le résultat sur votre écran.

<img src="https://raw.githubusercontent.com/Raxgahrax/GPS_Adrasec/master/Images/Screen_1.jpg" height= "155"> <img src="https://raw.githubusercontent.com/Raxgahrax/GPS_Adrasec/master/Images/Screen_2.jpg" height= "155"> <img src="https://raw.githubusercontent.com/Raxgahrax/GPS_Adrasec/master/Images/Screen_3.jpg" height= "155">

## Démarrage

Pour lancer le programme, n'hésitez pas à vous rendre dans son dossier pour rendre exécutable ``GPS_Adrasec.py``.  
Ensuite rendez-vous dans ``/etc/rc.local`` et y ajouter la ligne suivante:  
``sudo python /home/_user_/Bureau/GPS/GPS_Adrasec.py`` pour lancer de manière automatique le script dès le démarrage du Raspberry.

* Remarques :

En cas de problèmes de connexion avec votre module GPS, n'hésitez pas à vous référer à [ce lien](https://stackoverflow.com/a/34967951) qui pourra sans doute, solutionnez votre problème.  
Si la date et l'heure viennent à ne pas se synchroniser dès le démarrage, n'hésitez pas à relancer le Raspberry.

## Fabriqué avec

* Raspberry Pi 3B+ - [Adafruit](https://www.adafruit.com/product/3775)
* Écran LCD 20x04 (+ module I2C) - [Aliexpress](https://fr.aliexpress.com/item/710350488.html?spm=a2g0s.9042311.0.0.481f6c37MmyCNt)
* Convertiseur de niveau logique - [Aliexpress](https://fr.aliexpress.com/item/32996331532.html?spm=a2g0s.9042311.0.0.481f6c37MmyCNt)
* Module GPS (GlobalSat BU-353-S4) - [Amazon](https://www.amazon.fr/GlobalSat-BU-353-S4-R%C3%A9cepteur-SiRF-Star/dp/B008200LHW)

