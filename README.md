# Discord-Webhook-Interface

Discord-Webhook-Interface is a GUI based program that allows users to take advantage of webhooks outside of a commandline format. This allows users who are not experienced in code to use the benefits that webhooks have, namely ease of use and formatting syntax. 

The interface for DWI was created in the Python module tkinter. It also utilizes several other modules such as discord.py, pillow and aiohttp.

## What Is A Webhook?

A webhook is a type of bot that only has access to sending messages and files within one channel of a server. Using webhooks are useful as they allow you to make use of formatting syntax that is disabled for bots and users. 

One advantage of using a webhook is that it is a lot easier to change the name and profile picture of the webhook on the fly. This allows the webhook to take on the appearence of a new bot each message.

Webhooks are arguably more secure than traditional bots, too, as they only let the user of the webhook send messages. They can't even recieve them!

## How Do I Connect?

To connect to a webhook through DWI you will need to locate the webhook url inside the webhook section of your server. As mentioned earlier, this webhook can *only* send messages, so it is safe to put into DWI. It is *not* recommended, however, to share the webhook online, as this can let anyone send messaged through your webhook.

After you have located the webhook url, input it into the "Webhook Url" section of the DWI window. When sending a message, a connection will be made to the webhook and maintained until the program is closed or another webhook is selected.

## What Can I Do While Connected?

To get the obvious out of the way, you will be able to send messages when connected. You will also be able to delete the webhook using the "Delete" button on the right-hand side. This does not ask for confirmation, and will immediately delete the webhook. This action cannot be undone.

The profile picture of the webhook can also be changed while you are connected. The preview on the right-hand side does not update until you give it a new profile picture, as the Discord API will not serve me the avatars of webhooks for some reason. *shrug*

## Do Changes I Make To The Webhook Show Up On The Audit Log?

Changes that you make to the webhook, such as profile picture and name, do not show up on the audit log. This is because, from Discords point-of-view, you are connected through the webhook and the webhook is making changes towards itself. When you connect through DWI, there is no trace back to your personal Discord account.

## Does This Mean I'm Annonymous?

In a sense, yes. While Discord staff would still be able to compare the ip addresses of the request and trace it back to you, the average user would not be able to tell that it was you who connected through the webhook.

## Does This Mean I Can Prank Without Being Caught?

Yes it does. Remember that webhooks can *only* send messages, meaning that your pranking opportunities are limited somewhat.

## So What Are My Pranking Opportunities?

As I stated earlier, webhooks have access to certain formatting syntax that bots and other users do not. One example of this would be link formatting. While bots *can* use link formatting, it can only be inside embeds. Webhooks can use this syntax in regular messages.

To use link formatting, you would type ``[Link Text](Link)``. If you are redirected to something that would auto-embed its content, remember to cancel the embed with ``< >``
