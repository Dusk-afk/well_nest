"""Add date_of_birth to User model

Revision ID: f2388107862c
Revises: 58911f23e967
Create Date: 2025-04-18 04:22:34.518112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2388107862c'
down_revision = '58911f23e967'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('refresh_tokens')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_of_birth', sa.Date(), nullable=True))
        batch_op.alter_column('full_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('phone_number',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('phone_number',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
        batch_op.alter_column('full_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.drop_column('date_of_birth')

    op.create_table('refresh_tokens',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('token', sa.VARCHAR(length=500), nullable=False),
    sa.Column('expires_at', sa.DATETIME(), nullable=False),
    sa.Column('revoked', sa.BOOLEAN(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###
