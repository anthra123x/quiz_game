#Ejemplo de validación de edad y estatura

edad = int(input("ingrese su edad: "))

if edad < 18 or edad > 65:
    print("no puedes subir por seguridad")
else:
    estatura = float(input("ingrese su estatura en metros:"))
    if estatura < 1.55: 
        print("no puedes subir, no alcanzas la estatura minima")
    elif edad > 40:
        problema_cardiaco = input("sufre algun problema cardiaco (sino")
        if problema_cardiaco.lower() == "si":
            print("no puedes subir por su salud")
        else:
            print("puede subir")
    else: 
        print("puede subir")