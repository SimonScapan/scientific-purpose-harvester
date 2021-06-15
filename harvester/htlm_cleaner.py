import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>|[\n\t\r]|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, ' ', raw_html)
  return cleantext