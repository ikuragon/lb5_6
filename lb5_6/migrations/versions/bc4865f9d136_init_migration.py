"""init migration

Revision ID: bc4865f9d136
Revises: e4cfdd936f72
Create Date: 2023-06-08 14:12:52.905600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc4865f9d136'
down_revision = 'e4cfdd936f72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.alter_column('employee_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('position_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('division_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.alter_column('division_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('position_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('employee_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
