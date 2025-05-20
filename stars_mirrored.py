def star_mirror(n):
    spaces = n-1
    stars = 1
    op = []
    while stars < 2*n:
        op.append(spaces*" " + stars * "*" + spaces*" ")
        spaces -= 1
        stars += 2
    print(f"op------------{op}")
    print(f"stars--------{stars}")
    print(f"spaces------{spaces}")
    stars -= 4
    spaces = 1
    while stars > 0:
        print(f"spaces---->>>>>>{spaces}")
        op.append(spaces * " " + "*" * stars + " " * spaces)
        spaces += 1
        stars -= 2
    return op

# Example usage
if __name__ == "__main__":
    n = 3
    print(star_mirror(n))
    # Output: ['    *****    ', '   *********   ', '  ***********  ', ' ************* ', '***************']