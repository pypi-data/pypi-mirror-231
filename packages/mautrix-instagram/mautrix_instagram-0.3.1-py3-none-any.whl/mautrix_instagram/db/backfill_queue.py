# mautrix-instagram - A Matrix-Instagram puppeting bridge.
# Copyright (C) 2022 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar
from datetime import datetime, timedelta

from asyncpg import Record
from attr import dataclass

from mautrix.types import RoomID, UserID
from mautrix.util.async_db import Database

fake_db = Database.create("") if TYPE_CHECKING else None


@dataclass
class Backfill:
    db: ClassVar[Database] = fake_db

    queue_id: int | None
    user_mxid: UserID
    priority: int
    portal_thread_id: str
    portal_receiver: int
    num_pages: int
    page_delay: int
    post_batch_delay: int
    max_total_pages: int
    dispatch_time: datetime | None
    completed_at: datetime | None
    cooldown_timeout: datetime | None

    @staticmethod
    def new(
        user_mxid: UserID,
        priority: int,
        portal_thread_id: str,
        portal_receiver: int,
        num_pages: int,
        page_delay: int = 0,
        post_batch_delay: int = 0,
        max_total_pages: int = -1,
    ) -> "Backfill":
        return Backfill(
            queue_id=None,
            user_mxid=user_mxid,
            priority=priority,
            portal_thread_id=portal_thread_id,
            portal_receiver=portal_receiver,
            num_pages=num_pages,
            page_delay=page_delay,
            post_batch_delay=post_batch_delay,
            max_total_pages=max_total_pages,
            dispatch_time=None,
            completed_at=None,
            cooldown_timeout=None,
        )

    @classmethod
    def _from_row(cls, row: Record | None) -> Backfill | None:
        if row is None:
            return None
        return cls(**row)

    columns = [
        "user_mxid",
        "priority",
        "portal_thread_id",
        "portal_receiver",
        "num_pages",
        "page_delay",
        "post_batch_delay",
        "max_total_pages",
        "dispatch_time",
        "completed_at",
        "cooldown_timeout",
    ]
    columns_str = ",".join(columns)

    @classmethod
    async def get_next(cls, user_mxid: UserID) -> Backfill | None:
        q = f"""
        SELECT queue_id, {cls.columns_str}
        FROM backfill_queue
        WHERE user_mxid=$1
            AND (
                dispatch_time IS NULL
                OR (
                    dispatch_time < $2
                    AND completed_at IS NULL
                )
            )
            AND (
                cooldown_timeout IS NULL
                OR cooldown_timeout < current_timestamp
            )
        ORDER BY priority, queue_id
        LIMIT 1
        """
        return cls._from_row(
            await cls.db.fetchrow(q, user_mxid, datetime.now() - timedelta(minutes=15))
        )

    @classmethod
    async def get(
        cls,
        user_mxid: UserID,
        portal_thread_id: str,
        portal_receiver: int,
    ) -> Backfill | None:
        q = f"""
        SELECT queue_id, {cls.columns_str}
        FROM backfill_queue
        WHERE user_mxid=$1
          AND portal_thread_id=$2
          AND portal_receiver=$3
        ORDER BY priority, queue_id
        LIMIT 1
        """
        return cls._from_row(
            await cls.db.fetchrow(q, user_mxid, portal_thread_id, portal_receiver)
        )

    @classmethod
    async def delete_all(cls, user_mxid: UserID) -> None:
        await cls.db.execute("DELETE FROM backfill_queue WHERE user_mxid=$1", user_mxid)

    @classmethod
    async def delete_for_portal(cls, portal_thread_id: str, portal_receiver: int) -> None:
        q = "DELETE FROM backfill_queue WHERE portal_thread_id=$1 AND portal_receiver=$2"
        await cls.db.execute(q, portal_thread_id, portal_receiver)

    async def insert(self) -> None:
        q = f"""
        INSERT INTO backfill_queue ({self.columns_str})
        VALUES ({','.join(f'${i+1}' for i in range(len(self.columns)))})
        RETURNING queue_id
        """
        row = await self.db.fetchrow(
            q,
            self.user_mxid,
            self.priority,
            self.portal_thread_id,
            self.portal_receiver,
            self.num_pages,
            self.page_delay,
            self.post_batch_delay,
            self.max_total_pages,
            self.dispatch_time,
            self.completed_at,
            self.cooldown_timeout,
        )
        self.queue_id = row["queue_id"]

    async def mark_dispatched(self) -> None:
        q = "UPDATE backfill_queue SET dispatch_time=$1 WHERE queue_id=$2"
        await self.db.execute(q, datetime.now(), self.queue_id)

    async def mark_done(self) -> None:
        q = "UPDATE backfill_queue SET completed_at=$1 WHERE queue_id=$2"
        await self.db.execute(q, datetime.now(), self.queue_id)

    async def set_cooldown_timeout(self, timeout) -> None:
        """
        Set the backfill request to cooldown for ``timeout`` seconds.
        """
        q = "UPDATE backfill_queue SET cooldown_timeout=$1 WHERE queue_id=$2"
        await self.db.execute(q, datetime.now() + timedelta(seconds=timeout), self.queue_id)
