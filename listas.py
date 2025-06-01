#Listas (crear, agregar, eliminar, mostrar)

actividades = ["desayunar","estudiar", "leer"]

#elimiar una actividad
actividad_completada = "estudiar"
if actividad_completada in actividades:
  actividades.remove(actividad_completada)

#agregar una actividad
nueva_actividad = "dormir"
actividades.append(nueva_actividad)

print("agenda actual", actividades)