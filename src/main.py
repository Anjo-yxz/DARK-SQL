import os
from full.exe import execute


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(base_dir, "database", "database.txt")

    if not os.path.exists(database_path):
        print(f"arquivo nao encontrado: {database_path}")
        return

    app = execute()
    app.execute(database_path)


if __name__ == "__main__":
    main()
