import time

class RateLimiter:
    def __init__(self):
        self.buckets = {}

    def addRule(self, reqId, maxBucketSize, refillRate):
        bucket = TokenBucket(maxBucketSize, refillRate)
        self.buckets[reqId] = bucket

    def allowRequest(self, reqId, tokens):
        if reqId not in self.buckets:
            return False

        return self.buckets[reqId].allowRequest(tokens)


class TokenBucket:
    # Singeton pattern
    def __init__(self, maxBucketSize, refillRate):
        self.maxBucketSize = maxBucketSize
        self.refillRate = refillRate
        self.curBucketSize = maxBucketSize
        # time in milliseconds
        self.lastRefilled = int(round(time.time() * 1000))

    def allowRequest(self, tokens):
        # handle threadeding
        self._refill()

        if self.curBucketSize > tokens:
            self.curBucketSize -= tokens

            return True

        return False

    def _refill(self):
        now = int(round(time.time() * 1000))
        tokens_to_add = int((now - self.lastRefilled) * (refillRate // 1000))
        self.curBucketSize = max(self.maxBucketSize, token_to_add)
        self.lastRefilled = now
