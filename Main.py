import discord, aiohttp, asyncio
from modules.client import Client
from modules.webhookhandler import WebhookHandler
from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO

client = Client()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Webhook Studio")
    
        self.url_entry_box = Text(self.master, width=40, height=4)
        self.url_entry_box.place(x=50, y=35)
        self.url_label = Label(self.master, text="Webhook Url")
        self.url_label.place(x=375, y=44)
        self.url_select_button = Button(self.master, text="Select", width=14, command= lambda: self.url_select_update_boxes_command())
        self.url_select_button.place(x=375, y=64)

        self.pfp_entry_box = Text(self.master, width=37, height=5)
        self.pfp_entry_box.place(x=750, y=200)

        self.delete_button = Button(self.master, text="Delete", width=42, height=5, command= lambda: client.delete(self.url_entry_box.get('1.0', END)))
        self.delete_button.place(x=750, y=300)

        self.send_button = Button(self.master, text="Send", width=42, height=5, command= lambda: client.run_event("_send_event"))
        self.send_button.place(x=750, y=400)

        self.message_entry_box = Text(self.master, width=80, height=5)
        self.message_entry_box.place(x=50, y=400)

        self.pfp_preview = self.get_image_from_url("https://cdn.discordapp.com/embed/avatars/0.png")
        self.pfp_preview_pannel = Label(self.master, image=self.pfp_preview)
        self.pfp_preview_pannel.image = self.pfp_preview
        self.pfp_preview_pannel.place(x=860, y=4)

        self.pfp_preview_label = Label(self.master, text="Pfp Preview")
        self.pfp_preview_label.place(x=750, y=150)

        self.pfp_change_button = Button(self.master, text="Change", width=14,  command= lambda: self.change_pfp())
        self.pfp_change_button.place(x=750, y=170)

        self.username_box = Entry(self.master, width=50)
        self.username_box.place(x=50, y=120)
        self.username_label = Label(self.master, text="Webhook Username")
        self.username_label.place(x=350, y=119)

    def change_pfp(self):
        new_img = self.get_image_from_url(self.pfp_entry_box.get('1.0', END))
        self.pfp_preview_pannel.image = new_img
        client.edit(self.url_entry_box.get('1.0', END), requests.get(self.pfp_entry_box.get('1.0', END).replace("\n", "")).content)

    def get_image_from_url(self, url):
        img = BytesIO(requests.get(str(url).replace("\n", "")).content)
        return ImageTk.PhotoImage(Image.open(img).resize((190,190), Image.ANTIALIAS))

    def url_select_update_boxes_command(self):
        url = self.url_entry_box.get('1.0', END)
        _webhook = client.get_info(url)
        new_pfp = str(_webhook.avatar_url)

@client.send_event
async def send():
    url = apps.url_entry_box.get('1.0', END)
    message = apps.message_entry_box.get('1.0', END)
    username = apps.username_box.get()
    await client.send(url, message, username)

if __name__ == "__main__":
    root = Tk()
    root.geometry("1100x530")
    apps = Window(root)
    #root.iconbitmap("./vms.ico") # iconbitmap function requires full path rather than ./, and os.getcwd() doesnt work either
    root.mainloop()