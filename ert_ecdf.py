import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from algo_types import types as algo_types
from os import scandir
import argparse

if __name__=="__main__":
    
    # Arguments
    can = argparse.ArgumentParser()

    can.add_argument("-d", "--delta", metavar="NR", default=620, type=int,
            help="comparison threshold")

    the = can.parse_args()
    
    solvers = algo_types()
    labels = []

    plt.figure(figsize=(20, 15))

    for solver in solvers:
        # File reading
        runs = []
        for idx, _file in enumerate(scandir(f"./ert/{solver['name']}")):
            if _file.is_file():
                filename = f"ert/{solver['name']}/{_file.name}"
                runs.append(pd.read_csv(filename, header=None, names=[f"run_{idx}"]))

        nb_runs = idx + 1

        runs = pd.concat(runs, axis=1)
        runs.dropna(inplace=True)

        # Radius calculation
        runs['ratio'] = runs.apply(lambda values: np.mean(np.where(values >= the.delta, 1, 0)), axis=1)
        
        # Plotting runs
        plt.plot(runs.index + 1, runs['ratio'], drawstyle='steps')
        labels.append(solver['name'])

    plt.ylim(0 - 1e-2, 1 + 1e-2)
    plt.xlabel("Number of calls to the objective function")
    plt.ylabel(f"Ratio of objective function values that reach $\delta$ = {the.delta}")
    plt.legend(labels)
    plt.title(f"ERT-ECDF {nb_runs} runs")
    plt.show()