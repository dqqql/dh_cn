import json
import markdown

rulebook_file = r"d:\Dql\Desktop\dh_cn\cn\中文表\Daggerheart_Core_Rulebook_领域卡.json"
target_file = r"d:\Dql\Desktop\dh_cn\cn\daggerheart.domains.json"

with open(rulebook_file, encoding='utf-8') as f:
    rulebook = json.load(f)

with open(target_file, encoding='utf-8') as f:
    domains_json = json.load(f)

if "mapping" not in domains_json:
    domains_json["mapping"] = {}
domains_json["mapping"]["description"] = "system.description"

card_dict = {}
for card in rulebook:
    name = card.get("名称")
    desc = card.get("描述", "")
    if name:
        card_dict[name] = desc

manual_map = {
  "Forager": "丰收采集",
  "Chain Lightning": "连锁闪电",
  "Phantom Retreat": "无踪影遁",
  "Wall Walk": "墙面行走",
  "Book of Tyfar": "提法之书",
  "Preservation Blast": "保护之域",
  "Hypnotic Shimmer": "催眠闪光",
  "Reckless": "鲁莽攻击",
  "Deft Deceiver": "欺瞒熟手",
  "Copycat": "如法炮制",
  "Gore and Glory": "血与荣耀",
  "Salvation Beam": "救赎光束",
  "Flight": "飞行奇术",
  "Cinder Grasp": "余烬之握",
  "Arcana-Touched": "奥术恩泽",
  "Strategic Approach": "战术方针",
  "Scramble": "快步急闪",
  "Eclipse": "日蚀无光",
  "Counterspell": "法术反制",
  "Codex-Touched": "典籍恩泽",
  "Through Your Eyes": "感官共享",
  "Breaking Blow": "碎骨打击",
  "Share the Burden": "解忧消难",
  "Wrangle": "缠斗乱战",
  "Untouchable": "不可侵犯",
  "Plant Dominion": "植物统御",
  "Wild Fortress": "荒野壁垒",
  "Shadowhunter": "暗影猎手",
  "Critical Inspiration": "关键鼓舞",
  "Banish": "放逐术",
  "Thought Delver": "挖掘思想",
  "Glyph of Nightfall": "夜幕符文",
  "Get Back Up": "卷土重来",
  "Bolt Beacon": "曳光信标",
  "Lean on Me": "中流砥柱",
  "Earthquake": "地动山摇",
  "Unbreakable": "坚不可摧",
  "Wild Surge": "狂野浪涌",
  "Battle Cry": "战斗咆哮",
  "Fane of the Wilds": "野地神殿",
  "Midnight Spirit": "午夜精魂",
  "Telekinesis": "心灵遥控",
  "Vanishing Dodge": "闪转腾挪",
  "Rune Ward": "符文护符",
  "Rage Up": "狂怒出击",
  "Blade-Touched": "利刃恩泽",
  "Healing Field": "治疗之域",
  "Swift Step": "灵巧机动", 
  "Tell No Lies": "沉默不言",
  "Pick and Pull": "妙手空空",
  "Teleport": "传送术",
  "Rejuvenation Barrier": "回春屏障",
  "Goad Them On": "激将大法",
  "Onslaught": "猛攻强袭",
  "Notorious": "恶名昭彰",
  "Book of Yarrow": "亚罗之书",
  "Splendor-Touched": "辉耀恩泽",
  "Conjured Steeds": "召唤坐骑",
  "Troublemaker": "惹是生非",
  "Forest Sprites": "森林精魂",
  "Shrug It Off": "火力全开",
  "Arcane Reflection": "奥术反射",
  "Divination": "预言卜筮",
  "Grace-Touched": "优雅恩泽",
  "Invisibility": "移形换影",
  "I Am Your Shield": "吾身为盾",
  "I See It Coming": "先见之明",
  "Signature Move": "招牌动作",
  "Force of Nature": "自然之力",
  "Reaper’s Strike": "死亡收割",
  "Frenzy": "狂暴反击",
  "Never Upstaged": "绝不怯场",
  "Stealth Expertise": "潜行专家",
  "Final Words": "临终遗言",
  "Battle-Hardened": "久经沙场",
  "Know Thy Enemy": "知己知彼",
  "Bone-Touched": "骸骨恩泽",
  "Life Ward": "生命护符",
  "Battle Monster": "战场猛兽",
  "Soothing Speech": "宽慰言语",
  "Brace": "泰然自若",
  "Blink Out": "闪烁现身",
  "Book of Grynn": "格林之书",
  "Chokehold": "锁喉勒颈",
  "Confusing Aura": "惑像灵光",
  "Sigil of Retribution": "惩戒符印",
  "Twilight Toll": "暮光丧钟",
  "Book of Ronin": "罗宁之书",
  "Full Surge": "蛮力冲撞",
  "Mending Touch": "修复之触",
  "Uncanny Disguise": "奇异伪装",
  "Splintering Strike": "分裂打击",
  "Natural Familiar": "自然魔宠",
  "Manifest Wall": "具现之墙",
  "Smite": "惩戒重击",
  "Rain of Blades": "滂沱剑雨",
  "Boost": "强化护甲",
  "Book of Vyola": "维奥拉之书",
  "Sage-Touched": "贤者恩泽",
  "Gifted Tracker": "追猎才能",
  "Tactician": "战术行家",
  "Healing Hands": "治愈之手",
  "Ground Pound": "撼地猛击",
  "Book of Norai": "诺莱伊之书",
  "Tempest": "狂风怒号", 
  "Invigoration": "蓬勃生命",
  "Inevitable": "命中注定",
  "Healing Strike": "治愈打击",
  "A Soldier’s Bond": "老兵羁绊",
  "Astral Projection": "星界投影",
  "Lead by Example": "以身作则",
  "Book of Ava": "艾娃之书",
  "Cloaking Blast": "无影无踪",
  "Words of Discord": "挑拨离间",
  "Adjust Reality": "调整现实",
  "Enrapture": "心醉神迷",
  "Premonition": "预见未来",
  "Body Basher": "强力冲撞",
  "Book of Vagras": "瓦格拉斯之书",
  "Whirlwind": "旋风猛袭",
  "Nature’s Tongue": "自然之语",
  "Cruel Precision": "残酷精准",
  "Book of Korvax": "库瓦斯之书",
  "Inspirational Words": "豪言壮语",
  "Armorer": "护甲大师",
  "Mass Disguise": "群体伪装",
  "Shape Material": "物质塑形",
  "Deft Maneuvers": "警戒防备",
  "Book of Illiat": "伊利亚特之书",
  "Book of Sitil": "斯泰尔之书",
  "Spellcharge": "法术充能",
  "Redirect": "借力打力",
  "Second Wind": "复苏之风",
  "Book of Homet": "霍梅特之书",
  "Veil of Night": "暗夜帷幕",
  "Sensory Projection": "感官投射",
  "Recovery": "恢复如新",
  "Hush": "无可讳言",
  "Falling Sky": "星辰陨落",
  "Overwhelming Aura": "威压灵光",
  "Specter of the Dark": "黑暗幽影",
  "Reassurance": "排忧解难",
  "Ferocity": "凶猛残暴",
  "Valor-Touched": "勇气恩泽",
  "Transcendent Union": "超凡联结",
  "Hold the Line": "坚守阵线",
  "Shadowbind": "暗影束缚",
  "Disintegration Wave": "解离波",
  "Encore": "再次上演",
  "Bare Bones": "白骨之躯",
  "Zone of Protection": "避风港湾",
  "Stunning Sunlight": "震撼烈阳",
  "Safe Haven": "安全避难",
  "Towering Stalk": "高茎成塔",
  "Glancing Blow": "斜掠攻势",
  "Unleash Chaos": "释放混沌",
  "Rise Up": "奋起直追",
  "Thorn Skin": "荆棘皮肤",
  "Fortified Armor": "不灭甲胄",
  "Book of Exota": "埃索塔之书",
  "Rousing Strike": "振奋打击",
  "Corrosive Projectile": "腐蚀射弹",
  "Vicious Entangle": "怨毒缠绕",
  "Conjure Swarm": "召唤虫群",
  "Shield Aura": "护盾灵光",
  "Champion’s Edge": "勇士锐锋",
  "Unyielding Armor": "铁骨铮铮",
  "Vitality": "生生不息", 
  "Support Tank": "坚盾后援",
  "Voice of Reason": "理性之声",
  "Endless Charisma": "无穷魅力",
  "Rapid Riposte": "迅速报复", 
  "Bold Presence": "刚健风采",
  "Midnight-Touched": "午夜恩泽",
  "Mass Enrapture": "群体心醉神迷",
  "Rift Walker": "裂隙行者",
  "Floating Eye": "浮游之眼",
  "Versatile Fighter": "多面武者",
  "Restoration": "复原术法",
  "Death Grip": "死亡卷握",
  "Deathrun": "死亡奔袭",
  "Not Good Enough": "还不够好",
  "Deadly Focus": "致命专注",
  "Master of the Craft": "技艺大师",
  "Dark Whispers": "黑暗低语",
  "Resurrection": "亡者苏生",
  "Forceful Push": "有力推击",
  "On the Brink": "生死边缘",
  "Night Terror": "夜魇降临"
}

entries = domains_json.get("entries", {})
matched_count = 0
unmatched = []

import difflib

for eng_key, obj in entries.items():
    c_name = obj.get("name")
    ru_name = manual_map.get(eng_key, c_name)
    
    # Try direct translation match first
    if ru_name in card_dict:
        obj["name"] = ru_name
        md_text = card_dict[ru_name]
        obj["description"] = markdown.markdown(md_text).replace('\n', '')
        matched_count += 1
    else:
        # Fallback 1: user translated name
        if c_name in card_dict:
            md_text = card_dict[c_name]
            obj["description"] = markdown.markdown(md_text).replace('\n', '')
            matched_count += 1
        else:
            # Fallback 2: fuzzy match against all keys
            matches = difflib.get_close_matches(ru_name, card_dict.keys(), n=1, cutoff=0.4)
            if not matches:
                matches = difflib.get_close_matches(c_name, card_dict.keys(), n=1, cutoff=0.3)
            
            if matches:
                best = matches[0]
                obj["name"] = best
                obj["description"] = markdown.markdown(card_dict[best]).replace('\n', '')
                matched_count += 1
            else:
                unmatched.append(eng_key)


with open(target_file, "w", encoding='utf-8') as f:
    json.dump(domains_json, f, ensure_ascii=False, indent=2)

for u in unmatched:
    print(f"FAILED TO MATCH: {u}")

print(f"Matched and updated {matched_count} domain cards.")
