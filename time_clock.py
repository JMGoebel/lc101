''' LC101 Time Clock Ex. 10.4 '''

def clock_in(worker_dict, worker_name, time_in):
    ''' takes the dictionary of workers, the name of the worker, and the clock
        in time as parameters. When the worker clocks in, enter and save their
        clock in time as the first element in the associated list value.'''
    worker_dict[worker_name][0] = time_in

def clock_out(worker_dict, worker_name, time_out):
    ''' takes the same parameters, but with a clock out time instead of clock
        in time. When the worker clocks out, enter and save their clock out time
        and calculate the hours worked for that day and store it as the third
        element in the list. '''
    worker_dict[worker_name][1] = time_out
    worker_dict[worker_name][2] = worker_dict[worker_name][1] - worker_dict[worker_name][0]

def main():
    ''' main entry point '''
    workers = {"George Spelvin": [0, 0, 0], "Jane Doe": [0, 0, 0], "John Smith": [0, 0, 0]}
    print(workers.get("George Spelvin"))   # should print [0,0,0]
    clock_in(workers, "George Spelvin", 8)
    clock_out(workers, "George Spelvin", 17)
    print(workers.get("George Spelvin"))   # should print [8, 17, 9]

if __name__ == "__main__":
    main()
