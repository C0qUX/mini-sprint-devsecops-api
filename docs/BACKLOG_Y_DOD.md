# Backlog de seguridad y Definition of Done

## Historias de seguridad

| ID | Historia | Riesgo | Prioridad | Criterios de aceptacion | Responsable |
|---|---|---|---|---|---|
| SEC-01 | Como equipo, queremos parametrizar la consulta de autenticación para impedir inyección SQL. | Acceso no autorizado a cuentas y datos. | Crítica | La consulta usa parámetros; una carga de inyección recibe 401; las pruebas pasan. | Cantos Yépez Elkin Omar |
| SEC-02 | Como equipo, queremos retirar secretos y contraseñas del código para evitar su exposición en Git. | Uso indebido de credenciales. | Alta | Los secretos se leen desde variables de entorno; `.env` está ignorado; detect-secrets bloquea una credencial falsa. | Fernández Zambrano José Carlos |
| SEC-03 | Como equipo, queremos actualizar las dependencias vulnerables para reducir el riesgo de CVE conocidos. | DoS, fuga de datos y fallos en clientes HTTP. | Crítica | `pip-audit -r requirements.txt` termina sin vulnerabilidades conocidas. | Lucas García Jork Davis |
| SEC-04 | Como equipo, queremos automatizar SAST, SCA, pruebas y detección de secretos para bloquear integraciones inseguras. | Regresiones de seguridad en la rama principal. | Alta | El workflow falla con la versión vulnerable y pasa con la versión corregida. | Todo el equipo |

## Definition of Done

Una historia solo puede cerrarse cuando:

1. Cumple sus criterios funcionales y tiene pruebas automatizadas relevantes.
2. Bandit termina sin hallazgos de severidad media o alta.
3. pip-audit termina sin vulnerabilidades conocidas en las dependencias declaradas.
4. detect-secrets no detecta credenciales nuevas y el hook pre-commit esta habilitado.
5. Otro integrante revisa y aprueba el cambio mediante Pull Request.
6. El pipeline de GitHub Actions termina en verde y la evidencia se adjunta al tablero.
