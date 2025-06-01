#Ejercicio 9: ¿Qué hora es?
#Juan está estudiando muy duro para
#las pruebas de Jala University y quiere
#saber cuando puede tomar un descanso.


from datetime import datetime 

hora_actual = datetime.now().time()
hora_descanso = datetime.strptime("14:00", "%H:%M").time()

if hora_actual >= hora_descanso:
    print("Es hora de descansar")
else:
    print("Aun no es hora de descansar")