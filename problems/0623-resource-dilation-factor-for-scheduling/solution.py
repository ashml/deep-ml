def compute_dilation_factor(tasks: list, capacity: int) -> dict:
    n = len(tasks)
    cp = [None] * n

    def calc(i):
        if cp[i] is not None:
            return cp[i]
        cp[i] = tasks[i]["duration"] + max(
            (calc(j) for j in tasks[i]["dependencies"]), default=0
        )
        return cp[i]

    critical = max((calc(i) for i in range(n)), default=0)
    work = sum(t["duration"] * t["resources"] for t in tasks)
    lower = max(critical, work / capacity)

    start = [None] * n
    done = set()
    running = []
    time = 0.0

    while len(done) < n:
        for f, i in running[:]:
            if f <= time:
                done.add(i)
                running.remove((f, i))

        used = sum(tasks[i]["resources"] for _, i in running)

        for i, t in enumerate(tasks):
            if start[i] is None and all(d in done for d in t["dependencies"]):
                if used + t["resources"] <= capacity:
                    start[i] = time
                    used += t["resources"]
                    running.append((time + t["duration"], i))

        if running:
            time = min(f for f, _ in running)

    makespan = max(start[i] + tasks[i]["duration"] for i in range(n))

    return {
        "dilation_factor": float(round(makespan / lower, 4)),
        "actual_makespan": float(round(makespan, 4)),
        "lower_bound": float(round(lower, 4)),
        "start_times": [float(round(x, 4)) for x in start]
    }