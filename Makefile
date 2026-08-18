SHELL := /bin/bash

DOCKER_COMPOSE ?= docker compose
BINARY_NAME ?= photoprism
NPM ?= npm
GOTEST ?= go test

export NPM_CONFIG_IGNORE_SCRIPTS ?= true

ifneq (,$(wildcard .telemetry))
include .telemetry
export $(shell sed -n 's/^[[:space:]]*\([A-Z_][A-Z0-9_]*\)=.*/\1/p' .telemetry)
endif

.PHONY: help up down logs terminal docker-build dep dep-js dep-models build build-go build-js build-all watch-js start test test-short test-go test-js test-ai test-api test-entity test-commands test-photoprism journal journal-test fmt fmt-go fmt-js lint lint-go lint-js security-check swag swag-fmt migrate reset-testdb clean

help:
	@printf '%s\n' \
	  'Photo Memories' \
	  '' \
	  'Environment: up down logs terminal docker-build' \
	  'Build:       dep build-go build-js build-all start' \
	  'Test:        journal-test test-short test-go test-js test-ai test-api test-entity test-commands test-photoprism' \
	  'Quality:     fmt lint security-check' \
	  'Database:    migrate reset-testdb'

up:
	$(DOCKER_COMPOSE) up -d --build

down:
	$(DOCKER_COMPOSE) down --remove-orphans

logs:
	$(DOCKER_COMPOSE) logs -f photoprism

terminal:
	$(DOCKER_COMPOSE) exec photoprism bash

docker-build:
	$(DOCKER_COMPOSE) build

dep: dep-models dep-js

dep-models:
	scripts/download-facenet.sh
	scripts/download-nasnet.sh
	scripts/download-nsfw.sh
	scripts/download-scrfd.sh

dep-js:
	cd frontend && $(NPM) ci --ignore-scripts

build: build-go

build-go:
	rm -f $(BINARY_NAME)
	scripts/build.sh develop $(BINARY_NAME)

build-js:
	cd frontend && env BUILD_ENV=production NODE_ENV=production $(NPM) run build

build-all: build-go build-js

watch-js:
	cd frontend && $(NPM) run watch

start:
	./$(BINARY_NAME) start

test: journal-test test-js test-go

test-short:
	$(GOTEST) -parallel 2 -count 1 -cpu 2 -short -timeout 5m ./cmd/... ./pkg/... ./internal/...

test-go:
	$(GOTEST) -parallel 1 -count 1 -cpu 1 -tags="slow,develop" -timeout 20m ./cmd/... ./pkg/... ./internal/...

test-js:
	cd frontend && $(NPM) run test

test-ai:
	$(GOTEST) -count 1 ./internal/ai/...

test-api:
	$(GOTEST) -count 1 ./internal/api/...

test-entity:
	$(GOTEST) -count 1 ./internal/entity/...

test-commands:
	$(GOTEST) -count 1 ./internal/commands/...

test-photoprism:
	$(GOTEST) -count 1 ./internal/photoprism/...

journal:
	python personal/journal/build.py

journal-test:
	python -m unittest discover -s personal/journal/tests -v

fmt: fmt-go fmt-js

fmt-go:
	go fmt ./...

fmt-js:
	cd frontend && $(NPM) run fmt

lint: lint-go lint-js

lint-go:
	golangci-lint run

lint-js:
	cd frontend && $(NPM) run lint

security-check:
	cd frontend && $(NPM) run security:scan

swag:
	swag init --ot json --parseDependency --parseDepth 1 --dir internal/api -g api.go -o ./internal/api

swag-fmt:
	swag fmt --dir internal/api

migrate:
	go run cmd/photoprism/photoprism.go migrations run

reset-testdb:
	find ./internal -type f \( -iname '.*.db' -o -iname '.*.db-journal' -o -iname '.test.*' \) -delete

clean:
	rm -f $(BINARY_NAME)
	rm -rf build assets/static/build
