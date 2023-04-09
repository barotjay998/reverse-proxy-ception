"""
:GLOSS::Description: kafkatastrophe

The 'kafkatastrophe' package is responsible for managing the configuration of the Kafka distributed streaming platform 
in the system. It provides tools and utilities for setting up and maintaining Kafka clusters, configuring topics and 
partitions, managing consumer groups, and optimizing performance. The package also includes features for monitoring and 
analyzing Kafka traffic, which can help identify issues and optimize performance. Additionally, the package may include 
integrations with other components of the distributed system, such as the reverse proxy, to enable seamless data processing 
and communication.

"""

# Import the key classes and functions from the package 
"""
IDEA:
We will need to import the classes and functions from the sub-packages.
The possible sub-packages are:

    - producer: KafkaProducer:: A class that is used to produce messages to a Kafka cluster. 
                                It is typically used by applications that need to send messages 
                                to Kafka topics.
from .producer import KafkaProducer

    - consumer: KafkaConsumer:: A class that is used to consume messages from a Kafka cluster. 
                                It is typically used by applications that need to read messages 
                                from Kafka topics.
from .consumer import KafkaConsumer

    - exceptions : Custom exceptions for the package
from .exceptions import *
from .exceptions.kafkatastrophe_exceptions import KafkaError
                                KafkaError:: An exception class that is raised when an error occurs while producing 
                                             or consuming messages with Kafka. This class provides information about the error 
                                             that occurred and can be used to handle errors gracefully in an application.
"""


# Define the list of objects that are imported when the package is imported
# Used in the case of "from kafkatastrophe import *"
__all__ = [
    # 'KafkaProducer', 
    # 'KafkaConsumer'
]

# Define the version number of the package
__version__ = '1.0.0'