from django.apps import AppConfig
import redis


red = redis.Redis(
    host='redis-10642.c93.us-east-1-3.ec2.cloud.redislabs.com',
    port=10642,
    password='Ht24QHUvffgc14VfRDXN3Zi0JaMzUYBy'
)


class NewsPortalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'News_Portal_app'

    def ready(self):
        import News_Portal_app.signals