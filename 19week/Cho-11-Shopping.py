### 문제 이해
# 1. 입력처리, shopper 클래스 구조 구현
# 2. 계산대 딕셔너리로 구현
# 3. 계산 알고리즘
# 4. Tie break
# 5. 최종 결과 리턴

from collections import defaultdict

class Shopper:
    def __init__(self, infomations=None) -> None:
        if infomations:
            self.ID = infomations[0]
            self.number_of_products = int(infomations[1])
        else:
            self.ID = None
            self.number_of_products = 999

class Solution:
    def Shopping(self, file_name):
        # 1. input processing & Shoppers list
        infile = open(file_name, 'r')
        first_line = infile.readline().split()
        N, K = int(first_line[0]), int(first_line[1])

        shoppers = [Shopper(line.split()) for line in infile]      
        infile.close()

        # 2. counter dictionary
        counter = defaultdict(Shopper)
        for i in range(K):
            counter[i]
        
        # 3. Counter Algorithms
        results = []

        while len(results) < N:
            # step 1: push shoppers into empty counter
            for i in counter:
                # empty counter and not empty shoppers
                if counter[i].ID == None and shoppers:
                    counter[i] = shoppers.pop(0)
            
            # step 2: calculate min & minus all counter
            min_product_shopper = min(counter, key=lambda x: counter[x].number_of_products if counter[x].number_of_products > 0 else float('inf'))
            min_product = counter[min_product_shopper].number_of_products
            
            for i in counter:
                counter[i].number_of_products -= min_product
            
            # step 3: exit finish shopper
            for i in counter:
                if counter[K-i-1].number_of_products == 0:
                    results.append(counter[K-i-1].ID)
                    counter[K-i-1] = Shopper()

        return results

### TEST CODE
if __name__ == "__main__":
    s = Solution()
    #print(s.Shopping("Cho-11-Test/01.inp"))
    for i in range(1, 10):
        input_file_name = "Cho-11-Test/0" + str(i) + ".inp"
        result_file_name = "Cho-11-Test/0" + str(i) + ".out"
        
        infile = open(result_file_name, "r")
        
        results = s.Shopping(input_file_name)

        outputs = []
        
        for line in infile:
            outputs.append(line.rstrip())

        infile.close()
        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")
    
    for i in range(10, 13):
        input_file_name = "Cho-11-Test/" + str(i) + ".inp"
        result_file_name = "Cho-11-Test/" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = s.Shopping(input_file_name)

        outputs = []
        
        for line in infile:
            outputs.append(line.rstrip())

        infile.close()
        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")