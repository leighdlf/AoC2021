import numpy as np
from scipy import stats

with open("03.txt", "r") as file:
    binary = np.array([[int(bit) for bit in line.strip("\n")] for line in file])

def power_consumption():
    # Selects for the modes along the first axis, excludes counts.
    bits = stats.mode(binary)[0][0]

    gamma_rate, epsilon_rate = '', ''
    for bit in bits:
        gamma_rate += str(bit)
        epsilon_rate += '1' if bit == 0 else '0'
    return eval(f"0b{gamma_rate}") * eval(f"0b{epsilon_rate}")  # Hack to get binary.


def life_support():

    def helper(index, array, mode):
        """Recursive helper function."""
        if len(array) == 1:  # Base case.
            return array[0]
        else:
            modes = stats.mode(array)
            vals, counts = modes[0][0], modes[1][0]

            if counts[index] % (len(array) // 2) == 0:  # If both occur the same amount.
                index_array = np.where(array[:, index] == mode)[0]
            else:
                if mode:  # Switching between mode and the non-mode value.
                    index_array = np.where(array[:, index] == vals[index])[0]
                else:
                    co2_val = 1 if not vals[index] else 0
                    index_array = np.where(array[:, index] == co2_val)[0]

            new_array = np.array([[array[i]] for i in index_array])[:, 0]
            return helper(index + 1, new_array, mode)

    def array_to_string(array):
        num_string = ''
        for num in array:
            num_string += str(num)
        return num_string

    o_gen = array_to_string(helper(0, binary, 1))
    co2_scrub = array_to_string(helper(0, binary, 0))

    return eval(f"0b{o_gen}") * eval(f"0b{co2_scrub}")
