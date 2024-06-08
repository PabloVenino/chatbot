import google.generativeai as genai
from model_commands import instructions, generation_config, safety_settings
import json
import jsonpickle
from models.customer.customer_model import CustomerModel
from order import Order
import db_connection

class Conversation:
  """Initiates a new conversation with the bot, with intentions to close a Order.
  """

  def __init__(self, customer: CustomerModel) -> None:
    genai.configure(api_key="AIzaSyDmjeHfiVP0dB84ojqJuP9gLIWTdOpBK7Q")

    self.cursor, self.connection = db_connection.connect_to_database()
    self.word_to_end = "FIM"
    self.model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings,
                                  system_instruction=instructions)
    self.order = Order(customer, 1, 2)
    self.customer = customer
    self.chat_id = ''


  def new_chat(self):
    print("############   INICIO DO CHAT  ############")
    print("\n")

    self.start_chat()
    
    prompt: str = input("Ola :) eu sou o bolobot Tavares b.IA, como posso te ajudar a pedir seu bolo hoje? \n")

    chat = self.model.start_chat(history=[])
    is_first_message = True

    while(prompt != self.word_to_end):
      if(is_first_message):
        is_first_message = False
        prompt = json.dumps(self.customer.to_json()) + prompt
        
      response = chat.send_message(prompt)      

      try:
        bot_response = json.loads(response.text)
        # if(bot_response["currentOrder"].length > 0):
        # print("TODO: Implement order")

        for move in bot_response["moves"]:
          match move["movement"]:
            case "finishOrder":
              teste = bot_response
              self.order.insert_new_order()
              break

            case "cancelOrder":
              self.order.cancel_order()
              break

            case "close":
              prompt="FIM"
              self.end_chat()
              break

        print(bot_response["response"])
        
        movements = [item["movement"] for item in bot_response["moves"]]
        moves = "|".join(movements)

        self.insert_bot_message(
          self.chat_id,
          bot_response["thought"],
          moves,
          bot_response["response"]
        )

        prompt = input("\n - ")
      
      except Exception as ex:
        print(ex)

    print("#### FIM DO CHAT ####")

    self.end_chat()



  def start_chat(self):
    self.cursor.execute("""
      set nocount on
      EXEC [dbo].[insert_chat]
        @customer_id = ?
    """, self.customer.id)

    row = self.cursor.fetchone()
    
    self.chat_id = row.chat_id

    print("Chat iniciado")


  def end_chat(self):
    self.cursor.execute("""
      set nocount on
      EXEC [dbo].[close_chat]
        @chat_id = ?
    """, self.chat_id)

  
  def insert_bot_message(self, chat_id, thought, moves, response):
    self.cursor.execute("""
      set nocount on
      exec [dbo].[insert_message]
        @chat_id = ?,
        @model_thought = ?,
        @moves = ?,
        @response = ?
    """, chat_id, thought, moves, response)


