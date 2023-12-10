class HashMap:
    def __init__(self, n):
        self.size = n
        self.data1 = [-1] * n
        self.data2 = [-1] * n

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        return (key // self.size) % self.size

    def lookup(self, key):
        hash_value1 = self.hash1(key)
        if self.data1[hash_value1] == key:
            print(f"1번 테이블에서 {key}을(를) 찾았습니다.")
            return hash_value1

        hash_value2 = self.hash2(key)
        if self.data2[hash_value2] == key:
            print(f"2번 테이블에서 {key}을(를) 찾았습니다.")
            return hash_value2

        return None

    def erase(self, key):
        position = self.lookup(key)
        if position is not None:
            self.data2[position] = -1
            print(f"{key}에 해당하는 원소를 삭제했습니다.")
        else:
            print(f"{key}키를 찾지 못했습니다.")

    def insert(self, key):
        self.insert_impl(key, 0, 1)

    def insert_impl(self, key, cnt, table):
        if cnt >= self.size:
            print(f"{key} 삽입 시 사이클 발생! 재해싱이 필요합니다!")
            return

        if table == 1:
            hash_value = self.hash1(key)
            if self.data1[hash_value] == -1:
                print(f"{table}번 테이블에 {key} 삽입")
                self.data1[hash_value] = key
            else:
                old = self.data1[hash_value]
                self.data1[hash_value] = key
                print(f"{table}번 테이블에 {key} 삽입: 기존의 {old} 이동 -> ", end="")
                self.insert_impl(old, cnt + 1, 2)
        else:
            hash_value = self.hash2(key)
            if self.data2[hash_value] == -1:
                print(f"{table}번 테이블에 {key} 삽입")
                self.data2[hash_value] = key
            else:
                old = self.data2[hash_value]
                self.data2[hash_value] = key
                print(f"{table}번 테이블에 {key} 삽입: 기존의 {old} 이동 -> ", end="")
                self.insert_impl(old, cnt + 1, 1)

    def print_table(self):
        print("Index:", end=" ")
        for i in range(self.size):
            print(i, end="\t")
        print()

        print("Data1:", end=" ")
        for i in self.data1:
            print(i, end="\t")
        print()

        print("Data2:", end=" ")
        for i in self.data2:
            print(i, end="\t")
        print()


if __name__ == "__main__":
    hashmap = HashMap(7)
    hashmap.print_table()
    print()

    hashmap.insert(10)
    hashmap.insert(20)
    hashmap.insert(30)
    print()

    hashmap.insert(104)
    hashmap.insert(2)
    hashmap.insert(70)
    hashmap.insert(9)
    hashmap.insert(90)
    hashmap.insert(2)
    hashmap.insert(7)
    print()

    hashmap.print_table()
    print()

    hashmap.insert(14)  # 사이클 발생!
