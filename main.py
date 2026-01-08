import customtkinter as ctk
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class QuoteApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap("logo.ico") 
        self.geometry("500x400")
        self.title("Make a Comeback! Quote Generator")
        self.geometry("1120x680")
        
        # UI
        self.quote_label = ctk.CTkLabel(self, text="Click to get a motivational Quote!", 
                                        wraplength=800, font=("Helvetica", 18, "italic"))
        self.quote_label.pack(pady=100)

        self.author_label = ctk.CTkLabel(self, text="", font=("Helvetica", 14, "bold"))
        self.author_label.pack(pady=5)

        self.button = ctk.CTkButton(self, text="Generate New Quote", command=self.show_quote)
        self.button.pack(pady=50)


    def show_quote(self):
        try:
            response = requests.get("https://api.quotable.io/random", verify=False)
            data = response.json()
            self.quote_label.configure(text=f'"{data["content"]}"')
            self.author_label.configure(text=f"- {data['author']}")
            
        except Exception as e:
            self.quote_label.configure(text="Oops! Could not connect to the quote server.")
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QuoteApp()
    app.mainloop()