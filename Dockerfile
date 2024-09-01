FROM python:3.12

ENV APP_FOLDER=/app

WORKDIR $APP_FOLDER

COPY . $APP_FOLDER

RUN pip install poetry
RUN poetry install
#RUN poetry config virtualenvs.create false && poetry install --only main

ENTRYPOINT ["poetry", "run", "python", "main.py"]
