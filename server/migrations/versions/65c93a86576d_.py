"""empty message

Revision ID: 65c93a86576d
Revises: 54537059c4f0
Create Date: 2024-09-28 22:38:14.932356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65c93a86576d'
down_revision = '54537059c4f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('inc_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('key', sa.String(), nullable=True))

    with op.batch_alter_table('keywords_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('keywords_table', schema=None) as batch_op:
        batch_op.drop_column('description')

    with op.batch_alter_table('inc_table', schema=None) as batch_op:
        batch_op.drop_column('key')

    # ### end Alembic commands ###