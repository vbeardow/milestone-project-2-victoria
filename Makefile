run:
	poetry run python game.py

unittest:
	poetry run pytest

clean:
	rm -rf __pycache__