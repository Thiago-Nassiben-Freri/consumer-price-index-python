import requests


def get_cpi(year):
    url = f'https://api.bls.gov/publicAPI/v2/timeseries/data/CUUR0000SA0?startyear={year}&endyear={year}'
    response = requests.get(url)
    if response.status_code == 200: 
        data = response.json()
        try: 
            cpi_value = data['Results']['series'][0]['data'][0]['value']
            return float(cpi_value)
        except(KeyError, IndexError):
            print("Error: Unable to retrieve CPI data for the year")
            return None 
    else:
        print(f"Error: Failed to fetch CPI data. HTTP Status Code: {response.status_code}")
        return None

def Consumer_Price_Index(value, year, today=2023): 
    cpi_year = get_cpi(year)
    cpi_today = get_cpi(today)
    if cpi_year is not None and cpi_today is not None: 
        adjusted_value = value * (cpi_today / cpi_year)
        percentage_cpi = (cpi_today / cpi_year) * 100
        return adjusted_value, percentage_cpi
    else:
        return None