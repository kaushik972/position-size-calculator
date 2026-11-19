"""Position size calculator for traders.

Risk a fixed % of your account on each trade, sized from your stop-loss.

Usage:
    python position_size.py --account 100000 --risk 1 --entry 2500 --stop 2400
    python position_size.py --account 50000 --risk 2 --entry 150.5 --stop 145 --target 165

Prints position size, number of shares, amount at risk and reward:risk.
"""
import argparse


def position_size(account, risk_pct, entry, stop, target=None):
    risk_per_share = abs(entry - stop)
    if risk_per_share == 0:
        raise ValueError("Entry and stop-loss cannot be the same price.")
    risk_amount = account * risk_pct / 100.0
    shares = int(risk_amount // risk_per_share)
    cost = shares * entry
    result = {
        "risk_amount": round(risk_amount, 2),
        "risk_per_share": round(risk_per_share, 2),
        "shares": shares,
        "position_cost": round(cost, 2),
    }
    if target is not None:
        reward_per_share = abs(target - entry)
        result["reward_per_share"] = round(reward_per_share, 2)
        result["reward_risk"] = round(reward_per_share / risk_per_share, 2)
        result["potential_profit"] = round(shares * reward_per_share, 2)
    return result


def main():
    p = argparse.ArgumentParser(description="Position size calculator")
    p.add_argument("--account", type=float, default=100000, help="Account size")
    p.add_argument("--risk", type=float, default=1.0, help="Risk per trade in %")
    p.add_argument("--entry", type=float, required=True)
    p.add_argument("--stop", type=float, required=True, help="Stop-loss price")
    p.add_argument("--target", type=float, default=None, help="Target price")
    a = p.parse_args()
    r = position_size(a.account, a.risk, a.entry, a.stop, a.target)
    print(f"Account: {a.account:,.0f} | Risk: {a.risk}% = {r['risk_amount']:,.2f}")
    print(f"Entry {a.entry} | Stop {a.stop} | Risk/share {r['risk_per_share']}")
    print(f"Buy {r['shares']} shares | Position cost {r['position_cost']:,.2f}")
    if "reward_risk" in r:
        print(f"Target {a.target} | Reward:risk 1:{r['reward_risk']} | "
              f"Potential profit {r['potential_profit']:,.2f}")


if __name__ == "__main__":
    main()
