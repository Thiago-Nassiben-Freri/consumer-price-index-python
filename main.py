from time import sleep 
import cpi_calc


def exit():
    print('Okay, exit...')
    sleep(2)
    print('Program finished!')

def cpi_ux():
    while True: 
        var_choice = str(input('Do you want to use the CPI Calculator? [Y/N]: '))

        if var_choice.upper() == 'Y':
            try:
                var_value = float(input('Enter the value: '))
                var_year = int(input('Enter the year you want to know the CPI: '))

                var_cpi = cpi_calc.Consumer_Price_Index(var_value, var_year)

                if var_cpi is not None:
                    print(f'The value ${var_value} in {var_year} will be worth ${var_cpi[0]:.2f} today.')
                    print(f'The CPI percentage for {var_year} compared to today is {var_cpi[1]:.2f}%.')
                else:
                    print('CPI data for the specified year does not exist.')
            except ValueError:
                print('Error: Please enter a valid number.')
        elif var_choice.upper() == 'N': 
            exit()
            break
        else:
            print(f'Error: invalid_choice!')

if __name__ == '__main__':
    cpi_ux()

