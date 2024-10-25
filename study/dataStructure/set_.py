# set : 키(중복 허용 X)만 있는 맵, 해싱
st = {20, 30, 10, 20}
st.add(30)
print(st)

# 빠른 검색 : 리스트에 in을 사용하면 0(n), 셋을 사용하면 0(1)
print(20 in st)
print(25 in st)
st.remove(20)
print(st)
# 검색 후, 존재하는 경우에만 삭제(remove)하는 것이 안전
# 대안 : discard 메서드