import P2 as Cls


trials = 1000
steps=20
coin_prob=0.4

# create a cohort
myCohort = Cls.Cohort(id=1, trials=trials,coin_prob=coin_prob)

# simulate the cohort
myCohort.simulate(steps)

# print the Average of these Realizations
print('Average of these Realizations:', myCohort.reward())