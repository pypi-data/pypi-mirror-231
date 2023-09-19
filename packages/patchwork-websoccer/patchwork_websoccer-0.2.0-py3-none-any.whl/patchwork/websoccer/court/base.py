# -*- coding: utf-8 -*-
from functools import cached_property
from typing import Iterable, Type

from patchwork.core import Component
from patchwork.core.client.task import FrozenTask
from patchwork.core.config.base import ClassConfig
from patchwork.websoccer.client.base import BaseClient
from patchwork.websoccer.router.base import BaseRouter


class BaseCourt(Component):

    class Config(Component.Config):
        router: ClassConfig[Type[BaseRouter]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subscription = {}
        self._clients = set()

    @cached_property
    def router(self) -> BaseRouter:
        return self.settings.router.instantiate()

    async def client(self, client: BaseClient):
        self._clients.add(client)
        await client.connect(self)
        try:
            await client.listen()
        finally:
            await client.disconnect(self)
            self._clients.remove(client)
            orphaned_routes = self.get_routes(client)
            if orphaned_routes:
                await self.remove_route(orphaned_routes, client)

    async def _stop(self) -> bool:
        for client in self._clients:
            await client.disconnect(self)

        return True

    async def forward_task(self, task: FrozenTask) -> bool:

        destinations = self.router.route_task(task)
        if not destinations:
            self.logger.debug(f"no route for task {task.uuid}")
            return True

        for client, payloads in destinations.items():
            try:
                for payload in payloads:
                    await client.send(payload)
            except Exception as e:
                self.logger.warning(
                    f"unable to forward task {task.uuid} to client {client}: {e.__class__.__name__}({e})",
                    exc_info=True
                )

        return True

    async def _subscribe(self, queue_names: Iterable[str]):
        raise NotImplementedError()

    async def _unsubscribe(self, queue_names: Iterable[str]):
        raise NotImplementedError()

    async def add_route(self, routes: Iterable[str], client: BaseClient):
        to_add = set()

        for route_id in routes:
            queue_names = self.router.add(route_id, client)

            for name in queue_names:
                if name not in self.subscription or self.subscription[name] == 0:
                    self.subscription[name] = 0
                    to_add.add(name)

                self.subscription[name] += 1

        if to_add:
            await self._subscribe(to_add)

    async def remove_route(self, routes: Iterable[str], client: BaseClient):
        to_remove = set()

        for route_id in routes:
            queue_names = self.router.remove(route_id, client)

            for name in queue_names:
                if name not in self.subscription:
                    # should never happen
                    continue
                self.subscription[name] = -1

                if self.subscription[name] == 0:
                    to_remove.add(name)

        if to_remove:
            await self._unsubscribe(to_remove)

    def get_routes(self, client: BaseClient):
        routes = self.router.get(client)
        return tuple(routes) if routes is not None else None
