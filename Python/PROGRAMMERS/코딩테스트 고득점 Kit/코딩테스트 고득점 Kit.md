# 코딩테스트 고득점 Kit

## 1. 해시

### 1-1. 완주하지 못한 선수

```python
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    answer = participant[-1]
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer
```



### 1-2. 전화번호 목록

```python
def solution(phone_book):
    answer = True
    n = len(phone_book)
    phone_book.sort()
    for i in range(n-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
    return answer
```



### 1-3. 위장

```python

```



### 1-4. 베스트앨범

```python

```

