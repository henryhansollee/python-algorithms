import sys
sys.stdin = open('input.txt', 'r')


def solution(new_id):
    answer = ''

    # 1단계
    step1_new_id = new_id.lower()

    # 2단계
    step2_new_id = ''
    for id2 in step1_new_id:
        # 알파벳 소문자
        if 97 <= ord(id2) <= 122:
            step2_new_id += id2
        # 숫자
        if id2.isnumeric():
            step2_new_id += id2
        # 빼기, 밑줄, 마침표
        if id2 in ['-', '_', '.']:
            step2_new_id += id2

    # 3단계
    step3_new_id = []
    for id3 in step2_new_id:
        if len(step3_new_id) > 0 and id3 == '.':
            if step3_new_id[-1] == '.':
                continue
        step3_new_id.append(id3)

    # 4단계
    if step3_new_id[0] == '.':
        step3_new_id.pop(0)
    elif step3_new_id[-1] == '.':
        step3_new_id.pop()

    # 5단계
    if not step3_new_id:
        step3_new_id.append('a')

    # 6단계
    step6_new_id = step3_new_id
    if len(step3_new_id) >= 16:
        step6_new_id = step3_new_id[:15]
        if step6_new_id[-1] == '.':
            step6_new_id.pop()

    # 7단계
    if len(step6_new_id) <= 2:
        while len(step6_new_id) != 3:
            step6_new_id.append(step6_new_id[-1])

    # 출력
    for id6 in step6_new_id:
        answer += id6

    return answer