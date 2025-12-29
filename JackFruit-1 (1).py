import tkinter as tk
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        root.title("Rock Paper Scissors")
        root.geometry("600x700")
        root.config(bg="#1a1a2e")
        
        self.scores = [0, 0]  # [player, computer]
        self.emojis = {'rock': '✊', 'paper': '✋', 'scissors': '✌️'}
        self.animating = False
        
        # Title
        tk.Label(root, text="ROCK PAPER SCISSORS", font=("Arial", 32, "bold"), 
                 fg="#00d9ff", bg="#1a1a2e").pack(pady=20)
        
        # Score
        self.score_label = tk.Label(root, text="YOU 0 - 0 COMPUTER", font=("Arial", 20, "bold"), 
                                    fg="white", bg="#1a1a2e")
        self.score_label.pack(pady=10)
        
        # Hands frame
        hands_frame = tk.Frame(root, bg="#1a1a2e")
        hands_frame.pack(pady=30)
        
        self.player_hand = tk.Label(hands_frame, text="✊", font=("Arial", 100), 
                                    bg="#2d2d5f", fg="white", width=3, height=2)
        self.player_hand.pack(side=tk.LEFT, padx=20)
        
        self.computer_hand = tk.Label(hands_frame, text="✊", font=("Arial", 100), 
                                      bg="#2d2d5f", fg="white", width=3, height=2)
        self.computer_hand.pack(side=tk.LEFT, padx=20)
        
        # Result
        self.result = tk.Label(root, text="", font=("Arial", 28, "bold"), 
                               fg="white", bg="#1a1a2e", height=2)
        self.result.pack(pady=20)
        
        # Buttons
        btn_frame = tk.Frame(root, bg="#1a1a2e")
        btn_frame.pack(pady=20)
        
        for choice, (emoji, color) in [('rock', ('✊', '#e63946')), 
                                       ('paper', ('✋', '#f77f00')), 
                                       ('scissors', ('✌️', '#06a77d'))]:
            btn = tk.Button(btn_frame, text=f"{emoji}\n{choice.upper()}", 
                          font=("Arial", 16, "bold"), bg=color, fg="white", 
                          width=10, height=3, relief=tk.RAISED, bd=5,
                          command=lambda c=choice: self.play(c))
            btn.pack(side=tk.LEFT, padx=10)
            btn.bind("<Enter>", lambda e, b=btn: b.config(relief=tk.SUNKEN, bd=8))
            btn.bind("<Leave>", lambda e, b=btn: b.config(relief=tk.RAISED, bd=5))
        
        # Reset
        tk.Button(root, text="🔄 RESET", font=("Arial", 14, "bold"), 
                 bg="#6c757d", fg="white", command=self.reset).pack(pady=15)
    
    def play(self, choice):
        if self.animating: return
        self.animating = True
        self.result.config(text="")
        self.shake(0, choice)
    
    def shake(self, count, choice):
        if count < 6:
            emoji = ['✊', '✋'][count % 2]
            self.player_hand.config(text=emoji)
            self.computer_hand.config(text=emoji)
            self.root.after(250, lambda: self.shake(count + 1, choice))
        else:
            comp = random.choice(list(self.emojis.keys()))
            self.player_hand.config(text=self.emojis[choice])
            self.computer_hand.config(text=self.emojis[comp])
            self.root.after(400, lambda: self.show_result(choice, comp))
    
    def show_result(self, p, c):
        wins = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
        if p == c:
            self.result.config(text="🤝 TIE!", fg="#fbbf24")
        elif wins[p] == c:
            self.result.config(text="🎉 YOU WIN!", fg="#4ade80")
            self.scores[0] += 1
            self.pulse_label(self.score_label, 3)
        else:
            self.result.config(text="💻 COMPUTER WINS!", fg="#f87171")
            self.scores[1] += 1
            self.pulse_label(self.score_label, 3)
        self.score_label.config(text=f"YOU {self.scores[0]} - {self.scores[1]} COMPUTER")
        self.animating = False
    
    def pulse_label(self, label, count):
        if count > 0:
            font = ("Arial", 24 if count % 2 else 20, "bold")
            label.config(font=font)
            self.root.after(100, lambda: self.pulse_label(label, count - 1))
    
    def reset(self):
        self.scores = [0, 0]
        self.score_label.config(text="YOU 0 - 0 COMPUTER")
        self.player_hand.config(text="✊")
        self.computer_hand.config(text="✊")
        self.result.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    RPSGame(root)
    root.mainloop()