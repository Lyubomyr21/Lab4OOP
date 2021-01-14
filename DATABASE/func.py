from sqlalchemy import or_
from Models import Session, Customer, Goods


def create_entry(model_class, *, commit=True, **kwargs):
    session = Session()
    entry = model_class(**kwargs)
    session.add(entry)
    if commit:
        session.commit()
    return entry


def delete_entry(model_class, id, *, commit=True):
    session = Session()
    session.query(model_class).filter_by(id=id).delete()
    session.commit()


def get_entry_by_id(model_class, id, **kwargs):
    session = Session()
    return session.query(model_class).filter_by(id=id, **kwargs).one()


def list_goods(*filters):
    session = Session()
    return (
        session.query(Goods)
        .all()
    )