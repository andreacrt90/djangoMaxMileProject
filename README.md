Il progetto si trova nella repository pubblica di gitHub reperibile all'indirizzo:

https://github.com/andreacrt90/djangoMaxMileProject

e la sua esecuzione prevede che sul PC di test sia già installata l'ultima versione di python 3.8.2.

## Installazione

Per installare il progetto occorre seguire i seguenti passi:
1) Scaricare o clonare la repository in una directory qualsiasi
2) Tramite Prompt dei comandi spostarsi all'interno della suddetta directory
3) Spostarsi all'interno della cartella principale appena clonata: 
cd djangoMaxMileProject-master
4) Effettuare l'attivazione del ambiente virtuale digitando:
mmProject\Scripts\activate.bat
(dovrebbe comparire all'inizio della riga il nome dell'ambiente 'mmProject')
5) Spostarsi quindi nella cartella:
cd mmProject/mmProject
6) Installare Django digitando:
pip install django
7) Installare le altre librerie digitando:
pip install Pillow
pip install django-filter
pip install django-bootstrap-form
pip install django-guardian
8) Eseguire il run del server digitando:
python manage.py runserver
9) Aprire un browser qualunque e digitare l'URL:
http://localhost:8000/

## Utenti

L'accesso al sito web non necessita registrazione da parte dell'utente; 
la pagina di amministrazione invece prevede login, ed è accessibile dall'indirizzo:
http://localhost:8000/admin
oppure cliccando sul link "Login" dalla barra di navigazione in alto.

E' possibile accedere con due diverse tipologie di utenti, di seguito descritte:

Amministratore:
Username: admin
Password: admin

Utente registrato n.1:
Username: user1
Password: usrpsw_1

Utente registrato n.2:
Username: user2
Password: usrpsw_2

Ogni utente è correlato a un Profilo in cui sono descritte informazioni aggiuntive relative ad esso. 

## Tempo di sviluppo

Il progetto ha previsto uno sviluppo durato circa una settimana, come si può notare dalla tempistica dei commit visualizzabili nella repository. 
