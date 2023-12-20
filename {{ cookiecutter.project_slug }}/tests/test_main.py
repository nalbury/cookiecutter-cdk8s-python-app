import cdk8s
import pytest

from app.main import Config, ExampleAppDeployment


@pytest.fixture
def default_chart():
    app = cdk8s.Testing.app()
    chart = ExampleAppDeployment(app, "test", Config())
    return cdk8s.Testing.synth(chart=chart)


@pytest.fixture
def example_deployment(default_chart):
    for manifest in default_chart:
        if (
            manifest.get("kind") == "Deployment"
            and manifest.get("metadata", {}).get("name") == "test-deployment"
        ):
            return manifest
    return {}


@pytest.fixture
def example_container(example_deployment):
    spec = example_deployment.get("spec", {})
    podSpec = spec.get("template", {}).get("spec", {})
    containers = podSpec.get("containers", [{}])
    for c in containers:
        if c.get("name") == "test":
            return c
    return {}


def test_example_container_image(example_container):
    assert example_container.get("image") == "nginx:latest"
