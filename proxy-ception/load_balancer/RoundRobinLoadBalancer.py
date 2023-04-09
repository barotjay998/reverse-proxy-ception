"""
:GLOSS::Description: RoundRobinLoadBalancer
"""

# Import necessary packages
import logging

class RoundRobinLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.logger = logging.getLogger(__name__)
        self.logger.debug("RoundRobinLoadBalancer initialized with servers: {}".format(self.servers))