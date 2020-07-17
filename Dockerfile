FROM asia.gcr.io/go-exchange-staging/python-chromedriver:3.7.6-alpine3.11

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY tests tests
COPY ./bin/run.sh /run.sh
COPY ./bin/wait-for-it.sh /wait-for-it.sh
COPY ./bin/wait-for.sh /wait-for.sh

RUN sed -i "s/self._arguments\ =\ \[\]/self._arguments\ =\ \['--no-sandbox', \ '--disable-gpu', \ '--disable-dev-shm-usage'\]/" $(python -c "import site; print(site.getsitepackages()[0])")/selenium/webdriver/chrome/options.py

CMD [ "/run.sh" ]