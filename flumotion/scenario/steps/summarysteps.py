# -*- Mode: Python -*-
# vi:si:et:sw=4:sts=4:ts=4

# Flumotion - a streaming media server
# Copyright (C) 2004,2005,2006,2007,2008,2009 Fluendo, S.L.
# Copyright (C) 2010,2011 Flumotion Services, S.A.
# All rights reserved.
#
# This file may be distributed and/or modified under the terms of
# the GNU Lesser General Public License version 2.1 as published by
# the Free Software Foundation.
# This file is distributed without any warranty; without even the implied
# warranty of merchantability or fitness for a particular purpose.
# See "LICENSE.LGPL" in the source distribution for more information.
#
# Headers in this file shall remain intact.

"""Summary steps for the ConfigurationAssistant

This file contains the summary steps, one for the live scenario and a
second one for the ondemand scenario.
"""
import gettext

from flumotion.ui.wizard import WizardStep

_ = gettext.gettext


class OndemandSummaryStep(WizardStep):
    name = "Summary"
    title = _("Summary")
    section = _("Summary")
    icon = 'summary.png'
    gladeFile = "summary-wizard.glade"
    lastStep = True
    docSection = 'help-configuration-assistant-summary'
    docAnchor = ''
    docVersion = 'local'

    # WizardStep

    def getNext(self):
        return None


class LiveSummaryStep(WizardStep):
    name = "Summary"
    title = _("Summary")
    section = _("Summary")
    icon = 'summary.png'
    gladeFile = "summary-wizard.glade"
    lastStep = True
    docSection = 'help-configuration-assistant-summary'
    docAnchor = ''
    docVersion = 'local'

    # WizardStep

    def getNext(self):
        return None
