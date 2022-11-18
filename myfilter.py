import panflute as pf

def action(elem, doc):
    if doc.format == 'html':
        if (isinstance(elem, pf.Code) or isinstance(elem, pf.CodeBlock)):
            return pf.convert_text(
                  '<div class = "downloadhint">{}</div>'
                  .format(elem.text))
    else:
        if (isinstance(elem, pf.Code) or isinstance(elem, pf.CodeBlock)):
            if ('exclude_in_pdf' in elem.classes):
                return []
    
if __name__ == '__main__':
    pf.toJSONFilter(action)
