import json
import markdown
import os

rulebook_file = r"d:\Dql\Desktop\dh_cn\cn\中文表\Daggerheart_Core_Rulebook_职业.json"
actions_file = r"d:\Dql\Desktop\dh_cn\cn\extracted_actions.json"
target_file = r"d:\Dql\Desktop\dh_cn\cn\daggerheart.subclasses.json"

with open(rulebook_file, encoding='utf-8') as f:
    rulebook = json.load(f)

with open(actions_file, encoding='utf-8') as f:
    extracted_actions = json.load(f)

with open(target_file, encoding='utf-8') as f:
    subclasses_json = json.load(f)

action_names_trans = {
    "Mark Stress": "标记压力",
    "Healing": "治疗",
    "Fire": "火元素",
    "Earth": "土元素",
    "Water": "水元素",
    "Air": "风元素",
    "Swap Dice Results": "交换结果",
    "Use Feature": "使用特性",
    "Relaxing Song": "舒缓曲",
    "Epic Song": "史诗乐",
    "Heartbreaking Song": "悲凉调",
    "Spend Hope": "花费希望",
    "Mark Armor Slot": "标记护甲槽",
    "Clear Hit Points": "清除生命点",
    "Clear Stress": "清除压力点",
    "Reroll": "重掷",
    "Recall": "回想",
    "Heal a creature": "治疗生物",
    "Target Additional Adversary": "指定额外敌人",
    "Talk to your allies!": "与盟友交谈",
    "Evade": "闪避",
    "Manipulate": "操弄魔法",
    "Comaraderie": "战友情谊",
    "Bonus to Roll": "判定加值",
    "Bonus to Damage": "伤害加值",
    "SpellCast: Dark Cloud": "施法：暗云",
    "Mark Adversary": "锁定敌人",
    "Prepare": "准备",
    "Transform": "转化",
    "Roll d6": "掷 d6",
    "Rush": "冲刺"
}

action_desc_trans = {
    "7Z9v7GWswIQFD5YH": "当你一次攻击成功时，你可以迫使目标额外标记1点生命点。", 
    "ozYzhQfRt5sp19di": "每长休一次，花费2希望点，近距离范围内的1d4个盟友恢复2生命点。", 
    "AdOnKhi7g6zQu2iv": "当敌人标记生命点时，其还必须标记1压力点。", 
    "xDBLH5TWidvrYF7z": "你盟友的力量值获得+1加值。", 
    "S4t5HlgxWlHwaBDw": "当敌人对你造成伤害时，你可以标记1压力点，将其移动到其当前位置极近范围内的任意地点。", 
    "hAsKFFewtTqd1gg9": "当你或盟友受到近战范围之外的攻击伤害时，伤害减少1d8点。", 
    "n8wSqR967o0pZDLR": "每长休一次，在盟友在你的帮助下完成施法掷骰后，你可以交换盟友的二元骰结果。", 
    "o1MWnafbLsXnvSUl": "允许盟友找到一件所需的普通物品或工具，在不花费希望点的情况下帮助一名盟友，或在其下一次休息期间给予其额外的休整行动。", 
    "xvs7ZKm93AlnZD3F": "你和近距离范围内的所有盟友恢复1生命点。", 
    "nvfJ8rOx8baI6POZ": "使近距离范围内的一个目标暂时处于易伤状态。", 
    "QTTgKnhpNE2XHz4u": "你和近距离范围内的所有盟友获得1希望点。", 
    "pHSfMDmfVQSgqk39": "花费1希望点，为掷骰添加一个d4加值。", 
    "Rgc7kBmU3kjHKvfx": "花费2希望点锁定一个敌人，同一时间只能锁定一个敌人。", 
    "ofdSzqY7IfAy5ayv": "你在造成伤害的攻击和法术的熟练值上获得+1加值。", 
    "knGm3snaplWYDaue": "为每个标记的生命点掷一个d6，每掷出6，你标记的生命点数量减少1点。", 
    "MocaqHUdyVwH0ZFu": "你可以标记1压力点，使攻击者暂时处于易伤状态。", 
    "AQMNJRmVyhJTSCfR": "你的闪避值获得+1加值，并且你可以飞行。", 
    "D6ClOGDgu6cLanjE": "当一个邻近范围内的盟友受到伤害时，你可以标记1护甲槽将伤害等级降低一级。", 
    "aanLNQkeO2ZTIqBl": "触碰一个生物，为其恢复2生命点。", 
    "cWdzCQJv8RFfi2NR": "触碰一个生物，为其清除2压力点。", 
    "vay9rVXJS3iksaVR": "花费1希望点，将你的副手武器的一个伤害骰加入到伤害掷骰中。", 
    "1bBFfxmywJpx5tfk": "每次长休，当你掷出杀手骰时，可以将所有结果为1的骰重掷。", 
    "rFZj0ZsnJCc0PS3h": "每次休息一次，当你回想宝库中的一张领域卡时，你可以将其回想费用减少1。", 
    "9WxcZ3BuXUKfqUMz": "你可以标记1压力点来减少1点盟友需要标记的生命点。", 
    "kD2kWWj0oR7ZxyVs": "触碰一个生物并花费3希望点。该生物恢复1d4生命点。", 
    "rg2sLCTqY2rTo861": "标记 1 压力点以携带另一个体型与你相近或更小的自愿生物。", 
    "1qjnoz5I7NqrWMkp": "花费 1 希望点以在成功攻击时造成额外的 1d8 伤害。", 
    "TDvWFqAxu7V33UIC": "标记1压力点，以相同的攻击掷骰额外攻击范围内的另一名敌人。", 
    "WNtHiko4DRGbxKnm": "远距离范围内的盟友清除2压力点。", 
    "0YRLL1HC4XS3tX00": "标记1压力点使熟练值获得+1加值。对一个敌人目标造成严重伤害时，其必须标记1压力点。", 
    "amJMKDdSgJHsOsOB": "掷一个d6并将骰值加入你对抗该攻击的闪避值上。", 
    "KL5l4QJjPtDiDBSv": "将法术或攻击的作用范围扩大，或获得+2加值，或翻倍伤害，或命中额外目标。", 
    "GZDYjtPh0lCJ5VNq": "召来一个联系人，获得物品、检定加值或伤害加值。", 
    "eBSXC0l2IrRb1F8f": "每场游戏你可以额外发起一次接力掷骰。", 
    "rxuFLfHP1FILDpds": "动作掷骰结果获得+2加值。", 
    "S7HvFD3qIR3ifJRL": "伤害掷骰结果获得+3加值。", 
    "az7YUpxy1ysn12tO": "清除等同于你本能值的压力点。", 
    "wVGSzAnJGs5eXKqI": "当近战范围内的敌人对你造成伤害时，其受到1d10魔法伤害。", 
    "6QXTThhnJpGDIvhJ": "你的伤害阈值获得等同于熟练值的加值。", 
    "pY2EdEMoyLGYWjK5": "极近范围内的所有其他敌人都必须标记1压力点。", 
    "uk8EgHMxCgoWENzt": "你可以悬浮并在敏捷掷骰上获得优势。", 
    "nIgBwYfAVAJ98lzb": "创造一个临时黑暗云团。你被视为处于隐蔽状态。", 
    "g1VIG6VjYKkm11qJ": "消失并在另一个阴影中重新出现，进入隐蔽状态。", 
    "Dxnu3gPSTSysJnb8": "冲刺到其身边，由你承受伤害。", 
    "BjAECQULugmbVqXU": "自动变为隐蔽状态直到下次休息。", 
    "yalzg4VRmZvakshJ": "增加下一次成功攻击的熟练值+1。", 
    "LHDsuveQznbcFUhV": "花费1希望点。如果攻击成功，从恐惧池中移除1恐惧点。", 
    "e00FXbyXZ8bHRY2t": "标记2压力点迫使攻击者标记1生命点。", 
    "UdZx74Vcz6ip4Plh": "清除2压力点并获得2希望点。", 
    "RIbyJjEkCgqoDmyn": "转化为元素的实体化身。", 
    "FOl7kaOG6DFWIpMm": "标记1压力点来代替花费希望点并使加值翻倍。", 
    "zCTrqPtGARSZ06CU": "掷一个d6。结果为5或更高时，无需花费希望点。", 
    "Z82YQzYWo4eektMa": "代替承受该伤害。" 
}

rulebook_map = {}

for cls in rulebook:
    for i in range(1, 10):
        subclass_name = cls.get(f"子职业{i}")
        if subclass_name:
            for lvl in ["基础", "进阶", "精通"]:
                feat_key = f"子职业{i}_{lvl}_特性"
                for feat in cls.get(feat_key, []):
                    rulebook_map[feat.get("名称")] = feat.get("描述", "")

for eng_key, obj in subclasses_json.get("entries", {}).items():
    c_name = obj.get("name")
    
    if c_name in rulebook_map:
        md_text = rulebook_map[c_name]
        html_text = markdown.markdown(md_text).replace('\n', '')
        obj["description"] = html_text
        obj["flags.babele.originalName"] = c_name
        
    actions_for_entry = [a for a in extracted_actions if a.get("entryName") == c_name]
    if actions_for_entry:
        for action in actions_for_entry:
            aid = action.get("actionId")
            obj[f"actions.{aid}.name"] = action_names_trans.get(action.get("actionName"), action.get("actionName"))
            obj[f"actions.{aid}.cost"] = action_desc_trans.get(aid, action.get("actionDescription"))
            obj["flags.babele.originalName"] = c_name

with open(target_file, "w", encoding='utf-8') as f:
    json.dump(subclasses_json, f, ensure_ascii=False, indent=2)

print("Subclasses updated successfully.")
