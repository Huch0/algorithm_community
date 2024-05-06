
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    start = h1*3600+m1*60+s1
    end = h2*3600+m2*60+s2

    # The number of times the second hand crosses the minute hand
    # The second hand crosses the minute hand once every minute,
    # except when it is on top of the minute hand (hh:00:00).
    # There are 60 minutes in an hour, so the second hand crosses the minute hand 59 times.\

    # end/3600: hours, end/3600*59: the number of times the second hand crosses the minute hand
    answer += int(end/3600*59)
    # 3600/59: the time it takes for the second hand to cross the minute hand
    answer -= start//(3600/59)

    # The number of times the second hand crosses the hour hand
    # The hour hand moves 360 degrees in 12 hours (43200 seconds), so it moves at a rate of 360 / 43200 degrees per second.
    # The second hand moves 360 degrees in 60 seconds, so it moves at a rate of 360 / 60 degrees per second.
    # The difference in their rates is (360 / 60) - (360 / 43200), which simplifies to 719 / 120 degrees per second.
    # Therefore, the second hand takes 360 / (719 / 120) seconds to catch up to the hour hand once.
    answer += end//(360*120/719)
    answer -= start//(360*120/719)

    # The second hand crosses the hour hand and the minute hand at the same time
    if start <= 12*60*60 <= end:
        answer -= 1

    # The second hand is on top of the hour hand and the minute hand
    if start == 0 or start == 12*60*60:
        answer += 1

    return answer
