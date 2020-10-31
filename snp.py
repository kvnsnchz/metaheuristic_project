#encoding: utf-8
import math
import numpy as np
import matplotlib.pyplot as plt
import os

from sho import make, algo, iters, plot, num, bit, pb

########################################################################
# Interface
########################################################################

if __name__=="__main__":
    import argparse

    # Dimension of the search space.
    d = 2

    can = argparse.ArgumentParser()

    can.add_argument("-n", "--nb-sensors", metavar="NB", default=3, type=int,
            help="Number of sensors")

    can.add_argument("-r", "--sensor-range", metavar="RATIO", default=0.3, type=float,
            help="Sensors' range (as a fraction of domain width, max is √2)")

    can.add_argument("-w", "--domain-width", metavar="NB", default=30, type=int,
            help="Domain width (a number of cells). If you change this you will probably need to update `--target` accordingly")

    can.add_argument("-i", "--iters", metavar="NB", default=100, type=int,
            help="Maximum number of iterations")

    can.add_argument("-s", "--seed", metavar="VAL", default=None, type=int,
            help="Random pseudo-generator seed (none for current epoch)")

    solvers = ["num_greedy","bit_greedy", "num_annealing", "bit_annealing", "bit_genetic"]
    can.add_argument("-m", "--solver", metavar="NAME", choices=solvers, default="num_greedy",
            help="Solver to use, among: "+", ".join(solvers))

    can.add_argument("-t", "--target", metavar="VAL", default=30*30, type=float,
            help="Objective function value target")

    can.add_argument("-y", "--steady-delta", metavar="NB", default=50, type=float,
            help="Stop if no improvement after NB iterations")

    can.add_argument("-e", "--steady-epsilon", metavar="DVAL", default=0, type=float,
            help="Stop if the improvement of the objective function value is lesser than DVAL")

    can.add_argument("-a", "--variation-scale", metavar="RATIO", default=0.3, type=float,
            help="Scale of the variation operators (as a ration of the domain width)")
    
    can.add_argument("-v", "--verbose", metavar="NB", default=1, type=int,
            help="Alpha for annealing")
    
    can.add_argument("-f", "--filename", metavar="NAME", default="ert/calls.csv",
            help="Filename with calls to the target function")

    can.add_argument("-C", "--calls", metavar="NB", default=100, type=int,
            help="Minimum number of calls to the target function")

    can.add_argument("-temp", "--temperature", metavar="DVAL", default=10.0, type=float,
            help="Temperature for annealing")

    can.add_argument("-c", "--cycles-temp", metavar="NB", default=10, type=int,
            help="Cycles per temperature value for annealing")

    can.add_argument("-alpha", "--alpha", metavar="DVAL", default=0.8, type=float,
            help="Alpha for annealing")
    

    the = can.parse_args()

    # Minimum checks.
    assert(0 < the.nb_sensors)
    assert(0 < the.sensor_range <= math.sqrt(2))
    assert(0 < the.domain_width)
    assert(0 < the.iters)
    assert(0 < the.calls)
    assert(0 < the.temperature)
    assert(0 < the.cycles_temp)
    assert(0 < the.alpha)

    # Do not forget the seed option,
    # in case you would start "runs" in parallel.
    np.random.seed(the.seed)

    # Weird numpy way to ensure single line print of array.
    np.set_printoptions(linewidth = np.inf)


    # Common termination and checkpointing.
    
    history = []

    agains = [
        make.iter(iters.max,
            nb_it = the.iters),
        make.iter(iters.save,
            filename = the.solver+".csv",
            fmt = "{it} ; {val} ; {sol}\n"),
        make.iter(iters.history,
            history = history),
        make.iter(iters.target,
            target = the.target),
        iters.steady(the.steady_delta, the.steady_epsilon)
    ]

    if the.verbose:
        agains.append(make.iter(iters.log, fmt="\r{it} {val}"))
    
    iters = make.iter(
                iters.several,
                agains = agains
            )

    # Erase the previous file.
    with open(the.solver+".csv", 'w') as fd:
        fd.write("# {} {}\n".format(the.solver,the.domain_width))

    if os.path.exists(the.filename):
        os.remove(the.filename)
    
    val,sol,sensors = None,None,None
    metadata = {
        "best_value": 0,
        "num_calls": 0,
        "min_calls": the.calls,
    };

    while the.calls > metadata["num_calls"]:
        if the.solver == "num_greedy":
            val,sol = algo.greedy(
                    make.func(pb.save,
                        func = num.cover_sum,
                        metadata = metadata,
                        filename = the.filename,
                        domain_width = the.domain_width,
                        sensor_range = the.sensor_range,
                        dim = d * the.nb_sensors),
                    make.init(num.rand,
                        dim = d * the.nb_sensors,
                        scale = the.domain_width),
                    make.neig(num.neighb_square,
                        scale = the.variation_scale,
                        domain_width = the.domain_width),
                    iters
                )
            sensors = num.to_sensors(sol)

        elif the.solver == "bit_greedy":
            val,sol = algo.greedy(
                    make.func(pb.save,
                        func = bit.cover_sum,
                        metadata = metadata,
                        filename = the.filename,
                        domain_width = the.domain_width,
                        sensor_range = the.sensor_range,
                        dim = d * the.nb_sensors),
                    make.init(bit.rand,
                        domain_width = the.domain_width,
                        nb_sensors = the.nb_sensors),
                    make.neig(bit.neighb_square,
                        scale = the.variation_scale,
                        domain_width = the.domain_width),
                    iters
                )
            sensors = bit.to_sensors(sol)
        
        elif the.solver == "num_annealing":
            val,sol = algo.annealing(
                    make.func(pb.save,
                        func = num.cover_sum,
                        metadata = metadata,
                        filename = the.filename,
                        domain_width = the.domain_width,
                        sensor_range = the.sensor_range,
                        dim = d * the.nb_sensors),
                    make.init(num.rand,
                        dim = d * the.nb_sensors,
                        scale = the.domain_width),
                    make.neig(num.neighb_square,
                        scale = the.variation_scale,
                        domain_width = the.domain_width),
                    iters,
                    the.temperature,
                    the.cycles_temp,
                    the.alpha
                )
            sensors = num.to_sensors(sol)
        
        elif the.solver == "bit_annealing":
            val,sol = algo.annealing(
                    make.func(pb.save,
                        func = bit.cover_sum,
                        metadata = metadata,
                        filename = the.filename,
                        domain_width = the.domain_width,
                        sensor_range = the.sensor_range,
                        dim = d * the.nb_sensors),
                    make.init(bit.rand,
                        domain_width = the.domain_width,
                        nb_sensors = the.nb_sensors),
                    make.neig(bit.neighb_square,
                        scale = the.variation_scale,
                        domain_width = the.domain_width),
                    iters,
                    the.temperature,
                    the.cycles_temp,
                    the.alpha
                )
            sensors = bit.to_sensors(sol)

        elif the.solver == "bit_genetic":
            func = make.func(pb.save,
                        func = bit.cover_sum,
                        metadata = metadata,
                        filename = the.filename,
                        domain_width = the.domain_width,
                        sensor_range = the.sensor_range,
                        dim = d * the.nb_sensors)

            val,sol = algo.genetic(
                    func,
                    make.init(bit.rand,
                        domain_width = the.domain_width,
                        nb_sensors = the.nb_sensors),
                    iters,
                    make.select(bit.selection,
                        nb_individuals = 5,
                        nb_sensors = the.nb_sensors,
                        func = func),
                    make.cross(bit.crossing,
                        nb_individuals = 8,
                        nb_sensors = the.nb_sensors),
                    make.mutate(bit.mutation,
                        nb_mutations = 1,
                        nb_sensors = the.nb_sensors),
                    make.evaluate(bit.evaluation,
                        func = func),
                    make.replace(bit.replacement,
                        func = func),
                    population_size=10
                )
            sensors = bit.to_sensors(sol)

    if(the.verbose):
        # Fancy output.
        print("\n{} : {}".format(val,sensors))
        print(metadata)
        
        shape=(the.domain_width, the.domain_width)

        fig = plt.figure()

        if the.nb_sensors ==1 and the.domain_width <= 50:
            ax1 = fig.add_subplot(121, projection='3d')
            ax2 = fig.add_subplot(122)

            f = make.func(num.cover_sum,
                            domain_width = the.domain_width,
                            sensor_range = the.sensor_range * the.domain_width)
            plot.surface(ax1, shape, f)
            plot.path(ax1, shape, history)
        else:
            ax2=fig.add_subplot(111)

        domain = np.zeros(shape)
        domain = pb.coverage(domain, sensors,
                the.sensor_range * the.domain_width)
        domain = plot.highlight_sensors(domain, sensors)
        ax2.imshow(domain)

        plt.show()
    
    
