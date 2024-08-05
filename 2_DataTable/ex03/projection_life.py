"""2_DataTable ex03"""

from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Main fonction"""
    try:
        normFile = 'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
        dataLife = load('../data/life_expectancy_years.csv')
        dataIncome = load(f'../data/{normFile}')

        life = dataLife['1900']
        income = dataIncome['1900']

        plt.title('1900')
        plt.scatter(income, life, color='r', alpha=0.5, marker='^')
        # plt.scatter(income, life)
        plt.xlabel('Gross domestic product')
        plt.xscale('log')
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.ylabel('Life Expectancy')
        plt.grid(True)
        p = '/mnt/c/Users/Malo/OneDrive/Documents/PythonMatplot/1900.png'
        plt.savefig(p)

    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
