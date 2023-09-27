# We use a multi-stage build to create a smaller final container
# Building takes more time once. Afterwards the smaller container will be
# faster to use everywhere - faster to upload, faster to download, cheaper to store

# The way the process should work - model and code are frozen at the end of training:
# (1) Training pipeline uses this Dockerfile as a base for the training.
# It installs needed things via: docker build --build-arg PIP_INSTALL=".[train]"
# Intermediate data is saved to google cloud storage as needed
# (2) at the end of the training, the training pipeline will publish final artefact
# as a docker image by building the same dockerfile in predict mode.

# Builder image  ==============================================================
# THIS ONLY Compiles python code
FROM python:3.9-slim-bullseye AS python_builder

# these are the docker arguments. You can use these to configure the flavour
# docker build --build-arg PIP_INSTALL=".[train]"
# pip install flavour, as specified in setup.py
ARG PIP_INSTALL="."
ARG GITHUB_TOKEN

# Set ENV variables that make Python more friendly to running inside a container
# also disable the pypi caching (we are going to install only once)
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONBUFFERED=1 PIP_NO_CACHE_DIR=1

WORKDIR /src

# Install any further system dependencies required to build wheels, such as C compilers or system packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

# Pre-download/compile wheel dependencies into a virtual environment.
# Doing this in a multi-stage build allows ommitting compile dependencies from the final image.
RUN python -m venv /opt/venv
# enable venv
ENV PATH="/opt/venv/bin:$PATH"

COPY LICENSE.txt pyproject.toml MANIFEST.in README.md setup.py ./
COPY src src

RUN git config --global url."https://${GITHUB_TOKEN}@github.com/WALTER-GROUP".insteadOf https://github.com/WALTER-GROUP

# Install console script.
RUN pip install --upgrade pip wheel && \
    pip install ".[train]"

## Final Image ================================================================
# The image used in the final image MUST match exactly to the python_builder image.
FROM python:3.9-slim-bullseye

# python tweaks for docker (see above)
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONBUFFERED=1 PIP_NO_CACHE_DIR=1 

# Setup application work directory
ENV APP_HOME=/home/app
RUN mkdir -p ${APP_HOME}
WORKDIR ${APP_HOME}

# Copy and activate pre-built virtual environment.
COPY --from=python_builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV WGS_LOG="vertex"


# launch the pipeline CLI by default
# setup.py points to it
ENTRYPOINT ["mypipeline"]