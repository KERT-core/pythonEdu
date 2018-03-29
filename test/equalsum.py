
def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    # check if the partial sum is equals to target
    if s == target:
        print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])
    return 

if __name__ == "__main__":
    print(subset_sum([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 22))