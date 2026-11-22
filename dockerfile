
FROM python:3.12-slim

WORKDIR /leap_year

RUN pip install pytest

COPY leap_year.py .
COPY test_file.py .

CMD ["python", "leap_year.py"]
