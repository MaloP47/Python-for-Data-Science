"""2_DataTable ex02"""

from load_csv import load
import matplotlib.pyplot as plt


def MtoInt(value):
    if isinstance(value, str):
        value = value.lower()
        if value.endswith('k'):
            return int(float(value.replace('k', '')) * 1_000)
        elif value.endswith('m'):
            return int(float(value.replace('m', '')) * 1_000_000)
    return int(value)


def main():
    """Main fonction"""
    try:
        data = load('../data/population_total.csv')

        france = data[data['country'] == 'France']
        belgium = data[data['country'] == 'Belgium']
        years = france.columns[1:]
        years = years.map(int)

        for year in years:
            belgium.loc[:, str(year)] = belgium.loc[:, str(year)].apply(MtoInt)
            france.loc[:, str(year)] = france.loc[:, str(year)].apply(MtoInt)

        popFrance = france.iloc[0, 1:].values
        popBelgium = belgium.iloc[0, 1:].values

        plt.plot(years, popFrance, color='g', label='France')
        plt.plot(years, popBelgium, color='b', label='Belgium')

        plt.title('Population Projections')
        plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
        plt.xlim(1800, 2040)
        plt.xlabel('Year')

        ticks = range(0, 80_000_000, 20_000_000)
        labels = ['0', '20M', '40M', '60M']
        plt.yticks(ticks, labels)

        plt.ylabel('Population')
        plt.legend(loc='lower right')
        p = '/mnt/c/Users/Malo/OneDrive/Documents/PythonMatplot/FrVsOther.png'
        plt.savefig(p)

    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
