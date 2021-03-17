class Repository(object):
  def __init__(self, adapter=None):
    self.client = adapter

  def delete(self, criteria, table):
    return self.client.delete(criteria, table)
 
  def create(self, data, table):
    return self.client.add(data, table)
  
  def update(self, new_data, criteria, table):
    return self.client.update(new_data, criteria, table)
  
  def find(self, select, from_tables, criteria, limit):
    return self.client.find(select, from_tables, criteria, limit)
