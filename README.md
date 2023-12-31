# Cookiecutter Cdk8s Python app

This is a cookiecutter template for creating cdk8s projects without the cdk8s cli. It differs from the primary cdk8s python framework in the following ways:
- No cdk8s cli or npm dependency (NOTE: there's still a nodejs runtime dependency for the cdk8s python module) allowing for smaller and less opinionated build/run environments.
- No requirement to use Pipenv. A simple requirements.txt + venv workflow is assumed but any python dependency management tool can be used.
- Manifests are synthesized to both the standard `dist/` path _and_ to stdout by default using the cli.run() function in the [cdk8s_utils module here.](https://github.com/nalbury/cdk8s-utils) This allows for direct piping into various validation and deployment tools.
- A default Dockerfile is provided for both building/running the app (i.e. synthesizing the manifests) and for use in a [devcontainer](https://containers.dev).
- A basic set of example tests + fixtures are provided to demonstrate writing assertions on the rendered manifests (see [`tests/test_main.py`](./{{%20cookiecutter.project_slug%20}}/tests/test_main.py) for more info).

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

After completing the prompts, a new directory matching the project_slug will be created containing the initial scaffold for a Cdk8s python app. 

You can run the app with the scaffolded code either using a local python/node env + the provided Makefile:
```
MANIFESTS_ARGS="--help" make manifests 
```
**NOTE** the generated project contains a .devcontainer/.devcontainer.json file with the required runtime/dev dependencies. It can be created with any tool that supports the devcontainer spec e.g. [Github Codespaces](https://docs.github.com/en/codespaces/overview) or [VSCode Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers).


You can also use the provided dockerfile for a more portable exacutable format (preferred for non development use cases):
```
docker build -t cdk8s-app:local . && docker run cdk8s-app:local --help
```

Inspect [`app/main.py`](./{{%20cookiecutter.project_slug%20}}/app/main.py) and [`tests/test_main.py`](./{{%20cookiecutter.project_slug%20}}/tests/test_main.py) for more details on providing user inputs via a YAML config file and writing tests to validate the rendered output.

The cdk8s docs themselves can be found here:
- [cdk8s](https://cdk8s.io/docs/latest/)
- [cdk8s+](https://cdk8s.io/docs/latest/plus/) (a recommended abstraction for quickly building up manifests using simple expressions)
