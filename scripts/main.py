from sqlmodel_poc.crud.commands import (  # type: ignore
    create_instance,
    delete_instance,
    update_instance,
    get_instance,
)

from sqlmodel_poc.database.tables import Location  # type: ignore


def run():
    location = create_instance(Location(name="Test", lat=0.0, lng=0.0))
    print(location)
    update_instance(model=Location, instance_id=location.id, name="Test2")
    location = get_instance(Location, location.id)
    print(location)

    delete_instance(Location, location.id)
