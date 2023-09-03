"""adding-v1-db

Revision ID: 5c40ea8dffe7
Revises: 
Create Date: 2023-09-03 16:35:11.081063

"""
from alembic import op
import sqlalchemy as sa


revision = "5c40ea8dffe7"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "yugioh_cards",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("external_id", sa.String(length=512), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("type", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=2048), nullable=False),
        sa.Column("archetype", sa.String(length=255), nullable=True),
        sa.Column("race", sa.String(length=255), nullable=True),
        sa.Column("scale", sa.Integer(), nullable=True),
        sa.Column("defense", sa.Integer(), nullable=True),
        sa.Column("attack", sa.Integer(), nullable=True),
        sa.Column("attribute", sa.String(length=255), nullable=True),
        sa.Column("level", sa.Integer(), nullable=True),
        sa.Column("link_value", sa.Integer(), nullable=True),
        sa.Column("links", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "yugioh_sets",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("set_id", sa.String(length=255), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("release_date", sa.Date(), nullable=True),
        sa.Column("card_count", sa.Integer(), nullable=False),
        sa.Column("set_image", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "yugioh_card_ban_list_entries",
        sa.Column("card_id", sa.String(length=36), nullable=False),
        sa.Column("format", sa.String(length=255), nullable=False),
        sa.Column("level", sa.String(length=255), nullable=False),
        sa.ForeignKeyConstraint(
            ["card_id"],
            ["yugioh_cards.id"],
        ),
        sa.PrimaryKeyConstraint("card_id", "format"),
    )
    op.create_table(
        "yugioh_card_images",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("card_id", sa.String(length=36), nullable=False),
        sa.Column("regular", sa.String(length=255), nullable=False),
        sa.Column("small", sa.String(length=255), nullable=False),
        sa.Column("cropped", sa.String(length=255), nullable=False),
        sa.ForeignKeyConstraint(
            ["card_id"],
            ["yugioh_cards.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "yugioh_card_prices",
        sa.Column("card_id", sa.String(length=36), nullable=False),
        sa.Column("tcgplayer_price", sa.String(length=255), nullable=True),
        sa.Column("cardmarket_price", sa.String(length=255), nullable=True),
        sa.Column("ebay_price", sa.String(length=255), nullable=True),
        sa.Column("amazon_price", sa.String(length=255), nullable=True),
        sa.Column("coolstuffinc_price", sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(
            ["card_id"],
            ["yugioh_cards.id"],
        ),
        sa.PrimaryKeyConstraint("card_id"),
    )
    op.create_table(
        "yugioh_card_set_associations",
        sa.Column("card_id", sa.String(length=36), nullable=False),
        sa.Column("set_id", sa.String(length=36), nullable=False),
        sa.Column("rarity", sa.String(length=255), nullable=False),
        sa.Column("rarity_code", sa.String(length=255), nullable=False),
        sa.Column("price", sa.String(length=255), nullable=False),
        sa.ForeignKeyConstraint(
            ["card_id"],
            ["yugioh_cards.id"],
        ),
        sa.ForeignKeyConstraint(
            ["set_id"],
            ["yugioh_sets.id"],
        ),
        sa.PrimaryKeyConstraint("card_id", "set_id"),
    )


def downgrade() -> None:
    op.drop_table("yugioh_card_set_associations")
    op.drop_table("yugioh_card_prices")
    op.drop_table("yugioh_card_images")
    op.drop_table("yugioh_card_ban_list_entries")
    op.drop_table("yugioh_sets")
    op.drop_table("yugioh_cards")
