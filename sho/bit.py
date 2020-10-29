import math
import numpy as np
import copy

from . import x,y,pb

########################################################################
# Objective functions
########################################################################

def cover_sum(sol, domain_width, sensor_range, dim):
    """Compute the coverage quality of the given array of bits."""
    assert(0 < sensor_range <= math.sqrt(2))
    assert(0 < domain_width)
    assert(dim > 0)
    assert(len(sol) >= dim)
    domain = np.zeros((domain_width,domain_width))
    sensors = to_sensors(sol)
    cov = pb.coverage(domain, sensors, sensor_range*domain_width)
    s = np.sum(cov)
    assert(s >= len(sensors))
    return s


def to_sensors(sol):
    """Convert an square array of d lines/columns containing n ones
    to an array of n 2-tuples with related coordinates.

    >>> to_sensors([[1,0],[1,0]])
    [(0, 0), (0, 1)]
    """
    assert(len(sol)>0)
    sensors = []
    for i in range(len(sol)):
        for j in range(len(sol[i])):
            if sol[i][j] == 1:
                sensors.append( (j,i) )
    return sensors


########################################################################
# Initialization
########################################################################

def rand(domain_width, nb_sensors):
    """"Draw a random domain containing nb_sensors ones."""
    domain = np.zeros( (domain_width,domain_width) )
    for x,y in np.random.randint(0, domain_width, (nb_sensors, 2)):
        domain[y][x] = 1
    return domain


########################################################################
# Neighborhood
########################################################################

def neighb_square(sol, scale, domain_width):
    """Draw a random array by moving every ones to adjacent cells."""
    assert(0 < scale <= 1)
    # Copy, because Python pass by reference
    # and we may not want to alter the original solution.
    new = copy.copy(sol)
    for py in range(len(sol)):
        for px in range(len(sol[py])):
            # Indices order is (y,x) in order to match
            # coordinates of images (row,col).
            if sol[py][px] == 1:
                # Add a one somewhere around.
                w = scale/2 * domain_width
                ny = np.random.randint(py-w,py+w)
                nx = np.random.randint(px-w,px+w)
                ny = min(max(0,ny),domain_width-1)
                nx = min(max(0,nx),domain_width-1)
                
                if new[ny][nx] != 1:
                    new[py][px] = 0 # Remove original position.
                    new[ny][nx] = 1
                # else pass
    return new

########################################################################
# Selection
########################################################################
def selection(population, nb_individuals, nb_sensors, func):
    assert(0 < nb_individuals < len(population))
    
    values = np.array([func(ind) for ind in population])
    return np.take(population, np.argsort(-values)[:nb_individuals], axis=0);

########################################################################
# Crossing
########################################################################
# def crossing(population, alpha, nb_individuals, nb_sensors):
#     assert(0 < nb_individuals)
#     assert(0 < alpha)

#     new_population = []
#     for ind in range(nb_individuals):
#         rand_matrix = np.random.random(population[0].shape) * alpha
#         sum_population = np.sum(population, axis=0) + rand_matrix
        
#         max_val = np.sort(sum_population.reshape(-1))[:nb_sensors]

#         new_solution = np.zeros_like(population[0])
#         sensors_placed = 0
#         for py in range(len(sum_population)):
#             for px in range(len(sum_population[py])):
#                 if sensors_placed == nb_sensors:
#                     break;
                
#                 if sum_population[py][px] in max_val:
#                     new_solution[py][px] = 1
#                     sensors_placed += 1

#         new_population.append(new_solution)

#     return np.array(new_population)

def crossing(population, alpha, nb_individuals, nb_sensors):
    assert(0 < nb_individuals)
    assert(0 < alpha)

    sensor_positions = [np.argwhere(ind == 1) for ind in population]
    new_population = []

    for idx in range(nb_individuals):
        new_solution = np.zeros_like(population[0])
        for sensor in range(nb_sensors):
            while True:
                ind = np.random.randint(len(population))
                sensor_position = sensor_positions[ind][sensor]
                if new_solution[sensor_position[0]][sensor_position[1]] == 0 :
                    break
            new_solution[sensor_position[0]][sensor_position[1]] = 1
       
        new_population.append(new_solution)

    return np.array(new_population)

########################################################################
# Mutation
########################################################################
def mutation(population, nb_mutations, nb_sensors):
    assert(0 < nb_mutations <= nb_sensors)

    mutated_population = population.copy()
    for ind in mutated_population:
        sensor_positions = np.argwhere(ind == 1)
        void_positions = np.argwhere(ind == 0)
        for idx in range(nb_mutations):
            pos_to_mutate = sensor_positions[np.random.randint(nb_sensors)]
            ind[pos_to_mutate[0], pos_to_mutate[1]] = 0
            
            pos_to_mutate = void_positions[np.random.randint(len(void_positions))]
            ind[pos_to_mutate[0], pos_to_mutate[1]] = 1

    return mutated_population

########################################################################
# Evaluation and Replacement
########################################################################
def eval_replacement(new_population, old_population, func):
    population = np.concatenate((new_population, old_population), axis=0)
    population = np.unique(population, axis=0)

    values = np.array([func(ind) for ind in population])
    return np.take(population, np.argsort(-values)[:len(old_population)], axis=0)