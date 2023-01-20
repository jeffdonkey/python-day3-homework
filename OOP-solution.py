class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  
  def repair(self):
    self.condition = "repaired"
    

class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  
  def boost(self):
    self.max_speed *= 2
    

class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  
  def flame_jet(self,other):
    other.condition = "trashed"

'''
Make sure to answer the following prompts about your coding experience:

How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
  # ENCAPSULATION: no.
  # ABSTRACTION: no.
  # INHERITANCE: yes. Three of the classes are "children" to "class Podracer".  The "child" classes inherit from it's parent.
  # POLYMORPHISM yes.  "condition" is set to 'repaired' on line 9 of "class Podracer".  "class SebuldasPod" changes the condition
    received from "class Podracer" to 'trashed'.

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
  # Maybe.  I do not know enough to know.

How in particular did Object Oriented Programming assist in the solving of this problem?
  # Not sure. The problem is stated: "Watto needs a new system for organizing his inventory of podracers".  The classes above
    do not seem to collect any identifier value for a specific podracer.  This program does something but I fail to see how it
    relates to organizing inventory.
'''

