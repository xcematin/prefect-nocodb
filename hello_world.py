from prefect import flow
import requests
@flow(log_prints=True)
def hello_world(name: str,rowId: str,server_url: str):
    if name and rowId and server_url:
        print(f"Update {name} data from Server! 🤗")
        response = requests.post(server_url,json={"name": name, "rowId": rowId})
        if response.status_code == 200:
            print(f"Data updated successfully! 🤗")
        else:
            raise ValueError(f"Error while updating data! 😔")
    else:
        raise ValueError("Name and rowId and server_url are required!")
    

if __name__ == "__main__":
    hello_world.from_source(
        source="https://github.com/xcematin/prefect-nocodb.git",
        entrypoint="hello_world.py:hello_world",
    ).deploy(name="Scrumball-Bot-Instagram", work_pool_name="Test")