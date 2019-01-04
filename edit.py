import json

# load json
with open('emoji-json/emojis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
emojilsit = data["emojis"]
## show number of emojis
print("before: {}".format(len(emojilsit)))

# edit

# write json
## show
print("after: {}".format(len(emojilsit)))

with open("emojis_picked.json", "w", encoding="utf-8") as out:
    data["emojis"] = emojilsit
    json.dump(data, out, indent=2, ensure_ascii=False, separators=(',', ': '))