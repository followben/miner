from main import schema

from graphql import GraphQLError, SourceLocation


def test_query_returns_sample_data():
    query = """
        query {
            person {
                email
                name
                address {
                    number
                    street
                    city
                    state
                }
            }
        }
    """

    result = schema.execute_sync(query)

    assert result.errors is None
    assert result.data["person"] == {
        "email": "a.miner@example.com",
        "name": "Ashley Miner",
        "address": {
            "number": 99,
            "street": "Hyalite St",
            "city": "Sydney",
            "state": "NSW",
        },
    }


def test_schema_validates_incorrect_input():
    query = """
        query {
            person {
                foo
                address {
                    bar
                }
            }
        }
    """

    result = schema.execute_sync(query)
    assert len(result.errors) is 2
    assert result.errors[0].message == "Cannot query field 'foo' on type 'PersonType'."
    assert result.errors[1].message == "Cannot query field 'bar' on type 'AddressType'."
