# Cookiecutter Cdk8s Python app

This is a cookiecutter template for creating cdk8s projects without the cdk8s cli. It differs from the primary cdk8s python framework in the following ways:
- No cdk8s cli or npm dependency (NOTE: there's still a nodejs runtime dependency for the cdk8s python module) allowing for smaller and less opinionated build/run environments.
- No requirement to use Pipenv. A simple requirements.txt + venv workflow is assumed but any python dependency management tool can be used.
- Manifests are synthesized to both the standard `dist/` path _and_ to stdout by default using rhe cli.run() function in the [cdk8s_utils module here.](TODO) This allows for direct piping into various validtion tools as well as kubectl apply etc.
- A default Dockerfile is provided for both building/running the app (i.e. synthesizing the manifests) and for use in a [devcontainer](https://containers.dev).
- A basic set of example tests + fixtures are provided to demonstrate writing assertions on the rendered manifests.

## Usage

To use this project first [install cookiecutter.](https://cookiecutter.readthedocs.io/en/stable/README.html#installation)

Then run:
```
cookiecutter gh:nalbury/cookiecutter-cdk8s-python-app
```

You'll be prompted to enter a project name:
```
  [1/2] project_name (Cookiecutter CDK8s Python App): cdk8s-cookiecutter-test
  [2/2] project_slug (cdk8s-cookiecutter-test):
```

After completing the prompts, a new directory matching the project_slug will be created containing the initial scaffold for a Cdk8s python app. You can run the app with the scaffolded code either using a local python/node env + the provided Makefile (the provided devcontainer.json can be used to create this for local dev purposes):
```
MANIFESTS_ARGS="--help" make manifests 
```

Or you can use the provided dockerfile for a more portable exacutable format:
```
docker build -t cdk8s-app:local . && docker run cdk8s-app:local --help
```

Inpect [`app/main.py`](./{{%20cookiecutter.project_slug%20}}/app/main.py) and [`tests/test_main.py`](./{{%20cookiecutter.project_slug%20}}/tests/test_main.py) for more details on providing user inputs via a YAML config file and writing tests to validate the rendered output.
