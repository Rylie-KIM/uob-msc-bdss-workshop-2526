class ClinDS:
  def __init__(self):
    self.data = {}
    self.metadata = {"age": 0, "sex": 1, "height": 2, "weight": 3}

  def add_row(self, id, age, sex, height, weight):
    # Adds a new row, here each row in the table system is a dictionary key paired with a list
    self.data[id] = [age, sex, height, weight]

  def remove_row(self, id):
    del self.data[id]

  def get_entry(self, id, feature):
    # YOUR CODE
    return self.data[id][feature]

  def change_entry(self, id, feature, new_value):
    # YOUR CODE HERE!
    self.data[id][feature] = new_value
    pass

  def mean(self, feature):
    # YOUR CODE HERE!
    sum = 0
    for key in self.data.keys():
        sum += self.data[key][feature]
    return sum / len(self.data[feature])

  def bmi(self, id):
    # YOUR CODE HERE!
    weight = data[id]["weight"]
    height = data[id]["height"]
    bmi = weight / (height ** 2)
    return bmi