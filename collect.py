import json

data = [
    {"title": "시스템 정상 작동 테스트", "place": "확인 완료", "date": "오늘"}
]

with open('events.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("파일 생성 성공")
