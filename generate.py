import re


outdir="."

if __name__ == "__main__":
    template = open("template.htm").read()
    pages=['index', 'contact', 'about', 'people', 'allpeople', 'publications', 'seminars']
    for p in pages:
        txt = open(p + ".htm").read()
        output = re.sub(r'\$content', txt, template)
        output = re.sub(r'\[\[{}\]\]'.format(p), p, output)
        output = re.sub(r'\[\[(\w+)\]\]', r'<a href="\1.html">\1</a>', output)
        output = re.sub(r'\[\[([\w ]+)\|([^\]]+)\]\]', r'<a href="\2">\1</a>', output)
        fp = open(p + ".html", "w")
        fp.write(output)
        fp.close()
