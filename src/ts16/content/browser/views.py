# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from Products.CMFPlone.utils import safe_unicode
import json
import logging


logger = logging.getLogger('morear.content')
LIMIT=20


class ToVote(BrowserView):

    def __call__(self):
        context = self.context
        request = self.request
        portal = api.portal.get()

#        import pdb; pdb.set_trace()

        userId = request.form.get('email', '')
        if not userId:
            try:
                userId = api.user.get_current().id
            except:
                request.response.redirect(portal.absolute_url())
                return

        if not userId:
            request.response.redirect(portal.absolute_url())
            return

        voteItems = request.form.get('voteItems', '')
        if not voteItems:
            voteItems = request.cookies.get('voteItems', '')

        import pdb; pdb.set_trace()
        voteItems = voteItems.split(',')
#        else:
#            voteItems = request.cookies.get('itemInCart', '')


        if len(voteItems) != 3:
            request.response.redirect(portal.absolute_url())
            return

        vote = portal['vote']
        voteResultString = vote.description
#        import pdb; pdb.set_trace()
        if voteResultString:
            voteResult = json.loads(voteResultString)
        else:
            voteResult = {}
        if userId in voteResult:
            request.response.redirect('%s?voted=1' % portal.absolute_url())
            return
        voteResult[userId] = voteItems
        vote.description = json.dumps(voteResult)
        request.response.redirect('%s?thanks=1' % portal.absolute_url())
        return


class CoverView(BrowserView):

    template = ViewPageTemplateFile("template/cover_view.pt")

    def __call__(self):
        context = self.context
        request = self.request
#        portal = api.portal.get()

        return self.template()

