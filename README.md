# PoeStat

This is a docker and web based application to view your character(s), stash pages and overall wealth.

Main feature will be the ability to browse and search your items by type and modifiers.

Experimental layouts created using Pencil wireframe tool and placed in layouts directory.

# Completed
* Docker compose setup for Database, Nginx, Flask and server components
* Shell code copied from MediaKraken for web components
* Fetch and store all stash's from the API for all leagues
* Fetch and store all account characters (name, class, passive, exp, etc)
* Fetch stashes for specific account and league
* Loaded database tables with items, essence, modifiers, etc (data from RePoE)

# TODO
* View characters and inventory/gear from website
* Find uniques that are not in your unique tab (if available)
* Find currency that wandered off (if available)
* Find divination cards that are not in divination tab (if available)
* Find essence that are not in essence tab (if available)
* Find maps that are not in map tab (if available)
* Calculate wealth based on current market value by league
* Search/Filter stashs for gear/items (including stats, ench, etc)
* Find items that can be done for vendor recipie (gems to 40, etc)
* Track map or act time via client.txt
* Store client.txt messages into database for chat history, etc
* Edit/Create loot filters

# Long term possibilities
* Overlay for running lab from data provided by PoeLab.com
* Passive tree planner/character builder
* Overlay and trade message tracking
