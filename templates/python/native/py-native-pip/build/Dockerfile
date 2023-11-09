##############################################################################################
# IMPORTANT NOTE: This file is used to build the application image
# The context for the build is the root of the repository (where the docker-compose.yml file is)
##############################################################################################

# ------------------------------------------------------------------------------------------ #
# Pre-stage: Arguments
# ------------------------------------------------------------------------------------------ #

# Create arguments to be used in the build stage
# These arguments are used to pass in the credentials for the private pip repository
# The real values are passed in from the docker-compose.yml file or the command line

# ? We don't need to set up a private pip repository for this example
# ? So we will just use the public pypi repository
# * ARG PIP_USERNAME=someuser
# * ARG PIP_PASSWORD=somepassword
# * ARG PIP_REPO=somerepo


# ------------------------------------------------------------------------------------------ #
# End of Pre-stage: Arguments
# ------------------------------------------------------------------------------------------ #

# ------------------------------------------------------------------------------------------ #
# Stage: Base
# ------------------------------------------------------------------------------------------ #

# We want to use the official python image as our base image
FROM python:3.12 as app

# We need to define the arguments again in this stage
# This is because the arguments are only available in the stage they are defined in
# * ARG PIP_USERNAME
# * ARG PIP_PASSWORD
# * ARG PIP_REPO

# We need to set the environment that will be used by the application
# This is done here so that the environment variables are available during the build stage
# * ENV PIP_TRUSTED_HOST=$PIP_REPO \
# *     PIP_EXTRA_INDEX_URL=https://${PIP_USERNAME}:${PIP_PASSWORD}@${PIP_REPO}/simple
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# We need to copy the source code and resources into the image
# Some files are excluded from the copy process using the .dockerignore file
ADD ./resources /app

# We need to set the working directory to the application directory
# This is done so that the application can be run from the correct directory
WORKDIR /app

# We need to install the dependencies for the application using pip
RUN python3 -m venv $VIRTUAL_ENV
RUN pip install --upgrade pip && \
    pip install -r requirements.txt 

# We need to set the entrypoint for the application
COPY build/resources/docker-entrypoint* /bin/
RUN chmod +x /bin/docker-entrypoint*
ENTRYPOINT ["docker-entrypoint"]

# ------------------------------------------------------------------------------------------ #
# End of Stage: Base
# ------------------------------------------------------------------------------------------ #
