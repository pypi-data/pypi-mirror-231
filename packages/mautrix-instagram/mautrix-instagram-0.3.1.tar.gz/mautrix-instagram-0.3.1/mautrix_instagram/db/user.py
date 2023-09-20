# mautrix-instagram - A Matrix-Instagram puppeting bridge.
# Copyright (C) 2020 Tulir Asokan
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

from attr import dataclass
import asyncpg

from mauigpapi.state import AndroidState
from mautrix.types import RoomID, UserID
from mautrix.util.async_db import Database

fake_db = Database.create("") if TYPE_CHECKING else None


@dataclass
class User:
    db: ClassVar[Database] = fake_db

    mxid: UserID
    igpk: int | None
    state: AndroidState | None
    notice_room: RoomID | None
    seq_id: int | None
    snapshot_at_ms: int | None
    oldest_cursor: str | None
    total_backfilled_portals: int | None
    thread_sync_completed: bool

    @property
    def _values(self):
        return (
            self.mxid,
            self.igpk,
            self.state.json() if self.state else None,
            self.notice_room,
            self.seq_id,
            self.snapshot_at_ms,
            self.oldest_cursor,
            self.total_backfilled_portals,
            self.thread_sync_completed,
        )

    _columns = ",".join(
        (
            "mxid",
            "igpk",
            "state",
            "notice_room",
            "seq_id",
            "snapshot_at_ms",
            "oldest_cursor",
            "total_backfilled_portals",
            "thread_sync_completed",
        )
    )

    async def insert(self) -> None:
        q = f"""
        INSERT INTO "user" ({self._columns})
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
        """
        await self.db.execute(q, *self._values)

    async def update(self) -> None:
        q = """
        UPDATE "user"
        SET igpk=$2, state=$3, notice_room=$4, seq_id=$5, snapshot_at_ms=$6,
            oldest_cursor=$7, total_backfilled_portals=$8, thread_sync_completed=$9
        WHERE mxid=$1
        """
        await self.db.execute(q, *self._values)

    async def save_seq_id(self) -> None:
        q = 'UPDATE "user" SET seq_id=$2, snapshot_at_ms=$3 WHERE mxid=$1'
        await self.db.execute(q, self.mxid, self.seq_id, self.snapshot_at_ms)

    @classmethod
    def _from_row(cls, row: asyncpg.Record) -> User:
        data = {**row}
        state_str = data.pop("state")
        return cls(state=AndroidState.parse_json(state_str) if state_str else None, **data)

    @classmethod
    async def get_by_mxid(cls, mxid: UserID) -> User | None:
        q = f'SELECT {cls._columns} FROM "user" WHERE mxid=$1'
        row = await cls.db.fetchrow(q, mxid)
        if not row:
            return None
        return cls._from_row(row)

    @classmethod
    async def get_by_igpk(cls, igpk: int) -> User | None:
        q = f'SELECT {cls._columns} FROM "user" WHERE igpk=$1'
        row = await cls.db.fetchrow(q, igpk)
        if not row:
            return None
        return cls._from_row(row)

    @classmethod
    async def all_logged_in(cls) -> list[User]:
        q = f'SELECT {cls._columns} FROM "user" WHERE igpk IS NOT NULL'
        rows = await cls.db.fetch(q)
        return [cls._from_row(row) for row in rows]
