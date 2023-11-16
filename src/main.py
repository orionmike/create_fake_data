
from data.product import create_category_list, create_product_list
from data.user import create_user_list


def main() -> None:

    create_user_list(100, delete=True)
    create_category_list(10, delete=True)
    create_product_list(1000, delete=True)


if __name__ == "__main__":
    main()
