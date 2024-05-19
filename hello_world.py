from prefect import flow


@flow(log_prints=True)
def hello_world(name: str = "world", goodbye: bool = False):
    print(f"Hello {name} from Prefect! 🤗")

    if goodbye:
        print(f"Goodbye {name}!")


if __name__ == "__main__":
    hello_world.from_source(
        source="https://github.com/xcematin/prefect-nocodb.git",
        entrypoint="hello_world.py:hello_world",
    ).deploy(name="Scrumball-Bot-Instagram", work_pool_name="Test")