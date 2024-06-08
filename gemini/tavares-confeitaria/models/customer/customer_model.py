
import datetime
import json

from models.customer.address_model import AddressModel

class CustomerModel:
  def __init__(self, id: str, name:str, birth_date:datetime = None, is_active:bool = False) -> None:
    self.id = id
    self.name = name
    self.birt_date = birth_date
    self.is_active = is_active
    self.addresses = {}

  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "birth_date": self.birth_date.isoformat() if self.birth_date else None,
      "is_active": self.is_active,
      "addresses": self.addresses
    }


  def to_json(self):
    return json.dumps(self.to_dict())