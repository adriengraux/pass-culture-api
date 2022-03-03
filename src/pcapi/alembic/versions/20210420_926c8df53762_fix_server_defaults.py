"""fix_server_defaults

Revision ID: 926c8df53762
Revises: e8d9aaa3890e
Create Date: 2021-04-15 16:13:18.521261

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "926c8df53762"
down_revision = "e8d9aaa3890e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic ###
    op.alter_column(
        "deposit",
        "dateCreated",
        existing_type=postgresql.TIMESTAMP(),
        server_default=sa.text("now()"),
        existing_nullable=False,
    )
    op.execute("COMMIT")

    op.alter_column(
        "feature", "isActive", existing_type=sa.BOOLEAN(), server_default=sa.text("true"), existing_nullable=False
    )
    op.execute("COMMIT")

    op.alter_column(
        "offer", "bookingEmail", existing_type=sa.VARCHAR(length=120), server_default=None, existing_nullable=True
    )
    op.execute("COMMIT")

    op.alter_column(
        "stock",
        "dateCreated",
        existing_type=postgresql.TIMESTAMP(),
        server_default=sa.text("now()"),
        existing_nullable=False,
    )
    op.execute("COMMIT")

    op.alter_column(
        "user", "firstName", existing_type=sa.VARCHAR(length=128), server_default=None, existing_nullable=True
    )
    op.execute("COMMIT")

    op.alter_column(
        "user", "lastName", existing_type=sa.VARCHAR(length=128), server_default=None, existing_nullable=True
    )
    op.execute("COMMIT")

    op.alter_column(
        "user", "postalCode", existing_type=sa.VARCHAR(length=5), server_default=None, existing_nullable=True
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic ###
    op.alter_column(
        "user",
        "postalCode",
        existing_type=sa.VARCHAR(length=5),
        server_default=sa.text("''::character varying"),
        existing_nullable=True,
    )
    op.alter_column(
        "user",
        "lastName",
        existing_type=sa.VARCHAR(length=128),
        server_default=sa.text("''::character varying"),
        existing_nullable=True,
    )
    op.alter_column(
        "user",
        "firstName",
        existing_type=sa.VARCHAR(length=128),
        server_default=sa.text("''::character varying"),
        existing_nullable=True,
    )
    op.alter_column(
        "stock",
        "dateCreated",
        existing_type=postgresql.TIMESTAMP(),
        server_default=sa.text("'1900-01-01 00:00:00'::timestamp without time zone"),
        existing_nullable=False,
    )
    op.alter_column(
        "offer",
        "bookingEmail",
        existing_type=sa.VARCHAR(length=120),
        server_default=sa.text("NULL::character varying"),
        existing_nullable=True,
    )
    op.alter_column("feature", "isActive", existing_type=sa.BOOLEAN(), server_default=None, existing_nullable=False)
    op.alter_column(
        "deposit",
        "dateCreated",
        existing_type=postgresql.TIMESTAMP(),
        server_default=sa.text("'1900-01-01 00:00:00'::timestamp without time zone"),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
