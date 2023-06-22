# Third-party libraries
from typing import Annotated, Union

from fastapi import APIRouter, Path, Query, Body
from fastapi.openapi.models import RequestBody
from pydantic import BaseModel

# User-defined libraries
from schema import Output, OutputesController, InputesController, UpdateController, DeleteController, Item
from samples import postdata

# router initialization
basic = APIRouter()

# temp storage
datastore = []


@basic.get('/welcome', response_model=str)
async def welcome():
    return "Welcome"


@basic.get('/input_controller', response_model=Output)
async def input_controller():
    output = Output()
    for i, data in enumerate(datastore):
        oc = OutputesController()
        oc.id = i + 1
        oc.status = data
        oc.comment = f"current status of the api is in {data}"
        output.data.append(oc)

    return output


@basic.post('/input_controller', response_model=OutputesController)
async def create_input_controller(input_value: InputesController, data: dict):
    datastore.append(input_value.value)
    oc = OutputesController()
    oc.id = len(datastore)
    oc.status = input_value.value
    oc.comment = f"current status of the api is in {input_value.value}"

    return oc


@basic.put('/input_controller/{id}', response_model=UpdateController)
async def update_controller(id: int, updatedata: InputesController):
    update_response = UpdateController()
    update_response.id = id
    try:
        datastore[id - 1] = updatedata.value
        update_response.status = "Updated successfully"
    except IndexError:
        update_response.status = "Invalid id for update controller"

    return update_response


@basic.patch('/input_controller/{id}', response_model=UpdateController)
async def patch_controller(id: int, updatedata: str):
    update_response = UpdateController()
    update_response.id = id

    try:
        datastore[id - 1] = updatedata
        update_response.status = "Patch update completed successfully"
    except IndexError:
        update_response.status = "Invalid id for patch update controller"

    return update_response


@basic.delete('/input_controller/{id}', response_model=DeleteController)
async def delete_controller(id: int):
    delete_response = DeleteController()
    try:
        del datastore[id - 1]
        delete_response.status = "success"
        delete_response.message = "Deleted successfully"
    except IndexError:
        delete_response.status = "failed"
        delete_response.message = f"Could not delete controller id {id}"

    return delete_response


class Item1(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


@basic.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item1, user: User, importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results