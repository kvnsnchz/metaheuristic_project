import math
import numpy as np

from . import pb

########################################################################
# Objective functions
########################################################################

# Decoupled from objective functions, so as to be used in display.
def to_sensors(sol):
    """Convert a vector of n*2 dimension to an array of n 2-tuples.

    >>> to_sensors([0,1,2,3])
    [(0, 1), (2, 3)]
    """
    assert(len(sol)>0)
    sensors = []
    for i in range(0,len(sol),2):
        sensors.append( ( int(math.floor(sol[i])), int(math.floor(sol[i+1])) ) )
    return sensors


def cover_sum(sol, domain_width, sensor_range, dim):
    """Compute the coverage quality of the given vector."""
    assert(0 < sensor_range <= domain_width * math.sqrt(2))
    assert(0 < domain_width)
    assert(dim > 0)
    assert(len(sol) >= dim)
    domain = np.zeros((domain_width,domain_width))
    sensors = to_sensors(sol)
    cov = pb.coverage(domain, sensors, sensor_range*domain_width)
    s = np.sum(cov)
    assert(s >= len(sensors))
    return s


########################################################################
# Initialization
########################################################################

def rand(dim, scale):
    """Draw a random vector in [0,scale]**dim."""
    return np.random.random(dim) * scale

def circle(radius, center, pos):
     return radius*np.cos(pos) + center, radius*np.sin(pos) + center

def init_circle(dim, scale, domain_width, nb_sensors, radius):
    assert(0 < radius < domain_width/2)

    domain = np.zeros(dim)
    div = np.ceil(nb_sensors/2)
    shift = np.random.uniform(0, np.pi)
    
    for idx in range(nb_sensors):
        x,y = circle(radius, domain_width/2, idx*np.pi/div + shift)
        domain[2*idx] = y
        domain[2*idx + 1] = x
    
    return domain

########################################################################
# Neighborhood
########################################################################

def neighb_square(sol, scale, domain_width):
    """Draw a random vector in a square of witdh `scale` in [0,1]
    as a fraction of the domain width around the given solution."""
    assert(0 < scale <= 1)
    side = domain_width * scale;
    new = sol + (np.random.random(len(sol)) * side - side/2)
    new = [min(max(pos, 0), domain_width - 1) for pos in new]
    return new

########################################################################
# Crossing
########################################################################
def get_new_value_from(a, b):
    n = a    
    if a > b:
        n = np.random.uniform(b, a)
    elif a < b:
        n = np.random.uniform(a, b)
    return n

def crossing(population, nb_individuals, nb_sensors):
    assert(0 < nb_individuals)
    #sensor_positions = [np.argwhere(ind == 1) for ind in population[:, 0]]
    sensors = [ind for ind in population[:, 0]]
    new_population = []
    population_size = len(population)
    
    for idx_i in range(population_size - 1):
        for idx_j in range(idx_i + 1, population_size):
            new_solution = []
            for sensor_idx in range(nb_sensors):
                s_iy = sensors[idx_i][2*sensor_idx]
                s_jy = sensors[idx_j][2*sensor_idx]
                ny = get_new_value_from(s_iy, s_jy)

                s_ix = sensors[idx_i][2*sensor_idx + 1]
                s_jx = sensors[idx_j][2*sensor_idx + 1]
                nx = get_new_value_from(s_ix, s_jx)

                new_solution.append(ny)
                new_solution.append(nx)

            new_population.append([new_solution, None])
            if len(new_population) == nb_individuals:
                return np.array(new_population)
    
    return np.array(new_population)

########################################################################
# Mutation
########################################################################
def mutation(population, nb_mutations, nb_sensors, domain_width):
    assert(0 < nb_mutations <= nb_sensors)

    mutated_population = population.copy()
    for sensors in mutated_population:
        for idx in range(nb_mutations):
            pos = np.random.randint(nb_sensors);
            sensors[0][2*pos] = np.random.uniform(0, domain_width) 
            sensors[0][2*pos + 1] = np.random.uniform(0, domain_width) 
    
    return mutated_population
