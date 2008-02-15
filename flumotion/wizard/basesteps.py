# -*- Mode: Python -*-
# vi:si:et:sw=4:sts=4:ts=4
#
# Flumotion - a streaming media server
# Copyright (C) 2004,2005,2006,2007,2008 Fluendo, S.L. (www.fluendo.com).
# All rights reserved.

# This file may be distributed and/or modified under the terms of
# the GNU General Public License version 2 as published by
# the Free Software Foundation.
# This file is distributed without any warranty; without even the implied
# warranty of merchantability or fitness for a particular purpose.
# See "LICENSE.GPL" in the source distribution for more information.

# Licensees having purchased or holding a valid Flumotion Advanced
# Streaming Server license may use this file in accordance with the
# Flumotion Advanced Streaming Server Commercial License Agreement.
# See "LICENSE.Flumotion" in the source distribution for more information.

# Headers in this file shall remain intact.

import gettext

from flumotion.common import messages
from flumotion.wizard.workerstep import WorkerWizardStep

__version__ = "$Rev$"
T_ = messages.gettexter('flumotion')
_ = gettext.gettext


class AudioSourceStep(WorkerWizardStep):
    section = _('Production')
    def __init__(self, wizard, model):
        self.model = model
        WorkerWizardStep.__init__(self, wizard)


class VideoSourceStep(WorkerWizardStep):
    section = _('Production')
    icon = 'widget_doc.png'

    def __init__(self, wizard, model):
        self.model = model
        WorkerWizardStep.__init__(self, wizard)

    # WizardStep

    def get_next(self):
        from flumotion.wizard.overlaystep import OverlayStep
        return OverlayStep(self.wizard, self.model)


class VideoEncoderStep(WorkerWizardStep):
    section = _('Conversion')

    def __init__(self, wizard, model):
        self.model = model
        WorkerWizardStep.__init__(self, wizard)


class AudioEncoderStep(WorkerWizardStep):
    glade_file = 'wizard_audio_encoder.glade'
    section = _('Conversion')

    def __init__(self, wizard, model):
        self.model = model
        WorkerWizardStep.__init__(self, wizard)

    # WizardStep

    def get_next(self):
        return None



