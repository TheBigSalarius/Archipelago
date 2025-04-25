from .Options import RiftWizardOptions

def create_regions(world, player: int, options: RiftWizardOptions):
    import itertools
    from . import create_region
    from .Locations import location_table

#    world.regions += [
#        create_region(world, player, 'Menu', None, ['Pre-Rift']),
#        create_region(world, player, 'Rift', [location for location in location_table])
    
    world.regions += [
        create_region(world, player, 'Menu', None, ['Pre-Rift']),
    ]

    consumable_location_table = dict(
        itertools.islice(location_table.items(), 76, 76 + (options.consumable_count.value)))

    if options.end_goal.value == 0:
        limited_location_table = dict(itertools.islice(location_table.items(), 76))
        complete_location_table = {**limited_location_table, **consumable_location_table}
        world.regions += [
            create_region(world, player, 'Rift', [location for location in complete_location_table])
        ]

    if options.end_goal.value == 1:
        limited_location_table = dict(itertools.islice(location_table.items(), (options.floor_goal.value-1)*3+1))
        complete_location_table = {**limited_location_table, **consumable_location_table}
        world.regions += [
            create_region(world, player, 'Rift', [location for location in complete_location_table])
        ]

    # link up our region with the entrance we just made
    world.get_entrance('Pre-Rift', player).connect(world.get_region('Rift', player))
