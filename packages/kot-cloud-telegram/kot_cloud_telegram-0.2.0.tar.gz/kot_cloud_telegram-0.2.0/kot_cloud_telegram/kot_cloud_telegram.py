#!/usr/bin/python3
# -*- coding: utf-8 -*-

from kot import KOT, KOT_Remote, HASHES, requires, no_exception
from kot_update import KOT_Update
import copy

telegram_controller = None

@requires("pyTelegramBotAPI", custom_import="telebot")
def initalize(token):
            import telebot
            if telegram_controller.get("bot") is None:
                telegram_controller.set("bot", telebot.TeleBot(token))
            if telegram_controller.get("commands") is None:
                telegram_controller.set("commands", {})

@requires("pyTelegramBotAPI", custom_import="telebot")
def send_message(chat_id, message):
    import telebot
    telegram_controller.get("bot").send_message(chat_id, message)


def register_command(command, func, description="COMMAND"):
    command = "/"+command
    currently_list = telegram_controller.get("commands")
    currently_list[command] = [func, description]

    from telebot import apihelper, util, types

    list_of_commands = []

    for command in currently_list:
        list_of_commands.append(types.BotCommand(command, currently_list[command][1]))

    telegram_controller.get("bot").set_my_commands(list_of_commands)

    telegram_controller.set("commands", currently_list)


def chatid(arguments, message):
    telegram_controller.get("bot").reply_to(message,str(message.chat.id))


def clear_commands():
    from telebot import apihelper, util, types
    telegram_controller.set("commands", {})

    telegram_controller.get("bot").delete_my_commands()


    


@no_exception
def process(update):
    commands = telegram_controller.get("commands")
    text = update.message.text
    for command in commands:
        if text.split(" ")[0] == command:

            result = ""
            for i in text.split(" ")[1:]:
                result = result + i
                if not text.split(" ")[1:][-1] == i:
                    result = result + " "
            commands[command][0](result, update.message)



@requires("pyTelegramBotAPI", custom_import="telebot")
def run():
    import telebot
    import time
    bot = telegram_controller.get("bot")
    offset = telegram_controller.get("offset")
    while True:
        messages = bot.get_updates(offset)
        for message in messages:
            if not message.update_id == offset:

                telegram_controller.get("process")(message)


                if messages[-1] == message:
                    telegram_controller.set("offset", message.update_id)
                    offset = message.update_id

        time.sleep(1)
    



@requires("pyTelegramBotAPI", custom_import="telebot")
def reply_to(message, reply):
    telegram_controller.get("bot").reply_to(message, reply)
    

class KOT_Cloud_Telegram:
    def __init__(self, encryption_key, cloud) -> None:
        
        self.connection = cloud
        self.connection.force_encrypt = encryption_key
        global telegram_controller
        telegram_controller = self.connection

    def run(self,):
        
        self.connection.get("run")()

    def register_command(self, command, func, description):
        self.connection.get("register_command")(command, func, description)
    def clear_commands(self,):
        self.connection.get("clear_commands")()
    def reply_to(self, message, reply):
        self.connection.get("reply_to")(message, reply)

    def send_message(self, chat_id, message):
        self.connection.get("send_message")(chat_id, message)

    def deploy(self, token):
        backup = copy.copy(self.connection.force_encrypt)
        updates = KOT_Update(self.connection)

        updates.pre_update("initalize") 
        updates.pre_update("register_command") 
        updates.pre_update("process")
        updates.pre_update("run") 
        updates.pre_update("clear_commands") 
        updates.pre_update("reply_to") 
        updates.pre_update("send_message") 

        self.connection.active(initalize)
        self.connection.active(process)
        self.connection.active(register_command)
        self.connection.active(run)

        self.connection.active(clear_commands)

        self.connection.active(reply_to)
        self.connection.active(send_message)




        updates.update() # Start to Update    
        self.connection.force_encrypt = backup    

        self.connection.get("initalize")(token)
        self.register_command("chatid", chatid, description="Returns Chat ID")



