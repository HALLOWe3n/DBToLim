from rest_framework.pagination import PageNumberPagination


class MessagesPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'm_page'
