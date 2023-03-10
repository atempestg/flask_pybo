"""empty message

Revision ID: bbc8a871f1c2
Revises: 10c43921a94e
Create Date: 2023-01-25 22:15:11.686763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbc8a871f1c2'
down_revision = '10c43921a94e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_constraint('fk_answer_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), server_default=sa.text("'1'"), nullable=True))
        batch_op.create_foreign_key('fk_answer_user_id_user', 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###
