"""
Program to analize the logs files of an apache server.
An example of file acommpanies this file: access.log
"""
import re

def get_user_agent(line: str) -> str:
    """
    Get the user agent of the line.

    Expamples
    ---------
    >>> get_user_agent('66.249.66.35 - - [15/Sep/2023:00:18:46 +0200] "GET /~luis/sw05-06/libre_m2_baja.pdf HTTP/1.1" 200 5940849 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"')
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

    >>> get_user_agent('147.96.46.52 - - [10/Oct/2023:12:55:47 +0200] "GET /favicon.ico HTTP/1.1" 404 519 "https://antares.sip.ucm.es/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"')
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0'
    """
    user_agent=re.compile('"\s".*"')
    agent=user_agent.findall(line)
    prue = agent[0].split('"')
#    prue2 = "'" + prue[2] + "'"
    return prue[2]

#a=get_user_agent('66.249.66.35 - - [15/Sep/2023:00:18:46 +0200] "GET /~luis/sw05-06/libre_m2_baja.pdf HTTP/1.1" 200 5940849 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"')
#print(a)


    #raise NotImplementedError()

def is_bot(line: str) -> bool:
    '''
    Check of the access in the line correspons to a bot

    Examples
    --------
    >>> is_bot('147.96.46.52 - - [10/Oct/2023:12:55:47 +0200] "GET /favicon.ico HTTP/1.1" 404 519 "https://antares.sip.ucm.es/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"')
    False

    >>> is_bot('66.249.66.35 - - [15/Sep/2023:00:18:46 +0200] "GET /~luis/sw05-06/libre_m2_baja.pdf HTTP/1.1" 200 5940849 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"')
    True

    >>> is_bot('213.180.203.109 - - [15/Sep/2023:00:12:18 +0200] "GET /robots.txt HTTP/1.1" 302 567 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"')
    True
    '''
    if "Bot" in get_user_agent(line) or "bot" in get_user_agent(line) or "BOT" in get_user_agent(line):
        return True
    else:
        return False
#bb = is_bot('66.249.66.135 - - [09/Oct/2023:23:29:50 +0200] "GET /sic/investigacion/publicaciones/pdfs/SIC-8-11.pdf HTTP/1.1" 302 648 "-" "Googlebot/2.1 (+http://www.google.com/bot.html)"')
#print(bb)
#cc= is_bot('34.105.93.183 - - [09/Oct/2023:07:17:31 +0200] "GET /favicon.ico HTTP/1.1" 404 461 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"')
#print(cc)
#dd=is_bot('20.120.74.197 - - [09/Oct/2023:12:46:37 +0200] "GET /robots.txt HTTP/1.1" 404 498 "-" "python-requests/2.27.1"')
#print(dd)
    #raise NotImplementedError()


def get_ipaddr(line):
    '''
    Gets the IP address of the line

    >>> get_ipaddr('213.180.203.109 - - [15/Sep/2023:00:12:18 +0200] "GET /robots.txt HTTP/1.1" 302 567 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"')
    '213.180.203.109'

    >>> get_ipaddr('147.96.46.52 - - [10/Oct/2023:12:55:47 +0200] "GET /favicon.ico HTTP/1.1" 404 519 "https://antares.sip.ucm.es/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"')
    '147.96.46.52'
    '''
    searchIP = line.split(' ')
#    userIP = "'"+searchIP[0]+"'"
    userIP=searchIP[0]
    return userIP
#myIP=get_ipaddr('34.105.93.183 - - [09/Oct/2023:07:17:30 +0200] "GET / HTTP/1.1" 200 464 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"')
#print(myIP)
    #raise NotImplementedError()



def get_hour(line: str) -> int:
    """
    Get the user agent of the line.

    Expamples
    ---------
    >>> get_hour('66.249.66.35 - - [15/Sep/2023:00:18:46 +0200] "GET /~luis/sw05-06/libre_m2_baja.pdf HTTP/1.1" 200 5940849 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"')
    0

    >>> get_hour('147.96.46.52 - - [10/Oct/2023:12:55:47 +0200] "GET /favicon.ico HTTP/1.1" 404 519 "https://antacres.sip.ucm.es/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"')
    12
    """
    corchete=re.compile(r'\[.*\]')
    fecha=corchete.findall(line)
    busco_hora = fecha[0].split(':')
    hora=int(busco_hora[1])
    return hora
#hh=get_hour('66.249.66.135 - - [09/Oct/2023:23:29:50 +0200] "GET /sic/investigacion/publicaciones/pdfs/SIC-8-11.pdf HTTP/1.1" 302 648 "-" "Googlebot/2.1 (+http://www.google.com/bot.html)"')
#print(hh)
#    raise NotImplementedError()


from typing import TypeVar, Dict
def histbyhour(filename: str) -> dict[int, int]:
    '''
    Computes the histogram of access by hour
    '''

    histo_horas=dict()
    with open(filename, 'r') as f:
        for log_line in f:
                hhh=get_hour(log_line)
                if hhh in histo_horas:
                    histo_horas[hhh]=histo_horas[hhh]+1
                else:
                    histo_horas[hhh]=1
    return histo_horas
    #raise NotImplementedError()
#myhisto=histbyhour('access_short.txt')
#print(myhisto)
def ipaddreses(filename: str) -> set[str]:
    '''
    Returns the IPs of the accesses that are not bots
    '''
    Not_bots_IPs =set()
    with open(filename, 'r') as f:
        for log_line in f:
            bot_ = is_bot(log_line)
            if(bot_ == False):
                Not_bots_IPs.add(get_ipaddr(log_line))
    return Not_bots_IPs
#listaIPs=ipaddreses('access.log')
#print(listaIPs)
#    raise NotImplementedError()



import doctest

def test_doc():
    doctest.run_docstring_examples(get_user_agent, globals(), verbose=True)
    doctest.run_docstring_examples(is_bot, globals(), verbose=True)
    doctest.run_docstring_examples(get_ipaddr, globals(), verbose=True)
    doctest.run_docstring_examples(get_hour, globals(), verbose=True)


def test_ipaddresses():
    assert ipaddreses('access_short.log') == {'34.105.93.183', '39.103.168.88'}

def test_hist():
    hist = histbyhour('access_short.log')
    assert hist == {5: 3, 7: 2, 23: 1}
