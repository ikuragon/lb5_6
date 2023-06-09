"""init migration

Revision ID: b17864c44e6f
Revises: a41233ab8673
Create Date: 2023-06-07 16:39:23.880058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b17864c44e6f'
down_revision = 'a41233ab8673'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('divisions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('job_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'job', ['job_id'], ['id'])

    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('job_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'job', ['job_id'], ['id'])

    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.drop_constraint('job_position_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('job_division_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('job_employee_id_fkey', type_='foreignkey')
        batch_op.drop_column('division_id')
        batch_op.drop_column('employee_id')
        batch_op.drop_column('position_id')

    with op.batch_alter_table('positions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('job_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'job', ['job_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('positions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('job_id')

    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.add_column(sa.Column('position_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('employee_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('division_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('job_employee_id_fkey', 'employees', ['employee_id'], ['id'])
        batch_op.create_foreign_key('job_division_id_fkey', 'divisions', ['division_id'], ['id'])
        batch_op.create_foreign_key('job_position_id_fkey', 'positions', ['position_id'], ['id'])

    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('job_id')

    with op.batch_alter_table('divisions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('job_id')

    # ### end Alembic commands ###
