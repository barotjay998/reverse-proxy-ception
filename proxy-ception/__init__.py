"""
:GLOSS::Description: proxy-ception

The 'proxy-ception' package is responsible for implementing the reverse proxy component of the distributed system. 
It provides functionality for handling incoming client requests, forwarding them to the appropriate web server, 
and returning the responses to the clients. The package also includes features for load balancing, caching, and security, 
which can help improve the performance and reliability of the system. Additionally, the package may include tools for 
monitoring and analyzing traffic to the system, which can help identify issues and optimize performance.

"""

# Import the key classes and functions from the package
"""
IDEA:
We will need to import the classes and functions from the sub-packages.
The possible sub-packages are:

    - proxy : Main class for the reverse proxy.
from .proxy import ReverseProxy

    - load_balancer: implementing simple round-robin load balancing
from .load_balancer import RoundRobinLoadBalancer

    - cache : LRU :: "Least Recently Used". 
                      An LRU cache will be a data structure that stores a limited number of items, 
                      and discards the least recently used items first when it reaches its maximum capacity.
from .cache import LRUCache

    - security
from .security import SSLCertificate

    - exceptions : Custom exceptions for the package
from .exceptions import *
"""

# Define the list of objects that are imported when the package is imported
# Used in the case of "from proxy-ception import *"
__all__ = [
    # 'ReverseProxy',
    # 'RoundRobinLoadBalancer',
    # 'LRUCache',
    # 'SSLCertificate'
]


# Define the version number of the package
__version__ = '1.0.0'