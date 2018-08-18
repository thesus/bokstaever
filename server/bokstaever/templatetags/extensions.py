from django.core.exceptions import ObjectDoesNotExist

from markdown.inlinepatterns import Pattern
from markdown.extensions import Extension

from markdown.util import etree

from bokstaever.models import Gallery


class EscapeHTMLExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        del md.preprocessors['html_block']
        del md.inlinePatterns['html']


class GalleryPattern(Pattern):
    def handleMatch(self, m):
        pk = m.groups()[1]

        try:
            gallery = Gallery.objects.get(pk=pk)
        except ObjectDoesNotExist:
            el = etree.Element('span')
            el.set('class', 'danger')
            el.text = "Gallery {} doesn't exist!".format(pk)
            return el

        root_element = etree.Element('div')
        root_element.set('class', 'gallery')

        wrapper_element = etree.SubElement(root_element, "div")
        wrapper_element.set('class', 'thumbnails')
        for image in gallery.images.all():
            link_element = etree.SubElement(wrapper_element, "a")
            link_element.set('href', image.image.url)

            thumbnail_element = etree.SubElement(link_element, "div")
            thumbnail_element.set('class', 'thumbnail')

            image_element = etree.SubElement(thumbnail_element, "img")
            image_element.set('src', image.thumbnail.url)

        return root_element


class GalleryExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        self.parser = md.parser

        GALLERY_PATTERN = r'\!\((\d+)\)'

        md.inlinePatterns.add('gallery', GalleryPattern(
            GALLERY_PATTERN, self), '<reference')
