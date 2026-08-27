"""Dependency-free structural checks for the static portfolio."""

import json
from html.parser import HTMLParser
from pathlib import Path


class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.hrefs = []
        self.tags = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if "href" in attrs:
            self.hrefs.append(attrs["href"])


root = Path(__file__).parent
html = (root / "index.html").read_text(encoding="utf-8")
parser = AuditParser()
parser.feed(html)

assert "script" not in parser.tags
assert "form" not in parser.tags
assert "@" not in html
for href in parser.hrefs:
    if href.startswith("#"):
        assert href[1:] in parser.ids, f"missing fragment target: {href}"
    elif href.startswith("/"):
        assert (root / href.lstrip("/")).exists(), f"missing local asset: {href}"

required_repos = {
    "scientific-reasoning-audit-loops",
    "evidence-conflict-circuits",
    "component-edit-bound-audit",
    "dose-response-audit-lab",
    "proof-carrying-policy-evals",
    "lattice-state-consistency-lab",
    "sheaf-connectome-sanity-lab",
    "eml-star-epistemos",
}
assert all(name in html for name in required_repos)

config = json.loads((root / "vercel.json").read_text(encoding="utf-8"))
headers = {item["key"]: item["value"] for rule in config["headers"] for item in rule["headers"]}
assert "Content-Security-Policy" in headers
assert "frame-ancestors 'none'" in headers["Content-Security-Policy"]
assert headers["Permissions-Policy"] == "camera=(), microphone=(), geolocation=()"

print("static portfolio verified")
