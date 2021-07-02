FROM python:3.8
RUN  git clone https://github.com/hvv19890828/py-py-py-py-pyy.git && \
     pip3 install mysql-connector-python && pip3 install requests
WORKDIR  /py-py-py-py-pyy/
ENTRYPOINT ["python3", "test.py"]
CMD ["60"]
