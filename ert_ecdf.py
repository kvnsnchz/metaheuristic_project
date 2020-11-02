import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import experiment
from os import scandir
import argparse

def plot_semifinal_comparison(solvers, algoritms, deltas):
    for solver_idx, solver in enumerate(solvers):
        fig = plt.figure(figsize=(20, 15))
        fig.subplots_adjust(hspace=0.5)
        axs = [
            fig.add_subplot(221),
            fig.add_subplot(222),
            fig.add_subplot(223)
        ]

        end = len(solver)
        labels = []

        for algoritm in algoritms:
            if  algoritm['name'][:end] != solver:
                continue
            
            # File reading
            runs = []
            for idx, _file in enumerate(scandir(f"./ert/{algoritm['name']}")):
                if _file.is_file():
                    filename = f"ert/{algoritm['name']}/{_file.name}"
                    runs.append(pd.read_csv(filename, header=None, names=[f"run_{idx}"]))

            nb_runs = idx + 1

            runs = pd.concat(runs, axis=1)
            runs.dropna(inplace=True)

            for idx, delta in enumerate(deltas):
                # Radius calculation
                ratio = runs.apply(lambda values: np.mean(np.where(values >= delta, 1, 0)), axis=1)
                # Plotting runs
                axs[idx].plot(runs.index + 1, ratio, drawstyle='steps', label=algoritm['name'])

        for idx, ax in enumerate(axs):
            ax.set_ylim(0 - 1e-2, 1 + 1e-2)
            ax.set_xlabel("Number of calls to the objective function")
            ax.set_ylabel(f"Ratio of obj. func. values that reach $\delta$")
            ax.legend(loc='upper left', prop={'size': 6})
            ax.set_title(f"ERT-ECDF {nb_runs} runs - {solver} - $\delta$ = {deltas[idx]}")
        
    plt.show()

def plot_final_comparison(solvers, algoritms, deltas):
    fig = plt.figure(figsize=(20, 15))
    fig.subplots_adjust(hspace=0.5)
    axs = [
        fig.add_subplot(221),
        fig.add_subplot(222),
        fig.add_subplot(223)
    ]

    for solver_idx, solver in enumerate(solvers):
        end = len(solver)
        labels = []

        for algoritm in algoritms:
            if  algoritm['name'] != solver:
                continue
            
            # File reading
            runs = []
            for idx, _file in enumerate(scandir(f"./ert/{algoritm['name']}")):
                if _file.is_file():
                    filename = f"ert/{algoritm['name']}/{_file.name}"
                    runs.append(pd.read_csv(filename, header=None, names=[f"run_{idx}"]))

            nb_runs = idx + 1

            runs = pd.concat(runs, axis=1)
            runs.dropna(inplace=True)

            for idx, delta in enumerate(deltas):
                # Radius calculation
                ratio = runs.apply(lambda values: np.mean(np.where(values >= delta, 1, 0)), axis=1)
                # Plotting runs
                axs[idx].plot(runs.index + 1, ratio, drawstyle='steps', label=algoritm['name'])
            
        
    for idx, ax in enumerate(axs):
        ax.set_ylim(0 - 1e-2, 1 + 1e-2)
        ax.set_xlabel("Number of calls to the objective function")
        ax.set_ylabel(f"Ratio of obj. func. values that reach $\delta$")
        ax.legend(loc='upper left', prop={'size': 6})
        ax.set_title(f"ERT-ECDF {nb_runs} runs - $\delta$ = {deltas[idx]}")
        
    plt.show()


if __name__=="__main__":
    
    # Arguments
    can = argparse.ArgumentParser()

    can.add_argument("-d", "--delta", metavar="NR", default=750, type=int,
            help="comparison threshold")

    can.add_argument("-v", "--delta-variation", metavar="NR", default=50, type=int,
            help="delta variation")

    phases = ["semifinal", "final"]
    can.add_argument("-p", "--phase", metavar="NAME", choices=phases, default="final",
            help="comparison phase, among: "+", ".join(phases))

    the = can.parse_args()

    assert(0 < the.delta)
    assert(0 < the.delta_variation < the.delta)
    
    deltas = [the.delta - the.delta_variation, the.delta, the.delta + the.delta_variation]

    if the.phase == 'final':
        plot_final_comparison(experiment.final, experiment.algoritms, deltas)
    else: 
        plot_semifinal_comparison(experiment.semifinal, experiment.algoritms, deltas)

    

    