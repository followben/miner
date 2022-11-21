import enum

import strawberry
from fastapi import FastAPI
from pydantic import BaseModel
from strawberry.fastapi import GraphQLRouter

app = FastAPI()


# Pydantic types validate input


class StateTerritory(str, enum.Enum):
    NSW = "NSW"
    VIC = "VIC"
    QLD = "QLD"
    NT = "NT"
    ACT = "ACT"
    TAS = "TAS"
    WA = "WA"
    SA = "SA"


class Address(BaseModel):
    number: int
    street: str
    city: str
    state: StateTerritory


class Person(BaseModel):
    email: str
    name: str
    address: Address


# Strawberry uses a code-first GraphQL schema can just bootstrap with pydantic

# Register enums manually for now
# https://github.com/strawberry-graphql/strawberry/issues/1598
strawberry.enum(StateTerritory)


@strawberry.experimental.pydantic.type(model=Address, all_fields=True)
class AddressType:
    pass


@strawberry.experimental.pydantic.type(model=Person, all_fields=True)
class PersonType:
    pass


# Define our Query type to support querying person returning sample data
@strawberry.type
class Query:
    @strawberry.field
    def person(self) -> PersonType:
        sample = {
            "email": "a.miner@example.com",
            "name": "Ashley Miner",
            "address": {
                "number": 99,
                "street": "Hyalite St",
                "city": "Sydney",
                "state": "NSW",
            },
        }
        return Person(**sample)


# Create the schema and serve it via a FastAPI endpoint
schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
