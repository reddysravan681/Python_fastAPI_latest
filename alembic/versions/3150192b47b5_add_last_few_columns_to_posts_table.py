"""add last few columns to posts table

Revision ID: 3150192b47b5
Revises: 94f979113ad5
Create Date: 2026-11-06 17:07:21.814284

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3150192b47b5'
down_revision: Union[str, Sequence[str], None] = '94f979113ad5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default=sa.text('1')))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP')))
    


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    
