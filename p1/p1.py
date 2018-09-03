def main():
    my_sum = 0
    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            my_sum += num
    print(my_sum)


if __name__ == "__main__":
    main()
