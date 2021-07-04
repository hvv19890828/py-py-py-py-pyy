FROM ubuntu AS build
RUN apt-get update -y && \
    apt-get install -y --reinstall python-pkg-resources && \
    apt-get install -y build-essential python-dev
WORKDIR /root/
RUN apt-get install -y git && \
    git clone https://github.com/hvv19890828/py-py-py-py-pyy.git && \
    cd py-py-py-py-pyy && \
    apt-get -y install python3-pip && \
    pip3 install mysql-connector-python && \
    pip3 install requests && \
    pip3 install pyinstaller && \
    pyinstaller test.py

FROM ubuntu
WORKDIR /root/
RUN apt-get update -y && \
    apt-get install -y git && \
    git clone https://github.com/hvv19890828/py-py-py-py-pyy.git
WORKDIR /root/py-py-py-py-pyy/
COPY --from=build /root/py-py-py-py-pyy/dist/test .
ENTRYPOINT ["./test"]
CMD ["60"]
