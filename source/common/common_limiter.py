"""
Limiter code to reduce/rate calls to metadata proviers

# Carlos A. Ibarra
# http://stackoverflow.com/questions/667508/whats-a-good-rate-limiting-algorithm/667706#667706
"""

import time

# calls per second
API_LIMIT = {
    'poe_api': (1, 1),
    'Z': (None, None),  # catch all for limiter api program
}


# want a maximum of 5 messages per 8 seconds,
# use @ratelimited(0.625) before your sendToQueue function.
def ratelimited(maxpersecond):
    """
    Rate limit by max per second
    """
    mininterval = 1.0 / float(maxpersecond)

    def decorate(func):
        """
        Decorator for rate limiter
        """
        lasttimecalled = [0.0]

        def ratelimitedfunction(*args, **kargs):
            """
            Function for decorator
            """
            lefttowait = mininterval - time.time() - lasttimecalled[0]
            if lefttowait > 0:
                time.sleep(lefttowait)
            lasttimecalled[0] = time.time()
            return func(*args, **kargs)

        return ratelimitedfunction

    return decorate
