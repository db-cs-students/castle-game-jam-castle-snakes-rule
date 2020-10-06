/** 
Title: 
Creators: Andrew McCrary and Parker Galloway
Description: partial dinosaur game and mario but you kill a snake to avenge your emus

 */
let double_jump = true
info.setScore(0)
info.setLife(2)
storyboard.registerScene("main", function main_game() {
    scene.setBackgroundImage(img`
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
    `)
    // Main character
    let mySprite_facing_right = img`
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . e e e . . . e e e . . .
        . . . e e e e e . e e e 2 e . .
        . . . e e e e e e e e e e e . .
        . . . e e e e e e e . . . . . .
        . . . e e e e e e e . . . . . .
        . . . . e e e e e e . . . . . .
        . . . . . e e e e e . . . . . .
        . . . . . e . . e . . . . . . .
        . . . . . e . . e . . . . . . .
        . . . . . e . . e . . . . . . .
        . . . . . e . . e . . . . . . .
        . . . . . . . . . . . . . . . .
    `
    let mySprite = sprites.create(mySprite_facing_right)
    let mySprite_facing_left = img`
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . e e e . . . e e e . . . .
        . . e 2 e e e . e e e e e . . .
        . . e e e e e e e e e e e . . .
        . . . . . . e e e e e e e . . .
        . . . . . . e e e e e e e . . .
        . . . . . . e e e e e e . . . .
        . . . . . . e e e e e . . . . .
        . . . . . . . e . . e . . . . .
        . . . . . . . e . . e . . . . .
        . . . . . . . e . . e . . . . .
        . . . . . . . e . . e . . . . .
        . . . . . . . . . . . . . . . .
    `
    game.onUpdate(function on_update() {
        if (controller.dx() > 0) {
            mySprite.setImage(mySprite_facing_right)
        } else if (controller.dx() < 0) {
            mySprite.setImage(mySprite_facing_left)
        }
        
    })
    // Tile Map
    scene.setTileMap(img`
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
    `)
    scene.setTile(13, img`
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
    `, true)
    scene.setTile(2, img`
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
    `, true)
    scene.onHitTile(SpriteKind.Player, 2, function on_hit_tile(sprite: Sprite) {
        //  info.change_life_by(-1)
        storyboard.replace("jumper")
    })
    // Controls and Camera
    controller.moveSprite(mySprite, 64, 0)
    mySprite.setPosition(5, 808)
    scene.cameraFollowSprite(mySprite)
    mySprite.setKind(SpriteKind.Player)
    // jump
    mySprite.ay = 120
    controller.moveSprite(mySprite, 65, 0)
    controller.A.onEvent(ControllerButtonEvent.Pressed, function jump() {
        
        if (double_jump) {
            mySprite.vy = -85
            double_jump = mySprite.isHittingTile(CollisionDirection.Bottom)
        }
        
    })
    game.onUpdate(function on_update2() {
        
        if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
            double_jump = true
        }
        
    })
})
storyboard.registerScene("jumper", function jumper() {
    scene.setBackgroundImage(img`
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
        8888888888888888888888888888888888eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444444444444444444444444444444444444444444444ccc44444444888888888cc
        8888888888888888888888888888888888eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444444444444444444444444444444444444444444444ccccc444444444888888ccc
        8888888888888888888888888888888888eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444444444444444444444444444444444444444444ccccc444444444488888ccc
        8888888888888888888888888888844444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444444444444444444444444444444444444444444444444ccccccc44c44c44c48c8cccc
        8888888888888888888888888444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444444444444444444444444444444444444444444ccccccc44c44c44c44c8cccc
        888888888888888888888884444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444444444444444444444444444444444444444ccccccccccccccccccccccccc
        888888888888888888884444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444444444444444444444444444444444444444444444ccccccccccccccccccccccccc
        88888888888888888884444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444444444444444444444444444444444444444ccccccccccccccccccccccccc
        88888888888888888444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee444444444444444444444444444444444444444444444444444ccccccccccccccccccccccccc
        8888888888888884444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444444444444444444444444444444444444444444ccfffffcccccccccccccccfff
        888888888888884444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee4444444444444444444444444444444444444444444444444ccf1f1fcccccccccccccccf1f
        888888888888844444444444444444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee44444444444444444444444444444444444444444444444ccfffffcccccffffffccccfff
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
        44444e44444444444444444444444444444444444444444444444444444444444444444444444ee44444444444444444444444444444f5555555f4444444444444444444444444444ddddddddd444444
        4444ee4444e4444444444444444444444444444444444444444444444444444444444444444444ee44444e444444444444444444444f555555555f444444444444444444444444444ddddddddd444444
        444e44444e4444444444444444444444444444444444444444444444444444444444444444444e444444e44444444444444444444444f5555555f444444444444444444444444444dddddddddd444444
        444e444ee44444444444444444444444444444444444444444444444444444444444444444444e44444e4444444444444444444444444f55555f4444444444444444444444444444ddddddddddd44444
        444e44e44444444444444444444444444444444444444444444444444444444444444444444444e444e444444444444444444444444444f555f44444444444444444444444444444ddddddddddd44444
        444e4e444444e44444444444444444444444444444444444444444444444444444444444444444ee4e4444e444444444444444444444444f5f444444444444444444444444444444ddddddddddd44444
        444ee444444e44444444444444444444444444444444444444444444444444444444444444444444eeeeee44444444444444444444444444f4444444444444444444444444444444ddddddddddd44444
        444eee4444e44444444444444444444444444444444444444444444444444444444444444444444e444ee444444444444444444444444444f4444444444444444444444444444444ddddddddddd44444
        44444ee4ee444444444444444444444444444444444444444444444444444444444444444444444e444e4444444444444444444444444444f4444444444444444444444444444444ddddddddddd44444
        44444e4ee4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f444444444444444444444444444444dddddddddddd44444
        4444e44e44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f444444444444444444444444444444dddddddddddd44444
        44444444e4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f44444444444444444444444444444ddddddddddddd44444
        444444444e444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f4444444444444444444444444444dddddddddddddd44444
        444444444e444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444f4444444444444444444444444444dddddddddddddd44444
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
    `)
    let my_sprite = sprites.create(img`
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
    `)
    my_sprite.setPosition(15, 100)
    my_sprite.ay = 120
    my_sprite.setFlag(SpriteFlag.StayInScreen, true)
    controller.A.onEvent(ControllerButtonEvent.Pressed, function on_jump() {
        my_sprite.vy = -80
    })
})
storyboard.start("main")
