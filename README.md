# miner

A simple project demonstrating the use of [FastAPI](https://fastapi.tiangolo.com) and [Strawberry](https://strawberry.rocks) to handle a graphql query.

## Quick Start

Ensure python >=3.7+ is on your path, then:

```bash
% python -m venv venv
% source venv/bin/activate
(venv) % pip install --upgrade pip setuptools wheel
(venv) % pip install -r requirements.txt
(venv) % uvicorn main:app
```

Then, either issue a standard HTTP `POST` request via your favourite cli:

```bash
curl -g \
-X POST \
-H "Content-Type: application/json" \
-d '{"query":"query{person {email name address { number street city state }}}"}' \
http://localhost:8000/graphql
```

Or submit the same query via the browser at `http://localhost:8000/graphql`:

```graphql
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
```

## Related examples

For more interesting examples, see:

- [groundsim](https://github.com/followben/groundsim) - a more complex containerized graphql project using a similar stack which includes mutations, REST, a basic visualisation of the data in React, and deploys via CI/ CD to the cloud.
- [datalogger](https://github.com/followben/datalogger) - an older sample api using Django and Graphene.