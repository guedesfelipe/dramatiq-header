from dramatiq.middleware import Middleware
import contextvars


class HeadersMessage(Middleware):
    """Expose headers via an options message through a thread-local
    variable in middleware.

    """

    _HEADERS: contextvars.ContextVar[dict] = contextvars.ContextVar(
        '_HEADERS', default={}
    )

    def __init__(self, header_name: str | None = None) -> None:
        self.header_name = header_name

    @classmethod
    def get_headers(cls):
        """Get the message that triggered the current actor. Messages
        are thread local so this returns ``None`` when called outside
        of actor code.
        """
        return cls._HEADERS.get()

    def before_process_message(self, _, message):
        if not self.header_name:
            self._HEADERS.set(message.options)
        else:
            # TODO: Add DEBUG log when don't find the header
            self._HEADERS.set(
                message.options.get(self.header_name, message.options)
            )
