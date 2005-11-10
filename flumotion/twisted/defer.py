# -*- Mode: Python; test-case-name: flumotion.test.test_defer -*-
# vi:si:et:sw=4:sts=4:ts=4
#
# Flumotion - a streaming media server
# Copyright (C) 2004,2005 Fluendo, S.L. (www.fluendo.com). All rights reserved.

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

from twisted.internet import defer
from twisted.python import reflect

# See flumotion.test.test_defer for examples
def defer_generator(proc):
    def wrapper(*args, **kwargs):
        gen = proc(*args, **kwargs)
        result = defer.Deferred()

        # Add errback-of-last-resort
        def default_errback(failure, d):
            def print_traceback(f):
                import traceback
                print 'flumotion.twisted.defer.py: ' + \
                    'Unhandled error calling', proc.__name__, ':', f.type
                traceback.print_exc()
            d.addErrback(print_traceback)
            raise
        result.addErrback(default_errback, result)

        def generator_next():
            try:
                x = gen.next()
                if isinstance(x, defer.Deferred):
                    x.addCallback(callback, x).addErrback(errback, x)
                else:
                    result.callback(x)
            except StopIteration:
                result.callback(None)
            except Exception, e:
                result.errback(e)

        def errback(failure, d):
            def raise_error():
                k = failure.type
                if isinstance(k, str):
                    k = reflect.namedClass(k)
                if not k:
                    k = lambda v: Exception('%s: %r' % (failure.type, v))
                raise k(failure.value)
            d.value = raise_error
            generator_next()

        def callback(result, d):
            d.value = lambda: result
            generator_next()

        generator_next()

        return result

    return wrapper

def defer_generator_method(proc):
    return lambda self, *args, **kwargs: \
        defer_generator(proc)(self, *args, **kwargs)

class Resolution:
    """
    I am a helper class to make sure that the deferred is fired only once
    with either a result or exception.

    @ivar d: the deferred that gets fired as part of the resolution
    @type d: L{twisted.internet.defer.Deferred}
    """
    def __init__(self):
        self.d = defer.Deferred()
        self.fired = False

    def cleanup(self):
        """
        Clean up any resources related to the resolution.
        Subclasses can implement me.
        """
        pass
        
    def callback(self, result):
        """
        Make the result succeed, triggering the callbacks with the given result.
        If a result was already reached, do nothing.
        """
        if not self.fired:
            self.fired = True
            self.cleanup()
            self.d.callback(result)
    
    def errback(self, exception):
        """
        Make the result fail, triggering the errbacks with the given exception.
        If a result was already reached, do nothing.
        """
        if not self.fired:
            self.fired = True
            self.cleanup()
            self.d.errback(exception)
