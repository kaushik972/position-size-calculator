# Position Size Calculator

A small Python CLI for traders: risk a fixed % of your account on each trade,
sized from the distance to your stop-loss.

## What it does
- Amount at risk from account size × risk %
- Number of shares to buy so a stop-loss hit costs exactly that amount
- Position cost, and reward:risk + potential profit when a target is given

## Run it
```bash
python position_size.py --account 100000 --risk 1 --entry 2500 --stop 2400
python position_size.py --account 50000 --risk 2 --entry 150.5 --stop 145 --target 165
```

## Example
Account 100,000, risk 1%, entry 2,500, stop 2,400 → risk 1,000, buy **10 shares**
(position cost 25,000).

Built by Shivam Kaushik as a daily mini project — Python, no dependencies.
