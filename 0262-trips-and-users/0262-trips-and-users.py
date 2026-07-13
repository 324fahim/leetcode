import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # Keep only requested date range
    t = trips[(trips["request_at"] >= "2013-10-01") & (trips["request_at"] <= "2013-10-03")].copy()

    # Attach client banned flag
    t = t.merge(
        users[["users_id", "banned"]].rename(columns={"users_id": "client_id", "banned": "client_banned"}),
        on="client_id",
        how="inner"
    )

    # Attach driver banned flag
    t = t.merge(
        users[["users_id", "banned"]].rename(columns={"users_id": "driver_id", "banned": "driver_banned"}),
        on="driver_id",
        how="inner"
    )

    # Keep trips where both client and driver are unbanned
    t = t[(t["client_banned"] == "No") & (t["driver_banned"] == "No")]

    # Cancelled indicator
    t["is_cancelled"] = t["status"].isin(["cancelled_by_client", "cancelled_by_driver"]).astype(int)

    # Daily cancellation rate
    out = (
        t.groupby("request_at", as_index=False)["is_cancelled"]
         .mean()
         .rename(columns={"request_at": "Day", "is_cancelled": "Cancellation Rate"})
    )
    out["Cancellation Rate"] = out["Cancellation Rate"].round(2)

    return out