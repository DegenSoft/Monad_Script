# Monad Testnet Automation

This tool automates interactions with the Monad testnet, including various DeFi operations and token interactions.

## Features
- 🌊 Connect Discord account
- 💱 Perform token swaps
- 🏦 Stake MON on Apriori
- 🌋 Stake MON on Magma
- 🦉 Deploy contract on Owlto
- 💎 Interact with Bima (lending & faucet)

## Features Description

### Faucet
Gets tokens from Monad faucet

### Connect Discord
Connects your Discord account to Monad testnet for additional rewards.

### Swaps
Performs random swaps between available tokens with configurable amounts.

### Apriori Staking
Stakes MON tokens on Apriori platform with configurable amounts.

### Magma Staking
Stakes MON tokens on Magma platform with configurable amounts.

### Owlto Contract Deployment
Deploys smart contracts on Owlto platform.

### Bima Operations
- Claims tokens from Bima faucet
- Performs lending operations with configurable percentage of balance

## Requirements
- Python 3.11 or higher

## Installation

1. Install dependencies
```bash
pip install -r requirements.txt
```

2. Configure the bot in `config.yaml`

```yaml
SETTINGS:
# number of concurrent threads
THREADS: 1
# number of retries for ANY action
ATTEMPTS: 5
# pause between attempts
PAUSE_BETWEEN_ATTEMPTS: [5, 15]
# pause in seconds between accounts
RANDOM_PAUSE_BETWEEN_ACCOUNTS: [3, 10]
# pause in seconds between actions
RANDOM_PAUSE_BETWEEN_ACTIONS: [2, 5]
FLOW:
# Available tasks:
# "connect_discord" - connect discord account
# "swaps" - swaps tokens
# "apriori" - stake MON token
# "magma" - stake MON token on Magma
# "owlto" - deploy contract on Owlto
# "bima" - lending and faucet
TASKS: ["connect_discord", "swaps", "apriori", "magma", "owlto", "bima"]
# number of swaps
NUMBER_OF_SWAPS: [1, 3]
# percent of balance to swap
PERCENT_OF_BALANCE_TO_SWAP: [10, 15]

```

3. Add your data to the following files:
- `data/private_keys.txt` - One private key per line
- `data/proxies.txt` - One proxy per line (format: `user:pass@ip:port`)
- `data/discord_tokens.txt` - One Discord token per line


4. Run the bot
```bash
python main.py
```