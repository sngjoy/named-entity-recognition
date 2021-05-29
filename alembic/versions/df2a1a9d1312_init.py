"""init

Revision ID: df2a1a9d1312

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "df2a1a9d1312"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "entities_count",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("entities", sa.String, nullable=False),
        sa.Column("count", sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table("entities_count")
