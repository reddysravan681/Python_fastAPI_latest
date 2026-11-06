"""add content col to post table

Revision ID: 631f28163212
Revises: 7e8184b6fa70
Create Date: 2026-11-05 21:10:57.973131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '631f28163212'
down_revision: Union[str, Sequence[str], None] = '7e8184b6fa70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.Text(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
