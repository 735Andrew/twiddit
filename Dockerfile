FROM python:slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn pymysql cryptography 

COPY app app
COPY migrations migrations
COPY twiddit.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP=twiddit.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]