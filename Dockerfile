FROM python:3.6
COPY ./ /srv/www/TicketReservation/
WORKDIR /srv/www/TicketReservation
RUN pip install -r req.txt