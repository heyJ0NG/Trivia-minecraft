respuestas_correctas = 0;

print("Bienvenido a trivia sobre Minecraft")
print()
print ("Pondre a prueba tus conocimientos sobre el juego en modo supervivencia:")
print()
print("Recuerda: Debes ingresar tus respuestas en MINÚSCULAS")
print()

# Es importante dar instrucciones sobre cómo jugar:
print ("Responder las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

print("1.Para entrar en contexto, inicias un mundo nuevo y apareces en un bosque, vas a necesitar una Mesa de Trabajo para fabricar tus primeras herramientas, ¿Cual es el material que necesitas para ello?")

print()
print("a) Obsidiana")
print("b) Madera")
print("c) Roca")
print("d) Hierro")
print()
respuesta_1 = input("Escribe la letra de la respuesta en MINÚSCULA: ")
print()
respuesta_correcta = "b"
if respuesta_1 == respuesta_correcta:
   print("¡Correcto!")
   respuestas_correctas = respuestas_correctas + 1;
elif respuesta_1 == "a":
 print("¡Incorrectoooo!")
elif respuesta_1 == "b":
 print("¡Correcto!")
elif respuesta_1 == "c":
 print("No es")
elif respuesta_1 == "d":
 print("No humano, eso no existe")
else:
  print("!Incorrecto¡")
print()
while respuesta_1 not in ("a","b","c","d"): respuesta_1 = input ("Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta ")
print()
print()


print("2. Ya has fabricado tus primeras herramientas, necesitas ahora una armadura de hierro para ser mas fuerte,¿Cual de las siguientes herramientas se necesita como MINIMO para picar el mineral de hierro?")
print()

print("a. Pico de Diamante")
print("b. Pico de Madera")
print("c. Pico de Piedra")
print("d. Asada de Oro")
print()
respuesta_2 = input("Escribe la letra de la respuesta en MINÚSCULA: ")
respuesta_correcta = "c"

if respuesta_2 == respuesta_correcta:
  print()
  print("¡Correcto!")
  respuestas_correctas = respuestas_correctas + 1;
elif respuesta_2 == "a":
 print("Si pero no") 
elif respuesta_2 == "b":
 print("Nope")
elif respuesta_2 == "c":
 print("¡Correcto!")
elif respuesta_2 == "d":
 print("nonononono")
else:
  print("!Incorrecto¡")
print()
while respuesta_2 not in ("a","b","c","d"): respuesta_2 = input ("Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta ")
print()
print()


print("3. El sol está pronto a ocultarse y llegará la primera noche, pronto empezaran a aparecer mobs hostiles y no tienes cama, necesitaras encontrar una zona segura para pasar la primera noche, ¿Cuál te parece la mejor opción?")
print()
print("a) Buscar una aldea y utilizar la cama de los aldeanos para evitar la noche")
print("b) Buscar ovejas y fabricar una cama con su lana y la madera obtenida previamante")
print("c) Hacer un hueco en la tierra, tapar el techo y hacerte bolita")
print("d) Aprovechar para minar que los diamantes no se encuentran solos")

print()
respuesta_3 = input("Escribe la letra de la respuesta en MINÚSCULA: ")
print()
respuesta_correcta = "d"

if respuesta_3 == respuesta_correcta:
  print("¡Correcto!, no hay tiempo que perder :D")
  print()

  respuestas_correctas = respuestas_correctas + 1;
elif respuesta_3 == "a":
 print("Nooo, esos diamantes no se consiguen solos") 
elif respuesta_3 == "b":
 print("Nooo, esos diamantes no se consiguen solos")
elif respuesta_3 == "c":
 print("Nooo, esos diamantes no se consiguen solos")
elif respuesta_3 == "d":
 print("Correcto")
else:
  print("!Incorrecto¡")
print()
while respuesta_3 not in ("a","b","c","d"): respuesta_3 = input ("Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta ")
print()
print()


print("4. De pronto crece en ti el espiritu de speedrunner y quieres ir al nether, ¿Que necesitas para hacer un portal funcional?")
print()
print("a) 8 de obsidiana y 2 palos para hacer fuego")
print("b) 14 de obsidiana y polvora")
print("c) 10 de obsidiana y 1 mechero")
print("d) 16 de obsidiana y gasolina")
print()
respuesta_4 = input("Escribe la letra de la respuesta en MINÚSCULA: ")
respuesta_correcta = "c"
print()
if respuesta_4 == respuesta_correcta:
  print("!Así es, como minimo son 10!")
  print()

  respuestas_correctas = respuestas_correctas + 1;
elif respuesta_4 == "a":
 print("Cosas que poca gente sabe (no es la respuesta)") 
elif respuesta_4 == "b":
 print("Ojala, pero no es")
elif respuesta_4 == "c":
 print("Correcto")
elif respuesta_4 == "d":
 print("Incorrecto")
else:
  print("!Incorrecto¡")
print()
while respuesta_4 not in ("a","b","c","d"): respuesta_4 = input ("Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta ")
print()


print("5. Has entrado al nether y apareces al lado de una fortaleza, ¿Cuales son los 2 objetos que necesitas para encontrar el portal al END y activarlo?")
print()
print("a) Lagrima de Ghast y Perla de ender")
print("b) Vara de Blaze y Verruga de nether")
print("c) Verruga de Nether y Arena de almas")
print("d) Vara de Blaze y Perla de Ender")
print()

respuesta_5 = input("Escribe la letra de la respuesta en MINÚSCULA: ")
print()
respuesta_correcta = "d"

if respuesta_5 == respuesta_correcta:
  print("!Correcto, la vara de Blaze te da polvo de Blaze y junto a la perla de ender podras fabricar Ojos de Ender!")
  print()
  respuestas_correctas = respuestas_correctas + 1;
elif respuesta_5 == "a":
 print("Incorrecto") 
elif respuesta_5 == "b":
 print("Incorrecto")
elif respuesta_5 == "c":
 print("Incorrecto")
elif respuesta_5 == "d":
 print("Correcto, la vara de Blaze te da polvo de Blaze y junto a la perla de ender podras fabricar Ojos de Ender")
else:
  print("!Incorrecto¡")
while respuesta_5 not in ("a","b","c","d"): respuesta_5 = input ("Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta ")
print()
print()


print("6. Has pasado la ultima hora buscando el portal al END y lo has activado, te paras al borde del ingreso y una criatura hostil te empuja debido a que no destruiste su generador que se encuentra al frente, ¿Cual puede ser el nombre de esta criatura?")
print()
print("a) Endermite")
print("b) Warden")
print("c) Piglin")
print("d) Pez de plata (Lepisma)")
print()
respuesta_6 = input("Escribe la letra de la respuesta en MINÚSCULA: ")
respuesta_correcta = "d"
print()
if respuesta_6== respuesta_correcta:
  print("!CORRECTO")
  print()
  respuestas_correctas = respuestas_correctas + 1;
elif respuesta_6 == "a":
 print("Incorrecto") 
elif respuesta_6 == "b":
 print("No es")
elif respuesta_6 == "c":
 print("No existe generadores de Piglin")
elif respuesta_6 == "d":
 print("Correcto")
else:
  print("!Incorrecto¡")
print()
while respuesta_6 not in ("a","b","c","d"): respuesta_6 = input ("Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta ")
print()
print()


print("7. Antes de empezar a atacar a la dragona del END, ¿Qué acción deberias completar primero?")
print()
print("a) Destruir las torres que regeneran su vida")
print("b) Colocar una cama y dormir para establecer un punto de reaparación")
print("c) Lanzarle una poción de debilidad")
print("d) Llamar al Rey de la Noche de GOT")
print()
respuesta_7 = input("Escribe la letra de la respuesta en MINÚSCULA: ")
respuesta_correcta = "a"
print()
if respuesta_7 == respuesta_correcta:
  print("!CORRECTO!")
  respuestas_correctas = respuestas_correctas + 1;
elif respuesta_7 == "a":
 print("Correcto") 
elif respuesta_7 == "b":
 print("Creo que es tu primera vez en el END")
elif respuesta_7 == "c":
 print("Incorrecto")
elif respuesta_7 == "d":
 print("Espero que haya un mod de eso, la respuesta esta mal")
else:
  print("!Incorrecto¡")
print()
while respuesta_7 not in ("a","b","c","d"): respuesta_7 = input ("Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta ")
print()
print()
print("*** PUNTAJE FINAL ***")

print()
print("RESPUESTAS CORRECTAS (+)")
print(respuestas_correctas)
print("RESPUESTAS INCORRECTAS (-)") 
print (7 - respuestas_correctas) 
print()
print("TOTAL DE PREGUNTAS: 7")
print()
print()
print("¡¡¡Gracias por participar, si me permites, te comparto la parte final del poema presentado en los creditos de este grandioso juego :D!!!")
print()
print()
print("...")
print("Y a veces el jugador creía que el universo le habló a través de ceros y unos,")
print("a través de la electricidad del mundo, a través de las palabras que se desplazan")
print("por una pantalla al final de un sueño.")
print()
print("Y el universo dijo Te amo.")
print("Y el universo dijo que jugaste bien al juego.")
print("Y el universo dijo que lo único que necesitas está en ti.")
print("Y el universo dijo que tú eres más fuerte de lo que sabes.")
print("Y el universo dijo que tú eres la luz del sol.")
print("Y el universo dijo que tú eres la noche.")
print("Y el universo dijo que la oscuridad con la que luchas está en ti.")
print("Y el universo dijo que la luz que buscas está en ti.")
print("Y el universo dijo que tú no estás solo.")
print()
print()
print("Y el universo dijo que no estás separado de todas las demás cosas.")
print("Y el universo dijo que tú eres el universo probándose a sí mismo,")
print("hablándose a sí mismo, leyendo su propio código.")
print("Y el universo dijo Te amo, porque tú eres el amor.")
print("Y el juego se terminó, y el jugador despertó del sueño.")
print("Y el jugador empezó un nuevo sueño. Y el jugador soñó otra vez,")
print("soñó mejor. Y el jugador fue el universo. Y el jugador fue el amor.")

print("Tú eres el jugador.")
print("Despierta.")
print("")
print("")
print("Poema completo en:")
print("https://minecraft.fandom.com/es/wiki/Poema_del_End")
print("")

Jugando = True                          

while Jugando:                          
  print("Trivia")                          
  print("opción: si ó no...")                           
  respuesta = input("¿Qusisieras jugar nuevamente?: ") 

  if respuesta == "si":                           
      print("¡Genial, corre el programa nuevamente") 
      Jugando = False 
  else:                                                
      if respuesta == "si":         
         print("Genial, corre el programa nuevamente")   
         Jugando = False
         while respuesta != "si" and respuesta !="no":                                             
            print("No te entendí")                                           
            respuesta = input("Deseas jugar de nuevo?: ")                    
      if respuesta == "no":                                         
          print("Hey, Muchas gracias por jugar")           
          Jugando = False                            
      else:                                                            
            print("ingrese su respuesta en minúsculas") 