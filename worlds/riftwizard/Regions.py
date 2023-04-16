def create_regions(world, player: int):
    import itertools
    from . import create_region
    from .Locations import location_table


#    world.regions += [
#        create_region(world, player, 'Menu', None, ['Pre-Rift']),
#        create_region(world, player, 'Rift', [location for location in location_table])
#    ]

    world.regions += [
        create_region(world, player, 'Menu', None, ['Pre-Rift']),
    ]

    if world.goal[player] == 0:
        world.regions += [
            create_region(world, player, 'Rift', [location for location in location_table])
        ]

    if world.goal[player] == 1:
        limited_location_table = dict(itertools.islice(location_table.items(), (world.floor_goal[player]-1)*3+1))
        world.regions += [
            create_region(world, player, 'Rift', [location for location in limited_location_table])
        ]

    # link up our region with the entrance we just made
    world.get_entrance('Pre-Rift', player).connect(world.get_region('Rift', player))
