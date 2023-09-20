from ..filters.base import BaseFilter
from ..middlewares.base import BaseMiddleware


class TelegramUpdate:
    def __init__(self, router, update: str):
        self.router = router
        self.update = update

    def register_middleware(self, middleware: BaseMiddleware):
        for handler in self.router.handlers:
            if handler[1] == self.update:
                self.router.handlers.remove(handler)
                middlewares = [] if len(handler) == 3 else [middle for middle in handler[3]]
                middlewares.append(middleware)
                self.router.handlers.append((handler[0], self.update, handler[2], middlewares,))

    def register(self, handler: callable, *filters: BaseFilter):
        self.router.handlers.append((handler, self.update, filters,))

    def __call__(self, *filters: BaseFilter):
        def wrapper(func):
            self.router.handlers.append((func, self.update, filters,))
        return wrapper