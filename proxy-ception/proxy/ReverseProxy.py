"""
:GLOSS::Description: ReverseProxy
"""

# Import necessary classes from the packages
import logging

class ReverseProxy(object):

    def __init__(self, load_balancer):
        self.load_balancer = load_balancer
        self.logger = logging.getLogger(__name__)