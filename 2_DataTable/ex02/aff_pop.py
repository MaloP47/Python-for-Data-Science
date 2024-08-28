"""2_DataTable ex02"""

from load_csv import load
import matplotlib.pyplot as plt


def dataToFloat(value) -> float:
    """Convert value to float"""
    if isinstance(value, str):
        value = value.lower()
        if value.endswith('k'):
            return float(value.replace('k', '')) * 1_000
        elif value.endswith('m'):
            return float(value.replace('m', '')) * 1_000_000
        elif value.endswith('b'):
            return float(value.replace('b', '')) * 1_000_000_000
    return float(value)


# def main():
#     """Main fonction"""
#     try:
#         data = load('../data/population_total.csv')

#         france = data[data['country'] == 'France']
#         belgium = data[data['country'] == 'Belgium']

#         years = france.columns[1:].astype(int)
#         yearsRange = (years <= 2050)
#         vY = years[yearsRange]

#         popFr = france.iloc[0, 1:].apply(dataToFloat)
#         popBel = belgium.iloc[0, 1:].apply(dataToFloat)

#         popFr = popFr[yearsRange]
#         popBel = popBel[yearsRange]

#         findMax = max(max(popFr), max(popBel))

#         yR = [year for year in vY if 1800 <= year <= 2040 and year % 40 == 0]

#         plt.plot(vY, popFr, label='France', color='g')
#         plt.plot(vY, popBel, label='Belgium', color='b')

#         plt.title('Population Projections')

#         plt.xticks(yR)
#         plt.xlabel('Year')

#         plt.ylabel('Population')
#         tickY = [i * 20e6 for i in range(1, int(findMax / 20e6) + 1)]

#         plt.yticks(tickY, ["{:,.0f}M".format(pop / 1e6) for pop in tickY])

#         plt.legend(loc='lower right')

#         p = './FrVsOth.png'
#         plt.savefig(p)

#     except Exception as e:
#         print(f'Error: {e}')

def main():
    """Main fonction"""
    try:
        data = load('../data/population_total.csv')

        france = data[data['country'] == 'France']
        belgium = data[data['country'] == 'Belgium']
        china = data[data['country'] == 'China']

        years = france.columns[1:].astype(int)
        yearsRange = (years <= 2050)
        vY = years[yearsRange]

        popFr = france.iloc[0, 1:].apply(dataToFloat)
        popBel = belgium.iloc[0, 1:].apply(dataToFloat)
        popCn = china.iloc[0, 1:].apply(dataToFloat)

        popFr = popFr[yearsRange]
        popBel = popBel[yearsRange]
        popCn = popCn[yearsRange]

        findMaxCn = max(max(popFr), max(popBel), max(popCn))

        yR = [year for year in vY if 1800 <= year <= 2040 and year % 40 == 0]

        plt.plot(vY, popFr, label='France', color='g')
        plt.plot(vY, popBel, label='Belgium', color='b')
        plt.plot(vY, popCn, label='China', color='r')

        plt.title('Population Projections')

        plt.xticks(yR)
        plt.xlabel('Year')

        plt.ylabel('Population')
        tickY = [i * 200e6 for i in range(1, int(findMaxCn / 200e6) + 1)]

        plt.yticks(tickY, ["{:,.0f}M".format(pop / 1e6) for pop in tickY])

        plt.legend(loc='lower right')

        p = './FrVsO.png'
        plt.savefig(p)

    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
