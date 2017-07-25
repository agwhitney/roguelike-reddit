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

### 7 July 2017

I found plenty of things saying *not* to use json for config files but:

1. Python's ConfigParser actually seems okay
2. YAML has package dependencies to read
3. I think a lot of people use json and it's high time that I do too.

Working with json seems really simple, and now I have an external file to store map and screen size variables.
I'm not sure what else to put in there (key-bindings, I suppose), but it was actually pretty simple to load the settings with json.
I'm wondering if I can load a default settings file, and overwrite it part-wise to have user-defined settings.
I'm not sure how a user would define them! but it's still a handy feature, and I think ConfigParser has it.

## Week 4 - 11 July 2017

I'm actually starting this a day before from boredom.
I want to get some insight on entity interaction that I can use for chess, but I think that might actually be next week.
I think the benefit libtcod has over the regular console for chess is layers.
There's a tile object with an entity object above it: not one or the other.
Perhaps I can redefine the chess board as a container of Tile and Piece objects?

I'm digressing.

Week 4 is Field of View.

Field of view is really cool. I'm definitely going to play around with the algorithms, and try and add torches.

Week 4 is also Enemy placement! 
There's a little bit of interaction, and it seems a bit inefficient to check *every* entity to see if you've bumped, but I guess that just comes with the territory.
Fairly straightforward, and I'm excited to work with an AI next week (I think). 

I'd still like to add torches, but I'll probably try to take more of this into chess.

## Week 5 - 18 July 2017
### Part 6 - Making Combat Kinda Serious
Today is "Going Berserk!" which I think is better combat, and also the GUI.

It's been a while since I've looked at this (been looking at chess), so it's welcoming to come back to it.

It begins with *Compositional* Programming - interested!

Compositional Programming seems interesting, though I'm not sure what the benefits might be over inheritance.
Update: Compositional programming lets entities inherit what they need to, rather than having it be a strict parent of something else.

There's a lot going on in this lesson - that, AI and path-making algorithms for them, and prep for GUI things.

In the Fighter component we have the results of combat being returned as a dictionary with a message.
This is pretty much the same as how we're already handling key presses - the object returns a result and a standard result,
but it's up to the engine as to what is actually done with it.
I think I like this method.
I feel as if it reduces complexity because things aren't doing more than they need to be, it seems easier for notekeeping,
and all the engine has to do is manipulate results rather than create them.

### Part 7 - GUI

Went through it pretty quickly; it's fairly simple and flexible, and I think there's plenty of room to add more detail.
It is primarily text-based - but the whole engine is ;)

## Week 6 - 25 July 2017

Has Part 8 about Items and Inventory and Part 9 about Ranged Combat and Spells
