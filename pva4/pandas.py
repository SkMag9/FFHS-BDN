import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    start_value = 0
    end_value = 361
    step_size = 0.01
    interval_size = 5
    multiplier = (1 / step_size)
    pd.set_option('display.max_rows', end_value)

    # 1
    print("\n\n\n")
    print(" =======================================================\n",
          "1. Datapoints:\n",
          "=======================================================\n")
    datapoints = pd.Series(np.arange(start_value, end_value, step_size))
    print(datapoints)

    # 2
    print("\n\n\n")
    print(" =======================================================\n",
          "2. Sin Values:\n",
          "=======================================================\n")
    datapoints_sin = datapoints.apply(lambda x: np.sin(np.deg2rad(x)))
    print(datapoints_sin)

    # 3
    print("\n\n\n")
    print(" =======================================================\n",
          "3. Means:\n",
          "=======================================================\n")
    sin_means = pd.DataFrame({'Interval': [], 'Mean': []})
    for i in range(start_value, int(end_value/interval_size)):
        interval_start = int(i * interval_size * multiplier)
        interval_end = int((i+1) * interval_size * multiplier)

        interval_mean = datapoints_sin[interval_start:interval_end].mean()

        dataframe_entry = pd.DataFrame({'Interval': [i * interval_size], 'Mean': [interval_mean]})

        sin_means = pd.concat([sin_means, dataframe_entry], ignore_index=True)

    print(sin_means)

    # 4
    plt.figure(figsize=(10, 6))
    plt.bar(sin_means['Interval'].tolist(), sin_means['Mean'], width=interval_size*0.75, align='edge')
    plt.xlabel('Intervalle')
    plt.ylabel('Mittelwerte der Sinus-Werte')
    plt.title(f'Mittelwerte der Sinus-Werte für Intervalle von {interval_size} Grad')

    plt.show()


if __name__ == '__main__':
    main()
