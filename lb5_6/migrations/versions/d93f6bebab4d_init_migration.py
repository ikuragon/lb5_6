"""init migration

Revision ID: d93f6bebab4d
Revises: bc4865f9d136
Create Date: 2023-06-08 14:13:33.628850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd93f6bebab4d'
down_revision = 'bc4865f9d136'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.alter_column('employee_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('position_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('division_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('date_of_employment',
               existing_type=sa.DATE(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.alter_column('date_of_employment',
               existing_type=sa.DATE(),
               nullable=False)
        batch_op.alter_column('division_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('position_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('employee_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###