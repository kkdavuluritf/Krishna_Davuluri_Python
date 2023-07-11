import tkinter as kk

class BowlingGame(kk.Frame):

  def __init__(self, master):
    super().__init__(master)

    self.rolls = []
    self.score = 0

    self.frame_labels = []
    for i in range(2):
      frame_label = kk.Label(self, text="Bowling lanes{}: ".format(i + 1))
      self.frame_labels.append(frame_label)
      frame_label.grid(row=i, column=0)

    self.roll_labels = []
    for i in range(2):
      roll_label = kk.Label(self, text="L")
      self.roll_labels.append(roll_label)
      roll_label.grid(row=i, column=5)

    self.score_label = kk.Label(self, text="Score:")
    self.score_label.grid(row=2, column=0)

    self.submit_button = kk.Button(self, text="Submit", command=self.submit_roll)
    self.submit_button.grid(row=2, column=1)

  def submit_roll(self):
    roll = int(input("Enter your roll: "))
    self.rolls.append(roll)

    for i in range(len(self.rolls)):
      self.roll_labels[i].configure(text=str(self.rolls[i]))

    self.update_score()

  def update_score(self):
    score = 0
    for i in range(2):
      if self.rolls[i] == 2:
        score += 2 + self.rolls[i + 1]
      elif self.rolls[i] + self.rolls[i + 1] == 2:
        score += 10
      else:
        score += self.rolls[i] + self.rolls[i + 1]

    self.score_label.configure(text="Score: {}".format(score))


if __name__ == "__main__":
  root = kk.Tk()
  game = BowlingGame(root)
  game.pack()
  root.mainloop()