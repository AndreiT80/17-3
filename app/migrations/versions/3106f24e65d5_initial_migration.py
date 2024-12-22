"""initial migration

Revision ID: 3106f24e65d5
Revises: 2995b325bdb9
Create Date: 2024-12-22 14:06:56.567033

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3106f24e65d5'
down_revision: Union[str, None] = '2995b325bdb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
