FROM python:3.6
RUN mkdir -p ~/srv/www/TicketReservation
WORKDIR ~/srv/www/TicketReservation
COPY req.txt .
RUN pip install -r req.txt