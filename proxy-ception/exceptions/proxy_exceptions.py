class ProxyError(Exception):
    """Base class for exceptions raised by the proxy module."""


class LoadBalancerError(Exception):
    """Base class for exceptions raised by the load_balancer module."""


class InvalidConfigurationException(ProxyError):
    """Exception raised when an invalid configuration is detected."""