import os, json, urllib.request, urllib.parse

CID = os.environ["NAVER_ID"]
CSEC = os.environ["NAVER_SECRET"]

# ===== 검색 키워드 목록 =====
KEYWORDS = [
    "청담 하이엔드 라운지 대관",
    "한남동 소셜 살롱 멤버십",
    "영리치 프라이빗 소셜 클럽",
    "스피크이지 바 서울",
    "압구정 로데오 시크릿 바",
    "청담 청음바",
    "한남 청음바",
    "성수 청음바",
    "용산 청음바",
    "강남 청음바",
    "압구정 청음바",
    "평창동 청음바",
    "성북동 청음바",
    "한남 LP바",
    "트리마제 펜트하우스 파티",
    "나인원 한남 입주민 라운지",
    "에테르노 청담 입주민 밋업",
    "더펜트하우스 청담 스카이라운지",
    "아크로서울포레스트 네트워킹",
    "한남 더힐 커뮤니티 행사",
    "시그니엘 레지던스 리셉션",
    "UN빌리지 프라이빗 다이닝",
    "반얀트리 클럽 카바나",
    "신라호텔 멤버십 네트워킹",
    "포시즌스 서울 클럽 라운지",
    "조선 팰리스 소셜 디너",
    "요트 클럽 선상 파티",
    "갤러리아 PSR 화이트",
    "신세계 트리니티 초청",
    "현대 쟈스민 블랙",
    "롯데 레니니스 VVIP",
    "백화점 VVIP 프라이빗 클래스",
    "피아제 하이주얼리 트렁크쇼",
    "로로피아나 오더메이드",
    "까르띠에 메종 청담",
    "불가리 컬렉션 프리뷰",
    "하이주얼리 트렁크 쇼",
    "마이바흐 오너스 모임",
    "슈퍼카 오너스 클럽 갈라",
    "청담 전시",
    "한남 갤러리",
    "평창동 갤러리",
    "프리즈 서울",
    "청담 화랑",
    "아트 옥션 VIP 프리뷰",
    "갤러리스트 네트워킹 살롱",
    "청담 오마카세",
    "오마카세 프라이빗 대관",
    "프라이빗 와인 테이스팅",
    "니치 향수 론칭",
    "성수 팝업",
    "성수동 복합문화공간 대관 파티",
    "청담동 핫플",
    "한남동 핫플",
    "하이엔드 오디오 청음회",
    "패션위크 애프터 파티",
    "엔터테인먼트 프라이빗 쇼케이스",
    "모델 에이전시 애프터파티",
    "하이소사이어티 자선 갈라",
    "연예인 맛집 청담",
]


def search(query):
    url = ("https://openapi.naver.com/v1/search/blog.json?query="
           + urllib.parse.quote(query) + "&display=20&sort=date")
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
    return (t.replace("<b>", "").replace("</b>", "")
             .replace("&quot;", '"').replace("&amp;", "&")
             .replace("&lt;", "<").replace("&gt;", ">"))


results = []
for kw in KEYWORDS:
    for item in search(kw):
        results.append({
            "keyword": kw,
            "title": clean(item.get("title", "")),
            "desc": clean(item.get("description", "")),
            "link": item.get("link", ""),
            "date": item.get("postdate", ""),
        })

seen, unique = set(), []
for r in results:
    if r["link"] not in seen:
        seen.add(r["link"])
        unique.append(r)

with open("events.json", "w", encoding="utf-8") as f:
    json.dump(unique, f, ensure_ascii=False, indent=2)

print(f"총 {len(unique)}건 저장 완료 (키워드 {len(KEYWORDS)}개)")
