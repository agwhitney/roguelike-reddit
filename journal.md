## Hello!

My contribution to the r/roguelikedev all-encompassing roguelike tutorial will not only be a roguelike, but a journal/guide of sorts to document what I did and possibly give insight for others doing the same thing

So let's get started just to get started, and we'll make it pretty in the future (will we, though?)

## Week 1 -- 20 June 2017

So what did I do on day 1?
-I hurt my neck, for one thing (something related to waking up).
-I created a working folder I called 'roguelike/' and created a virtual environment in it running Python 3.6.
	I'm under the impression that r/roguelikedev is going to be using Python 2.7, which I would prefer not to do
    (and I don't think that it's really the best solution for people new to Python either; why would you start with the old thing?).
	I'm sure other people will also use 3.6, so I'm sure it will be fine.
-I set up a bash alias in ~/.bash_aliases to create a shortcut into my virtual environment.
-I created a git repository to have some version control from the very beginning.
    I also made a .gitignore file, to ignore the 'venv/' folder

That's all that's outlined for today, and I think it's a solid prep process for the beginnings of a project!


## Week 2 -- 27 June 2017

A new challenger approaches, and it's u/AetherGrey, to usurp the mods and take his rightful place as tutorial guy.
READ: He's revamping the tutorial (for Python 3, which is good) and doing it alongside what's happening now.
So I'm going to be following that! It's on rogueliketutorials.com.

Installing SDL2 from apt (I have not idea what SDL2 is, but I think it's related to fonts):
	sudo apt-get install libsdl2-dev
Next is installing libtcod (which is not just a python package as I thought!):
	This required me getting the packages 'libtool' and 'autoconf'
	And then it worked! The libtcod directory is in Home, and the required stuff will be moved into my project folder.

I feel like I should split things into an assets folder, although I suppose the parent can just contain all of this stuff.
I'm adding the libtcod assets to my .gitignore, at least.

Let's really get started!
Note: Computer planes have positive x going right, positive y going down. Crazy, I know! I've seen it so often and I still need to remember!

Ok so at the end of it all that went well. The guide seems pretty straightforward and clear, for the most part.
I'm feeling like I do have some power with libtcod.
I did use 'solids' instead of 'blocked' as an attribute for tile.Tile. It might get confusing, so I may just change it back.
Otherwise, that wraps up the week. Perhaps I'll make a branch and see where I can take this from here.


### 28 June 2017

I put this on Github, and tbh I'm not sure why I didn't just do it from the beginning.
I always regret that...

I cleaned up a few things (.gitignore, readme, this).

Here's the how-to for libtcod and sdl2 setup on Linux:

1. **SDL2**

  * `sudo apt-get install libsdl2-dev` -> easy peasy

2. **libtcod**

  * Start in your home directory (it doesn't really matter but this is an alright place for it): `cd ~`

  * Get the most current (1.6.3 as of now) from bitbucket: `wget https://bitbucket.org/libtcod/libtcod/downloads/20170226-libtcod-1.6.3.tbz2`

  * Unpack the tarball (Linux zip flavor): `tar xf 20170226-libtcod-1.6.3.tbz2`

  * Don't need it anymore, so you might as well `rm 20170226-libtcod-1.6.3.tbz2`

  * Into the build folder: `cd 20170226-libtcod-1.6.3/build/autotools`

  * `autoreconf -i` -- this needs the packages autoconf  and libtool: `sudo apt-get install {package}`

  * `./configure`

  * `make`

  * And then just take the things you need and put them in your project folder: (from the root libtcod folder): `cp -dr build/autotools/.libs/libtcod.so* python/libtcodpy {project folder}`

Done!


## Week 3 - 4 July 2017

Week 3 was all about map generation, using the game map and tile objects created before and tying them together.
This journal doesn't really feel necessary, though I continue to type.
Something interesting about the tunnels: they connect rooms that are placed totally randomly, and could cross other rooms
in the process. It makes the tunnel system *look* a little more complex, but if you follow it in a straight line you see
that it's going from a center to another center, just as it was coded! If you wanted, you could follow the tunnels to see
exactly how the map was generated.

I could move ahead, but instead I'm going to try my own thing (which will happen soon anyway).
I'd like to have my variables stored externally in a json file, and I'd like to learn more json - so that's what I plan to do.
