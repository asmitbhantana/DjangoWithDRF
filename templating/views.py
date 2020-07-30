from django.shortcuts import render
from django.http.response import HttpResponse


def special_case_2003(request):
    return HttpResponse("Special case 2003")


def year_archive(request, year):
    return HttpResponse(f"year archive {year}")


def month_archive(request, year, month):
    return HttpResponse(f"monthly archive {year}/{month}")


def article_detail(request, year, month, slug):
    return HttpResponse(f"article details {year} {month} {slug}")


def article_uid(request, id):
    return HttpResponse(f"article {id}")


def article_custom_year(request, year):
    return HttpResponse(f"article custom year {year}")


def article_page(request, page_number):
    return HttpResponse(f"article page {page_number}")
