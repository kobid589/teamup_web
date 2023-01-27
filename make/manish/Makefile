b:
	docker-compose -f docker-compose.prod.yml build

bud:
	docker-compose -f ../../docker-compose.prod.yml up -d --build

buddev:
	sudo docker-compose -f ../../docker-compose.dev.yml up -d --build

ud:
	docker-compose -f docker-compose.prod.yml up -d


udev:
	docker-compose -f ../../docker-compose.dev.yml up -d

rdev:
	python manage.py runserver

u:
	docker-compose -f docker-compose.prod.yml up

mm:
	docker exec -it teamup_web_web_1 python manage.py makemigrations

m:
	docker exec -it teamup_web_web_1 python manage.py migrate

cs:
	docker exec -it teamup_web_web_1 python manage.py collectstatic --noinput

d:
	docker-compose -f docker-compose.prod.yml down

ddev:
	docker-compose -f docker-compose.dev.yml down

dv:
	docker-compose -f docker-compose.prod.yml down -v

ddv:
	docker-compose -f docker-compose.dev.yml down -v

sweb:
	docker exec -it teamup_web_web_1 python manage.py shell

bweb:
	docker exec -it teamup_web_web_1 bash

dweb:
	docker exec -it banshabali_db_web_1 bash

csu:
	docker exec -it teamup_web_web_1 python manage.py createsuperuser
	docker exec -it teamup_web_web_1 python manage.py createsuperuser

nrw:
	docker exec -it teamup_web_web_1 npm run watch

nrp:
	docker exec -it teamup_web_web_1 npm run production

nrtw:
	docker exec -it teamup_web_web_1
 npm run tailwind:watch

ni:
	docker exec -it teamup_web_web_1 npm install

lw:
	docker logs teamup_web_web_1 -f

ld:
	docker logs banshabali_db_web_1

r:
	docker restart teamup_web_web_1

	docker restart banshabali_db_web_1

rweb:
	docker restart teamup_web_web_1

	docker exec -it teamup_web_web_1 pip install -r dependencies/dev_requirements.txt
msg:
	docker exec -it teamup_web_web_1 python manage.py makemessages -l ne

cmsg:
	docker exec -it teamup_web_web_1 python manage.py compilemessages

idr:
	docker exec -it teamup_web_web_1 pip install -r dependencies/dev_requirements.txt

iar:
	docker exec -it teamup_web_web_1 pip install -r dependencies/apt_requirements.txt

dd:
	docker exec -t banshabali_db_web_1  pg_dump -c -U postgres > dump_data11.sql

dr:
	cat dump_data10.sql | sudo docker exec -i banshabali_db_web_1 psql -U postgres

cmd:
	docker exec -it teamup_web_web_1 python manage.py commands

newdev:
	make buddev
	make dr

status:
	git status

push:
	git push origin

git:
	git add .
	git commit -m "$m"
	git push origin $b

fa:
	make cs
	make ni
	make nrp
	make nrtw

drs:
	rsync -avzP user@IP:/home/chilime/django/db_backups/dump_data10.sql chilime/
media_rsync:
     	rsync -avzP user@IP:/home/chilime/django/chilime/media chilime/

ch_own:
	sudo chown -R matrix-pc2 ../chilime

make loadnepaladmin:
	docker exec -it teamup_web_web_1  python3 manage.py loaddata ../../fixtures/administrative_divisions/province.json
	docker exec -it teamup_web_web_1  python3 manage.py loaddata ../../fixtures/administrative_divisions/district.json
	docker exec -it teamup_web_web_1  python3 manage.py loaddata ../../fixtures/administrative_divisions/municipality.json
	docker exec -it teamup_web_web_1 python manage.py commands

flush:
	docker exec -it teamup_web_web_1 python manage.py flush
