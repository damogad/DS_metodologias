#################################################
#   Datos temporales y complejos
#   Ejercicios metodologías sobre Data Streams
#   Ejercicio 3
#   David Mora Garrido
#################################################


import argparse
from functools import lru_cache


def parse_sequence_file(file_path):
    with open(file_path, 'r') as f:
        return zip(*map(lambda x: (int(x[0]), int(x[1])), map(lambda x: x.split(':', 1), f.readline().strip(' \n\r\t').split(' '))))


@lru_cache
def bucket_squared_error(start, end):
    return (PP[end]-PP[start-1])-((P[end]-P[start-1])**2)/(end-start+1)


@lru_cache
def get_optimal_histogram(start, end, b):
    if b == 1:
        return bucket_squared_error(start, end), [[start, end]]
    min_error = float('inf')
    best_intervals = []
    for x in range(start, end):  # It is end-1 in range, so fits our goal
        left_side_val, left_intervals = get_optimal_histogram(start, x, b-1)
        right_side_val = bucket_squared_error(x+1, end)
        if left_side_val + right_side_val < min_error:
            min_error = left_side_val + right_side_val
            # We always add a new bucket since with an extra partition we are guaranteed
            # to obtain the same or smaller total squared error
            best_intervals = left_intervals + [[x+1, end]]
    return min_error, best_intervals


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--B', help='Maximum number of buckets', type=int, required=True)
    parser.add_argument('--sequence-file', help='File path containing the elements and their frequencies',
                        required=True)

    args = parser.parse_args()
    B = args.B
    sequence_file_path = args.sequence_file

    values, frequencies = parse_sequence_file(sequence_file_path)
    if any(j-i != 1 for (i,j) in zip(values, values[1:])):
        raise ValueError('Invalid sequence (check order, duplicates or gaps between values)')
    if B > len(values):
        raise ValueError('Cannot specify more buckets than values in the sequence')

    # We store an offset just in case we start by an element different from 1
    # (but we expect them to be consecutive)
    OFFSET_W_1 = values[0] - 1
    values = [i-OFFSET_W_1 for i in values]
    
    P = [0]
    PP = [0]
    for i, i_freq in enumerate(frequencies, start=1):
        P.append(P[i-1] + i_freq)
        PP.append(PP[i-1] + i_freq**2)

    print(P)
    print(PP)
    print(values)
    
    total_error, final_intervals = get_optimal_histogram(values[0], values[-1], B)
    histogram_values = [(P[x[1]] - P[x[0]-1])/(x[1]-x[0]+1) for x in final_intervals]
    # Undo the offset
    final_intervals = list([x[0] + OFFSET_W_1, x[1] + OFFSET_W_1] for x in final_intervals)

    print(f'V-Optimal histogram buckets: {final_intervals}, values: {histogram_values}, '
          f'total squared error = {total_error}')
