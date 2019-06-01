import discord, aiohttp, asyncio
from modules.client import Client
from modules.webhookhandler import WebhookHandler
from tkinter import *

url = ""
client = Client()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Webhook Studio")
    
        self.url_entry_Box = Text(self.master, width=40, height=4)
        self.url_entry_Box.place(x=50, y=35)
        self.url_label = Label(self.master, text="Webhook Url")
        self.url_label.place(x=900, y=34)

        self.button = Button(self.master, text="Send!", width=42, height=5, command= lambda: client.run_event("_send_event"))
        self.button.place(x=750, y=400)

@client.send_event
async def send():
    await client.send(url, "Hello World!", "TestingWebhook")

if __name__ == "__main__":
    root = Tk()
    root.geometry("1100x530")
    apps = Window(root)
    #root.iconbitmap("./vms.ico") # iconbitmap function requires full path rather than ./, and os.getcwd() doesnt work either
    root.mainloop()
    client.run()