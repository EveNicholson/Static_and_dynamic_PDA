### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:

  from src.card import Card
  
  

  def check_for_ace(self, card):
    value = 1
    if card.value == value:
      return True
    else:
      return False
   

  def highest_card(self, card1, card2):
    if card1.value > card2.value:
        return card1
    else:
        return card2
  


def value_total(self, value):
  total=0
  for card in card:
    total = total+ card.value
    return (f"You have a total of" + total)
  


    
