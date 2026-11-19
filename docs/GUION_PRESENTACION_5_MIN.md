# Guion para la presentacion ejecutiva de 5 minutos

## 0:00 a 0:40 Contexto

"En esta práctica recibimos una API Flask que funcionaba, pero tenía deuda de seguridad. Nuestro objetivo fue corregirla e integrar controles de seguridad sin detener el flujo de desarrollo." Después mostramos brevemente los tres endpoints y el tablero.

## 0:40 a 1:50 Hallazgos

- La autenticación concatenaba entradas del usuario en SQL, algo que Bandit confirmó con B608 y CWE-89.
- La API key y las contraseñas de demostración estaban dentro del código y la base guardaba texto plano.
- pip-audit encontró 54 avisos en 5 paquetes, equivalentes a 28 CVE únicos.
- No había pruebas, detección de secretos ni Build Breaker.

## 1:50 a 3:20 Mejoras

- Mostrar la consulta parametrizada y la verificacion de hashes.
- Explicar que `.env` no se versiona y que detect-secrets bloquea nuevas credenciales.
- Mostrar el cambio de dependencias y los SBOM antes y despues.
- Enseñar el Pull Request: primero el workflow rojo del estado `vulnerable` y luego el verde tras el commit de correccion.

## 3:20 a 4:20 Tablero y Definition of Done

Mostrar las historias SEC-01 a SEC-04, responsables y estados. Resaltar que una tarea no termina hasta que Bandit y pip-audit pasan, detect-secrets no encuentra credenciales, otro integrante revisa el Pull Request y el pipeline queda verde.

## 4:20 a 5:00 Leccion aprendida

"La principal dificultad fue acostumbrarnos a revisar la seguridad desde el inicio. Aprendimos que un pipeline rojo no significa que el equipo fracasó, sino que el control encontró el problema antes de que llegara a la rama principal. Con DevSecOps, la seguridad se volvió una responsabilidad compartida del equipo."
