# Codecentric Developer Finder

Ein Kunde fragt bei codecentric nach einem Scala Entwickler für ein
Projekt an.
Um nachzusehen, ob bei der codecentric ein Entwickler mit den
potentiellen Skills arbeitet, soll ein Tool entwickelt werden, das über eine
einfache Abfrage der Programmiersprache die passenden Mitarbeiter
anzeigt.

## Wir haben zwei Tools entwickelt:

Python-Tool:

Dieses Tool verwendet eine SQLite-Datenbank.
Es ruft die Daten einmalig von GitHub ab und speichert sie in der Datenbank.
Anschließend werden die Abfragen aus der lokalen Datenbank durchgeführt, was die Antwortzeiten beschleunigt und die Abhängigkeit von der GitHub-API verringert.

React-Tool:

Dieses Tool kommuniziert direkt mit der GitHub-API bei jeder Abfrage.
Es ermöglicht Echtzeitzugriff auf die neuesten Daten von GitHub, erfordert jedoch eine stabile Internetverbindung und kann durch API-Ratenbeschränkungen beeinflusst werden.

## Python - codecentric-python

Set your Github Token in setup.py
`github_token=your_token_here`

Fetch the members, repos and their associated languages from Github
`python3 setup.py`

Start the program
`python3 main.py`

Insert the name of the Programming language and you will get a developer that knows that language.

## React - codecentric-react

Create a .env file in the root directory

Insert your Github Token - `REACT_APP_GITHUB_TOKEN=your_token_here`

Run `npm i` to install the dependencies

Run `npm run start` to start the program

Insert the name of the Programming language and you will get a developer that knows that language.
