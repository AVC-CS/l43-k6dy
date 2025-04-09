def main():
    total = 0

    i = 0
    while i < 5:
        num = int(input("Enter a number: "))
        total += num
        i += 1

    return total


if __name__ == '__main__':
    result = main()
    print(result)