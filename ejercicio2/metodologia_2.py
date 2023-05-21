#################################################
#   Datos temporales y complejos
#   Ejercicios metodologías sobre Data Streams
#   Ejercicio 2
#   David Mora Garrido
#################################################

import argparse
import random


def f(n, num_iter, k):
    sequence = [i for i in range(1, n+1)]
    random.shuffle(sequence)
    num_correct_guesses = 0
    for _ in range(num_iter):
        selected_nums = [sequence[i] for i in [random.randint(0, n-1) for _ in range(k)]]
        if max(selected_nums) > 0.75*n:
            num_correct_guesses += 1
    print(f'Estimated error probability: {1 - num_correct_guesses/num_iter}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', help='Size of the sequence', type=int, required=True)
    parser.add_argument('--num-iter', help='Number of iterations to estimate the error probability',
                        type=int, required=True)
    parser.add_argument('--k', help='Number of elements to check', type=int, required=True)

    args = parser.parse_args()
    n = args.n
    num_iter = args.num_iter
    k = args.k

    f(n, num_iter, k)
        
