"""Create phone number for User Column

Revision ID: 2045bc1c6a54
Revises: 
Create Date: 2026-04-13 07:23:57.088781

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2045bc1c6a54'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Add Column phone_number to users table"""
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True))


def downgrade() -> None:
    """Delete Column phone_number from users table"""
    op.drop_column("users", "phone_number")
