import threading

from sqlalchemy import Column, String

from Yone.modules.sql import BASE, SESSION


class yoneChats(BASE):
    __tablename__ = "yone_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


yoneChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_yone(chat_id):
    try:
        chat = SESSION.query(yoneChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_yone(chat_id):
    with INSERTION_LOCK:
        yonechat = SESSION.query(yoneChats).get(str(chat_id))
        if not yonechat:
            yonechat = yoneChats(str(chat_id))
        SESSION.add(yonechat)
        SESSION.commit()


def rem_yone(chat_id):
    with INSERTION_LOCK:
        yonechat = SESSION.query(yoneChats).get(str(chat_id))
        if yonechat:
            SESSION.delete(yonechat)
        SESSION.commit()
