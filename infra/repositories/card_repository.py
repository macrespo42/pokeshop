import os
from typing import Any

import psycopg2
from dotenv import load_dotenv

from domain.entities.card import (
    Card,
    Edition,
    Name,
    PhysicalState,
    PokemonType,
    Rarity,
    Status,
)
from domain.repositories.card_repository import ICardRepository, SearchFilter


class InMemoryCardRepository(ICardRepository):
    def __init__(self) -> None:
        self._cards: dict[str, Card] = {}

    def save(self, card: Card) -> None:
        self._cards[card.id] = card

    def get_by_id(self, card_id: str) -> Card | None:
        return self._cards.get(card_id)

    def search(self, search_filter: SearchFilter) -> list[Card]:
        filters = [
            (search_filter.name, lambda c: c.name.value),
            (search_filter.rarity, lambda c: c.rarity.value),
            (search_filter.edition_code, lambda c: c.edition.code),
            (search_filter.edition_name, lambda c: c.edition.name),
            (search_filter.edition_years, lambda c: c.edition.years),
            (search_filter.physical_state, lambda c: c.physical_state.value),
            (search_filter.type, lambda c: c.type.value),
            (search_filter.status, lambda c: c.status.value),
        ]

        active = [(value, getter) for value, getter in filters if value is not None]

        return [
            c
            for c in self._cards.values()
            if all(getter(c) == value for value, getter in active)
        ]


class PostgresCardRepository(ICardRepository):
    def _row_to_card(self, row: tuple[Any, ...] | None) -> Card | None:
        if row is None:
            return None
        (
            id_,
            name,
            rarity,
            physical_state,
            type_,
            status,
            is_holo,
            illustration,
            edition_code,
            edition_name,
            edition_years,
            created_at,
        ) = row
        return Card(
            id=str(id_),
            name=Name(name),
            rarity=Rarity(rarity),
            physical_state=PhysicalState(physical_state),
            type=PokemonType(type_),
            status=Status(status),
            is_holo=is_holo,
            illustration=illustration,
            edition=Edition(code=edition_code, name=edition_name, years=edition_years),
            created_at=created_at,
        )

    def __init__(self) -> None:
        load_dotenv()

        POSTGRES_USER: str = os.getenv("POSTGRES_USER") or ""
        POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD") or ""
        POSTGRES_DB: str = os.getenv("POSTGRES_DB") or ""
        DB_HOST: str = os.getenv("DB_HOST") or ""
        DB_PORT: str = os.getenv("DB_PORT") or ""

        self.conn = psycopg2.connect(
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )

    def get_by_id(self, card_id: str) -> Card | None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM cards WHERE id= %s", card_id)
        result = cursor.fetchone()
        return self._row_to_card(result)

    def search(self, search_filter: SearchFilter) -> list[Card]:
        conditions = [
            ("name", search_filter.name),
            ("rarity", search_filter.rarity),
            ("edition_code", search_filter.edition_code),
            ("edition_name", search_filter.edition_name),
            ("edition_years", search_filter.edition_years),
            ("physical_state", search_filter.physical_state),
            ("type", search_filter.type),
            ("status", search_filter.status),
        ]
        active = [(col, val) for col, val in conditions if val is not None]

        query = "SELECT * FROM cards"
        params: list[Any] = []
        if active:
            where = " AND ".join(f"{col} = %s" for col, _ in active)
            query += f" WHERE {where}"
            params = [val for _, val in active]

        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return [
            card
            for row in cursor.fetchall()
            if (card := self._row_to_card(row)) is not None
        ]
