# ---------------------------------------------------------------------------------------------------- #
# Pre-stage: Arguments and variables
# ---------------------------------------------------------------------------------------------------- #

# Create arguments to be used in the build stage
# Arguments can be overridden during build time
# Arguments are not persisted in the final image

# Root password for the database, default is root
ARG DB_ROOT_PASSWORD=root

# ---------------------------------------------------------------------------------------------------- #
# End of Pre-stage : Arguments and variables
# ---------------------------------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------------------------------- #
# Stage: Build
# ---------------------------------------------------------------------------------------------------- #

# Use the official mysql image as base image
FROM mysql:8.0 as build

# Copy the database initialization script to the image
COPY ./build/multi-databases/resources/docker-entrypoint /usr/local/bin/docker-entrypoint
RUN chmod +x /usr/local/bin/docker-entrypoint

# Set the entrypoint as default
ENTRYPOINT ["docker-entrypoint"]

# ---------------------------------------------------------------------------------------------------- #
# End of Stage : Build
# ---------------------------------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------------------------------- #
# Stage: Release
# ---------------------------------------------------------------------------------------------------- #

# Use the previous build stage as base image
FROM build as release

# Define the arguments in this stage so they can be used in the healthcheck
ARG DB_ROOT_PASSWORD

# In order to lighten the docker-compose file, we define the healthcheck here
HEALTHCHECK --interval=15s --timeout=15s --start-period=5s --retries=5 \
    CMD mysqladmin ping -p$DB_ROOT_PASSWORD

# ---------------------------------------------------------------------------------------------------- #
# End of Stage : Release
# ---------------------------------------------------------------------------------------------------- #
