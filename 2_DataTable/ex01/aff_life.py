"""2_DataTable ex01"""

from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Main fonction"""
    try:
        data = load('../data/life_expectancy_years.csv')

        france = data[data['country'] == 'France']
        years = france.columns[1:]
        age = france.values[0][1:]

        plt.plot(years, age, label='Life expectancy')
        plt.title('France Life expectancy Projections')
        plt.xticks(years[::40])
        plt.xlabel('Year')
        plt.yticks(range(30, 100, 10))
        plt.ylabel('Life expectancy')
        plt.legend(loc='center right')
        p = '/mnt/c/Users/Malo/OneDrive/Documents/PythonMatplot/life.png'
        plt.savefig(p)

    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
