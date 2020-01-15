#---------------------------
#   Import Libraries
#---------------------------
import codecs
import json
import os
import re
import sys

#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "Webhook Discord Message"
Website = "https://www.twitch.tv/EncryptedThoughts"
Description = "Example of how to post your messages to discord using webhooks and not relying on the default slcb messaging method."
Creator = "EncryptedThoughts"
Version = "1.0.0.0"

#---------------------------
#   Define Global Variables
#---------------------------
SettingsFile = os.path.join(os.path.dirname(__file__), "settings.json")
ReadMe = os.path.join(os.path.dirname(__file__), "README.txt")

#---------------------------------------
# Classes
#---------------------------------------
class Settings(object):
    def __init__(self, SettingsFile=None):
        if SettingsFile and os.path.isfile(SettingsFile):
            with codecs.open(SettingsFile, encoding="utf-8-sig", mode="r") as f:
                self.__dict__ = json.load(f, encoding="utf-8")
        else:
            self.EnableDebug = True
            self.CommandName = "!webhookdiscord"
            self.WebhookUrl = "https://discordapp.com/api/webhooks/YOURWEBHOOK"
            self.PostFormat = "{\"username\":\"EncryptedThoughts\",\"avatar_url\":\"https://imgur.com/a/JV04tSO\",\"content\":\"Text message. Up to 2000 characters.\",\"embeds\":[{\"author\":{\"name\":\"Encrypted\",\"url\":\"https://www.reddit.com/r/cats/\",\"icon_url\":\"https://i.imgur.com/R66g1Pe.jpg\"},\"title\":\"Title\",\"url\":\"https://google.com/\",\"description\":\"Text message. You can use Markdown here. *Italic* **bold** __underline__ ~~strikeout~~ [hyperlink](https://google.com) `code`\",\"color\":15258703,\"fields\":[{\"name\":\"Text\",\"value\":\"More text\",\"inline\":true},{\"name\":\"Even more text\",\"value\":\"Yup\",\"inline\":true},{\"name\":\"Use `\\\"inline\\\": true` parameter, if you want to display fields in the same line.\",\"value\":\"okay...\"},{\"name\":\"Thanks!\",\"value\":\"You're welcome :wink:\"}],\"thumbnail\":{\"url\":\"https://upload.wikimedia.org/wikipedia/commons/3/38/4-Nature-Wallpapers-2014-1_ukaavUI.jpg\"},\"image\":{\"url\":\"https://upload.wikimedia.org/wikipedia/commons/5/5a/A_picture_from_China_every_day_108.jpg\"},\"footer\":{\"text\":\"Woah! So cool! :smirk:\",\"icon_url\":\"https://i.imgur.com/fKL31aD.jpg\"}}]}"
            Parent.Log(ScriptName, "Failed to read setting from file")

    def Reload(self, jsondata):
        self.__dict__ = json.loads(jsondata, encoding="utf-8")
        return

    def Save(self, SettingsFile):
        try:
            with codecs.open(SettingsFile, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.__dict__, f, encoding="utf-8")
            with codecs.open(SettingsFile.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
                f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8')))
        except:
            Parent.Log(ScriptName, "Failed to save settings to file.")
        return

#---------------------------------------
# Settings functions
#---------------------------------------

def ReloadSettings(jsondata):
    ScriptSettings.Reload(jsondata)

def SaveSettings(self, SettingsFile):
    with codecs.open(SettingsFile, encoding='utf-8-sig', mode='w+') as f:
        json.dump(self.__dict__, f, encoding='utf-8-sig')
    with codecs.open(SettingsFile.replace("json", "js"), encoding='utf-8-sig', mode='w+') as f:
        f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8-sig')))
    return

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():
    global ScriptSettings
    ScriptSettings = Settings(SettingsFile)
    ScriptSettings.Save(SettingsFile)
    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):

    if data.IsChatMessage() and data.GetParam(0).lower() == ScriptSettings.CommandName:
        send_message("Test message sent from Streamlabs Chatbot.")

    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return

#---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters) 
#---------------------------
def Parse(parseString, userid, username, targetid, targetname, message):
    return parseString
#---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
#---------------------------
def ReloadSettings(jsonData):
    # Execute json reloading here
    ScriptSettings.__dict__ = json.loads(jsonData)
    ScriptSettings.Save(SettingsFile)
    return

#---------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
#---------------------------
def Unload():
    return

#---------------------------
#   [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
#---------------------------
def ScriptToggled(state):
    return

# Explanation on how to obtain a webhook - https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks
# Webhook json formatting example - https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html
def send_message(message): 

    headers = {
      'Content-Type': 'application/json'
    }

    result = Parent.PostRequest(ScriptSettings.WebhookUrl,headers,json.loads(ScriptSettings.PostFormat), True)
  
    if ScriptSettings.EnableDebug:
        Parent.Log(ScriptName, result)

    return result

def openreadme():
    os.startfile(ReadMe)

def openjson():
    os.startfile("https://codebeautify.org/jsonviewer?input=" + ScriptSettings.PostFormat)