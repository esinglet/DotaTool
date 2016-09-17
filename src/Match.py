#https://dota2api.readthedocs.io/en/latest/responses.html#towers-and-barracks

#tower status
# 1	ANCIENT TOP	1	Alive
# 2	ANCIENT BOTTOM	0
# 3	TOP 3		1	Alive
# 4	TOP 2		0
# 5	TOP 1		0
# 6	MIDDLE 3	1	Alive
# 7	MIDDLE 2	1	Alive
# 8	MIDDLE 1	1	Alive
# 9	BOTTOM 3	0
# 10	BOTTOM 2	0
# 11	BOTTOM 1	0

#game mode
# Value	Description
# 0	None
# 1	All Pick
# 2	Captain’s Mode
# 3	Random Draft
# 4	Single Draft
# 5	All Random
# 6	Intro
# 7	Diretide
# 8	Reverse Captain’s Mode
# 9	The Greeviling
# 10	Tutorial
# 11	Mid Only
# 12	Least Played
# 13	New Player Pool
# 14	Compendium Matchmaking
# 16	Captains Draft

#lobby type
# -1	invalid
# 0	Public matchmaking
# 1	Practice
# 2	Tournament
# 3	Tutorial
# 4	Co-op with AI
# 5	Team match
# 6	Solo queue
# 7	Ranked matchmaking
# 8	1v1 solo mid

# {
#     season                  - Season the game was played in
#     radiant_win             - Win status of game (True for Radiant win, False for Dire win)
#     duration                - Elapsed match time in seconds
#     start_time              - Unix timestamp for beginning of match
#     match_id                - Unique match ID
#     match_seq_num           - Number indicating position in which this match was recorded
#     tower_status_radiant    - Status of Radiant towers
#     tower_status_dire       - Status of Dire towers
#     barracks_status_radiant - Status of Radiant barracks
#     barracks_status_dire    - Status of Dire barracks
#     cluster                 - The server cluster the match was played on, used in retrieving replays
#     cluster_name            - ?
#     first_blood_time        - Time elapsed in seconds since first blood of the match
#     lobby_type              - See lobby_type table
#     lobby_name              - See lobby_type table
#     human_players           - Number of human players in the match
#     leagueid                - Unique league ID
#     positive_votes          - Number of positive/thumbs up votes
#     negative_votes          - Number of negative/thumbs down votes
#     game_mode               - See game_mode table
#     game_mode_name          - See game_mode table
#     radiant_captain         - account ID for Radiant captain
#     dire_captain            - account ID for Dire captain
#     [pick_bans]
#     {
#         {
#             hero_id         - Unique hero ID
#             is_pick         - True if hero was picked, False if hero was banned
#             order           - Order of pick or ban in overall pick/ban sequence
#             team            - See team_id table.

#         }
#     }
#     [players]
#     {
#         account_id          - Unique account ID
#         player_slot         - Player's position within the team
#         hero_id             - Unique hero ID
#         hero_name           - Hero's name
#         item_#              - Item ID for item in slot # (0-5)
#         item_#_name         - Item name for item in slot # (0-5)
#         kills               - Number of kills by player
#         deaths              - Number of player deaths
#         assists             - Number of player assists
#         leaver_status       - Connection/leaving status of player
#         gold                - Gold held by player
#         last_hits           - Number of last hits by player (creep score)
#         denies              - Number of denies
#         gold_per_min        - Average gold per minute
#         xp_per_min          - Average XP per minute
#         gold_spent          - Total amount of gold spent
#         hero_damage         - Amount of hero damage dealt by player
#         tower_damage        - Amount of tower damage dealt by player
#         hero_healing        - Amount of healing done by player
#         level               - Level of player's hero
#         [ability_upgrades]  - Order of abilities chosen by player
#         {
#             ability         - Ability chosen
#             time            - Time in seconds since match start when ability was upgraded
#             level           - Level of player at time of upgrading
#         }

#         [additional_units]  - Only available if the player has a additional unit
#         {
#             unitname        - Name of unit
#             item_#          - ID of item in slot # (0-5)
#         }
#     }
#     // These fields are only available for matches with teams //
#     [radiant_team]
#     {
#         team_name            - team name for Radiant
#         team_logo            - team logo for Radiant
#         team_complete   - ?
#     }
#     [dire_team]
#     {
#         team_name               - team name for Dire
#         team_logo               - team logo for Dire
#         team_team_complete      - ?
#     }
# }




class Match:

