import datetime

def cost_calculation(start_year, start_month, start_day, end_year, end_month, end_day, meter_setings_end, meter_setings_start, cost, standing_cost):

    start_date = datetime.datetime(start_year, start_month, start_day)
    end_date = datetime.datetime(end_year, end_month, end_day)

    date_dif = end_date - start_date

    day_dif = date_dif.days

    meter_setings_dif = meter_setings_end - meter_setings_start

    calculation = ((day_dif * standing_cost) + (meter_setings_dif * cost) * 1.25) / 100

    return calculation

while True:
    try:
        start_year = int(input("start year: "))
        start_month = int(input("start month: "))
        start_day = int(input("start day: "))
        print()

        end_year = int(input("end year: "))
        end_month = int(input("end month: "))
        end_day = int(input("end day: "))
        print()

        meter_setings_start = int(input("start meter setings: "))
        meter_setings_end = int(input("end meter setings: "))
        print()

        cost = int(input("electricity cost: "))
        standing_cost = int(input("standing cost: "))
        print()

        break
    except ValueError:
        print("invalid number")
    except KeyboardInterrupt:
        break

print()
print(str(cost_calculation(start_year, start_month, start_day, end_year, end_month, end_day, meter_setings_end, meter_setings_start, cost, standing_cost)) + " sek")
print()