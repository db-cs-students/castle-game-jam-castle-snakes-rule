"""
Title: 
Creators: Andrew McCrary and Parker Galloway
Description: partial dinosaur game and mario but you kill a snake to avenge your emus
"""
double_jump = True
info.set_score(0)
info.set_life(2)

def main_game():
    scene.set_background_image(img("""
        c e e c e e c . . . . . . . . .
        e c c e c c e . . . . . . . . .
        e c c e c c e . . . . . . . . .
        c e e c e e c . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """))

    #Main character
    mySprite_facing_right = (img("""
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        .........eeeeeee................
        .......eeeeeeeeeee......eee.....
        ......eeeeeeeeeeeee.....e1e.....
        .....eeeeeeeeeeeeeee...eeeee....
        .....eeeeeeeeeeeeeeee..eeee.....
        .....eeeeeeeeeeeeeeeeeeeee......
        .....eeeeeeeeeeeeeeeeeeee.......
        ......eeeeeeeeeeeeeeeeee........
        ......eeeeeeeeeeeeeeeee.........
        .......eeeeeeeeeeeeee...........
        ..........e......e..............
        ..........e......e..............
        ..........e......e..............
        ..........e......e..............
        ..........e......e..............
        ..........e......e..............
        ..........ee.....ee.............
        ...........eee....eee...........
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
    """))
    mySprite = sprites.create(mySprite_facing_right)
    mySprite_facing_left = img("""
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................eeeeeee.........
        .....eee......eeeeeeeeeee.......
        .....e1e.....eeeeeeeeeeeee......
        ....eeeee...eeeeeeeeeeeeeee.....
        .....eeee..eeeeeeeeeeeeeeee.....
        ......eeeeeeeeeeeeeeeeeeeee.....
        .......eeeeeeeeeeeeeeeeeeee.....
        ........eeeeeeeeeeeeeeeeee......
        .........eeeeeeeeeeeeeeeee......
        ...........eeeeeeeeeeeeee.......
        ..............e......e..........
        ..............e......e..........
        ..............e......e..........
        ..............e......e..........
        ..............e......e..........
        ..............e......e..........
        .............ee.....ee..........
        ...........eee....eee...........
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
    """)

    def on_update():
        if controller.dx() > 0:
            mySprite.set_image(mySprite_facing_right)
        elif controller.dx() < 0:
            mySprite.set_image(mySprite_facing_left)
    game.on_update(on_update)
    #Tile Map
    scene.set_tile_map(img("""
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        dddddddddddd222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        d..........dd22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        d...........ddddddddddddddddddddddd222222222222222222222222222222222222222222ddddddddd2222222222222222222222222222222222
        ..................................dddddddd22222222222222222222222222222ddddddd.......d2222222222222222222222222222222222
        .......................................dddddd222222222222222222222222ddd.............dd222222222222222222222222222222222
        ...........................................ddddd2222222ddddddddd2222dd................d222222222222222222222222222222222
        ...............................................ddddddddd.......dddddd.................d222222222222222222222222222222222
        ......................................................................................dd222222222222222222222222dddddddd
        .......................................................................................d22222222222222222222dddddd......
        .......................................................................................d222222222222222dddddd...........
        .......................................................................................d222dddd222222ddd................
        .......................................................................................dddd...dddddddd..................
        ..............................................................................dd.22.....dd..........................dddd
        ddddd.......................................................................dddd2222................................d11d
        ddddddddddd.............ddd...............................................dddddd2222.................................11d
        ddddddddddd............dddd...........ddd..............................d..dddddd2222.................................11d
        ddddddddddd....ddddd...dddd......dddddddd........d...dd...ddd.......d.....d222222222.......................ddddddddddddd
        ddddddddddd2222ddddd222dddd...ddddddddddd.......dd22222222dddd............d222222222................dddd..2ddddddddddddd
        ddddddddddd2222ddddd222dddd222ddddddddddd......ddd22222222dddddddd........d222222222ddddd...d...d...dddd222ddddddddddddd
        ddddddddddd2222ddddd222dddd222ddddddddddd....ddddd22222222dddddddd22222222d222222222ddddd22222222222dddd222ddddddddddddd
        ddddddddddd2222ddddd222dddd222ddddddddddd2222ddddd22222222dddddddd22222222d222222222ddddd22222222222dddd222ddddddddddddd
        ddddddddddd2222ddddd222dddd222ddddddddddd2222ddddd22222222dddddddd22222222d222222222ddddd22222222222dddd222ddddddddddddd
    """))   
    scene.set_tile(13, img("""
        c c c c f c c c c f c c c c f c
        c c c c f c c c c f c c c c f c
        f f f f f f f f f f f f f f f f
        c c f c c c c f c c c c f c c c
        c c f c c c c f c c c c f c c c
        f f f f f f f f f f f f f f f f
        c c c c f c c c c f c c c c f c
        c c c c f c c c c f c c c c f c
        f f f f f f f f f f f f f f f f
        c c f c c c c f c c c c f c c c
        c c f c c c c f c c c c f c c c
        f f f f f f f f f f f f f f f f
        c c c c f c c c c f c c c c f c
        c c c c f c c c c f c c c c f c
        f f f f f f f f f f f f f f f f
        c c f c c c c f c c c c f c c c
    """),
    True)
    scene.set_tile(2, img("""
        2 2 2 2 4 2 2 4 2 4 4 2 2 4 2 2
        2 2 2 2 4 2 2 4 2 4 2 2 2 4 2 2
        2 2 2 2 4 2 2 4 2 4 2 2 4 4 2 2
        2 2 2 4 2 2 4 2 2 4 2 2 4 2 2 2
        2 2 2 4 4 4 4 2 4 4 4 4 4 2 2 2
        2 2 4 2 2 2 2 4 4 2 2 2 2 2 2 4
        4 4 2 2 2 4 4 4 2 2 2 2 2 4 4 4
        2 4 4 2 2 2 2 2 2 2 2 4 4 4 2 2
        2 2 4 2 2 2 2 2 2 4 4 2 2 2 2 2
        2 2 4 4 4 4 4 4 4 4 2 4 4 4 4 2
        2 4 4 2 2 2 2 2 2 2 2 2 2 2 2 4
        4 2 4 4 4 4 2 2 2 4 4 4 4 4 2 2
        2 2 2 2 2 4 4 4 4 4 2 2 2 4 4 2
        2 2 2 4 4 4 4 4 4 4 4 4 2 2 4 4
        4 4 4 4 2 2 4 2 2 2 2 4 4 4 2 2
        2 2 2 2 2 2 4 2 2 2 2 2 2 4 2 2
    """),
    True)

    def on_hit_tile(sprite):
        storyboard.replace("jumper")
    scene.on_hit_tile(SpriteKind.player, 2, on_hit_tile)

    #Controls and Camera
    controller.move_sprite(mySprite, 64, 0)



    mySprite.set_position(8, 795)
    scene.camera_follow_sprite(mySprite)
    mySprite.set_kind(SpriteKind.player)
    
    #jump
    mySprite.ay = 120

    controller.move_sprite(mySprite, 65, 0)
    def jump():
        global double_jump
        if double_jump:
            mySprite.vy = -85
            double_jump = mySprite.is_hitting_tile(CollisionDirection.BOTTOM)
    controller.A.on_event(ControllerButtonEvent.PRESSED, jump)
    def on_update2():
        global double_jump
        if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
            double_jump = True
    game.on_update(on_update2)

storyboard.register_scene("main", main_game)

def jumper():
    scene.set_background_image(img("""
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888881111118888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888811111111111111188888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888811111111111111118888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888111888888888888888888888888888888888811111111111111111888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888881111188888888888888888888888888888888811111111111111111888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888811111111188888888888888888888888888888888111111111111111888888888888888
        8888888888888888888811111888811111118888888888888888888888888888888888888888888888888888811111111111111188888888888888888888888888111111111111111111118888888888
        8888888888888888888111111111111111111188888888888888888888888888888888888888888888888888111111111111111111888888888888888888888888111111111111111111111888888888
        8888888888888888881111111111111111111188881118888888888888888888888888888888881111888881111111111111111111188888888888888888888888111111111111111111111188888888
        8888888888888888111111111111111111111118811111188888888888888888888888888888811111111111111111111111111111188888888888888888888888111111111111111111111188888888
        8888888888888881111111111111111111111111111111118888888888888888888888888888111111111111111111111111111111118888888888888888888888111111111111111111111111888888
        8888888888888111111111111111111111111111111111118888888888888888888888888888111111111111111111111111111111118888888888888888888888811111111111111111111111888888
        8888888888888111111111111111111111111111111111111888888888888888888888888888111111111111111111111111111111118888888888888888888888881111111111111111111111888888
        8888888888111111111111111111111111111111111111111888888888888888888888888888111111111111111111111111111111118888888888888888888888888111111111111111111111888888
        8888888888111111111111111111111111111111111111111888888888888888888888888888111111111111111111111111111111118888888888888888888888888811111111111111111111888888
        8888888881111111111111111111111111111111111111111888888888888888888888888888811111111111111111111111111111111888888888888888888888888888811111111111111118888888
        8888888881111111111111111111111111111111111111118888888888888888888888888888811111111111111111111111111111111111111188888888888888888888888111111111111118888888
        8888888888811111111111111111111111111118888888888888888888888888888888888881111111111111111111111111111111111111111111188888888888888888888881111111111118888888
        8888888888811111111111111111111111111188888888888888888888888888888888888811111111111111111111111111111111111111111111188888888888888888888888111111111118888888
        8888888888881111111111111111111111118888888888888888888888888888888888888811111111111111111111111111111111111111111111188888888888888888888888111111111118888888
        8888888888811111111111111111111111188888888888888888888888888888888888888881111111111111111111111111111111111111111111888888888888888888888888811111111118888888
        8888888888881111111111888888888888888888888888888888888888888888888888888881111111111111111111111111111111111111111111888888888888888888888888811111111118888888
        8888888888888111111118888888888888888888888888888888888888888888888888888888111111111111188888811111111111111111111118888888888888888888888888811111111111888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888811111111188888888888888888888888888888888888888888888888888888888811111111111188888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888111888888888888888888888888888888888888888888888888888888888888811111111111111888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888811111111111111888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888811111111111118888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888881111111111118888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888811111111188888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888111111888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888844444444444444444448888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888844444444444444444444444444444444888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888444444444444444444444444444444444444444888888888888888888888888888888
        888888888888888888888888888888888888888888888888888888888888888888888888eeee888888888884444444444444444444444444444444444444444444448888888888888888888888888888
        888888888888888888888888888888888888888888888888888888888888888888eeeeeeeeeee88888888444444444444444444444444444444444444444444444444448888888888888888888888888
        88888888888888888888888888888888888888888888888eeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444444444444444444444444444444444444444444444444444488888888888888888888888
        88888888888888888888888888888888888888888eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444444444444444444444444444444444444444444444444444444444888888888888888888
        888888888888888888888888888888888888eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444444444444444444444444444444444444444444444444c4444888888888888888c
        8888888888888888888888888888888888eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444444444444444444444444444444444444444444444ccc44444888888888888cc
        8888888888888888888888888888888888eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444444444444444444e44e44444444444444444444444ccc44444444888888888cc
        8888888888888888888888888888888888eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444444444444444444444e44e44e4444444444444444444444ccccc444444444888888ccc
        8888888888888888888888888888888888eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444444444444444e44e44e4444444444444444444444ccccc444444444488888ccc
        8888888888888888888888888888844444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444444444444444e44e4ee444444444444444444444ccccccc44c44c44c48c8cccc
        8888888888888888888888888444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444444444444444eeeee4444444444444444444444ccccccc44c44c44c44c8cccc
        888888888888888888888884444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444444444444444ee4e44444444444444444444ccccccccccccccccccccccccc
        888888888888888888884444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444444444444444444444eeee44444444444444444444cccccccccccc777777ccccccc
        88888888888888888884444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444444444444444e4e4ee444444444444444444cccccccccccc7cccccccccccc
        88888888888888888444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444444444444444444e444e44ee4444444444444444cccccccccccc777777ccccccc
        8888888888888884444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444444444444e4444e4444444444444444444ccfffffcccccccccc7ccccfff
        888888888888884444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444444444e444444444444444444444444ccf1f1fccccc777777ccccf1f
        888888888888844444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444444444444444ee4444444444444444444444ccfffffcccccffffffccccfff
        88888888888444444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444444444444444444444444444444ccf1f1fcccccffffffccccf1f
        8888888884444444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444444444444444444444444444ccfffffcccccffffffccccfff
        84444444444444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444444444444444444444444444ccccccccccccffffffccccccc
        444444444444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444444444444444444444444444ccccccccccccffffffccccccc
        44444444444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444444444444444444444ccccccccccccffffffccccccc
        4444444444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444444444444444444444444ccccccccccccffffffccccccc
        444444444444444444444eeeeeeeeeeeee4444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444444444444444444444444444444444444ccccccccccccffffffccccccc
        4444444444444444444eeeeeeeeeee4444444444444444444444eeeeeeeeeeeeeeeeeeeeeeeee4444444444444444444444444444444444444444444444444444444444444444444444ddddddd444444
        44444444444444444444eeeeeee444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444ddddddd444444
        44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444dddddddd444444
        44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444dddddddd444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f444444444444444444444444444444444dddddddd444444
        444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f5f44444444444444444444444444444444dddddddd444444
        44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f555f444444444444444444444444444444ddddddddd444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f55555f44444444444444444444444444444ddddddddd444444
        44444e444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f5555555f4444444444444444444444444444ddddddddd444444
        4444ee4444e444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f555555555f444444444444444444444444444ddddddddd444444
        444e44444e44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f5555555f444444444444444444444444444dddddddddd444444
        444e444ee4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f55555f4444444444444444444444444444ddddddddddd44444
        444e44e4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f555f44444444444444444444444444444ddddddddddd44444
        444e4e444444e4444444444444444444444444444444444444444444444444e444444444444444444444444444444444444444444444444f5f444444444444444444444444444444ddddddddddd44444
        444ee444444e444444444444444444444444444444444444444444444444444e444444444444444444444444444444444444444444444444f4444444444444444444444444444444ddddddddddd44444
        444eee4444e4444444444444444444444444444444444444444444444e444444e44444444444444444444444444444444444444444444444f4444444444444444444444444444444ddddddddddd44444
        44444ee4ee4444444444444444444444444444444444444444444444eeee444e444444444444444444444444444444444444444444444444f4444444444444444444444444444444ddddddddddd44444
        44444e4ee44444444444444444444444444444444444444444444444e444e44e444444444444444444444444444444444444444444444444f444444444444444444444444444444dddddddddddd44444
        4444e44e44444444444444444444444444444444444444444444444444eeeeee444444444444444444444444444444444444444444444444f444444444444444444444444444444dddddddddddd44444
        44444444e4444444444444444444444444444444444444444444444444e44ee4444444444444444444444444444444444444444444444444f44444444444444444444444444444ddddddddddddd44444
        444444444e444444444444444444444444444444444444444444444444e4444ee44444444444444444444444444444444444444444444444f4444444444444444444444444444dddddddddddddd44444
        444444444e444444444444444444444444444444444444444444444444444444ee4444444444444444444444444444444444444444444444f4444444444444444444444444444dddddddddddddd44444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f444444444444444444444444444ddddddddddddddd44444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444dddddddddddddddd44444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444ddddddddddddddd444444
        444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444dddddddddddddddd444444
        44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444ddddddddddddddddd444444
        444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444ddddddddddddddddddd444444
        44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444ddddddddddddddddddd4444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444dddddddddddddddddddd4444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444dddd44444ddddddddddddddddddddddd4444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444ddddddddddddddddddddddddddddddd44444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444ddddddddddddddddddddddddddddddd44444444
        44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444dddddddddddddddddddddddddddddd44444444
        444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444dddddddddddddddddddddddddddd444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444dddddddddddddddddddddddddd4444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444dddddddddddddddddddddd44444444444
        44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444dddddddddddddd444444444444444
        444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444dddddddd44444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
    """))
    my_sprite = sprites.create(img("""
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        .........eeeeee.....eeee........
        ........eeeeeeeee...eeeee.......
        .......eeeeeeeeee..eee11e.......
        .......eeeeeeeeeeeeeee1fee......
        .......eeeeeeeeeeeeeeeeeee......
        ........eeeeeeeeeeeeeee.........
        ........eeeeeeeeeeeeee..........
        ..........eeeeeeeeee............
        ..........eeeeeeeee.............
        ...........e....e...............
        ...........e....e...............
        ...........e....e...............
        ...........e....e...............
        ...........e....e...............
        ...........e....e...............
        ...........eeee.eeee............
        ................................
        ................................
        ................................
    """))
    my_sprite.set_kind(SpriteKind.player)
    my_sprite.set_position(15, 100)
    my_sprite.ay = 120
    info.set_score(0)
    info.set_life(1)
    my_sprite.set_flag(SpriteFlag.SHOW_PHYSICS, True)
    my_sprite.set_flag(SpriteFlag.StayInScreen, True)
    def on_jump():
        my_sprite.vy = -80
    controller.A.on_event(ControllerButtonEvent.PRESSED, on_jump)
    def jump():
        global double_jump
        if double_jump:
            my_sprite.vy = -80
        double_jump = my_sprite.is_hitting_tile(CollisionDirection.BOTTOM)
    controller.A.on_event(ControllerButtonEvent.PRESSED, jump)
    def on_update3():
        global double_jump
        if my_sprite.y > 99:
            double_jump = True
    game.on_update(on_update3)
    
    def on_update_interval():
        projectile = sprites.create_projectile_from_side(img("""
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ..................77777777......
        ................77777777777.....
        ...............7777777777777....
        ..............727777...77777....
        ..............77777....77777....
        ..............277.....777777....
        .............2.......777777.....
        .....................77777......
        .....................7777.......
        ....................7777........
        ...................7777.........
        ...................77777........
        ...................777777.......
        ....................77777777....
        .....................777777777..
        ................................
        ................................
        ................................
    """), -60, 0)
        projectile.set_position(170, 102.5) 
        projectile.set_kind(SpriteKind.enemy) 
    game.on_update_interval(1450, on_update_interval)

    def on_overlap(sprite, otherSprite):
        storyboard.replace("main")
        game.splash("Game Over", "You let the emus down!")
    sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap)


storyboard.register_scene("jumper", jumper)

storyboard.start("main")