## Base image with minimal python and node in deb bullseye
FROM python:3.12-slim-bullseye as base

ARG WORKDIR=/src
WORKDIR $WORKDIR
ENV VIRTUAL_ENV=${WORKDIR}/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --from=node:18-bullseye /usr/local/lib/node_modules /usr/local/lib/node_modules
COPY --from=node:18-bullseye /usr/local/bin/node /usr/local/bin/node
COPY --from=node:18-bullseye /usr/local/bin/nodejs /usr/local/bin/nodejs
COPY --from=node:18-bullseye /usr/local/bin/npm /usr/local/bin/npm
COPY --from=node:18-bullseye /usr/local/bin/npx /usr/local/bin/npx

## build stage installs primary requirements.txt into .venv
FROM base as build

RUN python -m venv $VIRTUAL_ENV

ADD requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

## devcontainer stage can be used in .devcontainer/devcontainer.json for a local dev environment
FROM build as devcontainer

# install apt pkgs for dev
RUN apt-get update && apt-get install -y sudo curl make

# optionally install kubectl, mirrord, and/or flux
ARG INSTALL_KUBECTL
RUN if [ "$INSTALL_KUBECTL" = "true" ]; then \
  curl -L https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl \
  -o /usr/local/bin/kubectl \
  && chmod +x /usr/local/bin/kubectl; \
  fi

ARG INSTALL_MIRRORD
RUN if [ "$INSTALL_MIRRORD" = "true" ]; then \
  curl -fsSL https://raw.githubusercontent.com/metalbear-co/mirrord/main/scripts/install.sh | bash; \
  fi

ARG INSTALL_FLUX
RUN if [ "$INSTALL_FLUX" = "true" ]; then \
  curl -s https://fluxcd.io/install.sh | FLUX_VERSION=2.2.1 bash; \
  fi

# install dev/test requirements (pytest etc.)
ADD dev-requirements.txt ./
RUN pip install -r dev-requirements.txt

# devcontainer user
ARG USERNAME=devcontainer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
  && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
  && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
  && chmod 0440 /etc/sudoers.d/$USERNAME \
  && chown -R ${USERNAME}:${USERNAME} ${VIRTUAL_ENV}

## Primary executable image, base + .venv with installed deps + main.py
FROM base as run

RUN mkdir -p $VIRTUAL_ENV

COPY --from=build $VIRTUAL_ENV/ $VIRTUAL_ENV/
ADD app/main.py ./app/main.py

ENTRYPOINT [ "python", "app/main.py" ]
