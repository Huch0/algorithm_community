class Song:
    def __init__(self, list) -> None:
        self.title = list[0]
        self.genre = list[1]
        self.broad = int(list[2])
        self.size = float(list[3])
        self.download = int(list[4])
    
class Solution:
    def SongRank(self, file_name):
        # 입력 처리
        infile = open(file_name, "r")
        k = int(infile.readline().split()[1])        

        song_list = []
        for line in infile:
            song_list.append(Song(line.split()))

        # 리스트 정렬
        song_list.sort(key =lambda song : (song.broad, song.download, -song.size), reverse= True)

        # 장르 연속 방지
        # 일단 O(n^2) 으로 구현하되, 스택을 쓰면 나아질 거라 추측함
        def find_different_genre(i):
            input_genre = song_list[i].genre
            j = i+1
            for _ in range(i+1, len(song_list)):
                if song_list[j].genre != input_genre:
                    return j
                j += 1

            return -1

        for i in range(len(song_list) - 1):
            if song_list[i].genre == song_list[i+1].genre:
                index = find_different_genre(i+1)
                if index < 0:
                    break
                song_list[i+1], song_list[index] = song_list[index], song_list[i+1]

        # K번째 값 출력
        return song_list[k-1].title
    
### TEST CODE
if __name__ == "__main__":
    s = Solution()
    for i in range(1, 10):
        input_file_name = "Cho-5-Test/0" + str(i) + ".inp"
        result_file_name = "Cho-5-Test/0" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        result = infile.readline().rstrip()

        infile.close()

        if result == s.SongRank(input_file_name):
            print("CORRECT")
        else:
            print("INCORRECT")
    
    for i in range(10, 13):
        input_file_name = "Cho-5-Test/" + str(i) + ".inp"
        result_file_name = "Cho-5-Test/" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        result = infile.readline().rstrip()

        infile.close()

        if result == s.SongRank(input_file_name):
            print("CORRECT")
        else:
            print("INCORRECT")