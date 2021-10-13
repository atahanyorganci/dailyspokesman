"""Rename fields of Article

Revision ID: 97c2a23f232b
Revises: aeb810095a89
Create Date: 2021-10-12 12:18:02.469591

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "97c2a23f232b"
down_revision = "aeb810095a89"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("article", "link", new_column_name="url", nullable=False)
    op.alter_column("article", "serialno", new_column_name="serial_no", nullable=False)


def downgrade():
    op.alter_column("article", "url", new_column_name="link", nullable=False)
    op.alter_column("article", "serial_no", new_column_name="serialno", nullable=False)
