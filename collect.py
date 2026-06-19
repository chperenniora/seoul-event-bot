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
