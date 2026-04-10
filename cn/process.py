import json
import markdown
import os

target_file = "daggerheart.classes.json"
source_file = "中文表\\Daggerheart_Core_Rulebook_职业.json"

with open(source_file, encoding='utf-8') as f:
    rulebook = json.load(f)

with open(target_file, encoding='utf-8') as f:
    classes_json = json.load(f)

rulebook_map = {}
class_info = {}

for cls in rulebook:
    name = cls.get("名称")
    if name:
        rulebook_map[name] = cls.get("简介", "")
        class_info[name] = cls
    
    hope_name = cls.get("希望特性名称")
    if hope_name:
        rulebook_map[hope_name] = cls.get("希望特性描述", "")
    
    for feat in cls.get("职业特性", []):
        rulebook_map[feat.get("名称")] = feat.get("描述", "")

    # Add subclass features
    for i in range(1, 10):
        sub_key = f"子职业{i}"
        if sub_key in cls:
            # check basic, adv, mastery features
            for lvl in ["基础", "进阶", "精通"]:
                feat_key = f"{sub_key}_{lvl}_特性"
                for feat in cls.get(feat_key, []):
                    rulebook_map[feat.get("名称")] = feat.get("描述", "")

# Update mapping in target file
classes_json.setdefault("mapping", {}).update({
    "backgroundQuestion0": "system.backgroundQuestions.0",
    "backgroundQuestion1": "system.backgroundQuestions.1",
    "backgroundQuestion2": "system.backgroundQuestions.2",
    "connection0": "system.connections.0",
    "connection1": "system.connections.1",
    "connection2": "system.connections.2"
})

class_names_list = ["吟游诗人", "德鲁伊", "守护者", "游侠", "游荡者", "神使", "术士", "战士", "法师"]

for eng_key, obj in classes_json.get("entries", {}).items():
    c_name = obj.get("name")
    if c_name in rulebook_map:
        md_text = rulebook_map[c_name]
        # Generate HTML from markdown
        html_text = markdown.markdown(md_text)
        # remove newlines to compress
        html_text = html_text.replace('\n', '')
        obj["description"] = html_text
        
        # If it's one of the classes, add bg & conn
        if c_name in class_names_list:
            bg = class_info[c_name].get("背景问题", [])
            conn = class_info[c_name].get("关系问题", [])
            for i in range(min(3, len(bg))):
                obj[f"backgroundQuestion{i}"] = bg[i]
            for i in range(min(3, len(conn))):
                obj[f"connection{i}"] = conn[i]

with open(target_file, "w", encoding='utf-8') as f:
    json.dump(classes_json, f, ensure_ascii=False, indent=2)

print("Replacement complete.")
