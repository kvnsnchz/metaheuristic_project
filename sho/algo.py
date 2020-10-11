########################################################################
# Algorithms
########################################################################
import numpy as np

def random(func, init, again):
    """Iterative random search template."""
    best_sol = init()
    best_val = func(best_sol)
    val,sol = best_val,best_sol
    i = 0
    while again(i, best_val, best_sol):
        sol = init()
        val = func(sol)
        if val >= best_val:
            best_val = val
            best_sol = sol
        i += 1
    return best_val, best_sol


def greedy(func, init, neighb, again):
    """Iterative randomized greedy heuristic template."""
    best_sol = init()
    best_val = func(best_sol)
    val,sol = best_val,best_sol
    i = 1
    while again(i, best_val, best_sol):
        sol = neighb(best_sol)
        val = func(sol)
        # Use >= and not >, so as to avoid random walk on plateus.
        if val >= best_val:
            best_val = val
            best_sol = sol
        i += 1
    return best_val, best_sol

# TODO add a simulated-annealing template.
def annealing(func, init, neighb, again, T, kmax, alpha):
    best_sol = init()
    best_val = func(best_sol)
    val,sol = best_val,best_sol
    i = 1

    while again(i, best_val, best_sol):
        for k in range(kmax):
            sol = neighb(best_sol)
            val = func(sol)

            if val >= best_val or (np.exp((best_val - val) / T) > np.random.rand(1)[0] and val > best_val):
                best_val = val
                best_sol = sol
         
        i += 1
        T *= alpha
    return best_val, best_sol

# TODO add a population-based stochastic heuristic template.
def genetic(func, init, again, select, cross, mutate, replace, population_size):
    population = [init() for idx in range(population_size)]
    selection = select(population)
    
    best_sol = selection[0]
    best_val = func(best_sol)
    i = 1

    while again(i, best_val, best_sol):
        crossing = cross(selection)
        mutation = mutate(crossing)
        population = replace(mutation, population)
        
        selection = select(population)
        best_sol = selection[0]
        best_val = func(best_sol)
        i += 1
    
    return best_val, best_sol


