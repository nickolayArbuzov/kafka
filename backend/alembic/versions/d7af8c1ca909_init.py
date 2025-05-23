"""init

Revision ID: d7af8c1ca909
Revises:
Create Date: 2025-05-23 22:14:01.636621

"""

from typing import Sequence, Union
import uuid

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d7af8c1ca909"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table(
        "inventory",
        sa.Column(
            "warehouse_id",
            sa.UUID(as_uuid=True),
            sa.ForeignKey("warehouse.id"),
            primary_key=True,
        ),
        sa.Column(
            "product_id",
            sa.UUID(as_uuid=True),
            sa.ForeignKey("product.id"),
            primary_key=True,
        ),
        sa.Column("quantity", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )
    op.create_index("ix_inventory_product_id", "inventory", ["product_id"])
    op.create_index("ix_inventory_warehouse_id", "inventory", ["warehouse_id"])

    op.create_table(
        "movement",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
        sa.Column("product_id", sa.UUID(as_uuid=True), sa.ForeignKey("product.id")),
        sa.Column(
            "from_warehouse_id", sa.UUID(as_uuid=True), sa.ForeignKey("warehouse.id")
        ),
        sa.Column(
            "to_warehouse_id", sa.UUID(as_uuid=True), sa.ForeignKey("warehouse.id")
        ),
        sa.Column("departure_time", sa.DateTime(), nullable=True),
        sa.Column("arrival_time", sa.DateTime(), nullable=True),
        sa.Column("departure_quantity", sa.Integer(), nullable=True),
        sa.Column("arrival_quantity", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )
    op.create_index("ix_movement_product_id", "movement", ["product_id"])
    op.create_index("ix_movement_from_warehouse_id", "movement", ["from_warehouse_id"])
    op.create_index("ix_movement_to_warehouse_id", "movement", ["to_warehouse_id"])

    op.create_table(
        "product",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )

    op.create_table(
        "warehouse",
        sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("inventory")
    op.drop_index("ix_inventory_product_id", table_name="inventory")
    op.drop_index("ix_inventory_warehouse_id", table_name="inventory")

    op.drop_table("movement")
    op.drop_index("ix_movement_product_id", table_name="movement")
    op.drop_index("ix_movement_from_warehouse_id", table_name="movement")
    op.drop_index("ix_movement_to_warehouse_id", table_name="movement")

    op.drop_table("product")

    op.drop_table("warehouse")
