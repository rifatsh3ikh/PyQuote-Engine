import customtkinter as ctk
import requests
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class QuoteApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.iconbitmap("logo.ico")
        self.title("Make a Comeback! Quote Generator")
        self.geometry("1120x680")

        self.quote_label = ctk.CTkLabel(
            self,
            text="Click to get a motivational Quote!",
            wraplength=800,
            font=("Helvetica", 18, "italic")
        )
        self.quote_label.pack(pady=100)

        self.author_label = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 14, "bold")
        )
        self.author_label.pack(pady=5)

        self.button = ctk.CTkButton(
            self,
            text="Generate New Quote",
            command=self.show_quote   
        )
        self.button.pack(pady=50)

    def show_quote(self):
        try:
            response = requests.get(
                "https://zenquotes.io/api/random",
                timeout=5
            )
            data = response.json()

            if isinstance(data, dict) and "too many requests" in data.get("message", "").lower():
                raise Exception("Rate limited")

            self.quote_label.configure(text=f'"{data[0]["q"]}"')
            self.author_label.configure(text=f'— {data[0]["a"]}')

        except Exception:
            offline_quotes = [
    ("Stay hungry, stay foolish.", "Steve Jobs"),
    ("Security is a process, not a product.", "Bruce Schneier"),
    ("First solve the problem, then write the code.", "John Johnson"),
    ("Code is like humor. When you have to explain it, it’s bad.", "Cory House"),
    ("Simplicity is the soul of efficiency.", "Austin Freeman"),
    ("Discipline beats motivation.", "Unknown"),
    ("Slow progress is better than no progress.", "System"),
    ("Dreams don’t work unless you do.", "Unknown"),
    ("Consistency is what transforms average into excellence.", "Unknown"),
    ("Great things never come from comfort zones.", "Unknown"),
    ("Push yourself, because no one else is going to do it for you.", "Unknown"),
    ("Learning never exhausts the mind.", "Leonardo da Vinci"),
    ("Success is the sum of small efforts repeated daily.", "Robert Collier"),
    ("Do not fear failure. Fear being in the same place next year.", "Unknown"),
    ("Programs must be written for people to read.", "Harold Abelson"),
    ("Experience is the name everyone gives to their mistakes.", "Oscar Wilde"),
    ("Make it work, make it right, make it fast.", "Kent Beck"),
    ("Your limitation—it’s only your imagination.", "Unknown"),
    ("Hard work beats talent when talent doesn’t work hard.", "Tim Notke"),
    ("The best way to predict the future is to create it.", "Peter Drucker"),
]

            quote, author = random.choice(offline_quotes)
            self.quote_label.configure(text=f'"{quote}"')
            self.author_label.configure(text=f"— {author}")


if __name__ == "__main__":
    app = QuoteApp()
    app.mainloop()
