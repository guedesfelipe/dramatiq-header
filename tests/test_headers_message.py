from unittest.mock import Mock
from dramatiq_header import HeadersMessage


def test_get_headers_no_header_name():
    middleware = HeadersMessage()
    message = Mock(options={'key': 'value'})

    middleware.before_process_message(None, message)

    headers = HeadersMessage.get_headers()
    assert headers == {'key': 'value'}

def test_get_headers_with_header_name():
    middleware = HeadersMessage(header_name='custom_header')
    message = Mock(options={'custom_header': 'custom_value'})

    middleware.before_process_message(None, message)

    headers = HeadersMessage.get_headers()
    assert headers == 'custom_value'

def test_get_headers_with_missing_header():
    middleware = HeadersMessage(header_name='nonexistent_header')
    mock_header ={'other_header': 'other_value'} 
    message = Mock(options=mock_header)

    middleware.before_process_message(None, message)

    headers = HeadersMessage.get_headers()
    assert headers == mock_header

def test_get_headers_without_message_options():
    middleware = HeadersMessage()
    message = Mock(options=None)

    middleware.before_process_message(None, message)

    headers = HeadersMessage.get_headers()
    assert headers is None
