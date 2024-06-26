import requests


def get_data(place, forecast_days=None, kind=None):
    api_key = "d9b34069c72fc45b35f44fd7f1f2f912"
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days  # 8 registos por dia
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))