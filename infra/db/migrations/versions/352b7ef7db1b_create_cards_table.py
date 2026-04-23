"""create_cards_table

Revision ID: 352b7ef7db1b
Revises: 
Create Date: 2026-04-23 21:41:45.330402

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '352b7ef7db1b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE TYPE card_status AS ENUM ('available', 'reserved', 'sold', 'removed');
        CREATE TYPE card_rarity AS ENUM ('common', 'uncommon', 'rare', 'rare_holo', 'ultra_rare', 'secret');
        CREATE TYPE card_physical_state AS ENUM ('mint', 'near mint', 'excellent', 'played', 'damaged');
        CREATE TYPE pokemon_type AS ENUM ('normal', 'fire', 'water', 'electric', 'grass', 'ice',
            'fighting', 'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost',
            'dragon', 'dark', 'steel', 'fairy');

        CREATE TABLE cards (
            id             UUID PRIMARY KEY,
            name           VARCHAR(32) NOT NULL,
            rarity         card_rarity NOT NULL,
            physical_state card_physical_state NOT NULL,
            type           pokemon_type NOT NULL,
            status         card_status NOT NULL DEFAULT 'available',
            is_holo        BOOLEAN NOT NULL DEFAULT FALSE,
            illustration   TEXT,
            edition_code   VARCHAR(32) NOT NULL,
            edition_name   VARCHAR(32) NOT NULL,
            edition_years  SMALLINT NOT NULL,
            created_at     TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );
    """)


def downgrade() -> None:
    op.execute("""
        DROP TABLE cards;
        DROP TYPE card_status;
        DROP TYPE card_rarity;
        DROP TYPE card_physical_state;
        DROP TYPE pokemon_type;
    """)
