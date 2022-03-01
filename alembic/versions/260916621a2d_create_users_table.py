"""create_users_table

Revision ID: 260916621a2d
Revises: 
Create Date: 2021-08-08 16:54:01.841964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '260916621a2d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('age', sa.Integer, nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime, onupdate=sa.text('NOW()'))

    )


def downgrade():
    op.drop_table('users')
