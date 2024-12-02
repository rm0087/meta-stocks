"""added comments

Revision ID: 2aa349888150
Revises: 419449ea9e76
Create Date: 2024-09-11 22:25:45.021183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2aa349888150'
down_revision = '419449ea9e76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments_table', schema=None) as batch_op:
        batch_op.drop_column('author')

    # ### end Alembic commands ###
