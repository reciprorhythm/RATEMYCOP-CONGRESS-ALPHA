"""cops table

Revision ID: 1b4da7564ba5
Revises: 
Create Date: 2022-10-16 14:50:16.079866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b4da7564ba5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cops',
    sa.Column('copID', sa.String(length=100), nullable=False),
    sa.Column('lastN', sa.String(length=100), nullable=False),
    sa.Column('firstN', sa.String(length=100), nullable=True),
    sa.Column('rank', sa.String(length=100), nullable=True),
    sa.Column('dept', sa.String(length=100), nullable=False),
    sa.Column('sal', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('copID')
    )
    op.create_table('reports',
    sa.Column('postID', sa.Integer(), nullable=False),
    sa.Column('postTime', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('datetime', sa.String(length=150), nullable=False),
    sa.Column('location', sa.String(length=150), nullable=False),
    sa.Column('eviUp', sa.String(length=200), nullable=True),
    sa.Column('descrip', sa.String(length=1500), nullable=False),
    sa.Column('cw', sa.String(length=150), nullable=True),
    sa.Column('escDesc', sa.String(), nullable=True),
    sa.Column('copTag', sa.String(), nullable=True),
    sa.Column('depTag', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('postID')
    )
    op.create_index(op.f('ix_reports_postTime'), 'reports', ['postTime'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reports_postTime'), table_name='reports')
    op.drop_table('reports')
    op.drop_table('cops')
    # ### end Alembic commands ###
