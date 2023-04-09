"""
:GLOSS::

This will be a script that demonstrates how to use the ReverseProxy and RoundRobinLoadBalancer
classes from the proxy-ception package, and the KafkaProducer class from the
kafkatastrophe package, to build a distributed system that uses a reverse proxy
with a round-robin load balancer to forward requests to backend servers, and a Kafka
message broker to send messages between components.

Usage:
    python main.py

Requirements:
    - Python 3.x
    - proxy-ception package
    - kafkatastrophe package

License:
    This code is released under the MIT License.
"""

# Import necessary classes from the packages
import logging

"""
IDEA:
We will need to import the classes and functions from the sub-packages.
The possible sub-packages are:

from proxy-ception.proxy import ReverseProxy
from proxy-ception.load_balancer import RoundRobinLoadBalancer
from kafkatastrophe.producer import KafkaProducer
"""

# Define main function
def main():
    try:
        # obtain a system wide logger and initialize it to debug level to begin with
        logging.info ("Main - acquire a child logger and then log messages in the child")
        logger = logging.getLogger ("ReverseProxyAppln") # use this logger to log messages

        """
        TODO:
        IDEA: 

        Step1: We will need to set up the reverse proxy with a round-robin load balancer
        # load_balancer = RoundRobinLoadBalancer(["http://backend1.com", "http://backend2.com"])
        # reverse_proxy = ReverseProxy(load_balancer)

        Step2: We will need to send a message to a Kafka topic using the KafkaProducer
        # producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        # producer.send('my_topic', b'My message')

        Step3: We will need to use the reverse proxy to forward a request to a backend server
        # response = reverse_proxy.forward_request('/some/path', {'param1': 'value1'}, 'GET')
        """

    except Exception as e:
        logger.error ("Exception caught in main: {}".format (e))
        return


# Run main function if script is executed directly
if __name__ == "__main__":

    # set underlying default logging capabilities
    logging.basicConfig (level = logging.DEBUG,
                         format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s' )
  
    main()
