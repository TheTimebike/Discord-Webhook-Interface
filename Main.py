import discord, aiohttp, asyncio
from modules.client import Client
from modules.webhookhandler import WebhookHandler
from tkinter import *
from PIL import ImageTk, Image

url = ""
client = Client()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Webhook Studio")
    
        self.url_entry_box = Text(self.master, width=40, height=4)
        self.url_entry_box.place(x=50, y=35)
        self.url_label = Label(self.master, text="Webhook Url")
        self.url_label.place(x=375, y=54)

        self.delete_button = Button(self.master, text="Delete", width=42, height=5, command= lambda: client.delete(self.url_entry_box.get('1.0', END)))
        self.delete_button.place(x=750, y=200)

        self.edit_button = Button(self.master, text="Edit", width=42, height=5, command= lambda: client.edit(self.url_entry_box.get('1.0', END)))
        self.edit_button.place(x=750, y=300)

        self.send_button = Button(self.master, text="Send", width=42, height=5, command= lambda: client.run_event("_send_event"))
        self.send_button.place(x=750, y=400)

        self.message_entry_box = Text(self.master, width=80, height=5)
        self.message_entry_box.place(x=50, y=400)

        self.pfp_preview = ImageTk.PhotoImage(Image.open("./TestImage.png").resize((190, 190), Image.ANTIALIAS))
        self.pfp_preview_pannel = Label(self.master, image=self.pfp_preview)
        self.pfp_preview_pannel.image = self.pfp_preview
        self.pfp_preview_pannel.place(x=860, y=4)

        self.pfp_preview_label = Label(self.master, text="Pfp Preview")
        self.pfp_preview_label.place(x=750, y=150)

        self.pfp_change_button = Button(self.master, text="Change", width=14)
        self.pfp_change_button.place(x=750, y=170)

@client.send_event
async def send():
    url = apps.url_entry_box.get('1.0', END)
    message = apps.message_entry_box.get('1.0', END)
    username = "Test"
    await client.send(url, message, username)

if __name__ == "__main__":
    root = Tk()
    root.geometry("1100x530")
    apps = Window(root)
    #root.iconbitmap("./vms.ico") # iconbitmap function requires full path rather than ./, and os.getcwd() doesnt work either
    root.mainloop()