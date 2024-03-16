"""
GUI
"""

from typing import TypeVar
import tkinter as tk
from tkinter import ttk, Tk
from tkinter import messagebox

import json

from ControllerChat import Controller

# InteractiveMessages = TypeVar("InteractiveMessages")
DefCallbackGui = TypeVar("DefCallbackGui")


class Gui:
    def __init__(
        self,
        root: Tk
    ) -> None:
        self.controller = Controller()

        self.is_register = False
        self.root = root

        self.root.title("PyChatGui")
        self.root.geometry("600x600")
        self.root.resizable(False, True)

        self.main()

    def main(self) -> None:
        if self.is_register:
            # print(self.is_register)

            # print('--> ', self.controller)

            self.set_title(title=self.controller.username)

            interactiveMessages = InteractiveMessages(
                                            parentFrame=self.root,
                                            controller=self.controller
                                        )
            interactiveMessages.render()

        else:
            data = FormUserData(
                        rootFrame=self.root,
                        controller=self.controller,
                        callback=self.user_data_callback
                    )
            data.display()

    def user_data_callback(
        self,
        instance_controller: Controller = None
    ) -> None:
        # print(self.controller, instance_controller)
        self.is_register = True
        if instance_controller is not None:
            self.controller = instance_controller
        self.main()

    def set_title(self, title: str) -> None:
        new_title = 'PyChatGui  (%s - Chat %s)' % (
                            self.controller.username,
                            self.controller.chatroom
                        )
        self.root.title(new_title)

    def close_connection(self, *args) -> None:
        self.controller.send_message(message=None)
        self.controller.socket_stop()


class InteractiveMessages(Gui):
    def __init__(
        self,
        parentFrame: ttk.Frame,
        controller: Controller
    ) -> None:
        self.root = parentFrame
        self.controller = controller

        self.textMessages = None
        self.entryMessage = None

    def render(self):
        self.render_messages_section()
        self.render_redaction_section()

        self.controller.recv_messages(
            text_element=self
        )

        self.root.bind('<Destroy>', super().close_connection)

    def render_messages_section(self) -> None:
        frameMessages = ttk.Frame(
                            self.root,
                            relief='solid',
                            padding=(5, 5, 5, 5)
                        )

        textMessages = tk.Text(
                            frameMessages,
                            font=("", 12, ""),
                            wrap=tk.WORD
                        )
        textMessages.config(state=tk.DISABLED)
        textMessages.place(x=0, y=0, relwidth=1, relheight=1)

        frameMessages.place(x=0, y=0, relwidth=1, height=400)

        self.textMessages = textMessages

    def render_redaction_section(self) -> None:
        key_combination = "<Control-Return>"
        frameRedaction = ttk.Frame(
                            self.root,
                            relief='solid',
                            padding=(1, 5, 1, 5)
                        )

        entryMessage = tk.Text(frameRedaction)
        entryMessage.place(x=0, y=0, width=500, relheight=1)
        entryMessage.bind(key_combination, self.sendMessage)

        sendButton = ttk.Button(
                            frameRedaction,
                            text='Send',
                            command=self.sendMessage
                        )
        sendButton.place(x=502, y=30, width=90, height=80)
        sendButton.bind(key_combination, self.sendMessage)

        frameRedaction.place(x=0, y=420, relwidth=1, height=180)

        self.entryMessage = entryMessage

    def get_content_text(self) -> str:
        return self.entryMessage.get("1.0", tk.END)

    def insert_message(
        self,
        message: str
    ) -> None:
        self.textMessages.config(state=tk.NORMAL)
        self.textMessages.insert(tk.END, message)
        self.textMessages.config(state=tk.DISABLED)

    def sendMessage(self, evento=None) -> None:
        message = self.get_content_text()
        prefix = '%s-%s : ' % (
                            self.controller.username,
                            self.controller.get_hash_client()[:8]
                        )
        self.clear_message_redactor()
        self.insert_message(message=prefix + message)
        self.controller.send_message(message=message)

    def clear_message_redactor(self) -> None:
        self.entryMessage.delete('1.0', tk.END)


class FormUserData(Gui):

    def __init__(
        self,
        rootFrame: ttk.Frame,
        controller: Controller,
        callback: DefCallbackGui
    ) -> None:
        self.rootFrame = rootFrame
        self.controller = controller
        self.callback_main_gui = callback

        self.frame_username = None
        self.entryName = None
        self.entryChatroom = None

    def display(self) -> dict:
        frame_username = ttk.Frame(
                self.rootFrame,
                relief='solid',
                padding=(1, 20, 1, 1)
            )
        self.frame_username = frame_username

        infoLabel = ttk.Label(
                frame_username,
                text='Enter data to join to chatroom.',
                justify='center',
                anchor=tk.CENTER,
                font=("", 14, "bold")
            )
        infoLabel.place(x=0, y=0, relwidth=1, height=30)

        nameLabel = ttk.Label(frame_username, text='Username')
        nameLabel.place(x=130, y=50, width=80, height=30)

        nameEntryVar = tk.StringVar()
        entryName = ttk.Entry(frame_username, textvariable=nameEntryVar)
        entryName.place(x=220, y=50, width=250, height=30)

        chatroomLabel = ttk.Label(frame_username, text="ChatRoom")
        chatroomLabel.place(x=130, y=90, width=100, height=30)

        chatroomEntryVar = tk.StringVar()
        entryChatroom = ttk.Entry(
                                frame_username,
                                textvariable=chatroomEntryVar
                            )
        entryChatroom.place(x=220, y=90, width=250, height=30)

        accept = ttk.Button(
                            frame_username,
                            text='Join',
                            command=self.buttonClbk
                        )
        accept.place(x=250, y=130, width=100, height=30)

        frame_username.place(x=2, y=200, relwidth=0.99, height=200)

        self.entryName = entryName
        self.entryChatroom = entryChatroom

    def buttonClbk(self) -> None:
        data = self.check_data(
                username=self.entryName.get(),
                chat_id=self.entryChatroom.get()
            )
        if data['username'] is not None and data['chat_id'] is not None:
            self.frame_username.destroy()

            #   CONTROLLER
            self.controller.set_user_data(
                username=data['username'],
                chatroom=data['chat_id']
            )
            self.controller.create_connection(
                host='localhost',
                port=50008
            )
            self.controller.to_connect()
            #
            self.callback_main_gui(
                    instance_controller=self.controller
                )
        else:
            message = 'Username not be empty,\nChatRoom must be a number.'
            messagebox.showinfo(title='Complete form', message=message)

    def check_data(
        self,
        username: str,
        chat_id: str
    ) -> dict:
        if username.strip() == "":
            username = None
        try:
            chat_id = int(chat_id)
        except ValueError:
            chat_id = None
        return {
            'username': username,
            'chat_id': chat_id
        }



class Main():
    root = Tk()
    gui = Gui(root)
    root.mainloop()


if __name__ == '__main__':
    Main()
