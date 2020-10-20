from django.core.exceptions import ObjectDoesNotExist

from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension

import xml.etree.ElementTree as etree

from bokstaever.models import Gallery
from images.models import Image


class EscapeHTMLExtension(Extension):
    def extendMarkdown(self, md):
        del md.preprocessors["html_block"]
        del md.inlinePatterns["html"]


def error_el(what, pk):
    el = etree.Element("span")
    el.set("class", "danger")
    el.text = f"{what} {pk} does not exist!"
    return el


class ImagePattern(InlineProcessor):
    def handleMatch(self, m, data):
        pk = m.group(1)

        try:
            image = Image.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return error_el("Image", pk), m.start(0), m.end(0)

        root_element = etree.Element("img")
        srcset = ""
        for img in image.files.filter(width__gt=200):
            srcset += f"{img.image_file.url} {img.width}w,"

        root_element.set("srcset", srcset)
        root_element.set("alt", image.title)
        root_element.set("src", image.files.last().image_file.url)
        return root_element, m.start(0), m.end(0)


class ImageExtension(Extension):
    def extendMarkdown(self, md):
        self.parser = md.parser

        IMAGE_PATTERN = r"\!\[(\d+)\]"

        md.inlinePatterns.register(ImagePattern(IMAGE_PATTERN), "image", 1000)


class GalleryPattern(InlineProcessor):
    def handleMatch(self, m, data):
        pk = m.group(1)

        try:
            gallery = Gallery.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return error_el("Gallery", pk), m.start(0), m.end(0)

        root_element = etree.Element("div")
        root_element.set("class", "gallery")

        wrapper_element = etree.SubElement(root_element, "div")
        wrapper_element.set("class", "thumbnails")
        for image in gallery.images.all():
            link_element = etree.SubElement(wrapper_element, "a")
            link_element.set("href", image.files.last().image_file.url)

            thumbnail_element = etree.SubElement(link_element, "div")
            thumbnail_element.set("class", "thumbnail")

            image_element = etree.SubElement(thumbnail_element, "img")
            image_element.set("src", image.thumbnail.image_file.url)

        return root_element, m.start(0), m.end(0)


class GalleryExtension(Extension):
    def extendMarkdown(self, md):
        self.parser = md.parser

        GALLERY_PATTERN = r"\!\((\d+)\)"

        md.inlinePatterns.register(GalleryPattern(GALLERY_PATTERN), "gallery", 1000)
