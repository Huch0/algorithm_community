search_lines=int(input())
search=input()
for i in range(search_lines-1):
    search+=input() 
    
searchee_lines=int(input())
searchee=input()
for i in range(searchee_lines-1):
    searchee+=input()
    
def RK(q):
    global searchee, search
   # Initialize the hash values for characters from 'A' to 'Z'
    hash_values = {chr(i): (i - ord('A')) for i in range(ord('A'), ord('Z') + 1)}
    d=len(search)
    
    # Compute the hash value of the pattern
    pattern_hash = 0
    for char in search:
        pattern_hash = (pattern_hash * d + hash_values[char]) % q

    # Iterate over the text with a sliding window
    m = len(search)
    n = len(searchee)
    text_hash = 0
    for i in range(m):
        text_hash = (text_hash * d + hash_values[searchee[i]]) % q
    count=0
    # Slide the window and check for matches
    for i in range(n - m + 1):
        count+=1
        if text_hash == pattern_hash:
            if searchee[i:i + m] == search:               
                count+=d
                break
        if i < n - m:
            # Update the hash value for the next window
            text_hash = (d * (text_hash - hash_values[searchee[i]] * (d**(m - 1)%q)) + hash_values[searchee[i + m]]) % q
            
    return count

def compute_partial_match_table(search):
    count=1
    table = [0] * len(search)  # Initialize the partial match table with zeros
    j = 0  # Pointer for the table
    for i in range(1, len(search)):
        while j > 0 and search[i] != search[j]:
            j = table[j - 1]  # Move j to the position of the previous match
        if search[i] == search[j]:
            j += 1
        table[i] = j
        count+=1
    #print("hashing count",count)
    return table,count

def kmp_search():
    global searchee, search
   
    partial_match_table,count = compute_partial_match_table(search)  

    j = 0
    i=0
    while i < len(searchee): 
        count += 1
        if searchee[i] == search[j]:
            j += 1
            i += 1
            if j == len(search):
                count-=len(search)
                break
        else:           
            if j != 0:
                j = partial_match_table[j - 1]
            else:
                i += 1
   
    return count

def bad_character_rule():
    global search
  
    bad_char_shift = {char: -1 for char in range(256)}
    for i, char in enumerate(search):
        bad_char_shift[ord(char)] = i
    return bad_char_shift

def boyer_moore_search():
    global searchee, search
    
    count=0
    m = len(search)
    n = len(searchee)
    bad_char_shift = bad_character_rule()

    shift = 0
    while(shift <= n - m):
        j = m - 1

        while j >= 0 and search[j] == searchee[shift + j]:
            j -= 1
            count+=1
            
        if j >= 0:
            count += 1
        
        if j < 0:
            break      
        else:
            shift_char = ord(searchee[shift + j]) if ord(searchee[shift + j]) in bad_char_shift else -1
            shift += max(1, j - bad_char_shift.get(shift_char, m))
            
       
    return count       
        

a = RK(101)  
b = kmp_search()  
c = boyer_moore_search()  
#print(a)
#print(b)
#print(c)

if a == b and b == c:
    algorithms = [("0", 0), ("0", 0), ("0", 0)]
else:
    if a == b:
        algorithms = [("0", a), ("0", b), ("BM", c)]
    elif a == c:
        algorithms = [("0", a), ("KMP", b), ("0", c)]
    elif b == c:
        algorithms = [("RK", a), ("0", b), ("0", c)]
    else:
        algorithms = [("RK", a), ("KMP", b), ("BM", c)]

sorted_algorithms = sorted(algorithms, key=lambda x: x[1], reverse=False)

for alg_name, _ in sorted_algorithms:
    print(alg_name, end=" ")

    