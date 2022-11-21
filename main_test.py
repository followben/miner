from main import schema


def test_returns_expected_sample_data():
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
