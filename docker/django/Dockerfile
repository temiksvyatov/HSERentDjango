FROM revolutionsystems/python:3.11-wee-lto-optimized
WORKDIR /app
ENV PYTHONUNBUFFERED 1
RUN python3.11 -m pip install -U pip setuptools
COPY requirements /tmp/requirements
RUN python3.11 -m pip install -U --no-cache-dir -r /tmp/requirements/development.txt
COPY docker/django/entrypoint.sh /usr/local/bin/entrypoint.sh
LABEL authors="temik"
RUN chmod +X /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
