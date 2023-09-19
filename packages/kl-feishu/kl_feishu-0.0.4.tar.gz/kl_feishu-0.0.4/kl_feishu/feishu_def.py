from typing import List
from pydantic import BaseModel

class GroupMember(BaseModel):
    member_id: str = ""
    member_id_type: str = ""
    name: str = ""
    tenant_key: str = ""


class GroupInfo(BaseModel):
    avatar: str = ""
    chat_id: str = ""
    description: str = ""
    external: bool = False
    name: str = ""
    owner_id: str = ""
    owner_id_type: str = ""
    tenant_key: str = ""
    members: List[GroupMember] = []


class Text(BaseModel):
    content: str = ""
    tag: str = ""


class Config(BaseModel):
    wide_screen_mode: bool = True


class Extra(BaseModel):
    tag: str = ""
    text: Text = None
    type: str = ""
    url: str = ""


class ElementAction(BaseModel):
    tag: str = ""
    url: str = ""
    type: str = ""
    text: Text = None


class Element(BaseModel):
    extra: Extra = None
    tag: str = ""
    content: str = ""
    text: Text = None
    actions: List[ElementAction] = None


class Title(BaseModel):
    content: str = ""
    tag: str = ""


class Header(BaseModel):
    template: str = ""
    title: Title = Title()



