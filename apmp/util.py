from bs4 import BeautifulSoup


def modify_html_code(html_code):
    soup = BeautifulSoup(html_code, features='html.parser')

    for x in soup.find_all('h3'):
        x.attrs =  {'class': 'd-flex pt-2 pb-2 ps-4', 'style': 'background-color: #546B62; color: white;'}

    for x in soup.find_all('ul'):
        x.attrs = {'style': 'font-size: 16px; font-weight: 500; color: #454545', 'class': 'ms-5'}
    
    for x in soup.find_all('ol'):
        x.attrs = {'style': 'font-size: 16px; font-weight: 500; color: #454545', 'class': 'ms-5'}
    
    for x in soup.find_all('p'):
        x.attrs = {'style': 'font-size: 18px; color: #454545; text-indent:4%', 'align' : 'justify', 'class': 'ms-5 mt-4'}

    

    return soup

"""

<h3>
    Comming Soon
</h3>


modify_tag = modify_html_code(tag)
print(modify_tag)

"""