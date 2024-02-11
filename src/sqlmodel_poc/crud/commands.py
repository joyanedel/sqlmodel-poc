from typing import TypeVar, Type
from typing_extensions import Unpack
from sqlmodel import SQLModel, Session

from sqlmodel_poc.database.connection import engine as connection
from sqlmodel_poc.crud.exceptions import InstanceNotFound

T = TypeVar("T", bound=SQLModel)


def create_instance(instance: T) -> T:
    with Session(connection) as session:
        session.add(instance)
        session.commit()
        session.refresh(instance)
    return instance


def get_instance(model: Type[T], instance_id: int) -> T:
    with Session(connection) as session:
        instance = session.get(model, instance_id)

        if instance is None:
            raise InstanceNotFound(f"{model.__name__} with id {instance_id} not found")
    return instance


def delete_instance(model: Type[T], instance_id: int) -> T:
    with Session(connection) as session:
        instance = session.get(model, instance_id)

        if instance is None:
            raise InstanceNotFound(f"{model.__name__} with id {instance_id} not found")

        session.delete(instance)
        session.commit()
        return instance


def update_instance(model: Type[T], instance_id: int, **kwargs: Unpack[T]) -> T:  # type: ignore
    with Session(connection) as session:
        instance = session.get(model, instance_id)

        if instance is None:
            raise InstanceNotFound(f"{model.__name__} with id {instance_id} not found")

        for key, value in kwargs.items():
            setattr(instance, key, value)
        session.commit()
        return instance
