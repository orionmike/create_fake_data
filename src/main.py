
from data.user import create_users


def main() -> None:

    create_users(100, delete=True)


if __name__ == "__main__":
    main()
