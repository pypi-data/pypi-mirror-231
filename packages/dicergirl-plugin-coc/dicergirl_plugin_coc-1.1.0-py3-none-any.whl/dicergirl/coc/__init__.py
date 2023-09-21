from .investigator import Investigator
from .nbhandlers import commands
from .coccards import coc_cards, coc_cache_cards, coc_attrs_dict
from .cocutils import coc_at, coc_dam, coc_ra, coc_en, message_regist
from dicergirl.common.messages import regist

regist(
    "coc",
    """用法：.coc [天命次数] [指令] [选项]
描述：
    完成 COC 人物作成。
指令：
    <ROLL>   天命次数
    cache    给出所有天命池中的人物卡
    set <ID>   使用天命池中序列为ID的人物卡
    age <AGE>    预设置调查员年龄
    name <名称>   调查员姓名
    sex <ID>   调查员性别
    age <ID>   调查员年龄
示例：
    .coc 7   进行7次COC天命
    .coc 5 name 欧若可 sex 女 age 20   预设定5次天命的人物卡为20岁女性人物欧若可
注意：
    - 以上指令均可缺省.
    - 调查员的外貌、教育值等值与年龄相关.""",
    alias=["coc", "克苏鲁"]
)
regist(
    "sc",
    """用法：.sc <成功表达式>/<失败表达式> [SAN]
描述：
    COC 疯狂检定。
示例：
    .sc 1d5/1d10
注意：
  - 表达式支持掷骰表达式语法, 例如1d10.
  - 指定检定的 SAN 值不会修改人物卡数据.
  - 缺省SAN则会自动使用该用户已保存的人物卡数据, 检定结束后人物卡SAN会被修改.""",
    alias=["sc", "sancheck", "疯狂检定"]
)
regist(
    "ti",
    """用法：.ti
描述：
    对调查员进行临时疯狂检定""",
    alias=["ti", "临时疯狂", "临时疯狂检定"]
)
regist(
    "li",
    """用法：.li
描述：
    对调查员进行总结疯狂检定""",
    alias=["li", "总结疯狂", "总结疯狂检定"]
)

coc_cards.load()

__version__ = "1.1.0"

__type__ = "plugin"
__charactor__ = Investigator
__name__ = "coc"
__cname__ = "调查员"
__cards__ = coc_cards
__cache__ = coc_cache_cards
__nbhandler__ = nbhandlers
__nbcommands__ = commands
__commands__ = {
    "at": coc_at,
    "dam": coc_dam,
    "ra": coc_ra,
    "en": coc_en
}
__baseattrs__ = coc_attrs_dict
__description__ = "COC 模式是以H.P.洛夫克拉夫特《克苏鲁的呼唤(Call of Cthulhu)》为背景的 TRPG 跑团模式."