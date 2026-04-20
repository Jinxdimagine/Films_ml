Movie Rating Predictor

Tento projekt slouží k predikci hodnocení filmů pomocí strojového učení.

Aplikace načítá data o filmu z TMDB API a pomocí natrénovaného modelu (XGBoost) odhaduje jeho výsledné hodnocení.

Funkce aplikace:

Zadání filmu pomocí TMDB ID
Automatické načtení dat z TMDB API
Feature engineering (stejný jako při trénování modelu)
Predikce hodnocení filmu pomocí ML modelu
Zobrazení skutečných dat filmu

Použité technologie:

Python
Streamlit (webová aplikace)
XGBoost (model strojového učení)
TMDB API (zdroj dat)

Instalace (bez IDE):

Stáhni projekt
Stáhni ZIP soubor projektu a rozbal ho do libovolné složky.
Otevři příkazovou řádku (CMD / PowerShell)
Přejdi do složky projektu:

cd cesta/k/projektu/Films_ml/src

Nainstaluj závislosti:

py -m pip install -r requirements.txt

Nastavení API klíče

V projektu se používá konfigurační soubor config.py, který obsahuje API klíč pro TMDB.

Vytvoř soubor config.py a vlož do něj:

TMDB_API_KEY = "TVUJ_API_KLIC"

👉 Nahraď svůj skutečný API klíč z TMDB.

V souboru app.py se klíč importuje takto:

from config import TMDB_API_KEY

Spusť aplikaci:

streamlit run app.py

Otevři v prohlížeči
Po spuštění se v terminálu zobrazí odkaz (např. http://localhost:8501
), který otevři v prohlížeči.

Jak aplikace funguje:

Uživatel zadá TMDB ID filmu.
Aplikace zavolá TMDB API a načte data o filmu.
Data se převedou na feature pomocí stejné pipeline jako při trénování modelu.
Model XGBoost provede predikci hodnocení.
Výsledek se zobrazí uživateli spolu se základními informacemi o filmu.

Omezení:

Model pracuje pouze s numerickými daty
Nezohledňuje kvalitu filmu (například scénář nebo herecké výkony)
Přesnost závisí na kvalitě vstupních dat

Autor:

Projekt byl vytvořen jako školní práce zaměřená na:

sběr dat
zpracování dat
strojové učení
deployment jednoduché webové aplikace

Rychlé spuštění:

py -m pip install -r requirements.txt
streamlit run src/app.py
