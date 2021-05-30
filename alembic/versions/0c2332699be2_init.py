"""init

Revision ID: 0c2332699be2
Create Date: 2021-05-30 08:07:14.499355

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "0c2332699be2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "entities_count",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("article_id", sa.String, nullable=False),
        sa.Column("entities", sa.String, nullable=False),
        sa.Column("counts", sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table("entities_count")
