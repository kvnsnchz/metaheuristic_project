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
    #assert(len(sol) >= dim)
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
        while domain[y][x] == 1:
            x,y = np.random.randint(0, domain_width, 2)
        domain[y][x] = 1
    
    return domain

def circle(radius, center, pos):
     return int(radius*np.cos(pos) + center), int(radius*np.sin(pos) + center)

def init_circle(domain_width, nb_sensors, radius):
    assert(0 < radius < domain_width/2)

    domain = np.zeros( (domain_width,domain_width) )
    div = np.ceil(nb_sensors/2)
    for idx in range(nb_sensors):
        x,y = circle(radius, domain_width/2, idx*np.pi/div)
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
def selection(population, nb_individuals, nb_sensors):
    assert(0 < nb_individuals < len(population))
    #print(f"size: {len(to_sensors(population[0,0]))}")
    return np.take(population, np.argsort(-population[:,1])[:nb_individuals], axis=0);

########################################################################
# Crossing
########################################################################
def get_new_value_from(a, b):
    n = a    
    if a > b:
        n = np.random.randint(b, a)
    elif a < b:
        n = np.random.randint(a, b)
    return n

def crossing(population, nb_individuals, domain_width, nb_sensors):
    assert(0 < nb_individuals)
    #sensor_positions = [np.argwhere(ind == 1) for ind in population[:, 0]]
    sensors = [to_sensors(ind) for ind in population[:, 0]]
    new_population = []
    population_size = len(population)
    
    for idx_i in range(population_size - 1):
        for idx_j in range(idx_i + 1, population_size):
            new_solution = np.zeros_like(population[0,0])
            #print(f"\n{len(sensors[idx_j])}")
            for sensor_idx in range(nb_sensors):
                s_iy = sensors[idx_i][sensor_idx][0]
                #print(f"{idx_j}, {sensor_idx} : {len(sensors)}, {len(sensors[idx_j])}, {sensors[idx_j]}")
                s_jy = sensors[idx_j][sensor_idx][0]
                ny = get_new_value_from(s_iy, s_jy)

                s_ix = sensors[idx_i][sensor_idx][1]
                s_jx = sensors[idx_j][sensor_idx][1]
                nx = get_new_value_from(s_ix, s_jx)
                    
                while new_solution[ny][nx] == 1:
                    ny,nx = np.random.randint(0, domain_width, 2)

                new_solution[ny][nx] = 1

            new_population.append([new_solution, None])
            if len(new_population) == nb_individuals:
                return np.array(new_population)
    
    return np.array(new_population)

########################################################################
# Mutation
########################################################################
def mutation(population, nb_mutations, nb_sensors):
    assert(0 < nb_mutations <= nb_sensors)

    mutated_population = population.copy()
    for ind in mutated_population:
        sensor_positions = np.argwhere(ind[0] == 1).tolist()
        void_positions = np.argwhere(ind[0] == 0).tolist()
        
        for idx in range(nb_mutations):
            pos_to_mutate = sensor_positions.pop(np.random.randint(len(sensor_positions)))
            ind[0][pos_to_mutate[0], pos_to_mutate[1]] = 0

            pos_to_mutate = void_positions.pop(np.random.randint(len(void_positions)))
            ind[0][pos_to_mutate[0], pos_to_mutate[1]] = 1

    return mutated_population

########################################################################
# Evaluation
########################################################################
def evaluation(population, func):
    for ind in population:
        if(ind[1] == None):
            ind[1] = func(ind[0])

########################################################################
# Replacement
########################################################################
def replacement(new_population, old_population, func):
    population = np.concatenate((new_population, old_population), axis=0)
    #population = np.unique(population, axis=0)

    return np.take(population, np.argsort(-population[:,1])[:len(old_population)], axis=0)