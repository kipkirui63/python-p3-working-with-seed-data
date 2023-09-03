
...


botw = Game(title="Breath of the Wild", platform="Switch", genre="Adventure", price=60)
ffvii = Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30)
mk8 = Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)

session.bulk_save_objects([botw, ffvii, mk8])
session.commit()