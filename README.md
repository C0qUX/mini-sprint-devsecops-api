# Mini Sprint DevSecOps para una API REST

Este repositorio contiene la remediacion verificable de la API vulnerable entregada en la practica. La version original se conserva en `legacy/` y en la etiqueta Git `vulnerable`; la rama `main` contiene la version corregida.

## Equipo

- Cantos Yépez Elkin Omar
- Fernández Zambrano José Carlos
- Lucas García Jork Davis

Docente: Ing. Sandra Jackeline Soledispa Pereira.

## Arquitectura y endpoints

- Flask expone `GET /api/health`, `GET /api/profile` y `POST /api/login`.
- SQLite almacena usuarios con hash de contrasena.
- Las credenciales de demostracion y la API key se cargan desde variables de entorno.
- GitHub Actions ejecuta pruebas, Bandit, pip-audit y detect-secrets.

## Ejecucion local

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt -r requirements-dev.txt
Copy-Item .env.example .env
# Edita .env solo con valores de demostracion locales.
pre-commit install
python app.py
```

La API escucha en `http://127.0.0.1:5000`.

## Controles de seguridad

```powershell
python -m pytest -q
bandit -r app.py -ll
pip-audit -r requirements.txt
detect-secrets scan --baseline .secrets.baseline
cyclonedx-py requirements requirements.txt --output-format JSON --output-file evidencias/sbom-corregido.json
pre-commit run --all-files
```

## Prueba controlada del bloqueo de secretos

1. Crea temporalmente un archivo `prueba-secreto.txt` con una credencial ficticia de alta entropia.
2. Ejecuta `git add prueba-secreto.txt` y luego `git commit -m "prueba del hook"`.
3. Captura el rechazo de detect-secrets.
4. Elimina el archivo de prueba y no lo incorpores al historial.

## Evidencias incluidas

- Resultados JSON de Bandit y pip-audit antes y despues.
- SBOM CycloneDX del estado vulnerable y del estado corregido.
- Backlog, Definition of Done y tabla de decisiones para el informe.
- Workflow de Build Breaker listo para GitHub Actions.

Las capturas del tablero y del Pull Request deben ser reales y se obtienen siguiendo `docs/GUIA_GITHUB.md`.
