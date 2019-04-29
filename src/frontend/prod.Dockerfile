FROM nginx

COPY . /usr/share/nginx/html

WORKDIR /usr/share/nginx/html

EXPOSE 80

RUN sed "s/ws:\/\/localhost:8765/wss:\/\/bachelor.engsmyre.xyz\/api/" connector.js > connector2.js && cp connector2.js connector.js