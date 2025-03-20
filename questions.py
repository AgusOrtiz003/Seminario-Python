import random
 # Preguntas para el juego
questions = ["¿Qué función se usa para obtener la longitud de una cadena en Python?","¿Cuál de las siguientes opciones es un número entero en Python?",
 "¿Cómo se solicita entrada del usuario en Python?", "¿Cuál de las siguientes expresiones es un comentario válido en Python?","¿Cuál es el operador de comparación para verificar si dos valores son iguales?",]
 # Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
 ("size()", "len()", "length()", "count()"),
 ("3.14", "'42'", "10", "True"),
 ("input()", "scan()", "read()", "ask()"),
 (
 "// Esto es un comentario",
 "/* Esto es un comentario */",
 "-- Esto es un comentario",
 "# Esto es un comentario",
 ),
 ("=", "==", "!=", "==="),
 ]
exit_status=0
puntaje=0
 # Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
6. 
7. 
1. 
2. 
3.
# Se seleccionan las preguntas y las respuestas aleatoriamente
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)
for _ in range(3):
    # Se muestra la pregunta y las respuestas posibles
    question=questions_to_ask[_]
    print(question[0])
    for i, answer in enumerate(question[1]):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        # Se verifica si la respuesta es correcta
        if (user_answer.isdigit()==False or ((int(user_answer)-1)<0 or (int(user_answer)-1)>3)):
            print("Respuesta no válida")
            exit_status=1
            break
        elif int(user_answer)-1 == question[2]:
            print("¡Correcto!")
            puntaje+=1
            break
        elif intento==0:
            print("Incorrecto, te queda 1 intento")
            puntaje+=-0.5
            continue
        else:
            # Si el usuario no responde correctamente después de 2 intentos,
            # se muestra la respuesta correcta
            print("Incorrecto. La respuesta correcta es:")
            print(question[1][2])
            # Se imprime un blanco al final de la pregunta
            print()
            puntaje+=-0.5
    if exit_status==0:
        continue
    else:
        print(f"exit status = {exit_status}")
        break
print(f"Hiciste {puntaje} puntos")