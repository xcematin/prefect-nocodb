from prefect import flow
import requests
@flow(log_prints=True)
def hello_world(username: str,rowId: str,server: str):
    print(f"Hello {username}! Welcome to Scrumball-Bot-Instagram!")
    print(f"RowId: {rowId}")
    print(f"Server: {server}")
    if username and rowId and server:
        print(f"Update {username} data from Server! 🤗")
        response = requests.post(server,json={"username": username, "rowId": rowId})
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