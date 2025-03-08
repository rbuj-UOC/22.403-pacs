# 1. Preparació de l'entorn

Per tal d'executar els *notebooks* dins de VS Code necessitareu:
* Instal·lar [VS Code](https://code.visualstudio.com/),
* Instal·lar l'extensió [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) per VS Code,
* Instal·lar l'extensió [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) per VS Code,
* Crear un entorn virtual amb Conda

Primer cal instal·lar [VS Code](https://code.visualstudio.com/), l'[extensió de Python per VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) i l'[extensió de Jupyter per VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

A continuació detallarem els passos per crear un entorn virtual amb `Conda`.

## 1.1. Instal·lació de miniconda

Si treballeu en macOS, podeu fer:

```
brew install --cask miniconda
```

## 1.2. Creació de l'entorn virtual amb conda

Per crear entorns locals a VS Code mitjançant Conda, obriu `Command Palette` (⇧⌘P), cerqueu i seleccioneu l'ordre `Python: Create Environment`.

![](./img/create_environment.avif)

Es mostra una llista amb els tipus d'entorn: `Venv` o `Conda`. Seleccioneu `Conda`.

![](./img/create_environment_dropdown.avif)

L'ordre mostra una llista de versions de Python que es poden utilitzar al vostre projecte. Seleccioneu Python 3.11:

![](./img/conda_environment_python_versions.avif)

S'instal·laran automàticament les biblioteques definides al fitxer [environment.yml](environment.yml).

## 1.3. Com crear un fitxer environment.yml nou

Elimineu el fitxer environment.yml i la carpeta .conda:
```
rm -fr environment.yml .conda
```

Repetiu el pas anterior pe crear un entorn virtual nou amb la versió de Python que vulgueu, després obriu un terminal dins de VS Code i executeu les ordres següents:

```
conda install biopython chardet flake8 ipykernel matplotlib numpy pandas pycodestyle -q -y
pip install pycodestyle_magic
```

Ara ja podeu bolcar les biblioteques instal·lades amb conda amb la següent ordre:
```
conda export > environment.yml
```

# 2. Execució dels notebooks

Una vegada tingueu el programari instal·lat, obriu qualsevol dels *notebooks* amb les activitats a VS Code.

Per a executar-lo cal que seleccioneu l'entorn d'execució virtual, si no s'ha definit abans:

![](./img/select-environment.avif)

i seleccionar l'entorn virtual:

![](./img/select-interpreters-command-2.avif)

# 3. Ús del contenidor Docker

Per executar el contenidor, primer cal instal·lar i executar [Docker Desktop](https://www.docker.com/products/docker-desktop/).

Després cal Construir el contenidor:

```
docker-compose build
```

Un cop construit el contenidor, es podrà aixecar amb la següent ordre:

```
docker-compose up
```

Obriu l'url [http://localhost:8888/lab/](http://localhost:8888/lab/)