# miner

A single module [FastAPI](https://fastapi.tiangolo.com) and [Strawberry](https://strawberry.rocks) app that handles a graphql query.

## Quick Start

Ensure python 3.7+ is on your path, then in the root of this project:

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

To run tests, autoformatting or linting, first install all dev libraries:
```bash
(venv) % pip install -r requirements-dev.txt
```

Then:
- `black .` to autoformat
- `ruff .` to lint
- `pytest .` to run tests


If this were a more sophisticated project, I'd:
- split code into python packages and modules (a single `main.py` is appropriate for a small example, but a production service would typically contain more code; splitting into multiple files and directories allows clearer separation of concerns if correctly composed)
- add more unit tests (thanks to the runtime checks in Strawberry and Pydantic and static analysis via Pylance/ MyPy, there's not really much to test here outside of the dependencies themselves)
- add a mutation to create a `Person` and persist it somewhere (in memory? Redis? MongoDB? PostgreSQL?)
- containerize the api for production (and it's dependencies via compose for local development)
- depending on where the image is being deployed, use IaC such as Terraform, AWS CDK, ArgoCD to do that deployment
- add a github actions workflow to run linting and testing and deploy it

## Related examples

For more interesting examples, see:

- [groundsim](https://github.com/followben/groundsim) - a more complex (albeit still simple) graphql project using a similar stack which includes mutations, REST, a basic visualisation of the data in React, containerization, cloud deployment via CI/ CD etc.
- [datalogger](https://github.com/followben/datalogger) - an older sample api using Django and Graphene.
