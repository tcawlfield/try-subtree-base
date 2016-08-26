class Welford(object):
    M = 0.
    S = 0.
    N = 0

    def update(self, x):
        self.N += 1
        oldM = self.M
        self.M += (x - self.M) / self.N
        self.S += (x - self.M) * (x - oldM)

    def get_var(self):
        return self.S / (self.N - 1.)
