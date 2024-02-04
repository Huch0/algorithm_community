#hash함수는 key * 2 % 2000000
#키가 0이상 1000000이하라고 해서 모든 키를 다 넣어도 포화율이 0.5까지 올라가도록 테이블 크기를 2000000으로 잡아봄
#충돌 시에 선형으로 다음 공간 찾음
class MyHashMap:
    def __init__(self):
        self.table = [(-1,-1) for _ in range(2000000)] # (value, realkey) tuple
        self.TABLE_SIZE = 2000000

    def put(self, key: int, value: int) -> None:
        hashedKey = key*2%2000000
        while self.table[hashedKey][1] != -1 and self.table[hashedKey][1] != key:
            hashedKey = hashedKey + 1
            if hashedKey == self.TABLE_SIZE:
                hashedKey = 0
        self.table[hashedKey] = (value, key)

    def get(self, key: int) -> int:
        hashedKey = key*2%2000000
        while self.table[hashedKey][1] != key:
            hashedKey = hashedKey + 1
            if hashedKey == self.TABLE_SIZE:
                hashedKey = 0
            if self.table[hashedKey][1] == -1:
                break
        return self.table[hashedKey][0]

    def remove(self, key: int) -> None:
        hashedKey = key*2%2000000
        while self.table[hashedKey][1] != key and self.table[hashedKey][1] != -1:
            hashedKey = hashedKey + 1
        self.table[hashedKey] = (-1,-1)