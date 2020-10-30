def types():
    return [
        {
            'name': 'num_greedy',
            'args': [
                "-m", "num_greedy",
            ],
        },
        {
            'name': 'bit_greedy',
            'args': [
                "-m", "bit_greedy",
            ],
        },
        {
            'name': 'num_annealing',
            'args': [
                "-m", "num_annealing",
                "-temp", "10",
                "-c", "10",
                "-alpha", "10"
            ],
        }
    ]