import db_connection as db
import sys
from models.customer.customer_model import CustomerModel
from models.customer.address_model import AddressModel, AddressModelInsert

class Customer:
  """_summary_
  """

  def __init__(self, customer_id) -> dict:
    self.cursor, self.connection = db.connect_to_database()
    self.customer_id = customer_id


  def add_customer() -> None:
    print("TODO: Implement add new customer")

  
  def get_customer_data(self) -> CustomerModel:
    self.cursor.execute("""
        set nocount on
        exec [dbo].[select_customer_by_id]
          @customer_id = ?
      """, self.customer_id
    )

    rows = db.read_dataset(self.cursor)
    
    customer = CustomerModel(id=self.customer_id, 
                             name=rows[0]["name"], 
                             birth_date=rows[0]["birth_date"], 
                             is_active=rows[0]["is_active"])
    
    return customer

  def add_new_customer_address(address: AddressModelInsert) -> str:

    print("TODO: Implement add new address for the user")
    return "GUID"

  
  def get_customer_addresses(self) -> list[AddressModel]:
    self.cursor.execute("""
      set nocount on
      exec [dbo].[select_customer_addresses_by_id]
        @customer_id = ?

    """, self.customer_id)

    rows = db.read_dataset(self.cursor)
    
    addresses = []

    for row in rows:
      address = AddressModel(id=row["customer_address_id"], complete_address=row["complete_address"])
      addresses.append(address)

    return addresses