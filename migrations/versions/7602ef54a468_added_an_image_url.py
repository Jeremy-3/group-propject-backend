"""added an image url

Revision ID: 7602ef54a468
Revises: 836e17e68513
Create Date: 2024-10-18 20:42:58.062611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7602ef54a468'
down_revision = '836e17e68513'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rooms', sa.Column('image', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rooms', 'image')
    # ### end Alembic commands ###
