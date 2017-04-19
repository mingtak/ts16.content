# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from Products.CMFPlone.utils import safe_unicode
import json
import transaction
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
import logging


logger = logging.getLogger('morear.content')
LIMIT=20


class ToVote(BrowserView):

    def __call__(self):
        context = self.context
        request = self.request
        portal = api.portal.get()
        alsoProvides(request, IDisableCSRFProtection)

        userId = request.form.get('email', '')
        if not userId:
            request.response.redirect(portal.absolute_url())
            return

        voteItems = request.form.get('voteItems', '')
        voteItems = voteItems.split(',')
        if len(voteItems) != 3:
            request.response.redirect(portal.absolute_url())
            return

        vote = portal['vote']
        voteResultString = vote.description

        if voteResultString:
            voteResult = json.loads(voteResultString.split('|||')[0])
            voteCount = json.loads(voteResultString.split('|||')[1])
        else:
            voteResult = {}
            voteCount = {}
        if userId in voteResult:
            request.response.redirect('%s?voted=1' % portal.absolute_url())
            return
        voteResult[userId] = voteItems
        for uid in voteItems:
            count = voteCount.get(uid, 0) + 1
            voteCount[uid] = count


        vote.description = '%s|||%s' % (json.dumps(voteResult), json.dumps(voteCount))
        request.response.redirect('%s?thanks=1' % portal.absolute_url())
        transaction.commit()
        return


class CoverView(BrowserView):

    template = ViewPageTemplateFile("template/cover_view.pt")

    def __call__(self):
        context = self.context
        request = self.request
        portal = api.portal.get()

        vote = portal['vote']
        try:
            self.voteCount = json.loads(vote.description.split('|||')[1])
        except:
            self.voteCount = {}

        return self.template()

