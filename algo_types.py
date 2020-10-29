def types():
    return [
        {
            'name': 'num_greedy',
            'args': [],
        },
        {
            'name': 'bit_greedy',
            'args': [],
        },
        {
            'name': 'num_annealing',
            'args': [
                "-temp", "10",
                "-c", "10",
                "-alpha", "10"
            ],
        }
    ]