## Istorie

Pyhton este un limbaj de programare interpretat (nu necesita compilare). A fost creat in 1991 de catre Guido van Rossum, care este un programator olandez. Pentru crearea limbajului de programare a fost numit "Benevolent Dictator For Life".

## Setup "curs_1" virtual environment

```bash
# generarea unui virtual environment
cd ~
cd environments

virtualenv -p python3.5 curs_1_7

# acum activam virtual env.
source curs_1/bin/activate

# ne pregatim IDE-ul integrated development environment
# instalam jupyter, pentru a putea folosi jupyter notebook
pip install jupyter

# instalam si libraria tkinter pentru python3.5
sudo apt-get install python3-tk

# cream un folder "curs_1" unde vom genera toate materialele acestui curs
cd ~/Proiecte/
mkdir curs_1
```

## Trei principii de baza in programare
```bash
# KISS
Keep It Simple, Stupid

# DRY
Don't Repeat Yourself

# YAGNI
You Aren’t Gonna Need It
```
