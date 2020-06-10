import research


def main():
    print("Weather research data for Seattle, 2014-2015")
    print()
    research.init('nyc.csv')
    hot_days = research.hot_days()
    cold_days = research.cold_days()
    wet_days = research.wettest_days()

    print('======================================')
    print("The 5 hottest days:")
    for idx, d in enumerate(hot_days[:5], 1):
        print(f"{idx}. {d.date}: {d.actual_max_temp}F")
    print('======================================')
    print("The 5 coldest days:")
    for idx, d in enumerate(cold_days[:5], 1):
        print(f"{idx}. {d.date}: {d.actual_min_temp}F")
    print('======================================')
    print("The 5 wettest days:")
    for idx, d in enumerate(wet_days[:5], 1):
        print(f"{idx}. {d.date}: {d.actual_precipitation}in")


if __name__ == '__main__':
    for _ in range(1, 100):
        main()
