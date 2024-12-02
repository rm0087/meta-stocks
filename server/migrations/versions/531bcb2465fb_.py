"""empty message

Revision ID: 531bcb2465fb
Revises: 59cd7cd65fe9
Create Date: 2024-09-11 17:24:51.506198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '531bcb2465fb'
down_revision = '59cd7cd65fe9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company_keyword_association',
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('keyword_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies_table.id'], name=op.f('fk_company_keyword_association_company_id_companies_table')),
    sa.ForeignKeyConstraint(['keyword_id'], ['keywords_table.id'], name=op.f('fk_company_keyword_association_keyword_id_keywords_table'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company_keyword_association')
    # ### end Alembic commands ###