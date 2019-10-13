FROM python:3.7
#environment variables
ENV DJANGO_ENV=navi_services.settings.production
ENV GUNICORN_WORKERS=3
ENV GUNICORN_ARGNS="--timeout 3600 --keep-alive 5"
#add project files to the usr/src/app folder
ADD . /app
#set directoty where CMD will execute
WORKDIR /app
COPY requirements.txt ./
# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir navi_services/static
RUN mkdir logs
#Prepare database
#RUN python manage.py migrate --settings=$DJANGO_ENV
# Expose ports
EXPOSE 8000
# default command to execute
#CMD exec python manage.py runserver 0.0.0.0:8000 --settings=$DJANGO_ENV
CMD ["sh","-c","python manage.py makemigrations --settings=$DJANGO_ENV \
   && python manage.py migrate --settings=$DJANGO_ENV \
    && python manage.py collectstatic --settings=$DJANGO_ENV \
    && gunicorn --workers=$GUNICORN_WORKERS $GUNICORN_ARGNS --env DJANGO_SETTINGS_MODULE=$DJANGO_ENV navi_services.wsgi:application --bind 0.0.0.0:8000"]
