"""empty message

Revision ID: 96cbe9bcf713
Revises: 3106f24e65d5
Create Date: 2024-12-22 14:14:55.508281

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96cbe9bcf713'
down_revision: Union[str, None] = '3106f24e65d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
