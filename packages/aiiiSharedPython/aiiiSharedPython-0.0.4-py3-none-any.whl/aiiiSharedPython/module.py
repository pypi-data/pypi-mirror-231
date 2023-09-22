def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def echo(value):
    print(value)

def send_ga_log(client_id: str, events: list, measurement_id: str, api_secret: str):
    try:
        url = f"https://www.google-analytics.com/mp/collect?measurement_id={measurement_id}&api_secret={api_secret}"
        body = {
            "client_id": client_id,
            "events": events
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=body, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception:
        raise