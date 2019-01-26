"""Implementing threading in for-loops with limited amount of Threads"""

from multiprocessing.pool import ThreadPool as Pool

pool = Pool(5) # Maximum number of simultaneous Threads

lst = range(1, 10001) # Replace with actual list to iterate

def worker(item, idx, length): # With progress display
    """Worker function, which gets executed by Thread
    item = one item of the list
    idx = Index for calcualting progress
    length = total length of list for calculating progress"""
    
    percentage = (idx + 1) / length * 100
    print(f"Progress: {percentage:.2f}%")

    # Do something with item
    print(item)

"""
def worker(item): # Without progress display
    # Do something with item
    print(item)
"""

list_length = len(lst)

for idx, item in enumerate(lst):
    pool.apply_async(worker, (item, idx, list_length)) # Adding item to pool and starting Threads

pool.close()
pool.join()
