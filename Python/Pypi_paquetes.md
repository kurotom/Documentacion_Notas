# Empaquetar y enviar a Pypi

> [Packaging projects - doc](https://packaging.python.org/en/latest/tutorials/packaging-projects)

1. Crear una cuenta en [https://pypi.org/](https://pypi.org/)
2. Obtener una api key.
3. Crear fichero `.pypirc` en *home* del usuario, con permisos **600**.
4. Estructura del proyecto.
```
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── example_package_YOUR_USERNAME_HERE/
│       ├── __init__.py
│       └── example.py
└── tests/
```
5. Crear el fichero `pyproject.toml`. [configuring-metadata](https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata)
6. Crear el fichero README.md, LICENSE
7. Actualizar `pip`
```bash
python3 -m pip install --upgrade build
```
8. Construir la distribución.
```bash
python3 -m build
```
9. Instalar `twine`
```bash
python3 -m pip install --upgrade twine
```
10. Publicar proyecto en *Pypi*
```bash
python3 -m twine upload --repository testpypi dist/*
```
