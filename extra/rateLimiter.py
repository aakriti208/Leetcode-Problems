from collection import deque
import time

class RateLimiter:
    def __init__(self, max_requests: int, per_seconds: int):
        #  We first initialized the class with the max number of max_requests
        #  time window in per_seconds
        #  deque that stored the time stamps of the last made request
        self.max_requests = max_requests
        self.per_seconds = per_seconds
        self.time_stamps = deque()
        
    def rate_limited_request(self):
        # take the current timestamps
        # current_time = time.time() this returns the current time in seconds
        #  check if the length of the time_stamps in deque is less than the max number of requests made
        #  in that case, we keep on adding the current time to the deque
        #  an API request is made and the function returns immediately
        if len(self.time_stamps) < self.max_requests:
            self.time_stamps.append(current_time)
            self.api_call()
            return
        else:
            #  now if deque has already made 5 requests, it calculates how much time to wait before making another requests
            sleep_time = self.per_seconds - (current_time - self.time_stamps[0])
            if sleep_time > 0:
            # if the program needs to wait before making another request, we need to pause the execution of the program for that long
            # update the current time after sleeping
                time.sleep(sleep_time)
                current_time = time.time()
            
            self.time_stamps.popleft()
            self.time_stamps.append(current_time)
            self.api_call()
            
        
