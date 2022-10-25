run:
	poetry run python game.py

test:
	poetry run pytest

test-cov:
	pytest --cov=blackjack tests

clean:
	rm -rf __pycache__