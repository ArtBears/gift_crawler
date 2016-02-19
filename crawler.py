import urllib
import mechanize
from mechanize import ParseResponse, urlopen

uri = 'http://matchfinderonline.blackbaud.com/MatchGiftInquiry.aspx?cid=21227'

headers = {
    'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13',
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml; q=0.9,*/*; q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded'
}

form_field = (
  (r'OrganizationName', r'A'),
  (r'Submit', r'1')
)



response = urlopen(uri)
forms = ParseResponse(response, backwards_compat=False)
form = forms[0]
print form
form["OrganizationName"] = 'A'


# form.click() returns a mechanize.Request object
print urlopen(form.click()).read()