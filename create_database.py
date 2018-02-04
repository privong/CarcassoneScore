#!/usr/bin/env python
"""
Database initialization for Carcassonne score keeping system.

Copyright 2018 George C. Privon

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sqlite3

conn = sqlite3.connect('CarcassonneScore.db')
c = conn.cursor()

# player table
c.execute('''CREATE TABLE players (playerID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                   name TEXT NOT NULL DEFAULT "")''')
# player names
c.execute('''INSERT INTO players values (0,
                                         "John Smith")''')
c.execute('''INSERT INTO players values (1,
                                         "Jane Doe")''')

# games table
# gameID - unique ID
# location - free text
# starttime - timecode
# endtime - timecode
# expansions - comma-separated list of expansions used (by expansionID)
c.execute('''CREATE TABLE games (gameID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                 location TEXT NOT NULL DEFAULT "",
                                 starttime TEXT NOT NULL DEFAULT "",
                                 endtime TEXT NOT NULL DEFAULT "",
                                 expansions TEXT NOT NULL DEFAULT "")''')


# turns table
# gameID - corresponds to games table
# turnNum - incremented turn number (corresponds to a tile placement)
# time - time at which the placement was made
# builder - 0 if tile was placed as part of normal turn, 1 if placed
#           as a result of a builder token
# playerID - player who made the turn
c.execute('''CREATE TABLE turns (gameID INTEGER NOT NULL,
                                 turnNum INTEGER NOT NULL,
                                 time TEXT NOT NULL,
                                 builder INTEGER NOT NULL,
                                 playerID INTEGER NOT NULL)''')

# individual scores
# gameID - unique per game
# playerID - corresponds to entry from players table
# turnNum - turn number (corresponds to number in turns table)
# scoreID - ID number for the score (unique to game?)
# ingame - 1 if scored during regular play, 0 if scored after tiles are gone
# points - number of points awarded
# scoretype - road, city, meadow, etc.
# sharedscore - was this score shared with another player?
# token - token(s) used for score (e.g., meeple, wagon, pig)
# extras - any other items (e.g., trade goods)
# comments - text annotation
c.execute('''CREATE TABLE scores (gameID INTEGER NOT NULL,
                                  playerID INTEGER NOT NULL,
                                  turnNum INTEGER NOT NULL,
                                  scoreID INTEGER NOT NULL,
                                  ingame INTEGER NOT NULL,
                                  points INTEGER NOT NULL,
                                  scoretype TEXT NOT NULL,
                                  sharedscore INTEGER NOT NULL,
                                  token TEXT NOT NULL,
                                  extras NOT NULL,
                                  comments TEXT)''')

# list of expansions
# mini - 1 if a mini expanion, otherwise 0
# active - 1 if it can be played, otherwise 0
# tokens - additional tokens provided beyond the base game
# scoretypes - additional classes of scoring enabled
# Ntiles - number of tiles added
# tiletypes - special scorable tiles added
c.execute('''CREATE TABLE expansions (expansionID INTEGER PRIMARY KEY,
                                      name TEXT NOT NULL,
                                      mini INTEGER,
                                      active INTEGER,
                                      tokens TEXT,
                                      scoretypes TEXT,
                                      Ntiles INTEGER,
                                      tiletypes TEXT)''')
# large expansions
# taken from http://carcassonne.wikia.com/wiki/Official_expansions
# Only 1, 2, and 5 are currently populated
c.execute('''INSERT INTO expansions values (1,
                                            "Inns & Cathedrals",
                                            0,
                                            1,
                                            "BigMeeple",
                                            "",
                                            18,
                                            "Cathedral,InnonLake")''')
c.execute('''INSERT INTO expansions values (2,
                                            "Traders & Builders",
                                            0,
                                            1,
                                            "Pig,Builder",
                                            "",
                                            24,
                                            "TradeGoods")''')
c.execute('''INSERT INTO expansions values (3,
                                            "Princess & Dragon",
                                            0,
                                            0,
                                            "",
                                            "",
                                            0,
                                            "")''')
c.execute('''INSERT INTO expansions values (4,
                                            "The Tower",
                                            0,
                                            0,
                                            "",
                                            "",
                                            0,
                                            "")''')
c.execute('''INSERT INTO expansions values (5, 
                                            "Abbey & Mayor",
                                            0,
                                            1,
                                            "Mayor,Wagon,Barn",
                                            "",
                                            12,
                                            "Abbey")''')
c.execute('''INSERT INTO expansions values (6,
                                            "Count, King & Robber",
                                            0,
                                            0,
                                            "",
                                            "",
                                            0,
                                            "")''')
c.execute('''INSERT INTO expansions values (7,
                                            "The Catapult",
                                            0,
                                            0,
                                            "",
                                            "",
                                            0,
                                            "")''')
c.execute('''INSERT INTO expansions values (8,
                                            "Bridges, Castles & Bazaars",
                                            0,
                                            0,
                                            "",
                                            "",
                                            0,
                                            "")''')
c.execute('''INSERT INTO expansions values (9,
                                            "Hills & Sheep",
                                            0,
                                            0,
                                            "",
                                            "",
                                            0,
                                            "")''')
c.execute('''INSERT INTO expansions values (10,
                                            "Under the Big Top",
                                            0,
                                            0,
                                            "",
                                            "",
                                            0,
                                            "")''')
#mini expansions
c.execute('''INSERT INTO expansions values(101,
                                           "The River",
                                           1,
                                           1,
                                           "",
                                           "",
                                           12,
                                           "")''')
c.execute('''INSERT INTO expansions values(102,
                                           "The Abbott",
                                           1,
                                           1,
                                           "Abbott",
                                           "Garden",
                                           0,
                                           "")''')

conn.commit()
conn.close()
