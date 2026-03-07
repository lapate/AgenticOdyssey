from fastmcp import FastMCP
import json
import uuid
from pathlib import Path
from typing import Optional

DATA_DIR = Path(__file__).parent

DAILY_FILE = DATA_DIR / "chicken_daily_orders_financials.json"
HOURLY_FILE = DATA_DIR / "chicken_hourly_store_sales.json"

mcp = FastMCP(
    "Chicken Store Data",
    instructions=(
        "MCP server providing CRUD operations on chicken store datasets: "
        "daily orders/financials and hourly store sales."
    ),
)


def _read_json(path: Path) -> list[dict]:
    with open(path, "r") as f:
        return json.load(f)


def _write_json(path: Path, data: list[dict]) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


# ---------------------------------------------------------------------------
# Daily Financials CRUD
# ---------------------------------------------------------------------------

@mcp.tool()
def list_daily_financials(
    date: Optional[str] = None,
    store_id: Optional[str] = None,
) -> list[dict]:
    """List daily order and financial records. Optionally filter by date and/or store_id."""
    records = _read_json(DAILY_FILE)
    if date:
        records = [r for r in records if r["date"] == date]
    if store_id:
        records = [r for r in records if r["store_id"] == store_id]
    return records


@mcp.tool()
def get_daily_financial(record_id: str) -> dict:
    """Get a single daily financial record by its ID."""
    for r in _read_json(DAILY_FILE):
        if r["id"] == record_id:
            return r
    return {"error": f"Record {record_id} not found"}


@mcp.tool()
def create_daily_financial(
    date: str,
    store_id: str,
    chickens_bought: int,
    purchase_cost_usd: float,
    chickens_sold_total: int,
    sales_revenue_usd: float,
    gross_profit_usd: float,
) -> dict:
    """Create a new daily financial record. Returns the created record with its ID."""
    records = _read_json(DAILY_FILE)
    new_record = {
        "date": date,
        "store_id": store_id,
        "chickens_bought": chickens_bought,
        "purchase_cost_usd": purchase_cost_usd,
        "chickens_sold_total": chickens_sold_total,
        "sales_revenue_usd": sales_revenue_usd,
        "gross_profit_usd": gross_profit_usd,
        "id": str(uuid.uuid4()),
    }
    records.append(new_record)
    _write_json(DAILY_FILE, records)
    return new_record


@mcp.tool()
def update_daily_financial(
    record_id: str,
    date: Optional[str] = None,
    store_id: Optional[str] = None,
    chickens_bought: Optional[int] = None,
    purchase_cost_usd: Optional[float] = None,
    chickens_sold_total: Optional[int] = None,
    sales_revenue_usd: Optional[float] = None,
    gross_profit_usd: Optional[float] = None,
) -> dict:
    """Update an existing daily financial record. Only provided fields are changed."""
    records = _read_json(DAILY_FILE)
    for r in records:
        if r["id"] == record_id:
            updates = {
                k: v
                for k, v in {
                    "date": date,
                    "store_id": store_id,
                    "chickens_bought": chickens_bought,
                    "purchase_cost_usd": purchase_cost_usd,
                    "chickens_sold_total": chickens_sold_total,
                    "sales_revenue_usd": sales_revenue_usd,
                    "gross_profit_usd": gross_profit_usd,
                }.items()
                if v is not None
            }
            r.update(updates)
            _write_json(DAILY_FILE, records)
            return r
    return {"error": f"Record {record_id} not found"}


@mcp.tool()
def delete_daily_financial(record_id: str) -> dict:
    """Delete a daily financial record by ID. Returns the deleted record."""
    records = _read_json(DAILY_FILE)
    for i, r in enumerate(records):
        if r["id"] == record_id:
            deleted = records.pop(i)
            _write_json(DAILY_FILE, records)
            return {"deleted": deleted}
    return {"error": f"Record {record_id} not found"}


# ---------------------------------------------------------------------------
# Hourly Sales CRUD
# ---------------------------------------------------------------------------

@mcp.tool()
def list_hourly_sales(
    date: Optional[str] = None,
    store_id: Optional[str] = None,
    hour: Optional[str] = None,
) -> list[dict]:
    """List hourly store sales records. Optionally filter by date, store_id, and/or hour."""
    records = _read_json(HOURLY_FILE)
    if date:
        records = [r for r in records if r["date"] == date]
    if store_id:
        records = [r for r in records if r["store_id"] == store_id]
    if hour:
        records = [r for r in records if r["hour"] == hour]
    return records


@mcp.tool()
def get_hourly_sale(record_id: str) -> dict:
    """Get a single hourly sales record by its ID."""
    for r in _read_json(HOURLY_FILE):
        if r["id"] == record_id:
            return r
    return {"error": f"Record {record_id} not found"}


@mcp.tool()
def create_hourly_sale(
    date: str,
    store_id: str,
    hour: str,
    chickens_cooked: int,
    chickens_sold: int,
) -> dict:
    """Create a new hourly sales record. Returns the created record with its ID."""
    records = _read_json(HOURLY_FILE)
    new_record = {
        "date": date,
        "store_id": store_id,
        "hour": hour,
        "chickens_cooked": chickens_cooked,
        "chickens_sold": chickens_sold,
        "id": str(uuid.uuid4()),
    }
    records.append(new_record)
    _write_json(HOURLY_FILE, records)
    return new_record


@mcp.tool()
def update_hourly_sale(
    record_id: str,
    date: Optional[str] = None,
    store_id: Optional[str] = None,
    hour: Optional[str] = None,
    chickens_cooked: Optional[int] = None,
    chickens_sold: Optional[int] = None,
) -> dict:
    """Update an existing hourly sales record. Only provided fields are changed."""
    records = _read_json(HOURLY_FILE)
    for r in records:
        if r["id"] == record_id:
            updates = {
                k: v
                for k, v in {
                    "date": date,
                    "store_id": store_id,
                    "hour": hour,
                    "chickens_cooked": chickens_cooked,
                    "chickens_sold": chickens_sold,
                }.items()
                if v is not None
            }
            r.update(updates)
            _write_json(HOURLY_FILE, records)
            return r
    return {"error": f"Record {record_id} not found"}


@mcp.tool()
def delete_hourly_sale(record_id: str) -> dict:
    """Delete an hourly sales record by ID. Returns the deleted record."""
    records = _read_json(HOURLY_FILE)
    for i, r in enumerate(records):
        if r["id"] == record_id:
            deleted = records.pop(i)
            _write_json(HOURLY_FILE, records)
            return {"deleted": deleted}
    return {"error": f"Record {record_id} not found"}


if __name__ == "__main__":
    mcp.run(transport="sse")
