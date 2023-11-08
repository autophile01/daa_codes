def job_scheduling_with_deadlines(jobs):
    # Sort the jobs in descending order of profits
    jobs.sort(key=lambda x: x[2], reverse=True)

    n = len(jobs)
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    schedule = [-1] * (max_deadline + 1)

    total_profit = 0

    for job in jobs:
        deadline, profit = job[1], job[2]

        for i in range(deadline, 0, -1):
            if schedule[i] == -1:
                schedule[i] = job[0]
                total_profit += profit
                break

    return total_profit, [job for job in schedule if job != -1]

# Example usage:
jobs = [(1, 2, 90), (2, 1, 60), (3, 2, 100), (4, 2, 20), (5, 3, 70)]
max_profit, schedule = job_scheduling_with_deadlines(jobs)
print("Maximum Profit:", max_profit)
print("Scheduled Jobs:", schedule)

In this code:

We sort the jobs list in descending order of profits.
We create a schedule list to track which job is scheduled at each time slot, initializing it with -1.
We iterate through the sorted jobs list and for each job, we iterate through the time slots from the job's deadline down to 1.
If a slot is available (i.e., schedule[i] is -1), we schedule the job, update the schedule list, and add the profit to the total profit.
Finally, we return the maximum profit and the scheduled jobs.

