"""JSONB_everywhere
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "70946e8b0622"
down_revision = "28a13156d2d8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("email", sa.Column("contentNew", sa.dialects.postgresql.JSONB(), nullable=True))
    op.add_column("offer", sa.Column("jsonData", sa.dialects.postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    op.add_column(
        "offer_validation_config",
        sa.Column("specsNew", sa.dialects.postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    )
    op.add_column("product", sa.Column("jsonData", sa.dialects.postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("product", "jsonData")
    op.drop_column("offer_validation_config", "specsNew")
    op.drop_column("offer", "jsonData")
    op.drop_column("email", "contentNew")
    # ### end Alembic commands ###
