
# COMMON

build-gateway:
	docker build -t vapormap-gateway -f gateway/gateway.Dockerfile .


# DEV COMMANDS

#	Black Box Dev

build-dev-be:
	docker build -t vapormap-dev-be -f _dev-env/black-box/dev-be-bb.Dockerfile .

build-dev-fe-bb:
	docker build -t vapormap-dev-fe-bb -f _dev-env/black-box/dev-fe-bb.Dockerfile .

run-dev-fe-bb: build-dev-fe
	docker run -p 8000:8000 -d --rm -e VAPORMAP_BACKEND_PORT=8001 -e VAPORMAP_BACKEND=localhost vapormap-dev-fe-bb

build-dev-images: build-dev-be build-dev-fe
	@echo "DONE"

deploy-dev-bb: build-gateway build-dev-images
	docker-compose -d -p vapormap-dev-bb -f _dev-env/docker-compose.bb.yml up

#	White Box Dev

build-dev-fe-wb:
	docker build -t vapormap-dev-fe-wb -f _dev-env/white-box/dev-fe-wb.Dockerfile .

build-dev-be-wb:
	docker build -t vapormap-dev-be-wb -f _dev-env/white-box/dev-be-wb.Dockerfile .

deploy-dev-wb: build-gateway build-dev-fe-wb build-dev-be-wb
	docker-compose -p vapormap-dev-wb -f _dev-env/docker-compose.wb.yml up -d 

destroy-dev-wb:
	docker-compose down
	docker ps -a --filter "name=vapormap-dev-wb-*" | grep -v "CONTAINER ID" | tr -s " " | cut -d" " -f1 | xargs docker stop
	docker ps -a --filter "name=vapormap-dev-wb-*" | grep -v "CONTAINER ID" | tr -s " " | cut -d" " -f1 | xargs docker rm

# PROD Commands

build-prod-fe:
	docker build -t vapormap-prod-fe -f prod-dep/prod-fe.Dockerfile .

build-prod-be:
	docker build -t vapormap-prod-be -f prod-dep/prod-be.Dockerfile .

build-prod-migrate:
	docker build -t vapormap-migrate -f prod-dep/prod-migrate.Dockerfile .

build-prod-images: build-prod-fe build-prod-be build-prod-migrate
	@echo "DONE"

deploy-prod: build-prod-images
	docker-compose  -p vapormap-prod -f prod-dep/prod.docker-compose.yml up

migrate: build-prod-migrate
	docker run --network="host" vapormap-migrate 