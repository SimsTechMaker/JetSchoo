FROM python
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD python run.py 
EXPOSE 2095
