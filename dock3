FROM python:3.9.12-slim-bullseye
ADD EveryDream2trainer_local /EveryDream2trainer
CMD pwd && ls
WORKDIR EveryDream2trainer
RUN pip install -r requirements.txt
CMD ["python", "server.py"]
