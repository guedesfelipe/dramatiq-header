<h1 align="center">
  🦅 Dramatiq Header Middleware for RabbitMQ
</h1>


# 🛠 Installation

```sh
pip install dramatiq-header
```

# ⬆️  Upgrade version

```sh
pip install dramatiq-header --upgrade
```

# ✏️  Usage


## Worker code:

```py
import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from dramatiq_header import HeadersMessage # Import Middleware


rabbitmq_broker = RabbitmqBroker()
dramatiq.set_broker(rabbitmq_broker)


rabbitmq_broker.add_middleware(HeadersMessage()) # Add Middleware


@dramatiq.actor(queue_name='example')
def my_task(message):
    print(f'Message Received: {message}')
    print(HeadersMessage.get_headers()) # Get headers

```

> [!TIP]
> You can add middleware specifically to monitor a header key. For example:
```py
rabbitmq_broker.add_middleware(HeadersMessage('x-test-header'))
```


## Sender example

```py
import dramatiq
from dramatiq import Message
from dramatiq.brokers.rabbitmq import RabbitmqBroker


rabbitmq_broker = RabbitmqBroker()
dramatiq.set_broker(rabbitmq_broker)


def send_message(msg: str):
    message = Message(
        queue_name='example',
        actor_name='my_task',
        args=(msg, ),
        kwargs={},
        options={'x-test-header': 'test-header'}, # Send your entire header here
    )
    rabbitmq_broker.enqueue(message)


if __name__ == '__main__':
    send_message('test message')
```

> [!IMPORTANT]  
> This library does NOT transmit the header using the RabbitMQ header property; rather, it sends the header as metadata within the message that Dramatiq already dispatches.


---

<p align="center">
  <a href="https://ko-fi.com/guedesfelipe" target="_blank">
    <img src="https://user-images.githubusercontent.com/25853920/175832199-6c75d866-31b8-4209-bd1a-db116a6dd032.png" width=300 />
  </a>
</p>
