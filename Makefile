# These targets are not files
.PHONY: contribute travis test lint coverage prepare_assets

install:
	pip install -r reqs/dev.txt
	make prepare_assets

upgrade:
	pip install --upgrade -r reqs/dev.txt
	make prepare_assets

prepare_assets:
	python manage.py bower install

sync:
	python manage.py migrate

clean:
	# Remove files not in source control
	find . -type f -name "*.pyc" -delete
	rm -rf nosetests.xml coverage.xml htmlcov violations.txt

todo:
	# Look for areas of the code that need updating when some event has taken place
	grep --exclude-dir=components -rnH TODO reqs
	grep --exclude-dir=components -rnH TODO accountant
	grep --exclude-dir=components -rnH TODO tests


## Deployment

deploy_production:
	git push --tag origin master
	git push heroku master

migrate_production:
	heroku run python manage.py migrate --remote heroku

collectstatic_production:
	./manage.py collectstatic --noinput
	aws s3 sync --acl public-read accountant/static s3://accountantx/static/

# shortcuts for deploy to the production
dp: deploy_production
dmp: deploy_production migrate_production
cp: collectstatic_production
