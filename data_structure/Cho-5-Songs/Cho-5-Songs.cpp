#include <iostream>
#include <list>

using namespace std;

struct Song {
    string title;
    char genre;
    int broadcastCount;
    double fileSize;
    int downloadCount;
};

bool compareRule(const Song &song1, const Song &song2) {
    if( song1.broadcastCount != song2.broadcastCount ){
        return song1.broadcastCount > song2.broadcastCount;
    }
    else if( song1.downloadCount != song2.downloadCount ){
        return song1.downloadCount > song2.downloadCount;
    }
    else if( song1.fileSize != song2.fileSize ){
        return song1.fileSize < song2.fileSize;
    }
    return false;
}

int main() {
    int songsSize, ranking;
    cin >> songsSize >> ranking;

    list<Song> songs;

    for( int i = 0; i < songsSize; ++i ){
        Song inputSong;
        cin >> inputSong.title >> inputSong.genre >> inputSong.broadcastCount >> inputSong.fileSize >> inputSong.downloadCount;
        songs.push_back(inputSong);
    }

    songs.sort(compareRule);

    list<Song>::iterator it;
    for( it=songs.begin(); it!=prev(songs.end()); ++it ){
        if( it->genre == next(it)->genre ){
            list<Song>::iterator baseIt = next(it);
            list<Song>::iterator goalIt = next(baseIt);
            while( goalIt != songs.end() && baseIt->genre == goalIt->genre ){
                ++goalIt;
            }
            if( goalIt != songs.end() ) songs.splice(baseIt, songs, goalIt);
        }
    }

    list<Song>::iterator outputIt = songs.begin();
    advance(outputIt, ranking - 1);
    cout << outputIt->title << endl;

    return 0;
}