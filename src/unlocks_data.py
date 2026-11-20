class Unlocks:
    def __init__(self, cct, crt, cst, dbg, dbg2, dict, bone, exp, weird, func, grs, hat, imp, lead, list, loop,
                 gold, mega, ops, wood, poly, pump, sns, sim, spd, sun, rem, time, top, tree, util, var, water):
        self.Cactus = cct
        self.Carrots = crt
        self.Costs = cst
        self.Debug = dbg
        self.Debug_2 = dbg2
        self.Dictionaries = dict
        self.Dinosaurs = bone
        self.Expand = exp
        self.Fertilizer = weird
        self.Functions = func
        self.Grass = grs
        self.Hats = hat
        self.Import = imp
        self.Leaderboard = lead
        self.Lists = list
        self.Loops = loop
        self.Mazes = gold
        self.Megafarm = mega
        self.Operators = ops
        self.Plant = wood
        self.Polyculture = poly
        self.Pumpkins = pump
        self.Senses = sns
        self.Simulation = sim
        self.Speed = spd
        self.Sunflowers = sun
        self.The_Farmers_Remains = rem
        self.Timing = time
        self.Top_Hat = top
        self.Trees = tree
        self.Utilities = util
        self.Variables = var
        self.Watering = water

def GetUnlocksData():
    hay = [{"item": None, "cost": 0}]

    wood = [{"item": hay, "cost": 50}]  # plant upgrade, changed for simplicity

    carrot = [
		{"item": wood, "cost": 50},
		{"item": wood, "cost": 250},
		{"item": wood, "cost": 1250},
		{"item": wood, "cost": 6250},
		{"item": wood, "cost": 31200},
		{"item": wood, "cost": 156000},
		{"item": wood, "cost": 781000},
		{"item": wood, "cost": 3910000},
		{"item": wood, "cost": 19500000},
		{"item": wood, "cost": 97700000}
    ]

    pumpkin = [
		{"item": wood, "cost": 500, "item": carrot, "cost": 200},
		{"item": carrot, "cost": 1000},
		{"item": carrot, "cost": 4000},
		{"item": carrot, "cost": 16000},
		{"item": carrot, "cost": 64000},
		{"item": carrot, "cost": 256000},
		{"item": carrot, "cost": 1020000},
		{"item": carrot, "cost": 4100000},
		{"item": carrot, "cost": 16400000},
		{"item": carrot, "cost": 65500000}
    ]
    
    cactus = [
		{"item": pumpkin, "cost": 5000},
		{"item": pumpkin, "cost": 20000},
		{"item": pumpkin, "cost": 120000},
		{"item": pumpkin, "cost": 720000},
		{"item": pumpkin, "cost": 4320000},
		{"item": pumpkin, "cost": 25900000}
	]
	
    costs = [{"item": pumpkin, "cost": 2500}]
	
    debug = [
		{"item": hay, "cost": 50},
		{"item": wood, "cost": 50}
	]

    weird_substance = [ # fertilizer upgrade, renamed for simplicity
        {"item": wood, "cost": 500},
        {"item": wood, "cost": 1500},
        {"item": wood, "cost": 9000},
        {"item": wood, "cost": 54000}
    ]

    gold = [    # mazes upgrade, renamed for simplicity
        {"item": weird_substance, "cost": 1000},
        {"item": cactus, "cost": 12000},
        {"item": cactus, "cost": 72000},
        {"item": cactus, "cost": 432000},
        {"item": cactus, "cost": 2590000},
        {"item": cactus, "cost": 15600000}
    ]
	
    debug_2 = [{"item": gold, "cost": 500}]

    dictionaries = [{"item": pumpkin, "cost": 2500}]

    bone = [    # dinosaurs upgrade, renamed for simplicity
        {"item": cactus, "cost": 2000},
        {"item": cactus, "cost": 12000},
        {"item": cactus, "cost": 72000},
        {"item": cactus, "cost": 432000},
        {"item": cactus, "cost": 2590000},
        {"item": cactus, "cost": 15600000}
    ]

    expand = [
        {"item": hay, "cost": 30},
        {"item": wood, "cost": 20},
        {"item": wood, "cost": 30, "item": carrot, "cost": 20},
        {"item": wood, "cost": 100, "item": carrot, "cost": 50},
        {"item": pumpkin, "cost": 1000},
        {"item": pumpkin, "cost": 8000},
        {"item": pumpkin, "cost": 64000},
        {"item": pumpkin, "cost": 512000},
        {"item": pumpkin, "cost": 4100000}
    ]

    functions = [{"item": carrot, "cost": 40}]

    grass = [
        {"item": hay, "cost": 100},
        {"item": hay, "cost": 300},
        {"item": wood, "cost": 500},
        {"item": wood, "cost": 2500},
        {"item": wood, "cost": 12500},
        {"item": wood, "cost": 62500},
        {"item": wood, "cost": 312000},
        {"item": wood, "cost": 7810000},
        {"item": wood, "cost": 39100000}
    ]

    hats = [{"item": hay, "cost": 50}]

    imports = [{"item": carrot, "cost": 80}]

    leaderboard = [
        {"item": bone, "cost": 2000000},
        {"item": gold, "cost": 1000000}
    ]

    lists = [{"item": carrot, "cost": 500}]

    loops = [{"item": hay, "cost": 5}]

    megafarm = [
        {"item": gold, "cost": 2000},
        {"item": gold, "cost": 8000},
        {"item": gold, "cost": 32000},
        {"item": gold, "cost": 128000},
        {"item": gold, "cost": 512000}
    ]

    operators = [
        {"item": hay, "cost": 150},
        {"item": wood, "cost": 10}
    ]

    polyculture = [
        {"item": pumpkin, "cost": 3000},
        {"item": bone, "cost": 10000},
        {"item": bone, "cost": 50000},
        {"item": bone, "cost": 250000},
        {"item": bone, "cost": 1250000}
    ]

    senses = [{"item": hay, "cost": 100}]

    simulation = [{"item": gold, "cost": 5000}]

    speed = [
        {"item": hay, "cost": 20},
        {"item": wood, "cost": 20},
        {"item": wood, "cost": 50, "item": carrot, "cost": 50},
        {"item": carrot, "cost": 500},
        {"item": carrot, "cost": 1000}
    ]

    sunflowers = [{"item": carrot, "cost": 500}]

    the_farmers_remains = [{"item": bone, "cost": 100000000}]

    timing = [{"item": pumpkin, "cost": 1000}]

    top_hat = [
        {"item": hay, "cost": 1000000000},
        {"item": wood, "cost": 10000000000},
        {"item": carrot, "cost": 1000000000},
        {"item": cactus, "cost": 1000000000},
        {"item": gold, "cost": 100000000}
    ]

    trees = [
        {"item": wood, "cost": 50, "item": carrot, "cost": 70},
        {"item": hay, "cost": 300},
        {"item": hay, "cost": 1200},
        {"item": hay, "cost": 4800},
        {"item": hay, "cost": 19200},
        {"item": hay, "cost": 76800},
        {"item": hay, "cost": 307000},
        {"item": hay, "cost": 1230000},
        {"item": hay, "cost": 4920000},
        {"item": hay, "cost": 19700000}
    ]

    utilities = [{"item": pumpkin, "cost": 1000}]

    variables = [{"item": carrot, "cost": 35}]

    watering = [
        {"item": wood, "cost": 50},
        {"item": wood, "cost": 200},
        {"item": wood, "cost": 800},
        {"item": wood, "cost": 3200},
        {"item": wood, "cost": 12800},
        {"item": wood, "cost": 51200},
        {"item": wood, "cost": 205000},
        {"item": wood, "cost": 819000},
        {"item": wood, "cost": 3280000}
    ]

    data = Unlocks(
        cactus,
        carrot,
        costs,
        debug,
        debug_2,
        dictionaries,
        bone,
        expand,
        weird_substance,
        functions,
        grass,
        hats,
        imports,
        leaderboard,
        lists,
        loops,
        gold,
        megafarm,
        operators,
        wood,
        polyculture,
        pumpkin,
        senses,
        simulation,
        speed,
        sunflowers,
        the_farmers_remains,
        timing,
        top_hat,
        trees,
        utilities,
        variables,
        watering
    )

    return data