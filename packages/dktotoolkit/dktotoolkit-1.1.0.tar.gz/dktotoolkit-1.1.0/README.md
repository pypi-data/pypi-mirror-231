[![Latest Release](https://framagit.org/discord-catho/module_toolkit/-/badges/release.svg)](https://framagit.org/discord-catho/module_toolkit/-/releases)
[![pipeline status](https://framagit.org/discord-catho/module_toolkit/badges/main/pipeline.svg)](https://framagit.org/discord-catho/module_toolkit/-/commits/main)

---

[![coverage report](https://framagit.org/discord-catho/module_toolkit/badges/main/coverage.svg)](https://discord-catho.frama.io/module_toolkit/coveragepy_report/)
[![PEP8-Critical](https://img.shields.io/endpoint?url=https://discord-catho.frama.io/module_toolkit/badges/pep8-critical.json)](https://discord-catho.frama.io/module_toolkit/flake8_report/)
[![PEP8-NonCritical](https://img.shields.io/endpoint?url=https://discord-catho.frama.io/module_toolkit/badges/pep8-noncritical.json)](https://discord-catho.frama.io/module_toolkit/flake8_report/)
[![PEP8-Rate](https://img.shields.io/endpoint?url=https://discord-catho.frama.io/module_toolkit/badges/pep8-rate.json)](https://discord-catho.frama.io/module_toolkit/flake8_report/)
[![Profiling](https://img.shields.io/static/v1?label=Profiling&message=yep&color=informational)](https://discord-catho.frama.io/module_toolkit/profiler_report)

---

[![Downloads](https://pepy.tech/badge/dktotoolkit/month)](https://pepy.tech/project/dktotoolkit)
[![Supported Versions](https://img.shields.io/pypi/pyversions/dktotoolkit.svg)](https://pypi.org/project/dktotoolkit)

---

[![Catholic project](https://img.shields.io/static/v1?label=catholic&message=unofficial&color=orange&style=plastic&logo=feathub)]()

---

# Module toolkit (package name : dktotoolkit)

This is a module with different tools, very usefull !

For exemple, there is :
* Load .env class
* Parser for dates
* Compatibility mode for function arguments
* Transformer de l'utf8 en HTML et de l'HTML en Markdown principalement.
* ...

# Documentation :
* Please read the documentation at : https://discord-catho.frama.io/module_toolkit
* Voir le fichier requirements.txt pour les dépendances, puis "$ make -C docs html" à la racine du projet

# Tag names
* "v" : for "version"
* vX.Y.Z : release (any bugs)
** release (X) : major new implementations
** macro-release (Y) : minor implementations, major improvements of features
** micro-release (Z) : bug correction, minor improvements of features (ex : add verbose)


* vX.Y.ZaN : alpha version (working version)
** Sync on git
** Continous integration
** Not upload on Pypi

* vX.Y.ZbN : beta release (must be fixed, or allmost)
** Sync on git
** Continous integration
** Uploaded on Pypi

* vX.Y.ZrcN : release candidate (all is fixed)
** Sync on git
** Continous integration
** NOT uploaded on Pypi

* vX.Y.ZpostN : post release (correction of doc)
** Sync on git
** Using CI
** Uploaded on Pypi

To have more informations, see PEP440 : https://peps.python.org/pep-0440/


# Installation

Installation en tant que module à partir des sources :

* Créer un environnement
```
$ python3.9 -m venv env_module
$ source env_module/bin/activate
```

* Installer le module avec les paquets de base
```
$ pip3 install .
```

* Installer le module avec tous les paquets de base
```
$ pip3 install .[doc, test]
```

* Installer uniquement les paquets
```
$ pip3 install -r requirements.txt
```


## Comme submodule
* Attention : il est nécessaire d'installer les dépendances également
```
$ cd /path/superprojet
$ mkdir -p scripts/external && cd scripts/external
$ git submodule add git@framagit.org:discord-catho/parserhtml.git
$ git submodule update --recursive --init
$ git submodule update --recursive --remote

```

# TODO
* [ ] submodule git pour CI et setup
* [ ] Add substitution inside .. literalinclude:: ../../dktotoolkit/__version__.py (setup.rst)
* [ ] Improve tests for parserhtml
* [ ] load dotenv : if path : check if exists, add argument : raise if not exists
* [ ] Transformer les fonctions de dktotk en sous-modules
* [ ] Fix pipeline, coverage

# Licence
GNU AGPL 3 (cf LICENCE.md)