# ------------------------------------------------------------
# Auto generated test file `test_050_TestBancorV2.py`
# ------------------------------------------------------------
# source file   = NBTest_050_TestBancorV2.py
# test id       = 050
# test comment  = TestBancorV2
# ------------------------------------------------------------



"""
This module contains the tests for the exchanges classes
"""
from fastlane_bot import Bot, Config
from fastlane_bot.bot import CarbonBot
from fastlane_bot.tools.cpc import ConstantProductCurve
from fastlane_bot.tools.cpc import ConstantProductCurve as CPC
from fastlane_bot.events.exchanges import UniswapV2, UniswapV3, SushiswapV2, CarbonV1, BancorV3
from fastlane_bot.events.interface import QueryInterface
from fastlane_bot.helpers.poolandtokens import PoolAndTokens
from fastlane_bot.helpers import TradeInstruction, TxReceiptHandler, TxRouteHandler, TxSubmitHandler, TxHelpers, TxHelper
from fastlane_bot.events.managers.manager import Manager
from fastlane_bot.events.interface import QueryInterface
from joblib import Parallel, delayed
from fastlane_bot.tools.cpc import ConstantProductCurve as CPC, CPCContainer, T
from dataclasses import dataclass, asdict, field
import pytest
import math
import json
print("{0.__name__} v{0.__VERSION__} ({0.__DATE__})".format(CPC))
print("{0.__name__} v{0.__VERSION__} ({0.__DATE__})".format(Bot))
print("{0.__name__} v{0.__VERSION__} ({0.__DATE__})".format(UniswapV2))
print("{0.__name__} v{0.__VERSION__} ({0.__DATE__})".format(UniswapV3))
print("{0.__name__} v{0.__VERSION__} ({0.__DATE__})".format(SushiswapV2))
print("{0.__name__} v{0.__VERSION__} ({0.__DATE__})".format(CarbonV1))
print("{0.__name__} v{0.__VERSION__} ({0.__DATE__})".format(BancorV3))
from fastlane_bot.testing import *
from fastlane_bot.modes import triangle_single_bancor3
#plt.style.use('seaborn-dark')
plt.rcParams['figure.figsize'] = [12,6]
from fastlane_bot import __VERSION__
require("3.0", __VERSION__)



C = cfg = Config.new(config=Config.CONFIG_MAINNET)
C.DEFAULT_MIN_PROFIT_BNT = 0.02
C.DEFAULT_MIN_PROFIT = 0.02
cfg.DEFAULT_MIN_PROFIT_BNT = 0.02
cfg.DEFAULT_MIN_PROFIT = 0.02
assert (C.NETWORK == C.NETWORK_MAINNET)
assert (C.PROVIDER == C.PROVIDER_ALCHEMY)
setup_bot = CarbonBot(ConfigObj=C)
pools = None

with open('fastlane_bot/data/tests/latest_pool_data_testing_bancor_v2.json') as f:
    pools = json.load(f)
pools = [pool for pool in pools]
pools[0]
static_pools = pools
state = pools
exchanges = list({ex['exchange_name'] for ex in state})
db = QueryInterface(state=state, ConfigObj=C, exchanges=exchanges)
setup_bot.db = db

static_pool_data_filename = "static_pool_data"

static_pool_data = pd.read_csv(f"fastlane_bot/data/{static_pool_data_filename}.csv", low_memory=False)
    
uniswap_v2_event_mappings = pd.read_csv("fastlane_bot/data/uniswap_v2_event_mappings.csv", low_memory=False)
        
tokens = pd.read_csv("fastlane_bot/data/tokens.csv", low_memory=False)
        
exchanges = "carbon_v1,bancor_v3,uniswap_v3,uniswap_v2,sushiswap_v2"

exchanges = exchanges.split(",")


alchemy_max_block_fetch = 20
static_pool_data["cid"] = [
        cfg.w3.keccak(text=f"{row['descr']}").hex()
        for index, row in static_pool_data.iterrows()
    ]
static_pool_data = [
    row for index, row in static_pool_data.iterrows()
    if row["exchange_name"] in exchanges
]

static_pool_data = pd.DataFrame(static_pool_data)
static_pool_data['exchange_name'].unique()
mgr = Manager(
    web3=cfg.w3,
    cfg=cfg,
    pool_data=static_pool_data.to_dict(orient="records"),
    SUPPORTED_EXCHANGES=exchanges,
    alchemy_max_block_fetch=alchemy_max_block_fetch,
    uniswap_v2_event_mappings=uniswap_v2_event_mappings,
    tokens=tokens.to_dict(orient="records"),
)

start_time = time.time()
Parallel(n_jobs=-1, backend="threading")(
    delayed(mgr.add_pool_to_exchange)(row) for row in mgr.pool_data
)
cfg.logger.info(f"Time taken to add initial pools: {time.time() - start_time}")

mgr.deduplicate_pool_data()
cids = [pool["cid"] for pool in mgr.pool_data]
assert len(cids) == len(set(cids)), "duplicate cid's exist in the pool data"
def init_bot(mgr: Manager) -> CarbonBot:
    """
    Initializes the bot.

    Parameters
    ----------
    mgr : Manager
        The manager object.

    Returns
    -------
    CarbonBot
        The bot object.
    """
    mgr.cfg.logger.info("Initializing the bot...")
    bot = CarbonBot(ConfigObj=mgr.cfg)
    bot.db = db
    bot.db.mgr = mgr
    assert isinstance(
        bot.db, QueryInterface
    ), "QueryInterface not initialized correctly"
    return bot
bot = init_bot(mgr)
bot.db.handle_token_key_cleanup()
bot.db.remove_unmapped_uniswap_v2_pools()
bot.db.remove_zero_liquidity_pools()
bot.db.remove_unsupported_exchanges()
tokens = bot.db.get_tokens()
ADDRDEC = {t.key: (t.address, int(t.decimals)) for t in tokens if not math.isnan(t.decimals)}
flashloan_tokens = bot.setup_flashloan_tokens(None)
CCm = bot.setup_CCm(None)
pools = db.get_pool_data_with_tokens()

arb_mode = "multi"


# ------------------------------------------------------------
# Test      050
# File      test_050_TestBancorV2.py
# Segment   Test_MIN_PROFIT
# ------------------------------------------------------------
def test_test_min_profit():
# ------------------------------------------------------------
    
    assert(cfg.DEFAULT_MIN_PROFIT_BNT <= 0.02), f"[TestMultiMode], DEFAULT_MIN_PROFIT_BNT must be <= 0.02 for this Notebook to run, currently set to {cfg.DEFAULT_MIN_PROFIT_BNT}"
    assert(C.DEFAULT_MIN_PROFIT_BNT <= 0.02), f"[TestMultiMode], DEFAULT_MIN_PROFIT_BNT must be <= 0.02 for this Notebook to run, currently set to {cfg.DEFAULT_MIN_PROFIT_BNT}"
    

# ------------------------------------------------------------
# Test      050
# File      test_050_TestBancorV2.py
# Segment   Test_Combos_and_Tokens
# ------------------------------------------------------------
def test_test_combos_and_tokens():
# ------------------------------------------------------------
    
    arb_finder = bot._get_arb_finder("multi")
    finder2 = arb_finder(
                flashloan_tokens=flashloan_tokens,
                CCm=CCm,
                mode="bothin",
                result=bot.AO_TOKENS,
                ConfigObj=bot.ConfigObj,
            )
    all_tokens, combos = finder2.find_arbitrage()
    assert len(all_tokens) == 971, f"[NBTest_50_TestBancorV2] Using wrong dataset, expected 971 tokens, found {len(all_tokens)}"
    assert len(combos) == 5820, f"[NBTest_50_TestBancorV2] Using wrong dataset, expected 5820 tokens, found {len(combos)}"
    
    

# ------------------------------------------------------------
# Test      050
# File      test_050_TestBancorV2.py
# Segment   Test_Expected_Output_BancorV2
# ------------------------------------------------------------
def test_test_expected_output_bancorv2():
# ------------------------------------------------------------
    
    # +
    run_full = bot._run(flashloan_tokens=flashloan_tokens, CCm=CCm, arb_mode=arb_mode, data_validator=False, result=bot.XS_ARBOPPS)
    arb_finder = bot._get_arb_finder("multi")
    finder = arb_finder(
                flashloan_tokens=flashloan_tokens,
                CCm=CCm,
                mode="bothin",
                result=bot.AO_CANDIDATES,
                ConfigObj=bot.ConfigObj,
            )
    r = finder.find_arbitrage()
    arb_with_bancor_v2 = []
    
    for arb_opp in r:
        pools = []
        for pool in arb_opp[2]:
            pools += [curve for curve in CCm if curve.cid == pool['cid']]
        for pool in pools:
            if pool.params['exchange'] == "bancor_v2":
                arb_with_bancor_v2.append(arb_opp)
    
    # get specific arb for tests
    
    test_arb = None
    
    test_cids = ['0x297f9a0e8d3f57de8c62a8fde0ff09193b934ff0ae906085526f0b97b90e188a', '3743106036130323098097120681749450326076-0', '3743106036130323098097120681749450326076-1']
    
    for arb in arb_with_bancor_v2:
        all_match = True
        for pool in arb[2]:
            if pool['cid'] not in test_cids:
                all_match = False
        
        if all_match:
            test_arb = arb
    
    (
        best_profit,
        best_trade_instructions_df,
        best_trade_instructions_dic,
        best_src_token,
        best_trade_instructions,
    ) = test_arb
    
    # Order the trade instructions
    (
        ordered_trade_instructions_dct,
        tx_in_count,
    ) = bot._simple_ordering_by_src_token(
        best_trade_instructions_dic, best_src_token
    )
    
    # Scale the trade instructions
    ordered_scaled_dcts = bot._basic_scaling(
        ordered_trade_instructions_dct, best_src_token
    )
    
    # Convert the trade instructions
    ordered_trade_instructions_objects = bot._convert_trade_instructions(
        ordered_scaled_dcts
    )
    
    # Create the tx route handler
    tx_route_handler = bot.TxRouteHandlerClass(
        trade_instructions=ordered_trade_instructions_objects
    )
    
    # Aggregate the carbon trades
    agg_trade_instructions = (
        tx_route_handler.aggregate_carbon_trades(ordered_trade_instructions_objects)
        if bot._carbon_in_trade_route(ordered_trade_instructions_objects)
        else ordered_trade_instructions_objects
    )
    
    # Calculate the trade instructions
    calculated_trade_instructions = tx_route_handler.calculate_trade_outputs(
        agg_trade_instructions
    )
    
    # Aggregate multiple Bancor V3 trades into a single trade
    calculated_trade_instructions = tx_route_handler.aggregate_bancor_v3_trades(
        calculated_trade_instructions
    )
    
    # Get the flashloan token
    fl_token = fl_token_with_weth = calculated_trade_instructions[0].tknin_key
    
    # If the flashloan token is WETH, then use ETH
    if fl_token == T.WETH:
        fl_token = T.NATIVE_ETH
    
    best_profit = flashloan_tkn_profit = tx_route_handler.calculate_trade_profit(calculated_trade_instructions)
    
    # Use helper function to calculate profit
    best_profit, flt_per_bnt, profit_usd = bot.calculate_profit(
        CCm, best_profit, fl_token, fl_token_with_weth
    )
    
    # Check if the best profit is greater than the minimum profit
    if best_profit < bot.ConfigObj.DEFAULT_MIN_PROFIT:
        bot.ConfigObj.logger.info(
            f"Opportunity with profit: {num_format(best_profit)} does not meet minimum profit: {self.ConfigObj.DEFAULT_MIN_PROFIT}, discarding."
        )
    
    # Get the flashloan amount and token address
    flashloan_amount = int(calculated_trade_instructions[0].amtin_wei)
    flashloan_token_address = bot.ConfigObj.w3.toChecksumAddress(
        bot.db.get_token(key=fl_token).address
    )
    
    # Encode the trade instructions
    encoded_trade_instructions = tx_route_handler.custom_data_encoder(
        calculated_trade_instructions
    )
    
    # Get the deadline
    deadline = bot._get_deadline(1)
    
    # Get the route struct
    route_struct = [
        asdict(rs)
        for rs in tx_route_handler.get_route_structs(
            encoded_trade_instructions, deadline
        )
    ]
    assert arb_finder.__name__ == "FindArbitrageMultiPairwise", f"[NBTest_50_TestBancorV2] Expected arb_finder class name name = FindArbitrageMultiPairwise, found {arb_finder.__name__}"
    assert len(r) == 31, f"[NBTest_50_TestBancorV2] Expected 31 arb opps, found {len(r)}"
    assert len(arb_with_bancor_v2) == 4, f"[NBTest_50_TestBancorV2] Expected 4 arb opps with Bancor V2 pools, found {len(arb_with_bancor_v2)}"
    assert encoded_trade_instructions[0].amtin * 10 ** 18 == flashloan_amount, f"[NBTest_50_TestBancorV2] First trade in should match flashloan amount"
    assert route_struct[0]['customAddress'] == "0xb1CD6e4153B2a390Cf00A6556b0fC1458C4A5533" or route_struct[1]['customAddress'] == "0xb1CD6e4153B2a390Cf00A6556b0fC1458C4A5533", f"[NBTest_50_TestBancorV2] customAddress for Bancor V2.1 trade must be converter token address, expected: 0xb1CD6e4153B2a390Cf00A6556b0fC1458C4A5533 for one address, found: {route_struct[0]['customAddress']} and {route_struct[1]['customAddress']}"
    # -
    
    