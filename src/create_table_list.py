from database.database import Base, engine
from database.models_post import CategoryPost, Post, Tag, AssociationPostTag
from database.models_user import User
from database.models_product import CategoryProduct, Product


def recreate_table_list(table_list, engine) -> None:
    for model in table_list:
        try:
            model.__table__.drop(engine)
        except:
            pass
    Base.metadata.create_all(engine)


if __name__ == '__main__':

    # Base.metadata.create_all(engine)

    # recreate_table_list([User], engine)

    # recreate_table_list([CategoryProduct, Product], engine)
    recreate_table_list([CategoryPost, Tag, AssociationPostTag, Post], engine)
    # recreate_table_list([AssociationPostTag, Post], engine)
