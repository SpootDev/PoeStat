# PoeStat

This is a docker and web based application to view your character(s), stash pages and overall wealth.

Main feature will be the ability to browse and search your items by type and modifiers.

Experimental layouts created using Pencil wireframe tool and placed in layouts directory.

# Completed
* Docker compose setup for Database, Nginx, Flask and server components
* Shell code copied from MediaKraken for web components
* Fetch and store all stashes from the API for all leagues for market data
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
* Find items that can be done for vendor recipe (gems to 40, etc)
* Track map or act time via client.txt
* Store client.txt messages into database for chat history, etc
* Search/Filter stashes for gear/items (including stats, etc)
* Edit/Create loot filters
  * Is shaper item
  * Is elder item
  * Is corrupt item
  * Usable by selected character
  * Number of Sockets
  * Number of links
  * iLvl
  * Amount of affixes on an item
  * Particular enchant (from the lab)
  

# Long term possibilities
* Overlay for running lab from data provided by PoeLab.com
* Passive tree planner/character builder
* Overlay and trade message tracking
