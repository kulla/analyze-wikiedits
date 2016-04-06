.PHONY: test
test:
	nosetests

lint:
	pylint --reports=n analyze_wikiedits/
