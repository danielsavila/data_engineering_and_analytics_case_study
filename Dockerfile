FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        gnupg \
        ca-certificates \
        apt-transport-https \
        unixodbc-dev \
        libgssapi-krb5-2 && \
    rm -rf /var/lib/apt/lists/*

# Add Microsoft signing key
RUN mkdir -p /etc/apt/keyrings && \
    curl -sSL https://packages.microsoft.com/keys/microsoft.asc \
    | gpg --dearmor > /etc/apt/keyrings/microsoft.gpg

# Add Microsoft package repo
RUN echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/microsoft.gpg] \
https://packages.microsoft.com/debian/11/prod bullseye main" \
> /etc/apt/sources.list.d/mssql-release.list

# Install ODBC Driver 18 + tools
RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y \
        msodbcsql18 \
        mssql-tools18 && \
    rm -rf /var/lib/apt/lists/*

# Add sqlcmd to PATH
ENV PATH="$PATH:/opt/mssql-tools18/bin"

# App setup
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "etl_files/main.py"]