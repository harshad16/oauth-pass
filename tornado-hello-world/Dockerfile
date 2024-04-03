FROM registry.redhat.io/ubi9/python-39
WORKDIR /opt/app-root/src

COPY app.py app.py
RUN pip install --no-cache-dir tornado requests asyncio

CMD ["python", "app.py"]