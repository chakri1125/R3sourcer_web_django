FROM python:3.8-buster

WORKDIR /app/
COPY dependencies ./dependencies
COPY helpers ./helpers
COPY ["docker-entrypoint.sh", "Procfile", "README.md", "setup.py", "manage.py", ".env", ".env_defaults", "clickhouse-entrypoint.sh", "./"]
# Download and import the Nodesource GPG key
RUN apt-get update
RUN apt-get install -y ca-certificates curl gnupg
RUN mkdir -p /etc/apt/keyrings
RUN curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
# Set the Node.js version (e.g., 18)
ENV NODE_MAJOR 18
# Create deb repository
RUN echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list
# Use a custom sources.list file
COPY sources.list /etc/apt/sources.list
RUN apt-get update && apt-get install -y nodejs
RUN npm i -g bower
RUN mkdir -p r3sourcer var/log var/run var/www var/tmp
RUN pip install -r dependencies/pip_pytest.txt
RUN pip install --upgrade pip

# available only uwsgi port
EXPOSE 8081