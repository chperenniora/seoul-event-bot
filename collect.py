import os, json, urllib.request, urllib.parse

CID = os.environ["NAVER_ID"]
CSEC = os.environ["NAVER_SECRET"]

KEYWORDS = [
    "성수 팝업", "청담 전시", "한남 갤러리", "평창동 갤러리",
    "프리즈 서울", "청담 오마카세", "청담동 핫플", "한남동 핫플",
    "압구정 로데오", "서울 청음바", "한남 LP바", "청담 화랑",
    "강남 VIP 파티", "멤버스클럽 서울", "연예인 맛집 청담",
]

def search(query):
    url = "https://openapi.naver.com/v1/search/blog.json?query=" + urllib.parse.quote(query) + "&display=10&sort=date"
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", CID)
    req.add_header("X-Naver-Client-Secret", CSEC)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read().decode())["items"]
    except Exception as e:
        print("오류:", query, e)
        return []

def clean(t):
    return t.replace("<b>", "").replace("</b>", "").replace("&quot;", '"').replace("&amp;", "&").replace("&lt;","<").replace("&gt;",">")

results = []
for kw in KEYWORDS:
    for item in search(kw):
        results.append({
            "keyword": kw,
            "title": clean(item.get("title","")),
            "desc": clean(item.get("description","")),
            "link": item.get("link",""),
            "date": item.get("postdate",""),
        })

seen, unique = set(), []
for r in results:
    if r["link"] not in seen:
        seen.add(r["link"])
        unique.append(r)

with open("events.json", "w", encoding="utf-8") as f:
    json.dump(unique, f, ensure_ascii=False, indent=2)

print(f"총 {len(unique)}건 저장 완료")
