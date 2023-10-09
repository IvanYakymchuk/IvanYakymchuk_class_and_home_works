import numpy as np


def simulate_game(K, p, N):

    capital = K



    while capital > 0:

        random_number = np.random.randint(1,11)/10
        if random_number <= p:
            capital += 10
        else:
            capital -= 10

        if capital >= N:
            return 0
        if capital == 0:
            return 1

def calculate_probability(K, p, N, num_simulations):
    losses = 0
    for _ in range(num_simulations):
        losses += simulate_game(K, p, N)
    probability = losses / num_simulations
    return probability



K = 100
p = 0.4
N = 200


num_simulations = 1000


result = calculate_probability(K, p, N, num_simulations)
print(f'Ймовірність втрати всіх грошей при K = {K}, p = {p} і N = {N} складає {result:.2%}')