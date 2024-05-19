import config
from openai import OpenAI
client = OpenAI(
    api_key = config.api_key
)
#Lista de Mensajes y Roles
messages = [
            {"role": "system", "content": "Eres un asistente cordial y prestativo"} 
          ]
#Solicitud del usuario 
input_message = input ("Esperando tu pregunta: ")

#Adicionamos el input a la lista messages
messages.append({"role": "user", "content": input_message})

print("Bienvenido! Soy su asistente virtual")
while input_message != "fin":

  #Características de la respuesta
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature = 1, #Cuan creativa queremos que sea la respuesta (va de 0 a 2)
    max_tokens=200 #Delimitamos el prompt de respuesta
  )

  #Obtengo el rol del asistente
  role = response.choices[0].message.role

  #Obtengo la respuesta depurada.
  content = response.choices[0].message.content

  #Contextualizamos al asistente con la respuesta otorgada, para que en la próxima pregunta, tenga en cuenta la respuesta anterior.
  #Para ello, tambien hacemos un appen.
  messages.append({"role": "user", "content": content
      })

  #Muestro la respuesta con el formato deseado
  print("role: ", role) 
  print ("Respuesta:",response.choices[0].message.content)

  #Tener en cuenta que choices es un array, ya que puede tener mas de una respuesta para la pregunta del usuario

  #Solicitamos al usuario un nuevo ingreso
  input_message = input ("Esperando tu pregunta: ")

  #Adicionamos el nuevo ingreso a la lista de mensajes
  messages.append({"role": "user", "content": input_message})

