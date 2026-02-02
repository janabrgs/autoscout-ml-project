# AutoScout – Analyse & Preisvorhersage von Fahrzeugpreisen

Dieses Projekt analysiert Fahrzeugdaten aus AutoScout24 mit dem Ziel, Einblicke in den deutschen Automarkt zu gewinnen und Fahrzeugpreise mithilfe von Machine-Learning-Modellen vorherzusagen.
Der Fokus liegt auf einem vollständigen End-to-End-Workflow von der Datenaufbereitung über Modellierung bis hin zur Visualisierung.

## Projektinhalte

### Daten
- Datensatz mit Informationen zu in Deutschland verkauften Fahrzeugen
- Enthält u. a. Marke, Baujahr, Kilometerstand, Leistung, Kraftstofftyp und Verkaufspreis
- Quelle: Kaggle (AutoScout24 / Cars Germany Dataset)
- Die Daten sind vollständig im Repository enthalten

### Analyse
Im Rahmen der explorativen Datenanalyse wurden unter anderem folgende Fragestellungen untersucht:
- Anzahl der verkauften Fahrzeuge und betrachteter Zeitraum
- Erfasste Automarken und deren Verteilung
- Korrelationen zwischen numerischen Features (z. B. Preis, Leistung, Kilometerstand)
- Preis- und Marktveränderungen über die Jahre
- Weitere hersteller- und merkmalsbezogene Auswertungen

### Machine Learning
- Fokus auf die fünf am häufigsten vertretenen Hersteller
- Feature Engineering und Datenbereinigung
- Trainierte Modelle:
  - Lineare Regression
  - Random Forest Regressor
- Zielvariable: Verkaufspreis eines Fahrzeugs
- Modellbewertung mithilfe geeigneter Regressionsmetriken
- Random Forest wurde aufgrund besserer Ergebnisse für die finale Preisvorhersage verwendet

### Visualisierung & Dashboard
- **Power BI Dashboard** zur übersichtlichen Darstellung zentraler Analyseergebnisse
- Interaktive Visualisierungen zur Unterstützung der Dateninterpretation

### Streamlit App
- Lokale Web-App zur Vorhersage von Autopreisen
- Nutzer können Fahrzeugmerkmale eingeben und erhalten eine Preisprognose
- Implementierung auf Basis des trainierten Random-Forest-Modells

## Projektstruktur

```

autoscout-ml-project/
├── data/ # CSV- und Excel-Daten
├── notebooks/ # Jupyter Notebooks für Analyse & Modellierung
├── src/ # Python-Code (u. a. Streamlit App)
├── powerbi/ # Power BI Dashboard (.pbix)
├── model/ # Platzhalter für trainierte Modellartefakte (nicht versioniert)
└── README.md

```

## Tech Stack

- Python
- NumPy
- Pandas
- scikit-learn
- Jupyter Notebook
- Streamlit
- Power BI
- Excel
- Power Query (Excel & Power BI)
- joblib
- Visual Studio Code

## Ergebnisse & Learnings

- Umgang mit realistischen, unsauberen Marktdaten
- Strukturierung eines End-to-End-Data-Science-Projekts
- Vergleich und Bewertung unterschiedlicher Regressionsmodelle
- Kombination aus Analyse, Machine Learning und Business-orientierter Visualisierung
- Aufbau einer einfachen interaktiven ML-Anwendung mit Streamlit

## Hinweise
Das trainierte Modell wird nicht direkt im Repository versioniert, da große Binärdateien die GitHub-Größenbeschränkungen überschreiten.  
Das Modell kann jederzeit aus den Notebooks neu erzeugt werden.
