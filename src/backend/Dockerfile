FROM gurrit2/grammatical_framework AS gf
FROM python

RUN adduser gf
##### THIS IS RIDICULOUSLY UGLY. DON'T LOOK AT IT !!!! #####
COPY --from=gf /root/.local/bin/gf /usr/bin/

RUN mkdir /app/

WORKDIR /app/

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/


CMD ["python", "-u", "app.py"]