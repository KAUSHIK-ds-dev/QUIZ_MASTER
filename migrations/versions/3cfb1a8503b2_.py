"""

Revision ID: 3cfb1a8503b2
Revises: 320074a10f65
Create Date: 2025-03-29 12:32:03.668688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cfb1a8503b2'
down_revision = '320074a10f65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quiz', schema=None) as batch_op:
        batch_op.alter_column('subject_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.create_foreign_key('fk_quiz_subject', 'subject', ['subject_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quiz', schema=None) as batch_op:
        batch_op.drop_constraint('fk_quiz_subject', type_='foreignkey')
        batch_op.alter_column('subject_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
