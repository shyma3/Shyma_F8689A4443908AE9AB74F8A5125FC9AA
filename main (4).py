class player:
 def __init__(self):
  def play(self):
    print("The player is playing cricket.")
class batsman(player):
  def play(self):
    print("The batsman is batting")
class bowler(player):
  def play(self):
    print("The bowler is bowling")
b1=batsman()
b2=batsman()
b1.play()
b2.play()