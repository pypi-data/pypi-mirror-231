#!/usr/bin/python3
# -*- coding: utf-8 -*-

from kot import KOT, KOT_Remote, HASHES, requires, no_exception
from kot_update import KOT_Update
import copy
import traceback

telegram_controller = None
telegram = None

@requires("pyTelegramBotAPI", custom_import="telebot")
def initalize(token):

    from kot_update import KOT_Update
    update = KOT_Update(telegram_controller)    
    update.pre_update("bot")
    update.pre_update("commands")
    update.pre_update("restrict")
    update.pre_update("restrict_status")
    update.pre_update("allowed_users_list")

    import telebot
    if telegram_controller.get("bot") is None:
        telegram_controller.set("bot", telebot.TeleBot(token))
    if telegram_controller.get("commands") is None:
        telegram_controller.set("commands", {})

    if telegram_controller.get("restrict") is None:
        telegram_controller.set("restrict_status", False)
        telegram_controller.set("allowed_users_list", [])

    update.update(just_important=True)


def restrict(value):
    from kot_update import KOT_Update
    update = KOT_Update(telegram_controller)    
    update.pre_update("restrict_status")
    telegram_controller.set("restrict_status", value)
    update.update(just_important=True)
    

def allowed_users(the_list):
    from kot_update import KOT_Update
    update = KOT_Update(telegram_controller)    
    update.pre_update("allowed_users_list")
    telegram_controller.set("allowed_users_list", the_list)
    update.update(just_important=True)    
    


@requires("pyTelegramBotAPI", custom_import="telebot")
def send_message(chat_id, message):
    import telebot
    telegram_controller.get("bot").send_message(chat_id, message)


def commands_set(commands):
    from kot_update import KOT_Update
    update = KOT_Update(telegram_controller)    
    update.pre_update("commands")
    telegram_controller.set("commands", commands)
    update.update(just_important=True)



def register_command(command, func, description="COMMAND"):
    command = "/"+command
    currently_list = telegram_controller.get("commands")
    currently_list[command] = [func, description]

    from telebot import apihelper, util, types

    list_of_commands = []

    for command in currently_list:
        list_of_commands.append(types.BotCommand(command, currently_list[command][1]))

    telegram_controller.get("bot").set_my_commands(list_of_commands)

    telegram_controller.get("commands_set")(currently_list)


def delete_command(command):
    command = "/"+command
    currently_list = telegram_controller.get("commands")
    currently_list.pop(command)

    from telebot import apihelper, util, types

    list_of_commands = []

    for command in currently_list:
        list_of_commands.append(types.BotCommand(command, currently_list[command][1]))

    telegram_controller.get("bot").set_my_commands(list_of_commands)

    telegram_controller.get("commands_set")(currently_list)


def chat_id(arguments, message):
    telegram_controller.get("bot").reply_to(message,str(message.chat.id))
def user_id(arguments, message):
    telegram_controller.get("bot").reply_to(message,str(message.from_user.id))

def clear_commands():
    from telebot import apihelper, util, types
    telegram_controller.get("commands_set")({})

    telegram_controller.get("bot").delete_my_commands()


    


@no_exception
def process(update):
    commands = telegram_controller.get("commands")
    text = update.message.text
    for command in commands:
        if text.split(" ")[0] == command:

            commands[command][0](text.split(" ")[1:], update.message)



@requires("pyTelegramBotAPI", custom_import="telebot")
def run():
    import telebot
    import time
    bot = telegram_controller.get("bot")
    offset = telegram_controller.get("offset")
    while True:
        try:
            messages = bot.get_updates(offset)
            for message in messages:

                if not message.update_id == offset:

                    if messages[-1] == message:
                        telegram_controller.set("offset", message.update_id)
                        offset = message.update_id

                    if telegram_controller.get("restrict_status"):
                        if not message.message.from_user.id in telegram_controller.get("allowed_users_list"):
                            telegram.reply_to(message.message,"Not allowed")
                            continue
                    telegram_controller.get("process")(message)



        except:
            traceback.print_exc()
        time.sleep(1)
    



@requires("pyTelegramBotAPI", custom_import="telebot")
def reply_to(message, reply):
    telegram_controller.get("bot").reply_to(message, reply)
    

class KOT_Cloud_Telegram:
    def __init__(self, encryption_key, cloud) -> None:
        
        self.connection = cloud
        self.connection.force_encrypt = encryption_key
        global telegram_controller
        global telegram
        telegram_controller = self.connection
        telegram = self

    def command(self, value=None, description="COMMAND"):
        def decorate(value):
            key = value.__name__
            self.register_command(key,value,description)

        if value == None:
            return decorate
        else:
            decorate(value)
            return value


    def restrict(self, value):
        self.connection.get("restrict")(value)

    def allowed_users(self, the_list):
        self.connection.get("allowed_users")(the_list)

    def register_command(self, command, func, description):
        self.connection.get("register_command")(command, func, description)
    def delete_command(self, command):
        self.connection.get("delete_command")(command)        
    def clear_commands(self,):
        self.connection.get("clear_commands")()
    def reply_to(self, message, reply):
        self.connection.get("reply_to")(message, reply)

    def send_message(self, chat_id, message):
        self.connection.get("send_message")(chat_id, message)




    def deploy(self, token):
        updates = KOT_Update(self.connection)

        updates.pre_update("initalize") 
        updates.pre_update("register_command") 
        updates.pre_update("delete_command") 
        updates.pre_update("process")
        updates.pre_update("run") 
        updates.pre_update("clear_commands") 
        updates.pre_update("reply_to") 
        updates.pre_update("send_message") 
        updates.pre_update("commands_set")
        updates.pre_update("restrict")
        updates.pre_update("allowed_users")

        self.connection.active(restrict)
        self.connection.active(allowed_users)


        self.connection.active(initalize)
        self.connection.active(process)
        self.connection.active(register_command)
        self.connection.active(delete_command)
        self.connection.active(run)

        self.connection.active(clear_commands)

        self.connection.active(reply_to)
        self.connection.active(send_message)
        
        self.connection.active(commands_set)




        updates.update() # Start to Update    


        self.connection.get("initalize")(token)
        self.command(chat_id, "Returns Chat ID")
        self.command(user_id, "Returns User ID")

    def run(self,):
        
        self.connection.get("run")()

