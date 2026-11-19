# Tabla de decisiones de mitigacion

En la auditoría inicial del 19 de noviembre de 2026 encontramos 54 avisos en 5 paquetes, equivalentes a 28 CVE únicos. Como pip-audit no asignó una severidad CVSS uniforme en su salida, definimos la prioridad según la facilidad de explotación y el posible efecto sobre la autenticación, la confidencialidad y la disponibilidad.

| Hallazgo | Evidencia inicial | Prioridad | Decision | Verificacion final | Estado |
|---|---|---|---|---|---|
| Inyeccion SQL en `/api/login` | Bandit B608, CWE-89, severidad media; la consulta concatenaba `username` y `password`. | Critica | Usar consulta parametrizada, buscar solo por usuario y verificar un hash de contrasena. | Prueba de inyeccion devuelve 401; Bandit termina con 0 hallazgos. | Mitigado |
| API key y contrasenas fijas | `API_KEY` y usuarios de prueba estaban escritos en `app.py`; las contrasenas se guardaban en texto plano. | Alta | Leer valores desde `.env`, excluir `.env` de Git y almacenar hashes con Werkzeug. | detect-secrets pasa; `.env` esta ignorado; pruebas de login pasan. | Mitigado |
| Flask 2.2.2 | CVE-2023-30861 y CVE-2026-27205. | Alta | Actualizar a Flask 3.1.3. | pip-audit no reporta vulnerabilidades en Flask 3.1.3. | Mitigado |
| Werkzeug 2.2.2 | Multiples CVE de cookies, multipart, rutas y agotamiento de recursos, hasta CVE-2026-102598. | Alta | Actualizar a Werkzeug 3.1.9. | pip-audit no reporta vulnerabilidades en Werkzeug 3.1.9. | Mitigado |
| requests 2.20.0 y dependencias transitivas | CVE en requests, urllib3 e idna; entre ellos CVE-2023-32681, CVE-2024-35195 y CVE-2026-97689. | Alta | Actualizar requests a 2.34.2 y permitir transitivas corregidas. | pip-audit resuelve urllib3 2.8.0 e idna 3.20 sin vulnerabilidades conocidas. | Mitigado |
| Ausencia de controles automatizados | No existian hooks, pruebas ni pipeline. | Alta | Incorporar pre-commit, detect-secrets y GitHub Actions con pruebas, SAST y SCA. | Estado vulnerable: salida distinta de cero. Estado corregido: todos los controles pasan. | Mitigado |

Los resultados completos se conservan en `evidencias/` junto con los dos SBOM CycloneDX.
