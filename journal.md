Hello!
######

My contribution to the r/roguelikedev all-encompassing roguelike tutorial will not only be a roguelike, but a journal/guide of sorts to document what I did and possibly give insight for others doing the same thing

So let's get started just to get started, and we'll make it pretty in the future (will we, though?)

Day 1 -- 20 June 2017
#######################
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


Day 2 -- 27 June 2017
######################
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
