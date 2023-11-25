#include <iostream>
#include <queue>
#include <deque>
using namespace std;

struct Guest {
    int arrivalTime;
    int id;
    int restTime;
};

int timer = 30;

struct compareReservation {
    bool operator()(const Guest& l, const Guest& r) {
        if( l.arrivalTime > r.arrivalTime ) return true; // rule : if arrivalTime is smaller, it is prior.
        else return false;
    }
};
struct compareRoom {
    bool operator()(const Guest& l, const Guest& r) {
        if( l.restTime < r.restTime ) return true; // first rule : If restTime is bigger, it is prior.
        else if( l.restTime == r.restTime ) {
            if( l.arrivalTime > r.arrivalTime ) return true; // second rule : if arrivalTime is smaller, it is prior.
            else return false;
        }
        else return false;
    }
};

priority_queue<Guest, deque<Guest>, compareReservation> reservation;
priority_queue<Guest, deque<Guest>, compareRoom> room;

void support() {
    while (!reservation.empty() || !room.empty()) { // end at reservation and room is empty.
        if(!reservation.empty() && reservation.top().arrivalTime > timer ) timer = reservation.top().arrivalTime; // if not guest in room, timer set to next guest arrival time.
        while (!reservation.empty() && reservation.top().arrivalTime <= timer) { // push guest from reservation to room.
            room.push(reservation.top());
            reservation.pop();
        }
        
        if( room.top().restTime <= 10 ) { // if restTime is smaller(or equal) than 10, print it's id and pop.
            cout << room.top().id << endl;
            timer += room.top().restTime;
            room.pop();
        }
        else { // if restTime is bigger than 10, spend half of restTime and push it to reservation again.
            int half = room.top().restTime / 2;
            timer += half;
            reservation.push({timer, room.top().id, room.top().restTime - half});
            room.pop();
        }
    }
}

int main() {
    int N; cin >> N;
    for (int i=0; i<N; i++) {
        int arrivalTime, id, restTime;
        cin >> arrivalTime >> id >> restTime;
        reservation.push({arrivalTime, id, restTime});
    }

    support();

    return 0;
}