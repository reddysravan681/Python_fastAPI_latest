"""create posts table

Revision ID: 7e8184b6fa70
Revises: 
Create Date: 2026-11-05 19:45:38.619743

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e8184b6fa70'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.String(255),nullable=False))


def downgrade() -> None:
    op.drop_table('posts')
    pass
