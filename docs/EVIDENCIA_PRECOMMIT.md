# Evidencia del bloqueo local de secretos

Se instaló el hook de pre-commit y se intentó confirmar temporalmente un archivo llamado `prueba-secreto.txt` con una credencial ficticia. El archivo no se incorporó al historial.

Resultado real del hook:

```text
Detectar secretos........................................................Failed
- hook id: detect-secrets
- exit code: 1

ERROR: Potential secrets about to be committed to git repo!

Secret Type: AWS Access Key
Location:    prueba-secreto.txt:2

Secret Type: Base64 High Entropy String
Location:    prueba-secreto.txt:2

Secret Type: Secret Keyword
Location:    prueba-secreto.txt:2
```

El rechazo demuestra que el control shift-left funciona antes de que una credencial llegue al historial remoto.
