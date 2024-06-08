
class AddressModel:
  def __init__(self, id: str, complete_address: str) -> None:
    self.id = id
    self.complete_address = complete_address


class AddressModelInsert:
  def __init__(self,  street: str,
                      number: str,
                      complement: str,
                      neighborhood: str,
                      city: str,
                      state: str,
                      country: str,
                      zip_code: str
                ) -> None:
    self.street = street
    self.number = number
    self.complement = complement
    self.neighborhood = neighborhood
    self.city = city
    self.state = state
    self.country = country
    self.zip_code = zip_code
    
