from multiprocessing import Pool
import time


def read_info(name):
    all_data = []
    file = open(name, 'r')
    while True:
        stroke = file.readline()
        if not stroke:
            break
        all_data.append(stroke)
    file.close()



filenames = [f'./file {number}.txt' for number in range(1, 5)]
"""
time_start = time.time()
for filename in filenames:
    read_info(filename)
time_ended = time.time()
delta_time = time_ended - time_start
print(f"{delta_time} (линейный)")
"""
if __name__ == '__main__':
    multproc_time_start = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multproc_time_ended = time.time()
    multiproc_delta_time = multproc_time_ended - multproc_time_start
    print(f"{multiproc_delta_time} (многопроцессный)")
