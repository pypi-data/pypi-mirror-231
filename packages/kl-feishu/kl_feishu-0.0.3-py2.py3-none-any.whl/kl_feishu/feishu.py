import json
from requests import Response
from requests_html import HTMLSession
# import urllib3
import uuid
import logging
import time
from typing import List
import feishu_sdk.feishu_def as feishudef
from pydantic import BaseModel
from typing import List

class CardMsgRoot(BaseModel):
    config: feishudef.Config = feishudef.Config()
    elements: List[feishudef.Element] = []
    header: feishudef.Header = feishudef.Header()

class FeiShuHelp:
    _appid = ""
    _appsecret = ""
    _token = ""
    _group_list: List[feishudef.GroupInfo] = []

    def __init__(self, appid, appsecret):
        self._appid = appid
        self._appsecret = appsecret
        self.session = HTMLSession()
        self.session.verify = False  # fiddle抓包
        self.headers = {
            "Content-Type": "application/json",
        }
        self._init_data()

    def _checkErr(self, res: Response):
        retjson = json.loads(res.text)
        if retjson["code"] == 99991663 or retjson["code"] == 99991661:
            print(f'token过期，重新获取')
            self._get_token()
            return True
        return False

    # 请求
    def _get(self, url, **kwargs) -> Response:
        kwargs.setdefault('headers', self.headers)
        try:
            ret = self.session.get(url, timeout=10, **kwargs)
            if self._checkErr(ret):
                ret = self.session.get(url, timeout=10, **kwargs)
        except Exception as e:
            time.sleep(2)
            print(f'session过期：重新登录:{str(e)}')
            self._get_token()
            res = self.session.get(url, timeout=10, **kwargs)
            return res
        return ret

    # post
    def _post(self, url, dictdata=None, json_data=None, **kwargs) -> Response:
        kwargs.setdefault('headers', self.headers)
        try:
            ret = self.session.post(url, data=dictdata, json=json_data, timeout=10, **kwargs)
            if self._checkErr(ret):
                ret = self.session.post(url, data=dictdata, json=json_data, timeout=10, **kwargs)
        except Exception as e:
            time.sleep(2)
            print(f'session过期：重新登录:{str(e)}')
            self._get_token()
            ret = self.session.post(url, data=dictdata, json=json_data, timeout=10, **kwargs)
            return ret
        return ret

    def _get_token(self):
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
        data = {'app_id': self._appid, 'app_secret': self._appsecret}
        res = self._post(url, json_data=data)
        self._token = json.loads(res.text)['tenant_access_token']
        self.headers["Authorization"] = f'Bearer {self._token}'
        logging.info(f'飞书token获取成功:{self._token}')

    def _init_data(self):
        # self._get_token()
        self._get_group_list()

    def _get_group_list(self):
        url = 'https://open.feishu.cn/open-apis/im/v1/chats'
        data = {"page_size": 20}
        res = self._get(url, params=data)
        print(res.text)
        res_json = json.loads(res.text)
        for item in res_json["data"]["items"]:
            groupitem = feishudef.GroupInfo.parse_obj(item)
            self._group_list.append(groupitem)
        print(f'获取组数里:{len(self._group_list)}')

    def get_group_info_by_name(self, grouname) -> feishudef.GroupInfo:
        for group_info in self._group_list:
            if group_info.name == grouname:
                return group_info
        logging.info(f'群组找不到:{grouname}')

    def get_group_info_by_id(self, chat_id: str) -> feishudef.GroupInfo:
        for group_info in self._group_list:
            if group_info.chat_id == chat_id:
                return group_info
        logging.info(f'群组找不到:{chat_id}')

    def init_group_user_list(self, group_info: feishudef.GroupInfo):
        page_size = 20
        page_token = ""
        group_info.members = []
        while True:
            url = f'https://open.feishu.cn/open-apis/im/v1/chats/{group_info.chat_id}/members'
            req_data = {'page_size': page_size, 'page_token': page_token}
            res = self._get(url, params=req_data)
            res_json = json.loads(res.text)
            res_data = res_json["data"]
            page_token = res_data["page_token"]
            items = res_data["items"]
            for item in items:
                memberitem = feishudef.GroupMember.parse_obj(item)
                group_info.members.append(memberitem)
            if not res_data["has_more"]:
                break
            # total=res_data["member_total"]
        print(f'获取成员数里:{len(group_info.members)}')

    def get_group_user_info(self, group_info: feishudef.GroupInfo, username: str) -> feishudef.GroupMember:
        if len(group_info.members) == 0:
            self.init_group_user_list(group_info)
        for userinfo in group_info.members:
            if userinfo.name == username:
                return userinfo
        logging.info(f'群组{0}找不到:{1}', group_info.name, username)

    def send_msg(self, receive_type, userid, sendtext="", sendcard=None):
        url = f'https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type={receive_type}'
        req_data = {"receive_id": userid, "uuid": str(uuid.uuid4())}
        # print(f'sendtext内容:{sendtext}')
        # print(f'sendcard内容:{sendcard}')
        if sendtext:
            if isinstance(sendtext, str):
                req_data["msg_type"] = "text"
                req_data["content"] = json.dumps({"text": sendtext})
            else:
                req_data["msg_type"] = "post"
                req_data["content"] = json.dumps(sendtext)
        elif sendcard:
            req_data["msg_type"] = "interactive"
            req_data["content"] = json.dumps(sendcard)  #{"card": sendcard}
        # print(req_data)
        res = self._post(url, json_data=req_data)
        # print(res.text)
        res_json = json.loads(res.text)
        if res_json['code'] == 0:
            print(f'receive_type:{receive_type} userid:{userid} 发送成功')
            return True
        raise Exception(f'发送失败：{res.text}')

    def send_msg_to_user(self, userid:str, sendtext:str):
        return self.send_msg("open_id", userid, sendtext=sendtext)

    def send_msg_to_group(self, groupid:str, sendtext:str):
        return self.send_msg("chat_id", groupid, sendtext=sendtext)

    def send_card_to_user(self, userid:str, sendjson:str):
        return self.send_msg("open_id", userid, sendcard=sendjson)

    def send_card_to_group(self, groupid:str, sendjson:str):
        return self.send_msg("chat_id", groupid, sendcard=sendjson)
