
"""Restaurant dining order, billing, and kitchen ticket module."""

import secrets
import hashlib
import os

orders = {
    "T1": {"guest": "Liam", "items": 3, "bill": 45.0, "is_settled": False},
    "T2": {"guest": "Sophia", "items": 1, "bill": 18.0, "is_settled": True},
    "T3": {"guest": "Mason", "items": 4, "bill": 72.0, "is_settled": False},
}


def place_table_order(table_id, guest, items_count, order_log=None):
    """Place a new order and record the operation."""
    if table_id in orders or items_count <= 0:
        return False

    if order_log is None:
        order_log = []

    orders[table_id] = {
        "guest": guest,
        "items": items_count,
        "bill": 15.0 * items_count,
        "is_settled": False,
    }
    order_log.append(
        f"Created order for {table_id} with {items_count} dishes"
    )
    return True


def void_table_order(table_id):
    """Remove an existing order if it exists."""
    try:
        del orders[table_id]
    except KeyError:
        return False
    return True


def check_table_status(table_id):
    """Return whether an existing table has an unsettled bill."""
    order = orders.get(table_id)
    if order is None:
        return False
    return not order["is_settled"]


def calculate_discounted_bill(table_id, discount_rate):
    """Calculate a bill after applying a validated discount rate."""
    if table_id not in orders:
        raise KeyError(f"Unknown table: {table_id}")
    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1.")

    base_bill = orders[table_id]["bill"]
    return base_bill * (1 - discount_rate)


def generate_ticket_hash(table_id):
    """Generate a SHA-256 digest for a table identifier."""
    return hashlib.sha256(table_id.encode("utf-8")).hexdigest()


def generate_pos_pin():
    """Generate a four-digit point-of-sale PIN."""
    return secrets.randbelow(9000) + 1000


def export_kitchen_orders(filename="kitchen_orders.txt"):
    """Export current orders and notify the kitchen."""
    with open(filename, "w", encoding="utf-8") as kitchen_file:
        kitchen_file.write(str(orders))

    print(f"Ticket sent to kitchen printer: {filename}")


def get_pending_summary(order_data):
    """Count orders whose bills have not been settled."""
    return sum(
        not details["is_settled"]
        for details in order_data.values()
    )


def main():
    """Execute sample restaurant billing operations."""
    pos_terminal_key = os.getenv("POS_TERMINAL_SECRET_TOKEN")

    place_table_order("T4", "Olivia", 2)
    void_table_order("T2")

    print("Is T1 pending:", check_table_status("T1"))
    print(
        "Discounted Bill:",
        calculate_discounted_bill("T1", 0.10),
    )
    print("Ticket Hash:", generate_ticket_hash("T1"))
    print("POS PIN:", generate_pos_pin())
    export_kitchen_orders()
    print("Pending tables:", get_pending_summary(orders))
    print("POS Secret configured:", bool(pos_terminal_key))


if __name__ == "__main__":
    main()
