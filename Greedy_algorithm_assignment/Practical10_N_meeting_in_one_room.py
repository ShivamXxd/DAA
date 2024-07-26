def max_meetings(start_times, end_times):
    meetings = list(zip(start_times, end_times, range(len(start_times))))

    meetings.sort(key=lambda x: x[1])

    selected_meetings = []

    selected_meetings.append(meetings[0][2])
    time_limit = meetings[0][1]

    for i in range(1, len(meetings)):
        if meetings[i][0] > time_limit:
            selected_meetings.append(meetings[i][2])
            time_limit = meetings[i][1]

    return [i + 1 for i in selected_meetings]

start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]

selected_meetings = max_meetings(start_times, end_times)
print("Selected meeting positions:", selected_meetings)