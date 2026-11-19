# Evidencia controlada del Build Breaker

Esta rama se utiliza únicamente para demostrar el comportamiento del pipeline con el estado vulnerable heredado.

La primera ejecución debe ser rechazada por los controles SAST, SCA y las pruebas de seguridad. Después se restaura el código corregido en un nuevo commit para comprobar que los mismos controles terminan correctamente.
