import google.generativeai as genai
from model_commands import instructions, generation_config, safety_settings
import db_connection
import json

class Order:
  """ Class for orders, containing functions for creating, canceling, 
  """

  def __init__(self, customer_id) -> None:
    self.product_id = '279E50B4-5E81-4FF9-94BA-FBA024B73993'
    self.customer_id = customer_id


  def new_order(self):
    


    print(" ")
    print('############   FIM DO CHAT     ############')


  def insert_new_order(self, customerAddressId, productSizeId, Quantity, Discount):
    cursor, connection = db_connection.connect_to_database(
      # sqlserver_dsn,
      # sqlserver_user,
      # sqlserver_password
    )


    ## Aqui ja vou ter que ter o 
    ## customer_address_id,product_size_id, quantity, discount

    cursor.execute("""
      EXEC [dbo].[insert_new_order] 
        @customer_id = ?,
        @customer_address_id = ?,
        @product_id = ?,
        @product_size_id = ?,
        @quantity = ?,
        @discount = ?
    """, self.customer_id, customer_address_id, self.product_id, product_size_id, Quantity, Discount)


  def get_order_by_id(self, order_id):
    print("Implement get order by its id")


  def cancel_order(self, order_id):
    print("Implement cancel order")


  def get_order_by_customer_id(self, customer_id):

    print("Implement get order by customer id")
  
