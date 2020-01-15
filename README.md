# Webhook Discord Message

Mostly an example script for Streamlabs Chatbot testing sending messages to a discord webhook instead of using the built in discord message method included in streamlabs.

## Installing

This script was built for use with Streamlabs Chatbot.
Follow instructions on how to install custom script packs at:
https://github.com/StreamlabsSupport/Streamlabs-Chatbot/wiki/Prepare-&-Import-Scripts

Aside from installing the script pack a webhook to a discord server will also be needed.
This can be created/obtained from going to Server Setting -> Webhooks in Discord.
The link needed should look something like: https://discordapp.com/api/webhooks/YOURWEBHOOK

More info on discord webhooks can be found at: 
https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks

## Use

Once installed a command called !webhookdiscord (or whatever you set it as) can be used in chat.

Using it will post a message in the channel specified by the webhook at creation.

The message can be formated by modifying the Post Format setting json object under "Advanced - Format Options"
More info on options on how the message can be formatted can be found at:
https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html

Example of use:

![example](https://user-images.githubusercontent.com/50642352/72402841-fefc2600-3715-11ea-977b-c32c443dace6.png)

## Author

EncryptedThoughts - [Twitch](https://www.twitch.tv/encryptedthoughts)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
