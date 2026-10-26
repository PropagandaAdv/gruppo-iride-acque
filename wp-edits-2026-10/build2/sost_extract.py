"""Estrae da una pagina sostelia.it (HTML scaricato) la sequenza di blocchi di testo: h1-h6, p, li, button/a.
Uso: python -I sost_extract.py <file.html>   -> stampa JSON [(tag, testo, classi_padre)]"""
import sys, json, re
from html.parser import HTMLParser

SKIP = {"script", "style", "noscript", "svg", "head", "template", "iframe"}
BLOCK = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "a", "button", "span", "div", "td", "th"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.out = []
        self.cur = None  # (tag, [texts], href)
        self.stack = []
        self.sect = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in SKIP:
            self.skip += 1
            return
        if self.skip:
            return
        if tag in ("header", "footer", "nav"):
            self.out.append(("@" + tag, "", ""))
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "button"):
            self.flush()
            self.cur = [tag, [], a.get("href", ""), a.get("class", "")]
        elif tag == "a":
            if self.cur is None:
                self.cur = ["a", [], a.get("href", ""), a.get("class", "")]
        elif tag == "br" and self.cur:
            self.cur[1].append("\n")
        elif tag == "img":
            self.flush()
            self.out.append(("img", a.get("src", "") or a.get("data-src", ""), a.get("alt", "")))
        if a.get("id"):
            self.out.append(("@id", a["id"], ""))

    def handle_endtag(self, tag):
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if self.cur and tag == self.cur[0]:
            self.flush()
        if tag in ("header", "footer", "nav"):
            self.flush()
            self.out.append(("@/" + tag, "", ""))

    def handle_data(self, d):
        if self.skip:
            return
        if self.cur is not None:
            self.cur[1].append(d)

    def flush(self):
        if self.cur:
            t = re.sub(r"[ \t\r\f\v]+", " ", "".join(self.cur[1])).strip()
            t = re.sub(r" ?\n ?", "\n", t)
            if t:
                self.out.append((self.cur[0], t, self.cur[2]))
        self.cur = None


if __name__ == "__main__":
    p = P()
    p.feed(open(sys.argv[1], encoding="utf-8", errors="replace").read())
    p.flush()
    json.dump(p.out, sys.stdout, ensure_ascii=False, indent=0)
