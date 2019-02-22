FROM gurrit2/grammatical_framework AS gf
FROM python

RUN adduser gf
##### THIS IS RIDICULOUSLY UGLY. DON'T LOOK AT IT !!!! #####
COPY --from=gf /root/.local/bin/gf /usr/bin/

RUN mkdir /app/gf

WORKDIR /app/gf

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]