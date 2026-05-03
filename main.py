from fastapi import FastAPI
from pydantic import BaseModel
import random

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

moves = {
    # NPC Basic Attack
    "basic_attack": {
        "name": "Basic Attack",
        "type": "basic_attack",
        "cost": 0,
        "power": 5,
        "accuracy": 90,
        "critical": 20,
    },
    # Physical Attacks
    "lunge": {
        "name": "Lunge",
        "type": "physical",
        "cost": 5,
        "power": 60,
        "accuracy": 90,
        "critical": 20,
        "debuffs": "none",
        "description": "Light Physical damage to 1 foe."
    },
    "slash": {
        "name": "Slash",
        "type": "physical",
        "cost": 9,
        "power": 90,
        "accuracy": 90,
        "critical": 20,
        "times": 1,
        "debuffs": "none",
        "description": "Medium Physical damage to 1 foe."
    },
    "bite": {
        "name": "Bite",
        "type": "physical",
        "cost": 12,
        "power": 40,
        "accuracy": 70,
        "critical": 50,
        "debuffs": "none",
        "description": "Medium Physical damage to 1 foe. High critical rate."
    },
    "cavity": {
        "name": "Cavity",
        "type": "physical",
        "cost": 8,
        "power": 60,
        "accuracy": 90,
        "critical": 5,
        "debuffs": "defense",
        "description": "Light Physical damage and decrease Defense to 1 foe."
    },
    "pounce": {
        "name": "Pounce",
        "type": "physical",
        "cost": 17,
        "power": 120,
        "accuracy": 90,
        "critical": 20,
        "debuffs": "none",
        "description": "Heavy Physical damage to 1 foe."
    },
    "claw_swipe": {
        "name": "Claw Swipe",
        "type": "physical",
        "cost": 15,
        "power": 90,
        "accuracy": 90,
        "critical": 5,
        "debuffs": "agility",
        "description": "Medium Physical damage and decrease Agility to 1 foe."
    },
    "rusty_swipe": {
        "name": "Rusty Swipe",
        "type": "physical",
        "cost": 15,
        "power": 90,
        "accuracy": 90,
        "critical": 5,
        "debuffs": "attack",
        "description": "Medium Physical damage and decrease Attack to 1 foe."
    },
    "dirty_kick": {
        "name": "Dirty Kick",
        "type": "physical",
        "cost": 20,
        "power": 120,
        "accuracy": 90,
        "critical": 3,
        "debuffs": "defense",
        "description": "Heavy Physical damage and decrease Defense to 1 foe."
    },
    # Magic Attacks
    "shadow_lord": {
        "name": "Shadow Lord",
        "type": "magic_attack",
        "element": "dark",
        "cost": 12,
        "power": 190,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Heavy Dark damage to 1 foe."
    },
    "shadow": {
        "name": "Shadow",
        "type": "magic_attack",
        "element": "dark",
        "cost": 8,
        "power": 100,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Medium Dark damage to 1 foe."
    },
    "radiance": {
        "name": "Radiance",
        "type": "magic_attack",
        "element": "light",
        "cost": 12,
        "power": 190,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Heavy Light damage to 1 foe."
    },
    "flicker": {
        "name": "Flicker",
        "type": "magic_attack",
        "element": "light",
        "cost": 8,
        "power": 100,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Medium Light damage to 1 foe."
    },
    "fire_breath": {
        "name": "Fire Breath",
        "type": "magic_attack",
        "element": "fire",
        "cost": 12,
        "power": 190,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Heavy Fire damage to 1 foe."
    },
    "fire_bolt": {
        "name": "Fire Bolt",
        "type": "magic_attack",
        "element": "fire",
        "cost": 8,
        "power": 100,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Medium Fire damage to 1 foe."
    },
    "fire_spark": {
        "name": "Fire Spark",
        "type": "magic_attack",
        "element": "fire",
        "cost": 4,
        "power": 40,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Light Fire damage to 1 foe."
    },
    "thunderstorm": {
        "name": "Thunderstorm",
        "type": "magic_attack",
        "element": "electric",
        "cost": 12,
        "power": 190,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Heavy Electric damage to 1 foe."
    },
    "lightning_bolt": {
        "name": "Lightning Bolt",
        "type": "magic_attack",
        "element": "electric",
        "cost": 8,
        "power": 100,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Medium Electric damage to 1 foe."
    },
    "lightning_spark": {
        "name": "Lightning Spark",
        "type": "magic_attack",
        "element": "electric",
        "cost": 4,
        "power": 40,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Light Electric damage to 1 foe."
    },
    "ice_age": {
        "name": "Ice Age",
        "type": "magic_attack",
        "element": "ice",
        "cost": 12,
        "power": 190,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Heavy Ice damage to 1 foe."
    },
    "icicle": {
        "name": "Icicle",
        "type": "magic_attack",
        "element": "ice",
        "cost": 8,
        "power": 100,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Medium Ice damage to 1 foe."
    },
    "ice_cube": {
        "name": "Ice Cube",
        "type": "magic_attack",
        "element": "ice",
        "cost": 4,
        "power": 40,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Light Ice damage to 1 foe."
    },
    "hurricane": {
        "name": "Hurricane",
        "type": "magic_attack",
        "element": "wind",
        "cost": 12,
        "power": 190,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Heavy Wind damage to 1 foe."
    },
    "gale": {
        "name": "Gale",
        "type": "magic_attack",
        "element": "wind",
        "cost": 8,
        "power": 100,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Medium Wind damage to 1 foe."
    },
    "breeze": {
        "name": "Breeze",
        "type": "magic_attack",
        "element": "wind",
        "cost": 4,
        "power": 40,
        "accuracy": 99,
        "debuffs": "none",
        "description": "Light Wind damage to 1 foe."
    },
    # Buffs and Debuffs
    "arms_up": {
        "name": "Arms Up",
        "type": "buff",
        "stat": "attack",
        "cost": 8,
        "description": "Increase user's Attack power. Can stack."
    },
    "guard_up": {
        "name": "Guard Up",
        "type": "buff",
        "stat": "defense",
        "cost": 8,
        "description": "Increase user's Defense. Can stack."
    },
    "focus_up": {
        "name": "Focus Up",
        "type": "buff",
        "stat": "speed",
        "cost": 8,
        "description": "Increase user's Speed. Can stack."
    },
    "arms_down": {
        "name": "Arms Down",
        "type": "debuff",
        "stat": "attack",
        "cost": 8,
        "description": "Decrease 1 foe's Attack power. Can stack."
    },
    "guard_down": {
        "name": "Guard Down",
        "type": "debuff",
        "stat": "defense",
        "cost": 8,
        "description": "Decrease 1 foe's Defense. Can stack."
    },
    "focus_down": {
        "name": "Focus Down",
        "type": "debuff",
        "stat": "speed",
        "cost": 8,
        "description": "Decrease 1 foe's Speed. Can stack."
    },
    # Healing spells
    "prayer": {
        "name": "Prayer",
        "type": "heal",
        "cost": 3,
        "amount": 50,
        "description": "Slightly restore 1 ally's HP."
    },
    "second_wind": {
        "name": "Second Wind",
        "type": "heal",
        "cost": 6,
        "amount": 160,
        "description": "Moderately restore 1 ally's HP."
    },
    "holy_tear": {
        "name": "Holy Tear",
        "type": "heal",
        "cost": 18,
        "amount": 1000,
        "description": "Fully restores 1 ally's HP."
    },
    # Absorb spells
    "life_drain": {
        "name": "Life Drain",
        "type": "absorb",
        "cost": 3,
        "amount": 30,
        "resource": "hp",
        "description": "Drains 30 HP from 1 foe."
    },
    "spirit_drain": {
        "name": "Spirit Drain",
        "type": "absorb",
        "cost": 3,
        "amount": 10,
        "resource": "sp",
        "description": "Drains 10 SP from 1 foe."
    },
    # Cancel spells
    "neigh": {
        "name": "Neigh!",
        "type": "cancel",
        "cost": 10,
        "target": "all",
        "description": "Negate all user's and foe's buffs and debuffs."
    },
    "excel": {
        "name": "Excel!",
        "type": "cancel",
        "cost": 10,
        "target": "debuff",
        "description": "Negate all user's debuffs."
    },
    "exorcise": {
        "name": "Exorcise!",
        "type": "cancel",
        "cost": 10,
        "target": "buff",
        "description": "Negate all foe's buffs."
    },
}

foes = {
    # RUN 1
    "bowling_pin": {
        "name": "Bowling Pin Devil",
        "stats": {"health": 100, "spirit_points": 40, "strength": 2, "magic": 5, "endurance": 4, "agility": 1,
                  "luck": 2},
        "resistances": {"physical": "none", "fire": "weak", "ice": "null", "electric": "none", "wind": "weak",
                        "light": "none", "dark": "none"},
        "moves": ["ice_cube", "lunge", "guard_down"],
        "gold": 240,
        "xp_reward": 40,
        "level": 2
    },
    "candle": {
        "name": "Candle Devil",
        "stats": {"health": 86, "spirit_points": 14, "strength": 3, "magic": 5, "endurance": 8, "agility": 3,
                  "luck": 3},
        "resistances": {"physical": "none", "fire": "null", "ice": "weak", "electric": "resist", "wind": "none",
                        "light": "resist", "dark": "weak"},
        "moves": ["lunge", "prayer"],
        "gold": 175,
        "xp_reward": 25,
        "level": 2
    },
    "plunger": {
        "name": "Plunger Devil",
        "stats": {"health": 100, "spirit_points": 54, "strength": 4, "magic": 5, "endurance": 9, "agility": 4,
                  "luck": 5},
        "resistances": {"physical": "resist", "fire": "none", "ice": "none", "electric": "resist", "wind": "weak",
                        "light": "none", "dark": "none"},
        "moves": ["slash", "guard_up"],
        "gold": 280,
        "xp_reward": 60,
        "level": 3
    },
    "sponge": {
        "name": "Sponge Devil",
        "stats": {"health": 150, "spirit_points": 48, "strength": 4, "magic": 7, "endurance": 12, "agility": 7,
                  "luck": 5},
        "resistances": {"physical": "none", "fire": "weak", "ice": "null", "electric": "resist", "wind": "none",
                        "light": "none", "dark": "none"},
        "moves": ["gale", "lightning_bolt", "slash", "spirit_drain", "arms_down"],
        "gold": 280,
        "xp_reward": 65,
        "level": 6
    },
    "tombstone": {
        "name": "Tombstone Devil",
        "stats": {"health": 200, "spirit_points": 51, "strength": 10, "magic": 8, "endurance": 10, "agility": 2,
                  "luck": 4},
        "resistances": {"physical": "resist", "fire": "none", "ice": "none", "electric": "weak", "wind": "weak",
                        "light": "none", "dark": "resist"},
        "moves": ["guard_down", "shadow_lord", "bite", "arms_up", "excel"],
        "gold": 325,
        "xp_reward": 75,
        "level": 10
    },
}

runs = {
    "run_1": ["bowling_pin", "candle", "plunger", "sponge", "tombstone"]
}


class BattleInfo(BaseModel):
    foe_id: str
    foe_hp: int
    foe_max_hp: int
    foe_buffs: dict
    foe_extra_turn: bool

    hero_hp: int
    hero_resistances: dict

    turn: int


def get_bowling_pin_move(battle):
    if battle.foe_extra_turn:
        return "guard_down"

    return random.choice(["ice_cube", "lunge", "basic_attack"])


def get_candle_move(battle):
    if battle.foe_extra_turn:
        return "basic_attack"
    if battle.turn % 5 == 0 and battle.foe_hp < battle.foe_max_hp / 2:
        return "prayer"

    return random.choice(["lunge", "basic_attack"])


def get_plunger_move(battle):
    if battle.turn % 4 == 0:
        return "slash"

    return random.choice(["guard_up", "basic_attack"])


def get_sponge_move(battle):
    if battle.foe_extra_turn:
        return "arms_down"

    if battle.turn % 3 == 0:
        return "spirit_drain"

    return random.choice(["gale", "lightning_bolt", "slash"])


def get_tombstone_move(battle):
    if battle.foe_extra_turn:
        return "guard_down"

    for buff in battle.foe_buffs.values():
        if buff < 0:
            return "excel"

    if battle.foe_buffs["attack"] < 3:
        return random.choice(["bite", "shadow_lord", "arms_up"])

    return random.choice(["bite", "shadow_lord"])

foe_logic = {
    "bowling_pin": get_bowling_pin_move,
    "candle": get_candle_move,
    "plunger": get_plunger_move,
    "sponge": get_sponge_move,
    "tombstone": get_tombstone_move,
}


@app.get("/run/config/{run_id}")
def get_run_config(run_id: str):
    if run_id not in runs:
        return {"error": "Run not found"}

    run = runs[run_id]
    run_foes = [{"id": foe_id, **foes[foe_id]} for foe_id in run]
    return {"run_id": run_id, "foes": run_foes}


@app.post("/battle/foe-move")
def get_foe_move(battle: BattleInfo):
    if battle.foe_id in foe_logic:
        chosen_move = foe_logic[battle.foe_id](battle)
    else:
        foe_moves = foes[battle.foe_id]["moves"]
        chosen_move = random.choice(foe_moves)

    return {"move_id": chosen_move}


@app.get("/moves")
def get_moves():
    return {"moves": moves}
