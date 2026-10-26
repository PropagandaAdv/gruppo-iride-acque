import json, random
random.seed(64)
BASE = "https://gruppoirideacque.propagandaadv.com"
UP = BASE + "/wp-content/uploads/2026/10/"
t = json.load(open("backup_live/p64_buildcopy.json", encoding="utf8"))


def nid():
    return "%07x" % random.randrange(0x1000000, 0xfffffff)


LOGOS = [
    (382, "logo-iride-acque-gruppo.webp", "Logo Iride Acque"),
    (383, "logo-biemme-engineering-gruppo.webp", "Logo BIEMME Engineering"),
    (384, "logo-bieffe-costruzioni-gruppo.webp", "Logo BIEFFE Costruzioni"),
]
boxes = []


def walk(n):
    if isinstance(n, list):
        for x in n:
            walk(x)
        return
    s = n.get("settings", {}) or {}
    if n.get("elType") == "container" and isinstance(s.get("background_image"), dict) and "min_height" in s:
        boxes.append(n)
    for c in n.get("elements", []) or []:
        walk(c)


walk(t)
assert len(boxes) == 3, len(boxes)
for box, (mid, fn, alt) in zip(boxes, LOGOS):
    s = box["settings"]
    for k in ("background_image", "background_position", "background_size"):
        s.pop(k, None)
    s["background_background"] = "classic"
    s["background_color"] = "#00243C"
    s["flex_align_items"] = "center"
    s["flex_justify_content"] = "center"
    box["elements"] = [{
        "id": nid(), "elType": "widget", "widgetType": "image", "elements": [],
        "settings": {
            "image": {"url": UP + fn, "id": mid, "alt": alt},
            "image_size": "full",
            "width": {"unit": "px", "size": 340}, "width_mobile": {"unit": "px", "size": 240},
            "align": "center", "_css_classes": "soc-logo",
        },
    }]

json.dump(t, open("home/p64_new.json", "w", encoding="utf8"), ensure_ascii=False, separators=(",", ":"))
s = json.dumps(t, ensure_ascii=False, separators=(",", ":"))
print(len(s))
open("home/p64_new.min.json", "w", encoding="utf8").write(s)
