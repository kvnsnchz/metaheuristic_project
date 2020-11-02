from . import distance
import numpy as np

########################################################################
# Objective functions
########################################################################

def coverage(domain, sensors, sensor_range):
    """Set a given domain's cells to on if they are visible
    from one of the given sensors at the given sensor_range.

    >>> coverage(np.zeros((5,5)),[(2,2)],2)
    array([[ 0.,  0.,  0.,  0.,  0.],
           [ 0.,  1.,  1.,  1.,  0.],
           [ 0.,  1.,  1.,  1.,  0.],
           [ 0.,  1.,  1.,  1.,  0.],
           [ 0.,  0.,  0.,  0.,  0.]])
    """
    for py in range(len(domain)):
        for px in range(len(domain[py])):
            p = (px,py)
            for x in sensors:
                if distance(x,p) < sensor_range:
                    domain[py][px] = 1
    return domain


def line(x0, y0, x1, y1):
    """Compute the set of pixels (integer coordinates) of the line
    between the given line (x0,y0) -> (x1,y1).
    Use the Bresenham's algorithm.
    This make a generator that yield the start and the end points.
    """
    dx = x1 - x0
    dy = y1 - y0

    if dx > 0:
        xs = 1
    else:
        xs = -1

    if dy > 0:
        ys = 1
    else:
        xs = -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        ax, xy, yx, ay = xs, 0, 0, ys
    else:
        dx, dy = dy, dx
        ax, xy, yx, ay = 0, ys, xs, 0

    D = 2 * dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x*ax + y*yx , y0 + x*xy + y*ay

        if D >= 0:
            y += 1
            D -= 2 * dx

    D += 2 * dy

########################################################################
# General Wrapper Objective Functions
########################################################################

def save(sol, func, metadata, filename="calls.csv", **kwargs):
    value = func(sol,**kwargs)

    if value > metadata["best_value"]:
            metadata["best_value"] = value
    
    if metadata["min_calls"] > metadata["num_calls"]:
        with open(filename, "a") as file:    
            file.write(str(metadata["best_value"]) + "\n")
    
    metadata["num_calls"] += 1
    return value

########################################################################
# Selection - Genetic algorithm
########################################################################
def selection(population, nb_individuals, nb_sensors):
    assert(0 < nb_individuals < len(population))
    
    return np.take(population, np.argsort(-population[:,1])[:nb_individuals], axis=0);

########################################################################
# Evaluation - Genetic algorithm
########################################################################
def evaluation(population, func):
    for ind in population:
        if(ind[1] == None):
            ind[1] = func(ind[0])

########################################################################
# Replacement - Genetic algorithm
########################################################################
def replacement(new_population, old_population, func):
    population = np.concatenate((new_population, old_population), axis=0)
    return np.take(population, np.argsort(-population[:,1])[:len(old_population)], axis=0)