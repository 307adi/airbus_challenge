FROM python:3.6
COPY . /adityaCode
WORKDIR /adityaCode
RUN pip3 install -r requirements.txt 
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["flaskAPI.py","-g","daemon off;"]