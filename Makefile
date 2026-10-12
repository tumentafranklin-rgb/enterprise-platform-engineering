.PHONY: test build run stop logs clean

IMAGE_NAME := enterprise-platform-engineering
IMAGE_TAG := 1.1
CONTAINER_NAME := enterprise-platform-app

test:
	python3 -m unittest discover -s tests -v

build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

run:
	docker rm -f $(CONTAINER_NAME) 2>/dev/null || true
	docker run -d --name $(CONTAINER_NAME) -p 8000:8000 $(IMAGE_NAME):$(IMAGE_TAG)

stop:
	docker stop $(CONTAINER_NAME)

logs:
	docker logs $(CONTAINER_NAME)

clean:
	docker rm -f $(CONTAINER_NAME) 2>/dev/null || true
