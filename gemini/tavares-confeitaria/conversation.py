import google.generativeai as genai
from model_commands import instructions, generation_config, safety_settings
import json
from order import Order
import db_connection

class Conversation:
  """Initiates a new conversation with the bot, with intentions to close a Order.
  """

  def __init__(self, customer_id, customer_addresses) -> None:
    genai.configure(api_key="AIzaSyDmjeHfiVP0dB84ojqJuP9gLIWTdOpBK7Q")

    self.cursor, self.connection = db_connection.connect_to_database()
    self.word_to_end = "FIM"
    self.model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings,
                                  system_instruction=instructions)
    self.order = Order(customer_id)
    self.customer_id = customer_id
    self.customer_addresses = customer_addresses
    self.chat_id = ''


  def new_chat(self):
    print("############   INICIO DO CHAT  ############")
    print("\n")

    self.start_chat(self.customer_id)
    
    prompt = input("Ola :) eu sou o bolobot Tavares b.IA, como posso te ajudar a pedir seu bolo hoje? \n")

    chat = self.model.start_chat(history=[])

    while(prompt != self.word_to_end):
      response = chat.send_message(prompt)

      bot_response = json.loads(response.text)
      
      # if(bot_response["currentOrder"].length > 0):
        # print("TODO: Implement order")

      for move in bot_response["moves"]:
        match move.movement:
          case "finishOrder":
            
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

    print("#### FIM DO CHAT ####")

    self.end_chat()



  def start_chat(self, customer_id):
    self.cursor.execute("""
      set nocount on
      EXEC [dbo].[insert_chat]
        @customer_id = ?
    """, customer_id)

    self.chat_id = self.cursor.fetchval()
    
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


