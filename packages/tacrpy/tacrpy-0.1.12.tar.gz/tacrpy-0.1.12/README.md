## **tacrpy**

Python knihovna, která slouží pro práci s daty a vypracování analýz TA ČR

## Práce s repozitářem

1) Naklonuj si tento repozitář:

   `git clone git@git.tacr.cz:data-team/tacrpy.git`
2) Nainstaluj požadavky

   `pip install -r requirements.txt`

## Generování dokumentace
### Prerekvizity

- Python
- Sphinx (`pip install sphinx`)
- Read The Docs Theme (`pip install sphinx_rtd_theme`)

### Generování dokumentace
1) Naklonuj si tento repozitář:

   `git clone git@git.tacr.cz:data-team/tacrpy.git`
2) Přejdi do adresáře _'docs'_:

   `cd docs`
3) Spusť _'sphinx-apidoc'_ pro vygenerování souborů dokumentace

   `sphinx-apidoc -o source ../tacrpy`
4) Pro vygenerování html dokumentace:

   `make.bat html`

5) Vygenerovaná dokumentace se nachází v adresáři _'docs/build/html'_