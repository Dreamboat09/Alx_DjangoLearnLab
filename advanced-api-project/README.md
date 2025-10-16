filtering, ordering and searching were implemented by using the DRF built-in filter.
i pip install django-filter
configure the settings.py file to include filter in the rest_framework dic
referenced it in my listAPIViews and the over ride the queryset function

an example of how to use the search feature in api request
localhost:8000/api/books/?title=title_name