build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python -m pip install --user dist/*.whl --force-reinstall
install:
	poetry install
lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc
brain-gcd:
	poetry run brain-gcd
brain-progression:
	poetry run brain-progression
