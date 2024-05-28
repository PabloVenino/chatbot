import os
import configparser
from conversation import Conversation
from customer import Customer

ini = configparser.ConfigParser()
ini.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.ini'))

sqlserver_dsn = ini.get('sqlserver', 'dsn')
sqlserver_user = ini.get('sqlserver', 'usr')
sqlserver_password = ini.get('sqlserver', 'pwd')

customer_id = "199E8E11-ADB3-4C47-B20D-CFC9258E4E79"
customer_address_id = "122DBDAD-E8D9-4250-B35A-07DB34B9586B"
product_size_id = "DD90F233-957E-43F0-A10C-C08D5453163B"
    

def main():
  print("Inicio do Chatbot")

  ## TODO: Pensar em como vamos recuperar o customer_id.
  
  customer = Customer()
  customer_addresses = customer.get_customer_addresses(customer_id)

  conversation = Conversation(customer_id, customer_addresses)
  conversation.new_chat()

  print("Fim do Chatbot")

if __name__ == '__main__':
  main()