import db_connection

class Customer:
  """_summary_
  """

  def __init__(self) -> None:
    self.cursor, self.connection = db_connection.connect_to_database()


  def add_customer():
    print("TODO: Implement add new customer")

  
  def get_customer_data():
    print("TODO: Implement get customer data")


  def add_new_customer_address():
    print("TODO: Implement add new address for the user")

  
  def get_customer_addresses(self, customer_id):
    self.cursor.execute("""
      set nocount on
      exec [dbo].[select_customer_addresses_by_id]
        @customer_id = ?

    """, customer_id)

    columns = [column[0] for column in self.cursor.description]

    rows = [dict(zip(columns, row)) for row in self.cursor.fetchall()]

    return rows