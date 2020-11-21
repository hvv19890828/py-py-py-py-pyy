class parent:
  def __init__(self,arg1):
        print("printed arg1 from parent init: ", arg1)
  int = 33
  dict1 = {"dict_key1": "dict_value1"}
  strng = "par_string value"
  def func1(self, arg1):
     print("'printed arg1 + self.int, self.dict1, self.strng'from func1 ", arg1 + self.int, self.dict1, self.strng)
     self.strng =  "par_string value after reassigned incidev parent_func1"
     print("printed 'arg1+arg1," ", self.dict1," ", self.strng' from func1: ", arg1+arg1," ", self.dict1," ", self.strng)
#afterwow
