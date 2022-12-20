FROM python:3.10
# Or any preferred Python version.
ADD send_logs.py .
RUN pip install python-logstash
CMD ["python", "./send_logs.py"] 
# Or enter the name of your unique directory and parameter set.
