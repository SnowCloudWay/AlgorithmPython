# dict : 키의 중복이 없는 맵, 정렬되지 않은 맵(해싱)
# 키 : 나라명, 밸류 : 수도
d = {"대한민국":"서울", "프랑스":"파일", "일본":"동경"}
d["중국"] = "베이징"
print(d)
print(len(d))
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))
d["일본"] = "도쿄"
print(d)
for k, v in d.items():
    print(k, "-", v)

# 검색(존재유무) : in 키워드(연산자)
print("한국" in d)    # 키 검색
print("대한민국" in d)
print("서울" in d.values())   # 밸류 검색

# 검색(키로 검색 => 밸류) : []
print(d["일본"])      # 인덱스 대신 키를 대입
# print(d["한국"])    # 없는 키로 검색하면 KeyError 발생

# 검색(키로 검색 => 밸류) : get메서드
print(d.get("프랑"))  # None을 반환
print(d.get("프랑", "존재하지 않는 나라입니다."))    # 두번째 인수 : None인 경우

# 삭제
del d["중국"]
print(d)
# del d["중국"]   # KeyError : 없는 키를 삭제

country = "일본"
if d.get(country) == None:
    print(country, "는 없습니다 => 삭제 실패")
else:
    del d[country]
    print(country, "삭제 성공")