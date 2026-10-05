"""add foreign key to posts table

Revision ID: b0fd1ea34c03
Revises: 143a05d1c426
Create Date: 2026-10-05 07:56:11.567291

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0fd1ea34c03'
down_revision: Union[str, Sequence[str], None] = '143a05d1c426'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fkey', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_user_fkey', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
