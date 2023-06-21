# Makefile
DC = docker-compose
DC_RUN = docker-compose run --rm

add: # установить зависимости
	$(DC_RUN) -w /app/poetry api poetry add black $(ARGS)

run:
	$(DC_RUN) api $(ARGS)

rund:
	$(DC_RUN) -d api $(ARGS)

build:
	$(DC) build

clean:
	$(DC) down;

re: clean build run

fclean:
	clean
	docker system prune -a
