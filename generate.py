#!/usr/bin/python
import os
import re


outdir="."

def get_citation_stats():
    url=r'http://scholar.google.ca/citations?hl=en&user=WIF0SRYAAAAJ'
    #os.system('wget --quiet --output-document=scholar.html {}'.format(url))
    txt = open('scholar.html').read()
    res = re.search(r'cit-data', txt)
    print "Success!", res


if __name__ == "__main__":
    get_citation_stats()
    template = open("template.htm").read()
    for root, dirs, files in os.walk('.'):
        for p in [f for f in files if f.endswith('.htm')]:
            txt = open(os.path.join(root, p)).read()
            p = p[:-4]
            output = re.sub(r'\$content', txt, template)
            output = re.sub(r'\[\[{}\]\]'.format(p), p, output)
            output = re.sub(r'\[\[(\w+)\]\]', 
                            r'<a href="/\1.html">\1</a>', output)
            output = re.sub(r'\[\[([\w ]+)\|([^\]]+)\]\]', 
                            r'<a href="\2">\1</a>', output)
            fp = open(os.path.join(root, p) + ".html", "w")
            fp.write(output)
            fp.close()
