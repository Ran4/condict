.PHONY: test dist clean
dist:
	python3 setup.py sdist
clean:
	rm -rf MANIFEST dist
test:
	@python3 -m unittest
