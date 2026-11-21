# Python Brasov 2018

Aceasta este prima parte a cursului predat de Alex Girlea în colaborare cu AgileHub în 2018.

Imagini curs: 
https://www.linkedin.com/posts/agilehub_python-it-comunitate-activity-6508984711979757568-NbfW/
https://www.facebook.com/agilehub/photos/pcb.1030748847087095/1030748753753771/?type=1&theater

La baza cursului s-au folosit mai multe materiale educationale precum "Python: Journey from Novice to Expert - Fabrizio Romano, Dusty Phillips, Et al (Packt)"


Daca nu aveti Linux instalat pe PC-ul dumneavoastra, urmati toti pasii de mai jos pentru instalarea sistemului de operare Ubuntu.

Daca aveti Linux instalat, va rog sa urmati pasii de mai jos pentru setarea mediului de dezvoltare.

### Optiunea 1: Daca PC-ul este suficient de puternic (ex: i5, 8GB RAM) puteti instala VirtualBox
```bash
# descarcati VirtualBox de la link-ul de mai jos
https://www.virtualbox.org/wiki/Downloads
# cursantii vor primi pe mail-ul personal un link pentru descarcarea unei masinii virtuale
# aceasta va fi deschisa cu VirtualBox
```

### Optiunea 2: Cum instalam Ubuntu de la zero folosind sistemul de operare Windows
1. Putem da jos imaginea Ubuntu 16.04 de aici:
```
# accesati acest URL si alegeti "64-bit PC (AMD64) desktop image"
http://releases.ubuntu.com/16.04/
    
```
2. Creati un stick bootabil
```
# instalati programul Rufus de la link-ul de mai jos
https://rufus.akeo.ie/
# dupa instalarea programului, alegeti imaginea cu OS-ul Ubuntu si sitck-ul USB si incepeti procesul de creare
```

3. Cu stick-ul in PC, reporniti calulcatorul si urmati pasii de instalare indicati de Ubuntu
```bash
OBS: in cazul in care Ubuntu nu ruleaza direct la repornirea calculatorului, trebuie sa intrati in BIOS
si sa setati USB Stick ca primul mediu de bootare
```

### Optiunea 3: Instalati Ubuntu in paralel cu Windows (doar pentru utilizatori avansati)
Accesati acest [link](https://www.youtube.com/watch?v=0W7XYAB4cLc) si urmati instructiunile



### Pasii pentru setarea mediului de dezvoltare in Ubuntu
```bash
# deschide terminalul prin apasarea urmatoarelor combinatii de taste
Ctrl + Alt + T

# updateaza pachetele sistemului de operare
sudo apt-get update
sudo apt-get -y upgrade

# instaleaza pip pentru managementul librariilor python
sudo apt-get install -y python3-pip

# instaleaza diverse librarii de linux necesare mediului de dezvoltare
sudo apt-get install build-essential libssl-dev libffi-dev python-dev

# instaleaza libraria python pentru crearea si managemetul mediilor de dezvoltare virtuale
sudo apt-get install -y python3-venv

# ne asifuram ca lucram lucrăm in directorul Home al utilizatorului curent
cd ~

# vom crea un nou folder in care vom stoca toate mediile de dezvoltare virtuale
mkdir environments

# vom crea si un folder pentru proiectele la care vom lucra
cd ~
mkdir Proiecte


# vom instala git pentru versionarea codului
sudo apt-get install git

# vom instra in folderul de Proiecte
cd ~/Proiecte

# vom downloda codul pentru cursul Python Brasov 2018
git clone https://github.com/AlexandruGirlea/python_brasov_2018.git

# pentru updatarea cursurilor vom folosi urmatoarea comanda
cd ~/Proiecte/python_brasov_2018
git pull

```