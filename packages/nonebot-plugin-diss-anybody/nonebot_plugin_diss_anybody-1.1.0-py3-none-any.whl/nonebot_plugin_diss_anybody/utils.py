from nonebot import get_driver
from nonebot import logger
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11 import Message, MessageSegment

from .config import DissConfig

from tinydb import TinyDB, Query
from pathlib import Path
from datetime import datetime

import random


global_config = get_driver().config
config = DissConfig.parse_obj(global_config)
resource = getattr(global_config, "resources_dir", None)
if resource and Path(resource).exists():
    res_path = Path(resource) / "diss"
else:
    res_path = Path("data/diss")
res_path.mkdir(parents=True, exist_ok=True)

db = TinyDB(res_path / "diss_info.json", encoding="utf-8", ensure_ascii=False)
User = Query()


class diss_info:
    def __init__(self, event: GroupMessageEvent):
        self.user_id = event.user_id
        self.group_id = event.group_id
        self.message_id = event.message_id
        self.result = db.search(User.user_id == self.user_id)

    def get_reply(self):
        if self.result and self.check():
            reply = self.resolve_reply(self.result[0]["reply"])
            if reply:
                timestamp = datetime.timestamp(datetime.now())
                db.update(
                    {"last_diss": timestamp},
                    User.user_id == self.user_id,
                )
                logger.opt(colors=True).info(
                    f"Bot ready to send message, marking timestamp <e>{timestamp}</e>"
                )
            return reply
        return None

    def resolve_reply(self, reply: str | list[str]) -> MessageSegment | None:
        if type(self.result[0]["reply"]) == list:
            reply = random.choice(reply)

        if reply.startswith("image://"):
            file = res_path / "images" /reply[8:]
            try:
                logger.opt(colors=True).info(
                    f"Bot trying to diss <e>{self.user_id}</e> in group <e>{self.group_id}</e> with image <g>{file}</g>"
                )
                return MessageSegment.reply(id_=self.message_id) + MessageSegment.image(file)
            except FileNotFoundError:
                logger.opt(colors=True).warning(
                    f"Bot fail to diss with image: <r>{file}</r> not found"
                )
                return None
        elif reply.startswith("text://"):
            logger.opt(colors=True).info(
                f"Bot trying to diss <e>{self.user_id}</e> with <g>{reply}</g> in group <e>{self.group_id}</e>"
            )
            return MessageSegment.reply(id_=self.message_id) + MessageSegment.text(reply[6:])
        else:
            logger.opt(colors=True).info(
                f"Bot trying to diss <e>{self.user_id}</e> with raw meaasge <g>{reply}</g> in group <e>{self.group_id}</e>"
            )
            return MessageSegment.reply(id_=self.message_id) + Message(reply)

    def check(self):
        return self.check_blacklist() and self.check_chance() and self.check_cd()

    def check_blacklist(self):
        try:
            blacklist = self.result[0]["blacklist"].extend(config.diss_global_blacklist)
            blacklist = list(set(blacklist))
        except KeyError:
            blacklist = config.diss_global_blacklist
        return self.group_id not in blacklist

    def check_chance(self):
        try:
            chance = self.result[0]["chance"]
        except KeyError:
            chance = config.diss_global_chance
        return random.random() < chance

    def check_cd(self):
        try:
            cd = self.result[0]["cd"]
        except KeyError:
            cd = config.diss_global_cd

        if cd == 0:
            return True
        else:
            timestamp = datetime.timestamp(datetime.now())
            try:
                return (timestamp - self.result[0]["last_diss"]) > cd
            except KeyError:
                return True
