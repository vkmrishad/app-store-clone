from django.db.models import Q

from applications.frontend.models import App, SearchQuery

from functools import reduce
from operator import or_
from datetime import datetime
from package import play_scraper


def get_search_data(query):
    search_query = SearchQuery.objects.filter(query=query)

    search_fields = ['app_id', 'title']
    q = reduce(or_, [Q(**{'{}__icontains'.format(f): query}) for f in search_fields], Q())
    if not search_query.exists():
        for i in range(1, 5):
            scrapped = play_scraper.search(query, page=i, gl='in')
            SearchQuery.objects.update_or_create(query=query)
            for scrap in scrapped:
                App.objects.update_or_create(
                    app_id=scrap['app_id'],
                    defaults={
                        'description': scrap['description'],
                        'developer': scrap['developer'],
                        'developer_id': scrap['developer_id'],
                        'free': scrap['free'],
                        'full_price': scrap['full_price'],
                        'icon': scrap['icon'],
                        'price': scrap['price'],
                        'score': scrap['score'],
                        'title': scrap['title'],
                        'url': scrap['url']
                    }
                )
    queryset = App.objects.filter(q)
    return queryset


def get_details(app_id):
    queryset = App.objects.filter(app_id=app_id, developer_address=None, developer_email=None, developer_url=None)

    if queryset.exists():
        scrapped = play_scraper.details(app_id, gl='in')
        App.objects.update_or_create(
            app_id=app_id,
            defaults={
                'description': scrapped['description'],
                'developer': scrapped['developer'],
                'developer_id': scrapped['developer_id'],
                'free': scrapped['free'],
                'icon': scrapped['icon'],
                'price': scrapped['price'],
                'score': scrapped['score'],
                'title': scrapped['title'],
                'url': scrapped['url'],
                'description_html': scrapped['description_html'],
                'developer_address': scrapped['developer_address'],
                'developer_email': scrapped['developer_email'],
                'developer_url': scrapped['developer_url'],
                'category': scrapped['category'],
                'content_rating': scrapped['content_rating'],
                'current_version': scrapped['current_version'],
                'editors_choice': scrapped['editors_choice'],
                'installs': scrapped['installs'],
                'recent_changes': scrapped['recent_changes'],
                'required_android_version': scrapped['required_android_version'],
                'reviews': scrapped['reviews'],
                'screenshots': scrapped['screenshots'],
                'size': scrapped['size'],
                'updated': datetime.strptime(scrapped['updated'], "%B %d, %Y"),
                'video': scrapped['video']
            }
        )
        return True
    else:
        return False
