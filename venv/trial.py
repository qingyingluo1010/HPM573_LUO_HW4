from enum import Enum
import numpy as np


class Coinstate(Enum):
    """ health status of patients  """
    TAIL = 1
    HEAD = 0


class Game(object):
    def __init__(self, id, coin_prob):
        """ initiates a patient
        :param id: ID of the patient
        :param mortality_prob: probability of death during a time-step (must be in [0,1])
        """
        self._id = id
        self._rnd = np.random       # random number generator for this patient
        self._rnd.seed(self._id)    # specifying the seed of random number generator for this patient

        self._coin_prob = coin_prob
        self._CountTail = 0
        self._CountWin = 0

    def nextstep(self,steps=20):
        self._CountTail = 0
        self._CountWin = 0


        while self._CountTail < steps:
            if self._rnd.sample() < self._coin_prob:
                self.Coinstate = Coinstate.TAIL
                self._CountTail += 1
            elif self._rnd.sample() > self._coin_prob:
                self.Coinstate = Coinstate.HEAD
                self._CountTail += 1
        if self._CountTail >= 2:
            self._CountWin += 1

    def reward(self):
        return (250-self._CountWin*100)