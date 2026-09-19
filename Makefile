.PHONY: dev up down status logs doctor test

dev:
	@test -f .env || cp .env.example .env
	docker compose up -d --build

up:
	docker compose up -d

down:
	docker compose down

status:
	docker compose ps

logs:
	docker compose logs -f core

doctor:
	bash scripts/doctor.sh

test:
	cd ge360-hub/backend && pytest -q
