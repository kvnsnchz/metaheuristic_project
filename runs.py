

import argparse
import os
import subprocess
import multiprocessing
import shutil
import experiment
import time
from itertools import product

# Constants
NB_SENSORS = 15
SENSOR_RANGE = 0.15
DOMAIN_WITH = 30
ITERS = 200
TARGET = DOMAIN_WITH * DOMAIN_WITH
STEADY_DELTA = 50
STEADY_EPSILON = 50
VARIATION_SCALE = 0.3
VERBOSE = 0
INITIALIZER = "init_circle"
INIT_RADIUS = 10


def check_dir(solver):
    _dir = f"ert/{solver['name']}"
    print(f"Checkin dir {_dir} ...")

    if os.path.exists(_dir):
        shutil.rmtree(_dir)
            
    os.mkdir(_dir) 

def run(solver, command, idx):
    print(f"Solver: {solver['name']} run: {idx+1} ...")
    filename = f"ert/{solver['name']}/run_{idx}.csv"
    subprocess.run(command + solver['args'] + ["-f", filename, "-s", str(int(time.time() + os.getpid()*10))])

if __name__=="__main__":

    # Arguments
    can = argparse.ArgumentParser()

    can.add_argument("-nr", "--nb-runs", metavar="NR", default=50, type=int,
            help="Number of algorithm executions")
    
    can.add_argument("-C", "--calls", metavar="NR", default=1000, type=int,
            help="Minimum number of calls to the target function")
    
    # Here, None = os.cpu_count() 
    can.add_argument("-p", "--processes", metavar="NB", default=None, type=int,
            help="Number of parallel processes.")

    the = can.parse_args()

    assert(0 < the.nb_runs)
    assert(0 < the.calls)

    command = ["python3",
        "snp.py",
        "-n", str(NB_SENSORS),
        "-r", str(SENSOR_RANGE),
        "-w", str(DOMAIN_WITH),
        "-i", str(ITERS),
        "-t", str(TARGET),
        "-y", str(STEADY_DELTA),
        "-e", str(STEADY_EPSILON),
        "-a", str(VARIATION_SCALE),
        "-v", str(VERBOSE),
        "-I", INITIALIZER,
        "-R", str(INIT_RADIUS),
        "-C", str(the.calls),
    ]

    # Solvers
    solvers = experiment.algoritms
    
    with multiprocessing.Pool(the.processes) as pool:
        pool.map(check_dir, solvers)
        print("Folders ready!")
        pool.starmap(run, product(solvers, [command], range(the.nb_runs)))
