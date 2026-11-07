"""adding phone number column"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '4b025fe52553'
down_revision: Union[str, Sequence[str], None] = 'f7bfb2f42477'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass