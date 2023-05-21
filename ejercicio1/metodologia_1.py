#################################################
#   Datos temporales y complejos
#   Ejercicios metodologías sobre Data Streams
#   Ejercicio 1 (parte 2)
#   David Mora Garrido
#################################################

import argparse
import os
import time

import memory_profiler


def read_sequence(file_path):
    with open(file_path, 'r') as f:
        while num := f.readline().split('\n', 1)[0]:
            if num:
                yield int(num)


def get_missing_number(n, file_path):
    total_sum = (1 + n)*(n/2)
    sequence_sum = 0
    for num in read_sequence(file_path):
        sequence_sum += num
    missing_number = int(total_sum - sequence_sum)
    print(f'The missing number is: {missing_number}')
    return missing_number


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file-path', help='Path of the file containing the generated sequence from 1 to N',
                        required=True)

    args = parser.parse_args()
    file_path = args.file_path
    n = int(os.path.basename(file_path).split('_')[0])

    start_time = time.time()
    memory_usage = max(memory_profiler.memory_usage((get_missing_number, (), {'n': int(n), 'file_path': file_path}),
                                                    max_iterations=1))
    end_time = time.time()
    print(f'Memory usage: {memory_usage} MBs. Employed time: {end_time-start_time} s')
