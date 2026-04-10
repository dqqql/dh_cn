import json
import markdown
import os

rulebook_file = r"d:\Dql\Desktop\dh_cn\cn\中文表\Daggerheart_Core_Rulebook_领域卡.json"
target_file = r"d:\Dql\Desktop\dh_cn\cn\daggerheart.domains.json"

with open(rulebook_file, encoding='utf-8') as f:
    rulebook = json.load(f)

with open(target_file, encoding='utf-8') as f:
    domains_json = json.load(f)

# Ensure mapping exists for description
if "mapping" not in domains_json:
    domains_json["mapping"] = {}
domains_json["mapping"]["description"] = "system.description"

# Build dictionary
card_dict = {}
for card in rulebook:
    name = card.get("名称")
    desc = card.get("描述", "")
    if name:
        card_dict[name] = desc

# Update entries
entries = domains_json.get("entries", {})
matched_count = 0
unmatched = []

for eng_key, obj in entries.items():
    c_name = obj.get("name")
    if c_name in card_dict:
        md_text = card_dict[c_name]
        html_text = markdown.markdown(md_text).replace('\n', '')
        obj["description"] = html_text
        matched_count += 1
    else:
        unmatched.append(c_name)

with open(target_file, "w", encoding='utf-8') as f:
    json.dump(domains_json, f, ensure_ascii=False, indent=2)

print(f"Matched and updated {matched_count} domain cards.")
if unmatched:
    print(f"Unmatched cards ({len(unmatched)}): {', '.join(unmatched[:10])}...")
