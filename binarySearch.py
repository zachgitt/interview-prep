def binarySearchRecursive(vals, target, left, right):
    # Not found
    if left > right:
        return -1

    # Found
    mid = (left + right) / 2
    if vals[mid] == target:
        return mid

    # Look left
    elif target < vals[mid]:
        return binarySearchRecursive(vals, target, left, mid-1)

    # Look right
    else:
        return binarySearchRecursive(vals, target, mid+1, right)

def binarySearchIterative(vals, target):
    left = 0
    right = len(vals) - 1

    count = 0
    while left <= right:
        # Find middle
        mid = int((right + left) / 2)

        # Found idx
        if vals[mid] == target:
            return mid

        # Go left
        elif target < vals[mid]:
            right = mid - 1

        # Go right
        else:
            left = mid + 1

        count += 1
        if count == 10:
            break

    # Not found
    return -1


if __name__ == '__main__':

    """
    Tests:
        Even size array
        Odd size array
        All the way left
        All the way right
        Nonexistant target -- between two vals
        Nonexistant target -- out of range
    """
    tests = [
        ([1, 2, 4, 6, 8, 9], 4),
        ([1, 2, 3, 4, 5], 5),
        ([1, 2, 3, 4, 6], 1),
        ([1, 2, 3, 4, 5], 0)
    ]
    expects = [
        2,
        4,
        0,
        -1
    ]
    for test, expect in zip(tests, expects):
        iterative = binarySearchIterative(test[0], test[1])
        recursive = binarySearchIterative(test[0], test[1])
        print('iterative={} recursive={} expect={}'.format(iterative, recursive, expect))
        assert(iterative == expect)
        assert(recursive == expect)
