#!/usr/bin/env python3
"""
쇼츠 훅 즉시 생성기 — 댓글 대응 자동화
사용법: python generate_hooks.py 카페
       python generate_hooks.py --list
"""
import json
import sys
import os

DATA = os.path.join(os.path.dirname(__file__), "data", "hooks_100.json")


def load():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)


def main():
    hooks = load()

    if len(sys.argv) < 2 or sys.argv[1] in ("--list", "-l"):
        inds = sorted({h["업종"] for h in hooks})
        print(f"등록 업종 {len(inds)}개 (총 {len(hooks)}개 훅):")
        for i in inds:
            n = sum(1 for h in hooks if h["업종"] == i)
            print(f"  {i} ({n}개)")
        print("\n사용법: python generate_hooks.py 카페")
        return

    target = sys.argv[1].strip()
    picked = [h for h in hooks if h["업종"] == target]

    if not picked:
        # 부분 일치 시도
        picked = [h for h in hooks if target in h["업종"]]
        if not picked:
            print(f"'{target}' 업종 없음. --list 로 확인하세요.")
            return
        target = picked[0]["업종"]

    print(f"=== [{target}] 첫 3초 훅 {len(picked)}개 ===\n")
    for h in picked:
        print(f"{h['no']:3d}. [{h['훅유형']}]")
        print(f"     {h['훅']}")
        print()
    print("--- 복사해서 댓글로 바로 답변 가능 ---")


if __name__ == "__main__":
    main()
