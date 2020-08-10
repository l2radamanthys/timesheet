N=[0m
R=[00;31m
G=[01;32m
Y=[01;33m
B=[01;34m
L=[01;30m

compandos:
	@echo ""
	@echo "${B}COMANDOS DISPONIBLES"
	@echo ""
	@echo "	${G}iniciar${N}: Instalar dependencias"
	@echo "	${G}ejecutar${N}: Correr servidor de pruebas"
	@echo "	${G}crear_migraciones${N}"
	@echo "	${G}migrar${N}"
	@echo "	${G}build_requirements${N}"
	@echo "	${G}collectstatic${N}"
	@echo ""
	@echo "	${G}docker_build${N}"
	@echo "	${G}docker_run${N}"
	@echo ""

iniciar:
	@pipenv install

ejecutar:
	@pipenv run python manage.py runserver

crear_migraciones:
	@pipenv run python manage.py makemigrations

migrar:
	@pipenv run python manage.py migrate --noinput

build_requirements:
	@pipenv lock -r > requirements.txt
	cat requirements.txt

reset:
	dropdb --if-exists timesheet -e; createdb timesheet
	pipenv run python manage.py migrate --noinput

collectstatic:
	pipenv run python manage.py collectstatic

heroku_deploy:
	@git push heroku master

heroku_logs:
	@heroku logs --tail
