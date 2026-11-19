# Guion para la presentacion ejecutiva de 5 minutos

## 0:00 a 0:40 Contexto

Presentar el objetivo del mini-sprint: heredar una API Flask con deuda de seguridad y aplicar controles DevSecOps sin detener el flujo de desarrollo. Mostrar brevemente los tres endpoints y el tablero.

## 0:40 a 1:50 Hallazgos

- La autenticacion concatenaba entradas del usuario en SQL, confirmada por Bandit B608 y CWE-89.
- La API key y las contrasenas de demostracion estaban dentro del codigo y la base guardaba texto plano.
- pip-audit encontro 54 avisos en 5 paquetes, equivalentes a 28 CVE unicos.
- No habia pruebas, deteccion de secretos ni Build Breaker.

## 1:50 a 3:20 Mejoras

- Mostrar la consulta parametrizada y la verificacion de hashes.
- Explicar que `.env` no se versiona y que detect-secrets bloquea nuevas credenciales.
- Mostrar el cambio de dependencias y los SBOM antes y despues.
- Enseñar el Pull Request: primero el workflow rojo del estado `vulnerable` y luego el verde tras el commit de correccion.

## 3:20 a 4:20 Tablero y Definition of Done

Mostrar las historias SEC-01 a SEC-04, responsables y estados. Resaltar que una tarea no termina hasta que Bandit y pip-audit pasan, detect-secrets no encuentra credenciales, otro integrante revisa el Pull Request y el pipeline queda verde.

## 4:20 a 5:00 Leccion aprendida

El reto principal fue convertir la seguridad en controles repetibles y tempranos. En el modelo anterior, los defectos podian descubrirse al final; con DevSecOps, el hook local evita secretos antes del commit y el pipeline impide integrar codigo inseguro. La seguridad pasa a ser un criterio compartido del equipo y no una revision aislada.
