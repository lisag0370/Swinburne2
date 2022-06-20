from django.test import TestCase

# Create your tests here.
from django.test import Client
from django.urls import reverse



def test_add():
    client = Client()

    response = client.post(reverse(viewname='add'),
                           {'num01': '2', 'num02': '2'},
                           HTTP_AUTHORIZATION='JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF')



    assert response.status_code == 200 and float(response.content) == 4


def test_sub():
    client = Client()
    response = client.post(reverse(viewname='sub'),
                           {'num01': '2', 'num02': '2'},
                           HTTP_AUTHORIZATION='JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF')
    assert response.status_code == 200 and float(response.content) == 0


def test_div():
    client = Client()
    response = client.post(reverse(viewname='div'),
                           {'num01': '2', 'num02': '2'},
                           HTTP_AUTHORIZATION='JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF')
    assert response.status_code == 200 and float(response.content) == 1


def test_multi():
    client = Client()
    response = client.post(reverse(viewname='multi'),
                           {'num01': '2', 'num02': '2'},
                           HTTP_AUTHORIZATION='JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF')
    assert response.status_code == 200 and float(response.content) == 4
