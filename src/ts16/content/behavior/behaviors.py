# -*- coding: utf-8 -*-
from ts16.content import _
# from plone.autoform import directives
from plone.supermodel import directives
from zope import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope.component import adapts
from zope.interface import alsoProvides, implements
from zope.interface import provider
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.app.vocabularies.catalog import CatalogSource
from plone.dexterity.interfaces import IDexterityContent
#from plone.directives import dexterity
from plone.app.textfield import RichText
from plone.app.content.interfaces import INameFromTitle
from plone.namedfile.field import NamedBlobImage
from DateTime import DateTime
import random
#from plone.directives import form


class IBigImage(model.Schema):
    """ Add bigImage_* field """

    model.fieldset(
        'bigImage',
        label=_(u"bigImage"),
        fields=['bigImage_1',
                'bigImage_2',
                'bigImage_3',
                'bigImage_4',
                'bigImage_5',
                'bigImage_6',
                'bigImage_7',
                'bigImage_8',
                'bigImage_9',
                'bigImage_10',
        ]
    )

    bigImage_1 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page."),
        required=False,
    )

    bigImage_2 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page."),
        required=False,
    )

    bigImage_3 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page."),
        required=False,
    )

    bigImage_4 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page."),
        required=False,
    )

    bigImage_5 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page."),
        required=False,
    )

    bigImage_6 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page."),
        required=False,
    )

    bigImage_7 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page."),
        required=False,
    )

    bigImage_8 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page."),
        required=False,
    )

    bigImage_9 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page."),
        required=False,
    )

    bigImage_10 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page."),
        required=False,
    )


alsoProvides(IBigImage, IFormFieldProvider)



def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class BigImage(object):
    implements(IBigImage)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    bigImage_1 = context_property("bigImage_1")
    bigImage_2 = context_property("bigImage_2")
    bigImage_3 = context_property("bigImage_3")
    bigImage_4 = context_property("bigImage_4")
    bigImage_5 = context_property("bigImage_5")
    bigImage_6 = context_property("bigImage_6")
    bigImage_7 = context_property("bigImage_7")
    bigImage_8 = context_property("bigImage_8")
    bigImage_9 = context_property("bigImage_9")
    bigImage_10 = context_property("bigImage_10")
