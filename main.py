def saludar(nombre):
    return f"Hola, {nombre}. Jenkins está funcionando perfectamente."


if __name__ == "__main__":
    nombre = "Luis"
    mensaje = saludar(nombre)
    print(mensaje)
