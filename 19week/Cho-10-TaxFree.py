### 문제 이해
# 1. 입력 처리 및 상품 가격 순대로 정렬
# 2. 블랙리스트
# 3. 가격을 맞출 수 있는가 검증 함수 구현
# 4. 재귀 호출
# 5. 결과 처리

class Solution:
    def TaxFree(self, file_name):
        # 1. input processing & prices sort
        infile = open(file_name, 'r')
        K = int(infile.readline().split()[1])
        
        prices = [int(line.rstrip()) for line in infile]
        prices.sort()
        infile.close()

        # 2. verifying coupon can be exhausted function
        blacklist = []
        length_unique_prices = len(set(prices))
        set_of_exhausing = []

        def can_be_exhausted(products, K):
            if len(products) == 0 or K < products[0]:
                return False
            if K in products:
                set_of_exhausing.append(K)
                return True
            # 재귀 호출, 그러나 알고리즘 수정 필요
            else:
                for i in range(len(products)-1, -1, -1):
                    if can_be_exhausted(products[0:i]+products[i+1:-1], K - products[i]):
                        set_of_exhausing.append(products[i])
                        return True
            
        # 3. implements function
        def slice_prices():
            for price in prices:
                if price in blacklist:
                    prices.remove(price)

        while True:
            if can_be_exhausted(prices, K):
                break
            if len(blacklist) == length_unique_prices:
                return [0]
            K -= prices[-1]
            blacklist.append(prices[-1])
            slice_prices()

        # 4. max_price finding
        return sorted(set_of_exhausing)
        
        
### TEST CODE
if __name__ == "__main__":
    s = Solution()
    #print(s.TaxFree("Cho-10-Test/02.inp"))
    for i in range(1, 10):
        if i == 2:
            continue
        input_file_name = "Cho-10-Test/0" + str(i) + ".inp"
        result_file_name = "Cho-10-Test/0" + str(i) + ".out"
        
        infile = open(result_file_name, "r")
        
        results = s.TaxFree(input_file_name)

        outputs = []
        
        for line in infile:
            outputs.append(int(line.rstrip()))

        infile.close()
        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")
    
    for i in range(10, 13):
        if i == 11:
            continue
        input_file_name = "Cho-10-Test/" + str(i) + ".inp"
        result_file_name = "Cho-10-Test/" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = s.TaxFree(input_file_name)

        outputs = []
        
        for line in infile:
            outputs.append(int(line.rstrip()))

        infile.close()
        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")