# Backlog de seguridad y Definition of Done

## Historias de seguridad

| ID | Historia | Riesgo | Prioridad | Criterios de aceptacion | Responsable |
|---|---|---|---|---|---|
| SEC-01 | Como equipo, queremos parametrizar la consulta de autenticacion para impedir inyeccion SQL. | Acceso no autorizado a cuentas y datos. | Critica | La consulta usa parametros; una carga de inyeccion recibe 401; las pruebas pasan. | Integrante 1 |
| SEC-02 | Como equipo, queremos retirar secretos y contrasenas del codigo para evitar su exposicion en Git. | Uso indebido de credenciales. | Alta | Los secretos se leen desde variables de entorno; `.env` esta ignorado; detect-secrets bloquea una credencial falsa. | Integrante 2 |
| SEC-03 | Como equipo, queremos actualizar las dependencias vulnerables para reducir el riesgo de CVEs conocidos. | DoS, fuga de datos y fallos en clientes HTTP. | Critica | `pip-audit -r requirements.txt` termina sin vulnerabilidades conocidas. | Integrante 3 |
| SEC-04 | Como equipo, queremos automatizar SAST, SCA, pruebas y deteccion de secretos para bloquear integraciones inseguras. | Regresiones de seguridad en la rama principal. | Alta | El workflow falla con la version vulnerable y pasa con la version corregida. | Integrante 4 |

## Definition of Done

Una historia solo puede cerrarse cuando:

1. Cumple sus criterios funcionales y tiene pruebas automatizadas relevantes.
2. Bandit termina sin hallazgos de severidad media o alta.
3. pip-audit termina sin vulnerabilidades conocidas en las dependencias declaradas.
4. detect-secrets no detecta credenciales nuevas y el hook pre-commit esta habilitado.
5. Otro integrante revisa y aprueba el cambio mediante Pull Request.
6. El pipeline de GitHub Actions termina en verde y la evidencia se adjunta al tablero.
