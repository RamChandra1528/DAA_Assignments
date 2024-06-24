def first_bad_version(n, is_bad_version):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if is_bad_version(mid):
            right = mid
        else:
            left = mid + 1
    return left


def is_bad_version(version):
    return version >= 4

n = 5
print(first_bad_version(n, is_bad_version))
