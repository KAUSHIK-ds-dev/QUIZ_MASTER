"""Initial migration

Revision ID: 320074a10f65
Revises: 
Create Date: 2025-03-29 12:17:56.408989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '320074a10f65'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quiz', schema=None) as batch_op:
        batch_op.add_column(sa.Column('subject_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'subject', ['subject_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quiz', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('subject_id')

    # ### end Alembic commands ###
