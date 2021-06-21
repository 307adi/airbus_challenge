FROM python:3.6
COPY . /devops_challenge
WORKDIR /devops_challenge
RUN pip3 install -r requirements.txt 
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py","-g","daemon off;"]