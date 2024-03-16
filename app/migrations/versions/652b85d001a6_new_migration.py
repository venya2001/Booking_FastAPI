"""New migration

Revision ID: 652b85d001a6
Revises: bff982b0d8d6
Create Date: 2024-03-17 00:34:21.160265

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '652b85d001a6'
down_revision: Union[str, None] = 'bff982b0d8d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', sa.String(), nullable=False))
    op.drop_column('users', 'hached_password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hached_password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###
