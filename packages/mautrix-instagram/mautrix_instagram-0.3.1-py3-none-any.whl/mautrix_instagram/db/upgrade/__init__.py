# mautrix-instagram - A Matrix-Instagram puppeting bridge.
# Copyright (C) 2022 Tulir Asokan, Sumner Evans
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
from mautrix.util.async_db import UpgradeTable

upgrade_table = UpgradeTable()

from . import (
    v00_latest_revision,
    v02_name_avatar_set,
    v03_relay_portal,
    v04_message_client_content,
    v05_message_ig_timestamp,
    v06_hidden_events,
    v07_reaction_timestamps,
    v08_sync_sequence_id,
    v09_backfill_queue,
    v10_portal_infinite_backfill,
    v11_per_user_thread_sync_status,
    v12_portal_thread_image_id,
    v13_fix_portal_thread_image_id,
    v14_puppet_contact_info_set,
)
