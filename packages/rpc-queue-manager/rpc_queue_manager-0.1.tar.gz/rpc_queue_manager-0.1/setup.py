from setuptools import setup

setup(
    name='rpc_queue_manager',
    version='0.1',
    description='A simple library for interacting with RabbitMQ RPC in Django',
    author='Surya Dev Singh',
    author_email='surya.dev@careers360.com',
    packages=['rpc_queue_manager'],
    install_requires=[
        'pika',
    ],
)
