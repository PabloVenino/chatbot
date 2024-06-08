import google.generativeai as genai
from model_commands import instructions, generation_config, safety_settings
import db_connection
import json

from models.customer.customer_model import CustomerModel

class Order:
  """ Class for orders, containing functions for creating, canceling, 
  """

  def __init__(self, customer: CustomerModel, product, order_details) -> None:
    self.product = { 
      "id": "279E50B4-5E81-4FF9-94BA-FBA024B73993", 
      "size_id": "1D7DB326-3D62-440D-BF24-CC59C6485DFB"
    } # product
    self.order_details = {
      "quantity": 1,
      "discount": 0
    } # order_details
    self.customer = customer
    self.cursor, self.connection = db_connection.connect_to_database()


  def new_order(self):
    
    print(" ")
    print('############   FIM DO CHAT     ############')


  def insert_new_order(self):
    ## Aqui ja vou ter que ter o 
    ## customer_address_id,product_size_id, quantity, discount

    self.cursor.execute("""
      EXEC [dbo].[insert_new_order] 
        @customer_id = ?,
        @customer_address_id = ?,
        @product_id = ?,
        @product_size_id = ?,
        @quantity = ?,
        @discount = ?
    """, 
      self.customer.id, 
      self.customer.addresses.id, 
      self.product.id, 
      self.product.size_id, 
      self.order_details.quantity, 
      self.order_details.discount)


  def get_order_by_id(self, order_id):
    print("Implement get order by its id")

  def add_product_to_order(self, product):
    if (self.product != {}):
      return
    
    self.product = product


  def cancel_order(self, order_id):
    print("Implement cancel order")


  def get_order_by_customer_id(self):

    print("Implement get order by customer id")
  
