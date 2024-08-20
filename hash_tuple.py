if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    print(hash(tuple(integer_list)))


# Example input:
# 3
# 123

# Expected output:
# -6888551435698806353