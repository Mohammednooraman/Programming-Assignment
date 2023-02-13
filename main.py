def maxProfit(jobs):
    jobs.sort(key=lambda x: x[1]) # sort the jobs by end time
    n = len(jobs)
    dp = [0 for i in range(n)] # array to store the maximum profit for each job
    dp[0] = jobs[0][2] # base case: the first job has a profit equal to its own profit
    for i in range(1, n):
        for j in range(i):
            if jobs[i][0] >= jobs[j][1]: # job i can be performed after job j
                dp[i] = max(dp[i], dp[j] + jobs[i][2])
        dp[i] = max(dp[i], dp[i-1]) # choose the maximum between including job i and not including job i
    return dp[n-1]

def main():
    n = int(input("Enter the number of Jobs: "))
    jobs = []
    print("Enter job start time, end time, and earnings:")
    for i in range(n):
        start_time = int(input().strip())
        end_time = int(input().strip())
        profit = int(input().strip())
        jobs.append((start_time, end_time, profit))
    remaining_tasks = n - len([job for job in jobs if job[2] == maxProfit(jobs)])
    remaining_earnings = sum([job[2] for job in jobs if job[2] != maxProfit(jobs)])
    print("The number of tasks and earnings available for others")
    print("Tasks:", remaining_tasks)
    print("Earnings:", remaining_earnings)

if __name__ == '__main__':
    main()
