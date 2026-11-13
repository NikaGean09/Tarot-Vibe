import random
import tkinter as tk
from tkinter import ttk


CARDS = [
	("The Fool", "Beginnings", "A fresh start is calling. Stay curious and take a thoughtful first step."),
	("The Magician", "Resourcefulness", "You have useful tools at hand. Focus your energy and make something happen."),
	("The High Priestess", "Intuition", "Pause and listen to your inner voice; not every answer needs to be rushed."),
	("The Empress", "Nurture", "Give care to an idea, relationship, or part of yourself that needs room to grow."),
	("The Emperor", "Structure", "Clear boundaries and a practical plan can make your next move easier."),
	("The Hierophant", "Tradition", "A trusted teacher, shared value, or familiar practice may offer perspective."),
	("The Lovers", "Connection", "Consider what aligns with your values and where honest communication matters."),
	("The Chariot", "Momentum", "Choose a direction and guide competing demands with steady determination."),
	("Strength", "Courage", "Gentleness and patience can be more powerful than force right now."),
	("The Hermit", "Reflection", "Make space for quiet thought. A little distance may help you see clearly."),
	("Wheel of Fortune", "Change", "Circumstances shift. Stay adaptable and notice the opening in front of you."),
	("Justice", "Clarity", "Look at the facts, own your choices, and aim for a fair outcome."),
	("The Hanged One", "New perspective", "A pause is not wasted time. Try looking at the situation from another angle."),
	("Death", "Transition", "An ending can clear space for change. Let go of what has run its course."),
	("Temperance", "Balance", "Blend patience with action and seek a sustainable middle path."),
	("The Devil", "Attachments", "Notice habits or expectations that feel limiting; awareness creates options."),
	("The Tower", "Revelation", "A sudden change may expose what needs attention. Rebuild on what is true."),
	("The Star", "Hope", "Recover your sense of possibility and take one calm step toward renewal."),
	("The Moon", "Uncertainty", "Some details may be unclear. Move gently and separate evidence from worry."),
	("The Sun", "Joy", "Celebrate progress and let warmth, confidence, and openness guide you."),
	("Judgement", "Renewal", "Review what you have learned and answer the opportunity to begin again."),
	("The World", "Completion", "Recognize how far you have come and consider what you are ready to carry forward."),
]

POSITIONS = (
	("PAST", "What shaped this moment"),
	("PRESENT", "What deserves your attention"),
	("NEXT STEP", "A direction to consider"),
)

BG = "#11121b"
PANEL = "#1b1d2b"
GOLD = "#e8c879"
TEXT = "#f4f0e7"
MUTED = "#aaa8b5"


class TarotGame:
	def __init__(self, root):
		self.root = root
		root.title("The Little Tarot — a three-card reading")
		root.geometry("920x690")
		root.minsize(720, 600)
		root.configure(bg=BG)

		style = ttk.Style()
		style.theme_use("clam")
		style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=(18, 11))

		outer = tk.Frame(root, bg=BG, padx=34, pady=26)
		outer.pack(fill="both", expand=True)
		tk.Label(outer, text="✦  THE LITTLE TAROT  ✦", bg=BG, fg=GOLD,
				 font=("Georgia", 12, "bold")).pack(pady=(0, 9))
		tk.Label(outer, text="A moment to reflect", bg=BG, fg=TEXT,
				 font=("Georgia", 29, "bold")).pack()
		tk.Label(outer, text="Hold a question in mind, then draw three cards.", bg=BG,
				 fg=MUTED, font=("Segoe UI", 11)).pack(pady=(8, 20))

		self.cards_frame = tk.Frame(outer, bg=BG)
		self.cards_frame.pack(fill="both", expand=True)
		self.card_widgets = []
		for i, (position, subtitle) in enumerate(POSITIONS):
			panel = tk.Frame(self.cards_frame, bg=PANEL, highlightthickness=1,
							 highlightbackground="#343548", padx=16, pady=16)
			panel.grid(row=0, column=i, sticky="nsew", padx=8, pady=4)
			self.cards_frame.grid_columnconfigure(i, weight=1, uniform="card")
			tk.Label(panel, text=position, bg=PANEL, fg=GOLD,
					 font=("Segoe UI", 9, "bold")).pack()
			tk.Label(panel, text=subtitle, bg=PANEL, fg=MUTED,
					 font=("Segoe UI", 9), wraplength=220).pack(pady=(3, 10))
			art = tk.Canvas(panel, width=112, height=154, bg="#25263a",
							highlightthickness=1, highlightbackground=GOLD)
			art.pack(pady=(2, 12))
			self._draw_back(art)
			name = tk.Label(panel, text="—", bg=PANEL, fg=TEXT,
							font=("Georgia", 15, "bold"), wraplength=210)
			name.pack(pady=(0, 4))
			direction = tk.Label(panel, text="", bg=PANEL, fg=GOLD,
								 font=("Segoe UI", 9, "bold"))
			direction.pack()
			meaning = tk.Label(panel, text="Your card is waiting.", bg=PANEL, fg=MUTED,
							   font=("Segoe UI", 10), wraplength=220, justify="center")
			meaning.pack(pady=(9, 0), fill="x", expand=True)
			self.card_widgets.append((art, name, direction, meaning))

		self.status = tk.Label(outer, text="For fun and reflection—not a prediction.",
							   bg=BG, fg=MUTED, font=("Segoe UI", 9))
		self.status.pack(pady=(10, 8))
		buttons = tk.Frame(outer, bg=BG)
		buttons.pack()
		ttk.Button(buttons, text="Draw your cards", command=self.draw).pack(side="left", padx=6)
		ttk.Button(buttons, text="Start over", command=self.reset).pack(side="left", padx=6)

	@staticmethod
	def _draw_back(canvas):
		canvas.create_rectangle(8, 8, 104, 146, outline=GOLD, width=1)
		canvas.create_oval(31, 47, 81, 97, outline=GOLD, width=2)
		canvas.create_text(56, 72, text="✦", fill=GOLD, font=("Georgia", 28))
		canvas.create_text(56, 120, text="✧  ✧  ✧", fill=GOLD, font=("Georgia", 12))

	def draw(self):
		for (art, name, direction, meaning), card in zip(self.card_widgets, random.sample(CARDS, 3)):
			title, keyword, message = card
			reversed_card = random.choice((False, True))
			art.delete("all")
			art.configure(bg="#28283a" if not reversed_card else "#222335")
			art.create_rectangle(8, 8, 104, 146, outline=GOLD, width=1)
			art.create_text(56, 52, text="✦", fill=GOLD, font=("Georgia", 34))
			art.create_text(56, 94, text=title, fill=TEXT,
							font=("Georgia", 9, "bold"), width=82)
			art.create_text(56, 126, text="✧", fill=GOLD, font=("Georgia", 16))
			if reversed_card:
				art.create_text(56, 20, text="↻", fill=GOLD, font=("Segoe UI", 11))
				message = "Turn inward and take this theme gently: " + message[0].lower() + message[1:]
			name.configure(text=title)
			direction.configure(text=f"{keyword}  ·  {'REVERSED' if reversed_card else 'UPRIGHT'}")
			meaning.configure(text=message)
		self.status.configure(text="A reading for reflection. Keep what resonates; leave the rest.")

	def reset(self):
		for art, name, direction, meaning in self.card_widgets:
			art.delete("all")
			art.configure(bg="#25263a")
			self._draw_back(art)
			name.configure(text="—")
			direction.configure(text="")
			meaning.configure(text="Your card is waiting.")
		self.status.configure(text="For fun and reflection—not a prediction.")


if __name__ == "__main__":
	window = tk.Tk()
	TarotGame(window)
	window.mainloop()
