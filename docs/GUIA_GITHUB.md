# Guia para obtener las evidencias reales de GitHub

## Preparar el repositorio

1. Crea un repositorio vacio en la cuenta del equipo.
2. Configura el remoto con `git remote add origin URL_DEL_REPOSITORIO`.
3. Publica la rama principal con `git push -u origin main`.
4. Crea en GitHub Projects un tablero con las columnas Backlog, En progreso, En revision y Terminado.
5. Copia las historias de `docs/BACKLOG_Y_DOD.md` y asigna responsables reales.

## Demostracion roja y verde

El historial local conserva una etiqueta `vulnerable` y el estado corregido en `main`.

1. Crea una rama remota con el estado vulnerable: `git push origin vulnerable:mini-sprint`.
2. Abre un Pull Request de `mini-sprint` hacia `main` y captura el Build Breaker en rojo.
3. Lleva la correccion a esa rama: `git push origin mini-sprint:mini-sprint`.
4. Espera el nuevo workflow, comprueba que todas las verificaciones esten verdes y solicita la aprobacion de otro integrante.
5. Captura el Pull Request aprobado y el tablero actualizado; despues, integra el Pull Request en `main`.

No subas el archivo `.env`, bases de datos locales ni credenciales reales.
