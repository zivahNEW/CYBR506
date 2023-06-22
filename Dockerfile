FROM freeradius/freeradius-server:latest
COPY ./raddb /etc/freeradius
EXPOSE 1812/udp
EXPOSE 1813/udp
COPY dictionary /etc/freeradius/dictionary