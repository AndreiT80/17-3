"""empty message

Revision ID: c4bd9d5b5659
Revises: 96cbe9bcf713
Create Date: 2024-12-22 17:12:58.438424

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4bd9d5b5659'
down_revision: Union[str, None] = '96cbe9bcf713'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
