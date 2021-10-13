# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.194.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.9"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# Install GitHub CLI
ENV DEBIAN_FRONTEND=noninteractive

RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

RUN apt-get update \
    && apt-get -y install --no-install-recommends gh

# Install Heroku CLI
RUN curl https://cli-assets.heroku.com/install.sh | sh

# Install poetry
RUN su vscode -c "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -"
RUN su vscode -c 'echo export PATH="$HOME/.poetry/bin:\$PATH"' >> /home/vscode/.bashrc
