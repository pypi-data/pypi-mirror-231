from nonebot import get_driver
from nonebot import on_message
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11 import permission
from nonebot.plugin import PluginMetadata

from .config import DissConfig

from .utils import diss_info

__plugin_meta = PluginMetadata(
    name="nonebot-plugin-diss-anybody",
    description="在指定的用户发言时，有几率回复指定的内容",
    usage="怼人就完事了（",
    type="application",
    homepage="https://github.com/SherkeyXD/nonebot-plugin-diss-anybody",
    config=DissConfig,
    supported_adapters={"~onebot.v11"},
)


global_config = get_driver().config
config = DissConfig.parse_obj(global_config)

diss = on_message(priority=25, block=False, permission=permission.GROUP)


@diss.handle()
async def diss_somebody(event: GroupMessageEvent):
    msg = diss_info(event)

    reply = msg.get_reply()
    if reply:
        await diss.finish(reply)
    return None
