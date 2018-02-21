from enum import Enum
import numpy as np

class Coinstate(Enum):
    """ status of coins  """
    TAIL = 1
    HEAD = 0


class Game(object):
    def __init__(self, id, coin_prob=0.5):

        self._id = id
        self._rnd = np.random       # random number generator for trial
        self._rnd.seed(self._id)

        self._coin_prob = coin_prob
        self._CountTail = 0
        self._CountWin = 0
        self._step=0

    def simulate(self,steps):
        self._CountTail = 0
        self._CountWin = 0
        self._step = 0

        while self._step < steps:
            if self._rnd.sample() < self._coin_prob:
                self.Coinstate = Coinstate.TAIL
                self._CountTail += 1
                self._step +=1

            elif self._rnd.sample() > self._coin_prob:
                self.Coinstate = Coinstate.HEAD
                self._step +=1
                if self._CountTail >=2:
                    self._CountTail =0
                    self._CountWin += 1

    def reward(self):
        return (100*self._CountWin -250)


class Cohort:
    def __init__(self, id, trials,coin_prob):

        self._coin = []
        self._win = []

        for i in range(trials):

            coin = Game(id * trials + i, coin_prob)
            # add the results to the cohort
            self._coin.append(coin)

    def simulate(self,steps):

        for coin in self._coin:

            coin.simulate(steps)
            # record wins
            value = coin.reward()
            if not (value is None):
                self._win.append(value)

    def reward(self):
        """ returns the average reward in this cohort """
        return sum(self._win)/len(self._win)