"""add foreign key to posts table

Revision ID: 94f979113ad5
Revises: 8eb59d279b9f
Create Date: 2026-11-06 16:56:12.689621

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94f979113ad5'
down_revision: Union[str, Sequence[str], None] = '8eb59d279b9f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('posts_users_fk',source_table='posts',referent_table='users',local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE',onupdate='CASCADE')

    pass


def downgrade() -> None:
    op.drop_column('posts','owner_id')
    op.drop_constraint('posts_users_fk',table_name='posts')
    pass
