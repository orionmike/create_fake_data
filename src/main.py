
from data.post import create_category_post_list, create_post_list, create_tag_list
from data.product import create_category_list, create_product_list
from data.user import create_user_list


def main() -> None:

    create_user_list(100)

    create_category_list(10)
    create_product_list(1000)

    create_category_post_list(10)
    create_tag_list(30)
    create_post_list(200)


if __name__ == "__main__":
    main()
