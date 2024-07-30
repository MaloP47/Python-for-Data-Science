from give_bmi import give_bmi, apply_limit


def main():
    try:
        # height = [2.71, 1.15,]
        # weight = [165.3, 38.4]
        # height = [2.71, 1.15, 0]
        # weight = [165.3, 38.4]
        # height = [2.71, 1.15,'Hi']
        # weight = [165.3, 38.4, 12]
        # height = [2.71, 1.15, 4]
        # weight = [165.3, 38.4, 12]
        # height = [2.71, 1.15, 0.7]
        # weight = [165.3, 38.4, 120]
        height = [2, 2, 1]
        weight = [140, 70, 120]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except AssertionError as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
