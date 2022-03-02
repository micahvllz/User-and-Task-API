"""create admins table

Revision ID: 22fbe1c5830b
Revises: 15a9807d491d
Create Date: 2022-03-02 14:27:46.366956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22fbe1c5830b'
down_revision = '15a9807d491d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'admins',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime, onupdate=sa.text('NOW()'))
    )


def downgrade():
    op.drop_table('admins')
