from typing import List
from pydantic import BaseModel
from .application_item import ApplicationItem
from .update_item import UpdateItem


class ApplicationRepository(BaseModel):
    _applications: dict[str, ApplicationItem] = dict()
    _updates: dict[str, UpdateItem] = dict()

    def get_applications(self) -> list[ApplicationItem]:
        return list(self._applications.values())

    def get_application(self, application_id: str) -> ApplicationItem:
        return self._applications[application_id]

    def create_application(self, application_item: ApplicationItem):
        self._applications[application_item.guid] = application_item

    def create_update(self, update_item: UpdateItem):
        self._updates[update_item.guid] = update_item

    def get_update(self, update_id: str) -> UpdateItem:
        return self._updates[update_id]

    def get_application_updates(self, application_id: str) -> list[UpdateItem]:
        return [update for update in self._updates.values() if update.application_id == application_id]
