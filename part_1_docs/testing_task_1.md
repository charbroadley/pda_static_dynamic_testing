### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
# 2nd line: '=' is an assignment operator (should be '==' to mean 'equal to')
# 4th line: else needs a ':' after
   

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
# 1st line: spelling mistake - 'dif' should be 'def', missed comma after 'card1' 
# 2nd line: should be indented so it's within the function (and then all subsequent lines indented appropriately)
# 3rd line: 'card' is not defined (should be 'card1')


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
  return "You have a total of" + total
# 1st line: should be indented so it's within the class (and then all subsequent lines indented appropriately)
# 2nd line: 'total' has no value assigned to it
# 5th line: return should be an f string (f"You have a total of {total}"), should be indented equally to 'for' line (so the loop doesn't stop after only going over the first item in the cards list)
  
```
