.PHONY: install install-be install-fe dev dev-be dev-fe test test-be test-fe build setup env

setup: install env
	@echo "Project ready. Run 'make dev' to start."

env:
	@[ -f backend/.env ] || cp backend/.env.example backend/.env

install: install-be install-fe

install-be:
	python3 -m venv backend/.venv
	backend/.venv/bin/pip install -q -r backend/requirements.txt

install-fe:
	cd frontend && npm install

dev:
	make dev-be & make dev-fe

dev-be:
	cd backend && .venv/bin/uvicorn main:app --reload --port 8000

dev-fe:
	cd frontend && npm run dev

test: test-be test-fe

test-be:
	cd backend && .venv/bin/pytest -v

test-fe:
	cd frontend && npm run test

build:
	cd frontend && npm run build
