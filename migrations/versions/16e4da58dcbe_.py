"""empty message

Revision ID: 16e4da58dcbe
Revises: 8500f5ec6c45
Create Date: 2017-07-16 17:28:45.870431

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '16e4da58dcbe'
down_revision = '8500f5ec6c45'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_permissions', 'verified_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_permissions', sa.Column('verified_user', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
