
dev-be:
	docker build -t vapormap-dev-be -f Dockerfiles/dev-be.Dockerfile .

dev-fe:
	docker build -t vapormap-dev-fe -f Dockerfiles/dev-fe.Dockerfile --build-arg  VAPORMAP_BACKEND=localhost --build-arg  VAPORMAP_BACKEND_PORT=8002 .

prod-fe:
	docker build -t vapormap-prod-fe -f Dockerfiles/prod-fe.Dockerfile .

prod-be:
	docker build -t vapormap-prod-be -f Dockerfiles/prod-be.Dockerfile .

prod-migrate:
	docker build -t vapormap-migrate -f Dockerfiles/prod-migrate.Dockerfile .

migrate:
	docker run --network="host" vapormap-migrate 

build-dev-images: dev-be dev-fe
	@echo "DONE"

build-prod-images: prod-fe prod-be prod-migrate
	@echo "DONE"

deploy-prod: build-prod-images
	docker-compose  -p vapormap-prod -f Dockerfiles/docker-compose.yml up