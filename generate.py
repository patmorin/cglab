#!/usr/bin/python
import os
import re


outdir="../public_html"

def get_citation_stats():
    url=r'http://scholar.google.ca/citations?hl=en&user=WIF0SRYAAAAJ'
    #os.system('wget --quiet --output-document=scholar.html {}'.format(url))
    txt = open('scholar.html').read()
    res = re.search(r'cit-data', txt)
    print "Success!", res


if __name__ == "__main__":
    """Generate a website from a collection of .htm files"""

    # This file contains stuff common to all files.
    template = open("template.htm").read()

    # Walk around looking for files ending in .html.
    for root, dirs, files in os.walk('.'):
        for p in [f for f in files if f.endswith('.htm')]:
            txt = open(os.path.join(root, p)).read()
            p = p[:-4]

            # put this stuff into the template
            output = re.sub(r'\$content', txt, template)
            output = re.sub(r'\[\[{}\]\]'.format(p), p, output)

            # Substitute wiki-style [[ ]] links.
            if root != '.':
                subber =  r'<a href="/\1.html">\1</a>'
            else:
                subber =  r'<a href="\1.html">\1</a>'

            # The first form is [[pagename]].
            output = re.sub(r'\[\[(\w+)\]\]', subber, output)

            # The second form is [[text|url]].
            output = re.sub(r'\[\[([\w ]+)\|([^\]]+)\]\]', 
                            r'<a href="\2">\1</a>', output)

            # Write output .html file.
            fp = open(os.path.join(outdir, root, p) + ".html", "w")
            fp.write(output)
            fp.close()

