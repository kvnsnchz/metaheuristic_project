solvers =  [
    'num_greedy',
    'bit_greedy',
    'num_annealing',
    'bit_annealing',
    'num_genetic',
    'bit_genetic'
]

# Best: 
#   1. num_genetic_3
#   2. num_genetic_0
#   3. num_genetic_6

algoritms = [
    {
        'name': 'num_greedy',
        'args': [
            "-m", solvers[0]
        ],
    },
    {
        'name': 'bit_greedy',
        'args': [
            "-m", solvers[1]
        ],
    },
    {
        'name': 'num_annealing_0',
        'args': [
            "-m", solvers[2],
            "-T", "100",
            "-c", "10",
            "-A", "0.95",
            "-E", "1"
        ],
    },
    {
        'name': 'num_annealing_1',
        'args': [
            "-m", solvers[2],
            "-T", "100",
            "-c", "10",
            "-A", "0.9",
            "-E", "1"
        ],
    },
    {
        'name': 'num_annealing_2',
        'args': [
            "-m", solvers[2],
            "-T", "100",
            "-c", "10",
            "-A", "0.85",
            "-E", "1"
        ],
    },
    {
        'name': 'num_annealing_3',
        'args': [
            "-m", solvers[2],
            "-T", "200",
            "-c", "15",
            "-A", "0.95",
            "-E", "1"
        ],
    },
    {
        'name': 'num_annealing_4',
        'args': [
            "-m", solvers[2],
            "-T", "200",
            "-c", "15",
            "-A", "0.9",
            "-E", "1"
        ],
    },
    {
        'name': 'num_annealing_5',
        'args': [
            "-m", solvers[2],
            "-T", "200",
            "-c", "15",
            "-A", "0.85",
            "-E", "1"
        ],
    },
    {
        'name': 'num_annealing_6',
        'args': [
            "-m", solvers[2],
            "-T", "500",
            "-c", "20",
            "-A", "0.95",
            "-E", "1"
        ],
    },
    {
        'name': 'num_annealing_7',
        'args': [
            "-m", solvers[2],
            "-T", "500",
            "-c", "20",
            "-A", "0.9",
            "-E", "1"
        ],
    },
    {
        'name': 'num_annealing_8',
        'args': [
            "-m", solvers[2],
            "-T", "500",
            "-c", "20",
            "-A", "0.85",
            "-E", "1"
        ],
    },
    {
        'name': 'bit_annealing_1',
        'args': [
            "-m", solvers[3],
            "-T", "100",
            "-c", "10",
            "-A", "0.9",
            "-E", "1"
        ],
    },
    {
        'name': 'bit_annealing_2',
        'args': [
            "-m", solvers[3],
            "-T", "100",
            "-c", "10",
            "-A", "0.85",
            "-E", "1"
        ],
    },
    {
        'name': 'bit_annealing_3',
        'args': [
            "-m", solvers[3],
            "-T", "200",
            "-c", "15",
            "-A", "0.95",
            "-E", "1"
        ],
    },
    {
        'name': 'bit_annealing_4',
        'args': [
            "-m", solvers[3],
            "-T", "200",
            "-c", "15",
            "-A", "0.9",
            "-E", "1"
        ],
    },
    {
        'name': 'bit_annealing_5',
        'args': [
            "-m", solvers[3],
            "-T", "200",
            "-c", "15",
            "-A", "0.85",
            "-E", "1"
        ],
    },
    {
        'name': 'bit_annealing_6',
        'args': [
            "-m", solvers[3],
            "-T", "500",
            "-c", "20",
            "-A", "0.95",
            "-E", "1"
        ],
    },
    {
        'name': 'bit_annealing_7',
        'args': [
            "-m", solvers[3],
            "-T", "500",
            "-c", "20",
            "-A", "0.9",
            "-E", "1"
        ],
    },
    {
        'name': 'bit_annealing_8',
        'args': [
            "-m", solvers[3],
            "-T", "500",
            "-c", "20",
            "-A", "0.85",
            "-E", "1"
        ],
    },
    {
        'name': 'num_genetic_0',
        'args': [
            "-m", solvers[4],
            "-p", "10",
            "-S", "5",
            "-x", "8",
            "-M", "1"
        ],
    },
    {
        'name': 'num_genetic_1',
        'args': [
            "-m", solvers[4],
            "-p", "10",
            "-S", "5",
            "-x", "10",
            "-M", "2"
        ],
    },
    {
        'name': 'num_genetic_2',
        'args': [
            "-m", solvers[4],
            "-p", "10",
            "-S", "5",
            "-x", "12",
            "-M", "4"
        ],
    },
    {
        'name': 'num_genetic_3',
        'args': [
            "-m", solvers[4],
            "-p", "15",
            "-S", "5",
            "-x", "8",
            "-M", "1"
        ],
    },
    {
        'name': 'num_genetic_4',
        'args': [
            "-m", solvers[4],
            "-p", "15",
            "-S", "5",
            "-x", "10",
            "-M", "2"
        ],
    },
    {
        'name': 'num_genetic_5',
        'args': [
            "-m", solvers[4],
            "-p", "15",
            "-S", "5",
            "-x", "12",
            "-M", "4"
        ],
    },
    {
        'name': 'num_genetic_6',
        'args': [
            "-m", solvers[4],
            "-p", "20",
            "-S", "5",
            "-x", "8",
            "-M", "1"
        ],
    },
    {
        'name': 'num_genetic_7',
        'args': [
            "-m", solvers[4],
            "-p", "20",
            "-S", "5",
            "-x", "10",
            "-M", "2"
        ],
    },
    {
        'name': 'num_genetic_8',
        'args': [
            "-m", solvers[4],
            "-p", "20",
            "-S", "5",
            "-x", "12",
            "-M", "4"
        ],
    },
    {
        'name': 'bit_genetic_0',
        'args': [
            "-m", solvers[5],
            "-p", "10",
            "-S", "5",
            "-x", "8",
            "-M", "1"
        ],
    },
    {
        'name': 'bit_genetic_1',
        'args': [
            "-m", solvers[5],
            "-p", "10",
            "-S", "5",
            "-x", "10",
            "-M", "2"
        ],
    },
    {
        'name': 'bit_genetic_2',
        'args': [
            "-m", solvers[5],
            "-p", "10",
            "-S", "5",
            "-x", "12",
            "-M", "4"
        ],
    },
    {
        'name': 'bit_genetic_3',
        'args': [
            "-m", solvers[5],
            "-p", "15",
            "-S", "5",
            "-x", "8",
            "-M", "1"
        ],
    },
    {
        'name': 'bit_genetic_4',
        'args': [
            "-m", solvers[5],
            "-p", "15",
            "-S", "5",
            "-x", "10",
            "-M", "2"
        ],
    },
    {
        'name': 'bit_genetic_5',
        'args': [
            "-m", solvers[5],
            "-p", "15",
            "-S", "5",
            "-x", "12",
            "-M", "4"
        ],
    },
    {
        'name': 'bit_genetic_6',
        'args': [
            "-m", solvers[5],
            "-p", "20",
            "-S", "5",
            "-x", "8",
            "-M", "1"
        ],
    },
    {
        'name': 'bit_genetic_7',
        'args': [
            "-m", solvers[5],
            "-p", "20",
            "-S", "5",
            "-x", "10",
            "-M", "2"
        ],
    },
    {
        'name': 'bit_genetic_8',
        'args': [
            "-m", solvers[5],
            "-p", "20",
            "-S", "5",
            "-x", "12",
            "-M", "4"
        ],
    },
]