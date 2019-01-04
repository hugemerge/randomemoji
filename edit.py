import json

# load json
with open('emoji-json/emojis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
emojilist = data["emojis"]
## show number of emojis
print("before: {}".format(len(emojilist)))

# edit
## remove no "shortname"
emojilist = [i for i in emojilist if i["shortname"] != ""]

## remove nation flag
emojilist = [i for i in emojilist if not i["shortname"][:6] in (":flag_", ":flag-")]

# write json
## show
print("after: {}".format(len(emojilist)))

with open("emojis_picked.json", "w", encoding="utf-8") as out:
    data["emojis"] = emojilist
    json.dump(data, out, indent=2, ensure_ascii=False, separators=(',', ': '))