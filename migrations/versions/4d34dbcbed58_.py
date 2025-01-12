"""empty message

Revision ID: 4d34dbcbed58
Revises: 56d102569684
Create Date: 2019-04-19 14:14:02.372843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d34dbcbed58'
down_revision = '56d102569684'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('integration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('settings', sa.Text(), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    with op.batch_alter_table('category') as batch_op:
        batch_op.create_unique_constraint('udx_category', ['text'])
    with op.batch_alter_table('tag') as batch_op:
        batch_op.create_unique_constraint('udx_tag', ['text'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tag', type_='unique')
    op.drop_constraint(None, 'category', type_='unique')
    op.drop_table('integration')
    # ### end Alembic commands ###
