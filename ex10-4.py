''' Workers Time Clock '''
workers = {"Jason":[]}

def clock_in(worker_dict, worker, time):
    ''' asdf '''
    if worker_dict[worker]:
        print("Already Timed In")
        return
    worker_dict[worker].append(time)

clock_in(workers, "Jason", "08:00")
clock_in(workers, "Jason", "08:10")
print(workers)