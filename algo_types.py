def types():
    return [
        {
            'name': 'num_greedy',
            'args': [
                "-m", "num_greedy"
            ],
        },
        {
            'name': 'bit_greedy',
            'args': [
                "-m", "bit_greedy"
            ],
        },
        {
            'name': 'num_annealing_0',
            'args': [
                "-m", "num_annealing",
                "-T", "100",
                "-c", "10",
                "-A", "0.95",
                "-E", "1"
            ],
        },
        {
            'name': 'num_annealing_1',
            'args': [
                "-m", "num_annealing",
                "-T", "100",
                "-c", "10",
                "-A", "0.9",
                "-E", "1"
            ],
        },
        {
            'name': 'num_annealing_2',
            'args': [
                "-m", "num_annealing",
                "-T", "100",
                "-c", "10",
                "-A", "0.85",
                "-E", "1"
            ],
        },
        {
            'name': 'num_annealing_3',
            'args': [
                "-m", "num_annealing",
                "-T", "200",
                "-c", "15",
                "-A", "0.95",
                "-E", "1"
            ],
        },
        {
            'name': 'num_annealing_4',
            'args': [
                "-m", "num_annealing",
                "-T", "200",
                "-c", "15",
                "-A", "0.9",
                "-E", "1"
            ],
        },
        {
            'name': 'num_annealing_5',
            'args': [
                "-m", "num_annealing",
                "-T", "200",
                "-c", "15",
                "-A", "0.85",
                "-E", "1"
            ],
        },
        {
            'name': 'num_annealing_6',
            'args': [
                "-m", "num_annealing",
                "-T", "500",
                "-c", "20",
                "-A", "0.95",
                "-E", "1"
            ],
        },
        {
            'name': 'num_annealing_7',
            'args': [
                "-m", "num_annealing",
                "-T", "500",
                "-c", "20",
                "-A", "0.9",
                "-E", "1"
            ],
        },
        {
            'name': 'num_annealing_8',
            'args': [
                "-m", "num_annealing",
                "-T", "500",
                "-c", "20",
                "-A", "0.85",
                "-E", "1"
            ],
        },
        {
            'name': 'bit_annealing_1',
            'args': [
                "-m", "bit_annealing",
                "-T", "100",
                "-c", "10",
                "-A", "0.9",
                "-E", "1"
            ],
        },
        {
            'name': 'bit_annealing_2',
            'args': [
                "-m", "bit_annealing",
                "-T", "100",
                "-c", "10",
                "-A", "0.85",
                "-E", "1"
            ],
        },
        {
            'name': 'bit_annealing_3',
            'args': [
                "-m", "bit_annealing",
                "-T", "200",
                "-c", "15",
                "-A", "0.95",
                "-E", "1"
            ],
        },
        {
            'name': 'bit_annealing_4',
            'args': [
                "-m", "bit_annealing",
                "-T", "200",
                "-c", "15",
                "-A", "0.9",
                "-E", "1"
            ],
        },
        {
            'name': 'bit_annealing_5',
            'args': [
                "-m", "bit_annealing",
                "-T", "200",
                "-c", "15",
                "-A", "0.85",
                "-E", "1"
            ],
        },
        {
            'name': 'bit_annealing_6',
            'args': [
                "-m", "bit_annealing",
                "-T", "500",
                "-c", "20",
                "-A", "0.95",
                "-E", "1"
            ],
        },
        {
            'name': 'bit_annealing_7',
            'args': [
                "-m", "bit_annealing",
                "-T", "500",
                "-c", "20",
                "-A", "0.9",
                "-E", "1"
            ],
        },
        {
            'name': 'bit_annealing_8',
            'args': [
                "-m", "bit_annealing",
                "-T", "500",
                "-c", "20",
                "-A", "0.85",
                "-E", "1"
            ],
        },
        {
            'name': 'num_genetic_0',
            'args': [
                "-m", "num_genetic",
                "-p", "10",
                "-S", "5",
                "-x", "8",
                "-M", "1"
            ],
        },
        {
            'name': 'num_genetic_1',
            'args': [
                "-m", "num_genetic",
                "-p", "10",
                "-S", "5",
                "-x", "10",
                "-M", "2"
            ],
        },
        {
            'name': 'num_genetic_2',
            'args': [
                "-m", "num_genetic",
                "-p", "10",
                "-S", "5",
                "-x", "12",
                "-M", "4"
            ],
        },
        {
            'name': 'num_genetic_3',
            'args': [
                "-m", "num_genetic",
                "-p", "15",
                "-S", "5",
                "-x", "8",
                "-M", "1"
            ],
        },
        {
            'name': 'num_genetic_4',
            'args': [
                "-m", "num_genetic",
                "-p", "15",
                "-S", "5",
                "-x", "10",
                "-M", "2"
            ],
        },
        {
            'name': 'num_genetic_5',
            'args': [
                "-m", "num_genetic",
                "-p", "15",
                "-S", "5",
                "-x", "12",
                "-M", "4"
            ],
        },
        {
            'name': 'num_genetic_6',
            'args': [
                "-m", "num_genetic",
                "-p", "10",
                "-S", "5",
                "-x", "8",
                "-M", "1"
            ],
        },
        {
            'name': 'num_genetic_7',
            'args': [
                "-m", "num_genetic",
                "-p", "15",
                "-S", "5",
                "-x", "10",
                "-M", "2"
            ],
        },
        {
            'name': 'num_genetic_8',
            'args': [
                "-m", "num_genetic",
                "-p", "20",
                "-S", "5",
                "-x", "12",
                "-M", "4"
            ],
        },
        {
            'name': 'bit_genetic_0',
            'args': [
                "-m", "bit_genetic",
                "-p", "10",
                "-S", "5",
                "-x", "8",
                "-M", "1"
            ],
        },
        {
            'name': 'bit_genetic_1',
            'args': [
                "-m", "bit_genetic",
                "-p", "10",
                "-S", "5",
                "-x", "10",
                "-M", "2"
            ],
        },
        {
            'name': 'bit_genetic_2',
            'args': [
                "-m", "bit_genetic",
                "-p", "10",
                "-S", "5",
                "-x", "12",
                "-M", "4"
            ],
        },
        {
            'name': 'bit_genetic_3',
            'args': [
                "-m", "bit_genetic",
                "-p", "15",
                "-S", "5",
                "-x", "8",
                "-M", "1"
            ],
        },
        {
            'name': 'bit_genetic_4',
            'args': [
                "-m", "bit_genetic",
                "-p", "15",
                "-S", "5",
                "-x", "10",
                "-M", "2"
            ],
        },
        {
            'name': 'bit_genetic_5',
            'args': [
                "-m", "bit_genetic",
                "-p", "15",
                "-S", "5",
                "-x", "12",
                "-M", "4"
            ],
        },
        {
            'name': 'bit_genetic_6',
            'args': [
                "-m", "bit_genetic",
                "-p", "10",
                "-S", "5",
                "-x", "8",
                "-M", "1"
            ],
        },
        {
            'name': 'bit_genetic_7',
            'args': [
                "-m", "bit_genetic",
                "-p", "15",
                "-S", "5",
                "-x", "10",
                "-M", "2"
            ],
        },
        {
            'name': 'bit_genetic_8',
            'args': [
                "-m", "bit_genetic",
                "-p", "20",
                "-S", "5",
                "-x", "12",
                "-M", "4"
            ],
        },
    ]