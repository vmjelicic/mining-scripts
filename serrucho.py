import matplotlib.pyplot as plt
from typing import Tuple

ORE_TONNAGE = [400, 300, 280, 150, 360, 140]
WASTE_TONNAGE = [530, 500, 120, 200, 330, 580]
ORE_RATE = [35, 35, 30]
WASTE_RATE = [30, 45, 50]
ORE_TIME_RATE = [0, 24]
MINE_STATUS = 1  # 0: Abandonado, 1: Mina Nueva
STOCK_MONTHS = 2


def ore_schedule(
    ore_tonnage: list, ore_rate: list, time: list, mine_status: int, stock_months: int
) -> Tuple[list, list]:
    """
    docstring
    """
    time.append(9999)
    ore_time = [0]
    ore_movement = []
    partial_time = 0
    index_rate = 0
    if mine_status == 1:
        ore_movement.append(ore_tonnage[0])
        ore_tonnage[0] -= stock_months * ore_rate[0]
        ore_tonnage[-1] += stock_months * ore_rate[-1]

    else:
        ore_movement.append(ore_tonnage[0] + stock_months * ore_rate[0])
        ore_tonnage[-1] += stock_months * ore_rate[-1]

    for i in range(len(ore_tonnage)):
        if i != 0:
            ore_time.append(partial_time)
            ore_movement.append(ore_tonnage[i])

        partial_time += round(
            ore_tonnage[i] / ore_rate[index_rate], 2
        )
        if partial_time <= time[index_rate + 1]:
            ore_time.append(partial_time)
            if i != len(ore_tonnage) - 1:
                ore_movement.append(stock_months * ore_rate[index_rate])
            else:
                ore_movement.append(0)
        else:
            partial_tonnage = (partial_time - time[index_rate + 1]) * ore_rate[
                index_rate
            ]
            partial_tonnage -= stock_months * (
                ore_rate[index_rate + 1] - ore_rate[index_rate]
            )
            partial_time = time[index_rate + 1]
            ore_time.append(partial_time)
            ore_movement.append(partial_tonnage)
            index_rate += 1
            partial_time += round(partial_tonnage / ore_rate[index_rate], 2)
            ore_time.append(partial_time)
            ore_movement.append(stock_months * ore_rate[index_rate])

    return ore_time, ore_movement


def waste_schedule(waste_tonne, waste_rate, time):
    """
    docstring
    """
    pass


def plot(x, y):
    plt.plot(x, y)
    plt.xlabel("Tiempo [meses]")
    plt.ylabel("Tonelaje [Kt]")
    plt.title("Serrucho")
    for i_x, i_y in zip(x, y):
        plt.text(i_x, i_y, "({}, {})".format(round(i_x, 1), round(i_y, 1)))
    plt.show()


ore_t, ore_mov = ore_schedule(
    ORE_TONNAGE, ORE_RATE, ORE_TIME_RATE, MINE_STATUS, STOCK_MONTHS
)

print(ore_t, ore_mov, sep="\n")
plot(ore_t, ore_mov)
