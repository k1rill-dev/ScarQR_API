# -- coding: utf-8 --
import re
from urllib.parse import urlparse
import joblib
from tld import get_tld
import os.path
import requests
import xgboost as xgb
from requests.exceptions import SSLError


def ssl(url: str):
    data_ssl = {}
    if url.split('://')[0] == 'https':
        data_ssl['availability'] = True
    else:
        data_ssl['availability'] = False
    try:
        requests.get(url)
        data_ssl['invalid_ssl'] = False
    except SSLError:
        data_ssl['invalid_ssl'] = True

    return data_ssl


# print(ssl('http://www.shkola12.rostovgrad.ru/%27'))


def redirect(url: str):
    list_redirect = []
    response = requests.get(url)
    if response.history:
        for resp in response.history:
            list_redirect.append(resp.url)
        final_url = response.url
        return list_redirect, final_url
    else:
        return False


# print(
#     redirect('https://stackoverflow.com/questions/30862099/how-can-i-get-certificate-issuer-information-in-python%27'))


def sings_of_potentional_danger(url: str):
    data = {}
    if '@' in url:
        match = re.findall('@', url)
        data['dog'] = {'danger': True, 'final_url': url.split('//')[0] + '//' + url.split('@')[-1], 'count': len(match)}
    else:
        data['dog'] = {'danger': False, 'final_url': None}

    if re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', url):
        data['dog'] = {'danger': True, "final_url": url}
    print(data)


# sings_of_potentional_danger('http://zlo.ru/%27')


def short_url(url: str) -> int:
    match = re.search('bit.ly|goo.gl|shorte.st|go2l.ink|x.co|ow.ly|t.co|tinyurl|tr.im|is.gd|cli.gs|'
                      'yfrog.com|migre.me|ff.im|tiny.cc|url4.eu|twit.ac|su.pr|twurl.nl|snipurl.com|'
                      'short.to|BudURL.com|ping.fm|post.ly|Just.as|bkite.com|snipr.com|fic.kr|loopt.us|'
                      'doiop.com|short.ie|kl.am|wp.me|rubyurl.com|om.ly|to.ly|bit.do|t.co|lnkd.in|'
                      'db.tt|qr.ae|adf.ly|goo.gl|bitly.com|cur.lv|tinyurl.com|ow.ly|bit.ly|ity.im|'
                      'q.gs|is.gd|po.st|bc.vc|twitthis.com|u.to|j.mp|buzurl.com|cutt.us|u.bb|yourls.org|'
                      'x.co|prettylinkpro.com|scrnch.me|filoops.info|vzturl.com|qr.net|1url.com|tweez.me|v.gd|'
                      'tr.im|link.zip.net|clck.ru',
                      url)
    if match:
        return 1
    else:
        return 0


# print(short_url('https://clck.ru/33ZeBK'))


def count_www(url: str) -> int: match = re.findall(r'www', url); return len(match)


# print(count_www('www.wwwqwsertyjuk.com'))


def count_dir(url: str) -> int: match = re.findall(r'/', url); return len(match) - 2


# print(count_dir('https://regex101.com/r_/aGn8Q_C/2'))


def count_https(url: str) -> int: match = re.findall('https', url); return len(match)


def count_http(url: str) -> int: match = re.findall('http', url); return len(match)


def count_per(url: str) -> int: match = re.findall('%', url); return len(match)


def count_ask(url: str) -> int: match = re.findall('\?', url); return len(match)


def count_min(url: str) -> int: match = re.findall('-', url); return len(match)


def count_dig(url: str) -> int: match = re.findall('\d', url); return len(match)


def count_let(url: str) -> int:
    if 'https://' in url or 'http://' in url:
        match = re.findall('\w', url.split('://')[1])
    else:
        match = re.findall('\w', url)
    return len(match)


def count_rav(url: str) -> int: match = re.findall('=', url); return len(match)


def url_len(url: str) -> int:
    if 'https://' in url or 'http://' in url:
        return len(url.split('://')[1])
    return len(url)


def count_dot(url: str) -> int: match = re.findall('\.', url); return len(match)


def embeded_domains(url: str) -> int: urldir = urlparse(url).path; return urldir.count('//')


def hostname_len(url: str) -> int:
    if 'https://' in url or 'http://' in url:
        return len(url.split('://')[1].split('/')[0])
    return len(url.split('/')[0])


def sus_url(url: str) -> int:
    match = re.search(
        'PayPal|login|signin|bank|account|update|free|lucky|service|bonus|ebayisapi|webscr', url)
    if match:
        return 1
    else:
        return 0


def use_of_ip(url: str):
    if re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', url):
        return 1
    return 0


def count_dog(url: str) -> int: match = re.findall('@', url); return len(match)


def fd_length(url):
    urlpath = urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0


def tld_length(tld):
    try:
        return len(tld)
    except:
        return -1


def abnormal_url(url):
    hostname = urlparse(url).hostname
    hostname = str(hostname)
    match = re.search(hostname, url)
    if match:
        # print match.group()
        return 1
    else:
        # print 'No matching pattern found'
        return 0


# print(embeded_domains('https://api.github.com/k1rill-dev/ScarQR_API/blob/master/tools.py'))


url = 'myspace.com/thewarrenbrothers/blog'

signs_pred = [[use_of_ip(url),  count_dot(url), count_www(url), count_dog(url),
               count_dir(url), embeded_domains(url), short_url(url), count_https(url),
               count_http(url), count_per(url), count_ask(url), count_min(url),
               count_rav(url), url_len(url), hostname_len(url), sus_url(url),
               count_dig(url), count_let(url)]]

model = joblib.load('model/my_model.pkl')

print(model.predict(signs_pred))

# bst = xgb.Booster({'nthread': 4})  # init model
# bst.load_model('model/model.txt')  # load data
#
# print(bst.predict(xgb.DMatrix(signs_pred)))
