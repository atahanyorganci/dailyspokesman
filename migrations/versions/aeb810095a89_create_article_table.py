"""Create Article table

Revision ID: aeb810095a89
Create Date: 2021-06-20 23:15:14.529048

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "aeb810095a89"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "article",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("serialno", sa.Integer(), nullable=False),
        sa.Column("category", sa.Text(), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("subtitle", sa.Text(), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=True),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("link", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("serialno"),
    )


def downgrade():
    op.drop_table("article")
