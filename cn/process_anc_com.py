import json
import markdown

anc_map = {
    # Ancestries
    "Simiah": "猿族",
    "Giant": "巨人",
    "Halfling": "半身人",
    "Orc": "兽人",
    "Goblin": "哥布林",
    "Faun": "羊蹄人",
    "Ribbet": "蛙裔",
    "Fungril": "孢菌人",
    "Drakona": "龙人",
    "Faerie": "仙灵",
    "Galapa": "龟人",
    "Clank": "械灵",
    "Infernis": "魔裔",
    "Firbolg": "费尔博格",
    "Dwarf": "矮人",
    "Elf": "精灵",
    "Human": "人类",
    "Katari": "猫族",

    # Ancestry Features
    "Efficient": "高效休整",
    "Purposeful Design": "定制设计",
    "Scales": "鳞片保护",
    "Elemental Breath": "元素吐息",
    "Thick Skin": "厚实皮肤",
    "Increased Fortitude": "增强坚韧",
    "Quick Reactions": "快速反应",
    "Celestial Trance": "天界冥想",
    "Luckbender": "运气操控者",
    "Wings": "翅膀",
    "Caprine Leap": "跳跃",
    "Kick": "踢击",
    "Charge": "冲撞",
    "Unshakeable": "百折不挠",
    "Fungril Network": "孢菌网络",
    "Death Connection": "死亡连接",
    "Shell": "龟甲",
    "Retract": "缩壳",
    "Sturdy": "坚韧",
    "Reach": "长臂",
    "Surefooted": "稳健脚步",
    "Danger Sense": "危险感应",
    "Luckbringer": "幸运使者",
    "Internal Compass": "内在罗盘",
    "High Stamina": "精力充沛",
    "Adaptability": "随机应变",
    "Fearless": "无畏",
    "Dread Visage": "恐怖面容",
    "Feline Instincts": "猫科本能",
    "Retracting Claws": "伸缩猫爪",
    "Endurance": "强壮",
    "Tusks": "獠牙",
    "Amphibious": "两栖",
    "Long Tongue": "长舌",
    "Natural Climber": "天生攀爬者",
    "Nimble": "灵活"
}

com_map = {
    # Communities
    "Highborne": "高城之民",
    "Loreborne": "博识之民",
    "Orderborne": "结社之民",
    "Ridgeborne": "山岭之民",
    "Seaborne": "滨海之民",
    "Slyborne": "法外之民",
    "Underborne": "地下之民",
    "Wanderborne": "漂泊之民",
    "Wildborne": "荒野之民",

    # Features
    "Privilege": "高人一等",
    "Well-Read": "博览群书",
    "Dedicated": "恪守不渝",
    "Steady": "脚踏实地",
    "Know the Tide": "潮起潮落",
    "Scoundrel": "恶贯满盈",
    "Low-Light Living": "微光生存",
    "Nomadic Pack": "游牧行囊",
    "Lightfoot": "轻盈步伐"
}

def parse_features(rulebook_desc):
    features = {}
    for line in rulebook_desc.split('\n'):
        if ':' in line:
            parts = line.split(':', 1)
            features[parts[0].strip()] = parts[1].strip()
        elif '：' in line:
            parts = line.split('：', 1)
            features[parts[0].strip()] = parts[1].strip()
    return features

# --- Process Ancestries ---
with open(r'd:\Dql\Desktop\dh_cn\cn\中文表\Daggerheart_Core_Rulebook_种族.json', 'r', encoding='utf-8') as f:
    rb_anc = json.load(f)

anc_rb_data = {}
anc_feat_data = {}

for a in rb_anc:
    name = a["名称"]
    anc_rb_data[name] = markdown.markdown(a.get("简介", "")).replace('\n', '')
    
    # parse features
    feats = parse_features(a.get("描述", ""))
    for fname, fdesc in feats.items():
        anc_feat_data[fname] = markdown.markdown(fdesc).replace('\n', '')

with open(r'd:\Dql\Desktop\dh_cn\cn\daggerheart.ancestries.json', 'r', encoding='utf-8') as f:
    anc_json = json.load(f)

anc_json["label"] = "种族"
if "mapping" not in anc_json:
    anc_json["mapping"] = {}
anc_json["mapping"]["description"] = "system.description"

for eng_key, obj in anc_json.get("entries", {}).items():
    cn_name = anc_map.get(eng_key, eng_key)
    obj["name"] = cn_name
    
    if cn_name in anc_rb_data:
        obj["description"] = anc_rb_data[cn_name]
    elif cn_name in anc_feat_data:
        obj["description"] = anc_feat_data[cn_name]

with open(r'd:\Dql\Desktop\dh_cn\cn\daggerheart.ancestries.json', 'w', encoding='utf-8') as f:
    json.dump(anc_json, f, ensure_ascii=False, indent=2)


# --- Process Communities ---
with open(r'd:\Dql\Desktop\dh_cn\cn\中文表\Daggerheart_Core_Rulebook_社群.json', 'r', encoding='utf-8') as f:
    rb_com = json.load(f)

com_rb_data = {}
com_feat_data = {}

for a in rb_com:
    name = a["名称"]
    desc = a.get("简介", "")
    if a.get("性格"):
        desc += "\n\n" + a.get("性格")
    com_rb_data[name] = markdown.markdown(desc).replace('\n', '')
    
    feats = parse_features(a.get("描述", ""))
    for fname, fdesc in feats.items():
        com_feat_data[fname] = markdown.markdown(fdesc).replace('\n', '')

with open(r'd:\Dql\Desktop\dh_cn\cn\daggerheart.communities.json', 'r', encoding='utf-8') as f:
    com_json = json.load(f)

com_json["label"] = "社群"
if "mapping" not in com_json:
    com_json["mapping"] = {}
com_json["mapping"]["description"] = "system.description"

for eng_key, obj in com_json.get("entries", {}).items():
    cn_name = com_map.get(eng_key, eng_key)
    obj["name"] = cn_name
    
    if cn_name in com_rb_data:
        obj["description"] = com_rb_data[cn_name]
    elif cn_name in com_feat_data:
        obj["description"] = com_feat_data[cn_name]

with open(r'd:\Dql\Desktop\dh_cn\cn\daggerheart.communities.json', 'w', encoding='utf-8') as f:
    json.dump(com_json, f, ensure_ascii=False, indent=2)

print("Ancestries and Communities updated successfully!")
