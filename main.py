import json
import os

def load_verses():
    if not os.path.exists('verses.json'):
        return []
    with open('verses.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def run_test():
    verses = load_verses()
    if not verses:
        print("등록된 성구가 없습니다.")
        return

    # 가장 최근 성구로 테스트
    target = verses[-1]
    print(f"\n--- 성구 암송 테스트 ({target['reference']}) ---")
    print("성구를 입력하세요:")
    
    user_input = input("> ").strip()
    
    if user_input == target['text'].strip():
        print("\n✅ 정답입니다! 잘 외우셨네요.")
    else:
        print("\n❌ 틀렸습니다.")
        print(f"원문: {target['text']}")
        print(f"입력: {user_input}")

if __name__ == "__main__":
    run_test()
