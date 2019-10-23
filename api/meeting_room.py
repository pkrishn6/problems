def minMeetingRooms(schedule):
    if not schedule:
        return 0

    i = 0
    j = 1
    count = 1
    window_end = schedule[i][1]
    while(j < len(schedule)):
        s_i = schedule[i][0]
        e_i = schedule[i][1]
        s_j = schedule[j][0]
        e_j = schedule[j][1]

        if s_j < window_end:
            if e_i > e_j:
                window_end = e_j
                i = j
            count += 1
            j += 1
        else:
            window_end = schedule[j - 1][1]
            i = j
            j += 1

    return count



if __name__ == "__main__":
    schedule = [[1,30],[2,100],[9,36],[35,40]]
    print(minMeetingRooms(schedule))

