def get_max():
    grades = [9.6, 9.2, 9.7]

    max_local = max(grades)
    min_local = min(grades)
    min_max = f"Max: {max_local}, Min: {min_local}"
    return min_max


min_max_global = get_max()
print(min_max_global)