from django.core.exceptions import ObjectDoesNotExist

from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension

from markdown.util import etree

from bokstaever.models import Gallery


class EscapeHTMLExtension(Extension):
    def extendMarkdown(self, md):
        del md.preprocessors['html_block']
        del md.inlinePatterns['html']


class GalleryPattern(InlineProcessor):
    def handleMatch(self, m, data):
        pk = m.group(1)

        try:
            gallery = Gallery.objects.get(pk=pk)
        except ObjectDoesNotExist:
            el = etree.Element('span')
            el.set('class', 'danger')
            el.text = "Gallery {} doesn't exist!".format(pk)
            return el, m.start(0), m.end(0)

        root_element = etree.Element('div')
        root_element.set('class', 'gallery')

        wrapper_element = etree.SubElement(root_element, "div")
        wrapper_element.set('class', 'thumbnails')
        for image in gallery.images.all():
            link_element = etree.SubElement(wrapper_element, "a")
            link_element.set('href', image.files.first().image_file.url)

            thumbnail_element = etree.SubElement(link_element, "div")
            thumbnail_element.set('class', 'thumbnail')

            image_element = etree.SubElement(thumbnail_element, "img")
            image_element.set('src', image.files.first().image_file.url)

        return root_element, m.start(0), m.end(0)


class GalleryExtension(Extension):
    def extendMarkdown(self, md):
        self.parser = md.parser

        GALLERY_PATTERN = r'\!\((\d+)\)'

        md.inlinePatterns.register(
                GalleryPattern(GALLERY_PATTERN),
                'gallery',
                1000)
