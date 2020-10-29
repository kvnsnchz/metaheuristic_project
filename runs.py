

import argparse
import os
import subprocess
import shutil
from algo_types import types as algo_types

if __name__=="__main__":

    # Arguments
    can = argparse.ArgumentParser()

    can.add_argument("-nr", "--nb-runs", metavar="NR", default=4, type=int,
            help="Number of algorithm executions")
    
    can.add_argument("-C", "--calls", metavar="NR", default=200, type=int,
            help="Minimum number of calls to the target function")

    the = can.parse_args()

    # Constants
    NB_SENSORS = 3
    SENSOR_RANGE = 0.3
    DOMAIN_WITH = 30
    ITERS = 100
    TARGET = DOMAIN_WITH * DOMAIN_WITH
    STEADY_DELTA = 50
    STEADY_EPSILON = 50
    VARIATION_SCALE = 0.3

    # Solvers
    solvers = algo_types()

    for solver in solvers:
        _dir = f"ert/{solver['name']}"
        if os.path.exists(_dir):
            shutil.rmtree(_dir)
            
        os.mkdir(_dir) 
        
        command = ["python3",
            "snp.py",
            "-n", str(NB_SENSORS),
            "-r", str(SENSOR_RANGE),
            "-w", str(DOMAIN_WITH),
            "-i", str(ITERS),
            "-m", solver['name'],
            "-t", str(TARGET),
            "-y", str(STEADY_DELTA),
            "-e", str(STEADY_EPSILON),
            "-a", str(VARIATION_SCALE),
            "-v", "0",
        ] + solver['args']
        
        print(f"\n---- solver: {solver['name']} ----")
        for idx in range(the.nb_runs):
            print(f"\n-- run: {idx+1} --")
            filename = f"{_dir}/run_{idx}.csv"
            subprocess.run(command + ["-f", filename])