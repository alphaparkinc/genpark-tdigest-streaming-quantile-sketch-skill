import math

class TDigest:
    """
    t-Digest Streaming Quantile Sketch.
    Clusters centroids adaptively for extreme tail precision.
    """
    def __init__(self, delta=100):
        self.delta = delta
        self.centroids = []
        self.total_weight = 0

    def add(self, x, w=1.0):
        self.centroids.append([float(x), float(w)])
        self.total_weight += w
        if len(self.centroids) > self.delta * 2:
            self.compress()

    def compress(self):
        self.centroids.sort(key=lambda c: c[0])
        compressed = []
        q0 = 0.0
        for mean, weight in self.centroids:
            q1 = q0 + weight / self.total_weight
            k0 = self._k(q0)
            k1 = self._k(q1)
            if compressed and (k1 - self._k(q0 - compressed[-1][1]/self.total_weight) <= 1.0):
                last = compressed[-1]
                new_w = last[1] + weight
                last[0] = (last[0] * last[1] + mean * weight) / new_w
                last[1] = new_w
            else:
                compressed.append([mean, weight])
            q0 = q1
        self.centroids = compressed

    def _k(self, q):
        return (self.delta / 2.0) * (math.asin(2.0 * max(0.0, min(1.0, q)) - 1.0) / math.pi + 0.5)

    def quantile(self, q):
        if not self.centroids:
            return 0.0
        self.centroids.sort(key=lambda c: c[0])
        target_w = q * self.total_weight
        accum = 0.0
        for mean, w in self.centroids:
            accum += w
            if accum >= target_w:
                return mean
        return self.centroids[-1][0]
