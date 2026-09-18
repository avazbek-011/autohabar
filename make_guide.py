# -*- coding: utf-8 -*-
"""QOLLANMA.md dan ish stoliga chiroyli HTML qo'llanma yasaydi.

Ishlatish:
    python make_guide.py
"""
import io
import os
import re

from markdown_it import MarkdownIt

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "QOLLANMA.md")
LOGO = os.path.join(BASE, "static", "img", "logo.svg")
OUT = os.path.join(os.path.expanduser("~"), "Desktop", "AutoXabar-QOLLANMA.html")

CSS = """
:root{--p-900:#1E0526;--g-200:#FAE9B8;--g-300:#F4D477;--g-400:#E8BE3A;--g-500:#DCAB1E;
  --ink:#F7F1FB;--ink-2:#D9C7E6;--muted:#A98FBC;--line:rgba(255,255,255,.1);
  --surface:rgba(255,255,255,.045);--gold-line:rgba(220,171,30,.32)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Manrope',-apple-system,Segoe UI,Roboto,sans-serif;background:var(--p-900);
  color:var(--ink);line-height:1.7;font-size:16px;-webkit-font-smoothing:antialiased}
body::before{content:'';position:fixed;inset:0;z-index:-1;background:
  radial-gradient(900px 620px at 12% -8%,rgba(107,39,133,.5),transparent 62%),
  radial-gradient(820px 560px at 96% 4%,rgba(176,127,9,.1),transparent 60%),var(--p-900)}
.wrap{max-width:900px;margin:0 auto;padding:0 22px 90px}
.hero{text-align:center;padding:56px 0 40px;border-bottom:1px solid var(--line);margin-bottom:40px}
.hero svg{width:88px;height:88px;margin:0 auto 20px;display:block;
  filter:drop-shadow(0 14px 40px rgba(220,171,30,.3))}
.hero h1{font-size:2.3rem;font-weight:800;letter-spacing:-.03em;margin-bottom:10px;
  background:linear-gradient(102deg,#FBEAB4,var(--g-400) 45%,var(--g-500));
  -webkit-background-clip:text;background-clip:text;color:transparent}
.hero p{color:var(--muted)}
h2{font-size:1.6rem;font-weight:800;margin:52px 0 18px;padding-bottom:12px;
  border-bottom:1px solid var(--line);color:var(--g-300)}
h3{font-size:1.18rem;font-weight:800;margin:32px 0 12px}
h4{font-size:1rem;font-weight:800;margin:22px 0 8px;color:var(--ink-2)}
p{margin:12px 0;color:var(--ink-2)}
a{color:var(--g-300);text-decoration:none;border-bottom:1px solid rgba(244,212,119,.3)}
strong{color:var(--ink)}
hr{border:0;border-top:1px solid var(--line);margin:40px 0}
ul,ol{margin:12px 0 12px 24px;color:var(--ink-2)}
li{margin:7px 0}
li::marker{color:var(--g-500)}
code{font-family:ui-monospace,Consolas,monospace;font-size:.88em;background:rgba(0,0,0,.35);
  border:1px solid var(--line);padding:2px 7px;border-radius:6px;color:var(--g-200)}
pre{background:rgba(0,0,0,.4);border:1px solid var(--line);border-left:3px solid var(--g-500);
  border-radius:12px;padding:16px 18px;overflow-x:auto;margin:16px 0}
pre code{background:none;border:0;padding:0;color:var(--ink-2)}
table{width:100%;border-collapse:collapse;margin:18px 0;font-size:.93rem;border:1px solid var(--line)}
th{background:rgba(0,0,0,.32);color:var(--muted);text-align:left;padding:12px 15px;font-size:.76rem;
  text-transform:uppercase;letter-spacing:.09em;border-bottom:1px solid var(--line)}
td{padding:12px 15px;border-bottom:1px solid rgba(255,255,255,.055);color:var(--ink-2)}
blockquote{margin:18px 0;padding:14px 18px;border-radius:12px;background:rgba(220,171,30,.08);
  border:1px solid var(--gold-line);border-left:3px solid var(--g-500)}
blockquote p{margin:6px 0;color:var(--g-200)}
@media print{body{background:#fff;color:#000}body::before{display:none}
  .hero h1{color:#000;-webkit-text-fill-color:#000}h2{color:#000}p,td,li{color:#222}
  pre,code,table,blockquote{background:#f6f6f6;color:#000}}
@media (max-width:620px){.hero h1{font-size:1.7rem}h2{font-size:1.35rem}
  table{display:block;overflow-x:auto}}
"""


def main():
    md = MarkdownIt("commonmark", {"html": True, "linkify": True})
    md.enable("table")
    body = md.render(io.open(SRC, encoding="utf-8").read())
    body = re.sub(r"^<h1>.*?</h1>\s*", "", body, count=1, flags=re.S)
    body = re.sub(r"^<blockquote>.*?</blockquote>\s*", "", body, count=1, flags=re.S)
    logo = io.open(LOGO, encoding="utf-8").read()

    html = (
        '<!DOCTYPE html><html lang="uz"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        "<title>AutoXabar — to‘liq qo‘llanma</title>"
        '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800'
        '&display=swap" rel="stylesheet"><style>' + CSS + "</style></head><body>"
        '<div class="wrap"><div class="hero">' + logo +
        "<h1>AutoXabar — to‘liq qo‘llanma</h1>"
        "<p>VIPADSUZ · Telegram guruhlariga avtomatik xabar tarqatish</p></div>"
        + body + "</div></body></html>"
    )
    io.open(OUT, "w", encoding="utf-8").write(html)
    print("Yaratildi:", OUT)


if __name__ == "__main__":
    main()
