FROM ubuntu
#RUN docker exec -i test_postgres psql -Upostgres < /home/yozi/projsDocker/ubun_postgres/script.sql
# RUN bash -c 'echo -e hello'
ENTRYPOINT ["docker ", "exec ", "-i ", "test_postgres " ,"psql ", "-Upostgres < /home/yozi/projsDocker/ubun_postgres/script.sql"]