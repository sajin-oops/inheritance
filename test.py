class person:
  def __init__(self,fname,lname):
    self.firstname = fname
    self.lastname = lname
    
  def printname(self):
    print(self.firstname, self.lastname)
    
x = person("Sajin" , "AK")
x.printname()

#O/P - Sajin AK