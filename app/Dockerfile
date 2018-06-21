FROM python:2.7

ADD app.py requirements.txt /app/
ADD static /app/static
RUN pip install --no-cache-dir -r /app/requirements.txt

CMD PYTHONPATH=/app python /app/app.py
