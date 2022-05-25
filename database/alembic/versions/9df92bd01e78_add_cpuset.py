"""Add cpuset

Revision ID: 9df92bd01e78
Revises: 8c237d2acbc4
Create Date: 2022-05-25 16:19:37.930132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9df92bd01e78'
down_revision = '8c237d2acbc4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('trial', sa.Column('cpuset', sa.String, nullable=True))


def downgrade():
    op.drop_column('trial', 'cpuset')
