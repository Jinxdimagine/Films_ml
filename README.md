Movie Rating Predictor 

Tento projekt slouží k predikci hodnocení filmů pomocí strojového učení.

Aplikace načítá data o filmu z TMDB API a pomocí natrénovaného modelu (XGBoost) odhaduje jeho výsledné hodnocení.

--------------------------------------------------

 Funkce aplikace

- Zadání filmu pomocí TMDB ID
- Automatické načtení dat z API
- Feature engineering (stejný jako při trénování)
- Predikce hodnocení filmu
- Zobrazení skutečných dat filmu

--------------------------------------------------

Použité technologie

- Python
- Streamlit (webová aplikace)
- XGBoost (model strojového učení)
- TMDB API (zdroj dat)

--------------------------------------------------


⬇️ Instalace (bez IDE)

1. Stáhni projekt
- stáhni ZIP soubor projektu
- rozbal ho do libovolné složky

--------------------------------------------------

2. Otevři příkazovou řádku (CMD / PowerShell)

Přejdi do složky projektu:

cd cesta/k/projektu/Films_ml/src

--------------------------------------------------
4. Nainstaluj závislosti
py -m pip install -r requirements.txt

--------------------------------------------------

5. Nastav API klíč

V souboru app.py změň:

API_KEY = "TVUJ_API_KLIC"

Na svůj skutečný API klíč z TMDB.

--------------------------------------------------

6. Spusť aplikaci

streamlit run app.py

--------------------------------------------------

7. Otevři v prohlížeči

link z terminalu
--------------------------------------------------

🧠 Jak aplikace funguje

1. Uživatel zadá ID filmu
2. Aplikace zavolá TMDB API
3. Data se převedou na feature pomocí pipeline
4. Model provede predikci
5. Výsledek se zobrazí uživateli

--------------------------------------------------

⚠️ Omezení

- Model pracuje pouze s numerickými daty
- Nezohledňuje kvalitu filmu (scénář, herce apod.)
- Přesnost závisí na kvalitě dat

--------------------------------------------------

👨‍💻 Autor

Projekt byl vytvořen jako školní práce zaměřená na:
- sběr dat
- zpracování dat
- strojové učení
- deployment aplikace

--------------------------------------------------

▶️ Rychlé spuštění

pip install -r requirements.txt
streamlit run src/app.py
