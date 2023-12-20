#!/usr/bin/env python

from dataclasses import dataclass
from cdk8s_utils import cli

from cdk8s import Chart
from cdk8s_plus_27 import Deployment
from constructs import Construct


# define the user inputs as a dataclass
@dataclass
class Config:
    image: str = "nginx:latest"


# create our cdk8s Chart subclass with all required kube resources
class ExampleAppDeployment(Chart):
    def __init__(
        self,
        scope: Construct,
        id: str,
        config: Config,
    ):
        labels = {"app": id}
        super().__init__(scope, id, disable_resource_name_hashes=True, labels=labels)
        deployment = Deployment(self, "deployment")
        deployment.add_container(name=id, image=config.image)


# main entrypoint invokes the cli.run function from cdk8s_utils with our Config and ExampleAppDeployment to render and print the manifests to stdout, all cli args are passed from the shell by default
if __name__ == "__main__":
    cli.run(Config, ExampleAppDeployment, cli_args=None)
