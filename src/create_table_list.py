from database.database import Base, engine
from database.models import CategoryProduct, Product, User


def recreate_table_list(table_list, engine):
    for model in table_list:
        try:
            model.__table__.drop(engine)
        except:
            pass
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    # Base.metadata.create_all(engine)
    recreate_table_list([CategoryProduct, Product,  User], engine)
