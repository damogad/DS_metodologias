#################################################
#   Datos temporales y complejos
#   Ejercicios metodologías sobre Data Streams
#   Ejercicio 1 (parte 1)
#   David Mora Garrido
#################################################

import argparse
import random


def generate_sequence(n, missing_number):
    sequence = [i for i in range(1, n+1) if i != missing_number]
    random.shuffle(sequence)
    with open(f'{n}_{missing_number}.txt', 'w') as f:
        for num in sequence:
            f.write(f'{num}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', help='Maximum number of the sequence from 1', type=int, required=True)
    parser.add_argument('--missing-number', help='Missing number in the sequence from 1 to n', type=int, required=True)
    parser.add_argument('--seed', help='Seed for random ordering of sequence', type=int, default=1)

    args = parser.parse_args()
    n = args.n
    missing_number = args.missing_number
    seed = args.seed

    if not(1 <= missing_number <= n):
        raise ValueError('The specified missing number must belong to the sequence of consecutive numbers between 1 and n')

    random.seed(seed)
    generate_sequence(n, missing_number)
