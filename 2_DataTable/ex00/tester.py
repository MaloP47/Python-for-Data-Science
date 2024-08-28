from load_csv import load


def main():
    try:
        ld = "../data/test_life_expectancy_years.csv"
        print(type(load(ld)))
        # print(load("../data/life_expectancy_years.csv"))
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
