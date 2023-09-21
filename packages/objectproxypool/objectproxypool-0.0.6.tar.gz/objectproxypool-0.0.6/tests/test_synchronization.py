from objectproxypool import ProxyPool
import time
import threading
import numpy as np
import os

class catchtime:
    
    def __init__(self, verbose=False) -> None:
        self.verbose = verbose
    
    def __enter__(self):
        self.time = time.perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.time = time.perf_counter() - self.time
        self.readout = f"Time: {self.time:.3f} seconds"
        if self.verbose:
            print(self)

    def __str__(self):
        return self.readout


class TestObject:
    def test_method(self, argument):
        threadId = threading.get_native_id()
        pid = os.getpid()
        sleeptime = argument % 3
        if not argument: 
            sleeptime += np.random.rand() > 0.5
        time.sleep(sleeptime)
        return threadId, pid, argument, sleeptime

def test_synchronization():
    
    for argument in (0, range(os.cpu_count())):
        map_args = hasattr(argument, "__iter__")
        for separateProcesses in True, False:
            with ProxyPool(TestObject, separateProcesses=separateProcesses) as pool:
                results = np.array(pool.test_method(argument, map_args=map_args, synchronize_workers=True))
            assert np.unique(results[:,0]).size == os.cpu_count()
    
    return True


def time_me(separateProcesses, synchronize):
    with ProxyPool(TestObject, separateProcesses=separateProcesses) as pool:
        pool.test_method(1e-5, synchronize_workers=synchronize)

def test_speed():
    
    for synchronize in False, True:
        for separateProcesses in False, True:
            with catchtime() as timer:
                time_me(separateProcesses, synchronize)
                
            print("sync. = {}, sep. proc. = {}".format(synchronize, separateProcesses), timer)
        
if __name__ == "__main__":
    test_speed()
    print(test_synchronization())