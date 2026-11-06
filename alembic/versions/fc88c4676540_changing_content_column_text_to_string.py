"""changing content column text to string

Revision ID: fc88c4676540
Revises: a95a049e46f1
Create Date: 2026-11-06 18:10:44.721920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc88c4676540'
down_revision: Union[str, Sequence[str], None] = 'a95a049e46f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('posts', 'content',
                   existing_type=sa.String(length=255),
                   existing_nullable=False)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
