"""add content column to posts table

Revision ID: b24c3b6bfa3e
Revises: bc0e897db37b
Create Date: 2026-10-05 07:42:39.241572

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b24c3b6bfa3e'
down_revision: Union[str, Sequence[str], None] = 'bc0e897db37b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
