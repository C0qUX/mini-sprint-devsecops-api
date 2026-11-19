# Registro de evidencias reales de GitHub

## Repositorio y tablero

El repositorio se publico en https://github.com/C0qUX/mini-sprint-devsecops-api y se creo el proyecto `Mini-Sprint DevSecOps` en https://github.com/users/C0qUX/projects/2. Las historias SEC-01 a SEC-04 se registraron como Issues reales, se asignaron y se cerraron al completar sus criterios.

## Demostracion roja y verde completada

1. El Pull Request #6 reprodujo el estado vulnerable y los cuatro trabajos fallaron: pruebas, Bandit, pip-audit y detect-secrets.
2. Un segundo commit restauro las correcciones y los mismos cuatro trabajos terminaron en verde.
3. `ElkinC1` y `JoC1305` aprobaron la revision.
4. El Pull Request se integro en `main` y la ejecucion posterior tambien termino en verde.

No se subieron archivos `.env`, bases de datos locales ni credenciales reales.
