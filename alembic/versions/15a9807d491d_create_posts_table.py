"""create posts table

Revision ID: 15a9807d491d
Revises: 260916621a2d
Create Date: 2021-08-12 14:13:12.629151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15a9807d491d'
down_revision = '260916621a2d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('author_id', sa.String(36), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('body', sa.String(1000), nullable=False),
        sa.Column('created_at', sa.DateTime, default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime, onupdate=sa.text('NOW()'))
    )


def downgrade():
    op.drop_table('posts')
